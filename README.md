# Codery

![](https://github.com/Soumi7/codery/blob/master/Assets/codery_logo.png)

**Codery** is a **Zulip Bot**.

## Codery in action

<img src="https://github.com/Soumi7/codery/blob/master/Assets/codery_demo.gif" height="500" alt="Codery Demo"/>

## Instructions to run locally:

1. [Create a Zulip Realm](https://zulip.com/create_realm/)
2. Goto to settings and create a new generic bot named 'codery'. (Settings can be found in dropdown of gear icon present in top right corner of zulip realm)
3. Download the zuliprc file for your bot and place it in your Downloads directory as '.zuliprc'.
![](./images/instructions.png)  
4. Get into the directory cd python-zulip-api/zulip_bots/zulip_bots/bots/codery
5. Install all the requirements using ``` pip3 install -r requirements.txt ```  inside the codery folder
6. Now ```cd ..```
7. Activate the source ```source zulip-api-py3-venv/bin/activate```
8. Run the bot ```zulip-run-bot codery —config-file ~/Downloads/zuliprc```
9. Head over to your created zulip realm and start using the bot.

###### For a detailed description of how to run the bot, please check out this medium article https://medium.com/@soumibardhan10/codery-zulip-bot-for-competitive-programming-hackathons-jobs-and-more-8cd13106fe15

## Features

- **Latest Coding Contests and Hackathons** Gives you the latest contests and Hackathons from CodeChef, Hackereath, Hackerrank and Codeforces. 

- **Filters the top contests** Provides the name, time remaining to register and link to the contest or hackathon site.

- **Competitive programming news** get all news related to coding by specifying the keyword after news

- **Search Technical Terms** get the meanings of any technical term in an instant

- **Jokes** funny programming jokes to lighten up your mood but still keep you focused

- **Linux Man Page** gets the information about in linux command to zulip

- **Calculator** calculates any kind of mathematical operations to do directly on zulip

- **Latest Jobs** gives job titles and application links on zulip using the Github Jobs API

- **Udemy courses** gives the latest popular Udemy courses using the Udemy Affiliate API

- **Trending Problems** know what are the trending problems over all competitive coding platforms globally

- **Leaderboard** gives leaderboard of programmers all over the world

- **Memo** can keep a list of jobs to do


## Video Link

https://youtu.be/CujqAzNdcr0 is the link to a video demo.


## Screenshots :

-  ### **Codery Help**

![Codery Help](https://github.com/Soumi7/codery/blob/master/Assets/s_help.png)

- ### **Contests** 

![Codery Help](https://github.com/Soumi7/codery/blob/master/Assets/s_contests.png)

![Codery Help](https://github.com/Soumi7/codery/blob/master/Assets/s_contests_2.png)

- ### **Courses** 

![Codery Help](https://github.com/Soumi7/codery/blob/master/Assets/s_courses.png)

- ### **Leaderboard** 

![Codery Help](https://github.com/Soumi7/codery/blob/master/Assets/s_leaderboard.png)

- ### **Trending** 

![Codery Help](https://github.com/Soumi7/codery/blob/master/Assets/s_trending.png)

- ### **Linux command page** 
<img src="https://github.com/Soumi7/codery/blob/master/Assets/man1.png" height="500" alt="Screenshot"/>


- ### **News** 

![Codery Help](https://github.com/Soumi7/codery/blob/master/Assets/s_news.png)

- ### **Jokes**

![Codery Help](https://github.com/Soumi7/codery/blob/master/Assets/s_jokes.png)

- ### **Search**

![Codery Help](https://github.com/Soumi7/codery/blob/master/Assets/s_dictionary.png)

- ### **Calculator**

![Codery Help](https://github.com/Soumi7/codery/blob/master/Assets/s_calculator.png)

- ### **Jobs**

![Codery Help](https://github.com/Soumi7/codery/blob/master/Assets/s_jobs.png)

## License

Copyright (c) 2020 Souvik Biswas and Soumi Bardhan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
