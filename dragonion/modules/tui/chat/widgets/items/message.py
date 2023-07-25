from textual.app import ComposeResult
from textual.widgets import Static, Label

from datetime import datetime


class Avatar(Static):
    DEFAULT_CSS = """
    Avatar {
        width: auto;
    }
    """

    def __init__(self, symb: str):
        self.symb = symb
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Label(f"({self.symb}) ")


class MessageHeader(Static):
    DEFAULT_CSS = """
    MessageHeader {
        layout: horizontal;
        background: $boost;
        width: auto;
    }
    """

    def compose(self) -> ComposeResult:
        yield Label(f"[bold]{self.renderable}[/]")
        yield Label(" ")
        yield Label(f"[#a5abb3][{datetime.now().time().strftime('%H:%M:%S')}][/]")


class MessageContent(Static):
    DEFAULT_CSS = """
    MessageContent {
        layout: horizontal;
    }
    
    .dock-right {
        dock: right;
    }
    """

    def compose(self) -> ComposeResult:
        yield Static(self.renderable)
        yield Static(
            f"[#a5abb3][{datetime.now().time().strftime('%H:%M:%S')}][/]",
            classes='dock-right'
        )


class TextMessage(Static):
    def __init__(self, author: str, message: str):
        self.author = author
        self.message = message
        super().__init__()

    def compose(self) -> ComposeResult:
        yield MessageHeader(self.author)
        yield MessageContent(self.message)


class Message(Static):
    DEFAULT_CSS = """
    Message {
        layout: horizontal;
        margin-bottom: 1;
    }
    """

    def __init__(self, avatar: str, author: str, message: str):
        self.avatar = avatar
        self.author = author
        self.message = message
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Avatar(symb=self.avatar)
        yield TextMessage(
            author=self.author,
            message=self.message
        )

    def add_message(self, message: str):
        self.query_one(TextMessage).mount(
            MessageContent(message)
        )