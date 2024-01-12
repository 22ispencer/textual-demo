from typing import Any, Coroutine
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Button, Footer, Header, Static
from textual.binding import Binding


class DemoApp(App):

    CSS_PATH = "demo.tcss"

    BINDINGS = [
        Binding("q", "quit", "Quit the app", priority=True),
        ("d", "toggle_dark", "Toggle dark mode")
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="grid"):
            yield Button("1")
            yield Static("2")
            yield Static("3")
            yield Static("4")
            yield Static("5")
            yield Button("6-9", id="tall")
            yield Static("7-8", id="wide")
        yield Footer()

    def action_quit(self) -> Coroutine[Any, Any, None]:
        return super().action_quit()

    def action_toggle_dark(self) -> None:
        return super().action_toggle_dark()


if __name__ == "__main__":
    app = DemoApp()
    app.run()
