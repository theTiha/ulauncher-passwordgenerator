from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

import string
import secrets

def generate_password(length):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

class DemoExtension(Extension):

    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        item = []

        argument = event.get_argument() or ""
        argument = argument.strip()

        if not argument:
            item.append(
                ExtensionResultItem(
                    icon='images/icon.png',    
                    name = 'Password Generator',
                    description = 'Usage: pwg <length> (e.g. pwg 12)',
                )
            )
            return RenderResultListAction(item)
        
        if not argument.isdigit():
            item.append(
                ExtensionResultItem(
                    icon='images/icon.png',
                    name = 'Invalid input',
                    description = 'Length must be a number (e.g. pwg 12)',
                )
            )
            return RenderResultListAction(item)

        length = int(argument)

        item.append(
            ExtensionResultItem(
                icon='images/icon.png',
                name=f'Generate password ({length} characters)',
                description='Press Enter to generate',
            )
        )
        return RenderResultListAction(item)

if __name__ == '__main__':
    DemoExtension().run() 