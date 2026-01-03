import sys
import os

# Add the extension directory to Python path
extension_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if extension_dir not in sys.path:
    sys.path.insert(0, extension_dir)

from ulauncher.api.shared.action.BaseAction import BaseAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction

from src.password import generate_password


class GeneratePasswordAction(BaseAction):

    def __init__(self, length: int):
        self.length = length

    def run(self):
        password = generate_password(self.length)
        return CopyToClipboardAction(password)