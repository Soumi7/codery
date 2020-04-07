class MyBotHandler(object):
    '''
    This plugin will allow users to get latest contents
         on competitive coding sites like hackerearth 
         and hackerrank.  
    '''

    def usage(self):
        return '''
        This plugin will allow users to get latest contents
        on competitive coding sites like hackerearth and hackerrank.  
        Users should preface messages with "@followup".
        Before running this, make sure to create a stream
        called "followup" that your API user can send to.
        '''
    def handle_message(self, message, bot_handler):
        original_content = message['content']
        original_sender = message['sender_email']
        new_content = original_content.replace('@followup',
                                            'from %s:' % (original_sender,))

        bot_handler.send_message(dict(
            type='stream',
            to='followup',
            subject=message['sender_email'],
            content=new_content,
        ))

        bot_handler.send_message(dict(
        type='stream', # can be 'stream' or 'private'
        to=stream_name, # either the stream name or user's email
        subject=subject, # message subject
        content=message, # content of the sent message
        ))

        bot_handler.update_message(dict(
        message_id=self.message_id, # id of message to be updated
        content=str(self.number), # string with which to update message with
        ))

        bot_handler.storage.put("foo", "bar")  # set entry "foo" to "bar"

        bot_handler.storage.put("foo", "bar")
        print(bot_handler.storage.get("foo")) 

        bot_handler.storage.contains("foo")  # False
        bot_handler.storage.put("foo", "bar")
        bot_handler.storage.contains("foo")  # True



handler_class = MyBotHandler
