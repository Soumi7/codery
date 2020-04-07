


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
        content = 'Hey there! I am codery!'  # type: str
        bot_handler.send_reply(message, content)

handler_class = HelloWorldHandler