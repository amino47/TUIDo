from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Checkbox, Button
from textual.containers import HorizontalGroup, VerticalScroll
from textual.reactive import reactive

class TUIDo(App):
    """A Textual app to manage stopwatches."""
    CSS_PATH = "main.tcss"
    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("a", "add_item", "Add a new item to the list"),            
    ]

    class Item(HorizontalGroup):
        """A widget to represent an item in the list."""

        def compose(self) -> ComposeResult:
            """Create child widgets for the item."""
            yield Checkbox("Item", id="item_checkbox")
            yield Button("Remove", variant="error", id="remove_button")

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield VerticalScroll(self.Item(), id="item_list")
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )
    def action_add_item(self) -> None:
        """An action to add a new item to the list."""
        self.VerticalScroll.append(self.Item())

if __name__ == "__main__":
    app = TUIDo()
    app.run()
