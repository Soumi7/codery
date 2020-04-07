class Profile(object):
    """
        Class containing methods for retrieving
        submissions of user
    """
    site_name = "HackerEarth"

    # -------------------------------------------------------------------------
    def __init__(self, handle=""):
        """
            @param handle (String): HackerEarth Handle
        """

        self.site = Profile.site_name
        self.handle = handle

    # -------------------------------------------------------------------------
    @staticmethod
    def is_website_down():
        """
            @return (Boolean): If the website is down
        """
        return (Profile.site_name in current.REDIS_CLIENT.smembers("disabled_retrieval"))

    # -------------------------------------------------------------------------
    @staticmethod
    def get_tags(problem_link):
        """
            @param problem_link(String): Problem link

            @return (List): List of tags
        """
        all_tags = []
        response = get_request(problem_link)
        if response in REQUEST_FAILURES:
            return all_tags

        soup = BeautifulSoup(response.text, "lxml")
        try:
            tags = soup.find_all("div", class_="problem-tags")[0]
        except IndexError:
            return all_tags

        lis = tags.find_all("span")[1:]
        for li in lis:
            if li.contents[0] != "No tags":
                all_tags.append(li.contents[0].strip(", "))

        return all_tags

    # -------------------------------------------------------------------------
    @staticmethod
    def get_editorial_link(problem_link):
        """
            @param problem_link(String): Problem link

            @return (String): Editorial link
        """
        return problem_link + "editorial/"

    # -------------------------------------------------------------------------
    @staticmethod
    def get_problem_setters(problem_link, should_update):
        """
            @param problem_link(String): Problem link
            @param should_update(Boolean): If should call the API to get problem_setters

            @return (List/None): Problem authors or None
        """
        if should_update is False:
            return None

        problem_setters = None
        url = "https://www.hackerearth.com/pagelets/problem-author-tester/" + \
              "/".join(problem_link.split("/")[-3:])
        response = get_request(url)
        if response in REQUEST_FAILURES:
            return problem_setters

        try:
            author = BeautifulSoup(response.text,
                                   "lxml").find_all("a")[0]["href"].split("@")[1]
        except:
            print "HackerEarth Author is none", problem_link, url
            author = None

        return author if author is None else [author]

    # -------------------------------------------------------------------------
    @staticmethod
    def get_problem_details(**args):
        """
            Get problem_details given a problem link

            @param args (Dict): Dict containing problem link
            @return (Dict): Details of the problem returned in a dictionary
        """
        problem_link = args["problem_link"]

        return dict(tags=Profile.get_tags(problem_link),
                    editorial_link=Profile.get_editorial_link(problem_link),
                    problem_setters=Profile.get_problem_setters(
                                        problem_link,
                                        "problem_setters" in args["update_things"]
                                    ))

    # -------------------------------------------------------------------------
    @staticmethod
    def is_invalid_handle(handle):
        url = "https://www.hackerearth.com/submissions/" + handle
        response = get_request(url)
        if response in REQUEST_FAILURES:
            return True
        return False

    # -------------------------------------------------------------------------
    @staticmethod
    def rating_graph_data(handle):
        url = "https://www.hackerearth.com/ratings/AJAX/rating-graph/" + handle
        response = get_request(url)
        if response in REQUEST_FAILURES:
            return response

        if response.text == "":
            return NOT_FOUND

        contest_data = eval(re.findall(r"var dataset = \[.*?\]", response.text)[0][14:])
        if len(contest_data) == 0:
            return []

        hackerearth_data = {}
        for contest in contest_data:
            time_stamp = str(datetime.datetime.strptime(contest["event_start"], "%d %b %Y, %I:%M %p"))
            url = "https://www.hackerearth.com" + contest["event_url"]
            hackerearth_data[time_stamp] = {"name": contest["event_title"],
                                            "rating": contest["rating"],
                                            "url": url,
                                            "rank": contest["rank"]}

        return [{"title": "HackerEarth",
                 "data": hackerearth_data}]

    # -------------------------------------------------------------------------
    def get_submissions(self, last_retrieved, is_daily_retrieval):
        """
            Retrieve HackerEarth submissions after last retrieved timestamp
            @param last_retrieved (DateTime): Last retrieved timestamp for the user
            @param is_daily_retrieval (Boolean): If this call is from daily retrieval cron

            @return (Dict): Dictionary of submissions containing all the
                            information about the submissions
        """

        handle = self.handle

        url = "https://www.hackerearth.com/submissions/" + handle
        t = get_request(url, is_daily_retrieval=is_daily_retrieval)

        if t in REQUEST_FAILURES:
            return t

        tmp_string = t.headers["set-cookie"]
        csrf_token = re.findall(r"csrftoken=\w*", tmp_string)[0][10:]

        headers = {"host": "www.hackerearth.com",
                   "user-agent": user_agent,
                   "accept": "application/json, text/javascript, */*; q=0.01",
                   "accept-language": "en-US,en;q=0.5",
                   "accept-encoding": "gzip, deflate",
                   "content-type": "application/x-www-form-urlencoded",
                   "X-CSRFToken": csrf_token,
                   "X-Requested-With": "XMLHttpRequest",
                   "Referer": "https://www.hackerearth.com/submissions/" + handle + "/",
                   "Connection": "keep-alive",
                   "Pragma": "no-cache",
                   "Cache-Control": "no-cache",
                   "Cookie": tmp_string}

        submissions = []
        for page_number in xrange(1, 1000):
            url = "https://www.hackerearth.com/AJAX/feed/newsfeed/submission/user/" + handle + "/?page=" + str(page_number)

            tmp = get_request(url, headers=headers, timeout=20, is_daily_retrieval=is_daily_retrieval)

            if tmp in REQUEST_FAILURES:
                return tmp

            json_response = tmp.json()
            if json_response["status"] == "ERROR":
                break

            body = json_response["data"]
            soup = bs4.BeautifulSoup(body, "lxml")

            trs = soup.find("tbody").find_all("tr")
            for tr in trs:

                all_tds = tr.find_all("td")
                all_as = tr.find_all("a")
                time_stamp = all_tds[-1].contents[1]["title"]
                time_stamp = time.strptime(str(time_stamp), "%Y-%m-%d %H:%M:%S")

                # Time of submission
                time_stamp = datetime.datetime(time_stamp.tm_year,
                                               time_stamp.tm_mon,
                                               time_stamp.tm_mday,
                                               time_stamp.tm_hour,
                                               time_stamp.tm_min,
                                               time_stamp.tm_sec) + \
                                               datetime.timedelta(minutes=690)
                curr = time.strptime(str(time_stamp), "%Y-%m-%d %H:%M:%S")

                if curr <= last_retrieved:
                    return submissions

                # Problem Name/URL
                problem_link = "https://www.hackerearth.com" + all_as[1]["href"]
                problem_name = all_as[1].contents[0]

                # Status
                try:
                    status = all_tds[2].contents[1]["title"]
                except IndexError:
                    status = "Others"

                if status.__contains__("Accepted"):
                    status = "AC"
                elif status.__contains__("Partially"):
                    status = "PS"
                elif status.__contains__("Wrong"):
                    status = "WA"
                elif status.__contains__("Compilation"):
                    status = "CE"
                elif status.__contains__("Runtime"):
                    status = "RE"
                elif status.__contains__("Memory"):
                    status = "MLE"
                elif status.__contains__("Time"):
                    status = "TLE"
                else:
                    status = "OTH"

                if status == "AC":
                    points = "100"
                else:
                    points = "0"

                language = all_tds[5].contents[0]

                submissions.append((str(time_stamp),
                                    problem_link,
                                    problem_name,
                                    status,
                                    points,
                                    language,
                                    "https://www.hackerearth.com/submission/" + \
                                    tr["id"].split("-")[-1]))

        return submissions

# =============================================================================