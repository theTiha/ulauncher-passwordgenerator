from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
from ulauncher.api.shared.action.RunScriptAction import RunScriptAction

from src.password import generate_password

class DemoExtension(Extension):

    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []

        argument = event.get_argument() or ""
        argument = argument.strip()

        if not argument:
            items.append(
                ExtensionResultItem(
                    icon='images/icon.png',    
                    name = 'Password Generator',
                    description = 'Usage: pwg <length> (e.g. pwg 12)',
                )
            )
            return RenderResultListAction(items)
        
        if not argument.isdigit():
            items.append(
                ExtensionResultItem(
                    icon='images/icon.png',
                    name = 'Invalid input',
                    description = 'Length must be a number (e.g. pwg 12)',
                )
            )
            return RenderResultListAction(items)

        length = int(argument)

        password = generate_password(length)

        items.append(
            ExtensionResultItem(
                icon='images/icon.png',
                name=f'Password ({length} characters)',
                description='Press Enter to copy to clipboard',
                on_enter=CopyToClipboardAction(password)
            )
        )
        return RenderResultListAction(items)
    


if __name__ == '__main__':
    DemoExtension().run() 