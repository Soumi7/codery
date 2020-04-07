'''
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
'''

# See readme.md for instructions on running this code.

from typing import Any, Dict

class HelloWorldHandler(object):
    def usage(self) -> str:
        return '''
        This is a boilerplate bot that responds to a user query with
        "beep boop", which is robot for "Hello World".

        This bot can be used as a template for other, more
        sophisticated, bots.
        '''

    def handle_message(self, message: Dict[str, Any], bot_handler: Any) -> None:
        content = 'beep boop'  # type: str
        bot_handler.send_reply(message, content)

handler_class = HelloWorldHandler