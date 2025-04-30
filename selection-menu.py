from textual.app import App, ComposeResult, RenderResult
from textual.widgets import Label, Button
from rich_pixels import Pixels
from textual.containers import *
from rich.console import Console
from rich.segment import Segment
from rich.style import Style

console = Console()

class CodeView(Widget):
    """Widget to display Python code."""

    DEFAULT_CSS = """
    CodeView { height: auto; }
    """

    code = reactive("")

    def render(self) -> RenderResult:

    # Draw your shapes using any character you want
        grid = """\

                                                                                                     
                                                                                                     
        GGGGGGGGGGGGG                                     ffffffffffffffff                           
     GGG::::::::::::G                                    f::::::::::::::::f                          
   GG:::::::::::::::G                                   f::::::::::::::::::f                         
  G:::::GGGGGGGG::::G                                   f::::::fffffff:::::f                         
 G:::::G       GGGGGG   ooooooooooo      ooooooooooo    f:::::f       ffffffyyyyyyy           yyyyyyy
G:::::G               oo:::::::::::oo  oo:::::::::::oo  f:::::f              y:::::y         y:::::y 
G:::::G              o:::::::::::::::oo:::::::::::::::of:::::::ffffff         y:::::y       y:::::y  
G:::::G    GGGGGGGGGGo:::::ooooo:::::oo:::::ooooo:::::of::::::::::::f          y:::::y     y:::::y   
G:::::G    G::::::::Go::::o     o::::oo::::o     o::::of::::::::::::f           y:::::y   y:::::y    
G:::::G    GGGGG::::Go::::o     o::::oo::::o     o::::of:::::::ffffff            y:::::y y:::::y     
G:::::G        G::::Go::::o     o::::oo::::o     o::::o f:::::f                   y:::::y:::::y      
 G:::::G       G::::Go::::o     o::::oo::::o     o::::o f:::::f                    y:::::::::y       
  G:::::GGGGGGGG::::Go:::::ooooo:::::oo:::::ooooo:::::of:::::::f                    y:::::::y        
   GG:::::::::::::::Go:::::::::::::::oo:::::::::::::::of:::::::f                     y:::::y         
     GGG::::::GGG:::G oo:::::::::::oo  oo:::::::::::oo f:::::::f                    y:::::y          
        GGGGGG   GGGG   ooooooooooo      ooooooooooo   fffffffff                   y:::::y           
                                                                                  y:::::y            
                                                                                 y:::::y             
                                                                                y:::::y              
                                                                               y:::::y               
                                                                              yyyyyyy                
                                                                                                     
        """

# Map characters to different characters/styles
        mapping = {
            "G": Segment(" ", Style.parse("yellow on yellow")),
            "o": Segment(" ", Style.parse("on white")),
            "f": Segment(" ", Style.parse("on blue")),
            "y": Segment(" ", Style.parse("on green")),
            ":": Segment(" ", Style.parse("on red"))
        }

        # Syntax is a Rich renderable that displays syntax highlighted code
        syntax =Pixels.from_ascii(grid, mapping) 
        return syntax

class QuestionApp(App[str]):
    CSS_PATH = "selection-menu.tcss"
    def compose(self) -> ComposeResult:
        with Vertical(id='selection-menu-ascii'):
            yield CodeView()
            yield Vertical(
                Label("Which adventure game which you want?", id='selection-label'),
                Button("Story 1 - Direct", id="direct", variant="default"),
                Button("Story 2 - Egypt", id="egypt", variant="default"),
                Button("Story 3 - Belarus", id='belarus'),
                id='selection-menu'
            )
    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(event.button.id)


if __name__ == "__main__":
    app = QuestionApp()
    reply = app.run()
    print(reply)
