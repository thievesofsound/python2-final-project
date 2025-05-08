"""
Demonstrates a Rich "application" using the Layout and Live classes.

"""

from datetime import datetime
from rich.text import Text
import rich
from rich import box
from rich.align import Align
from rich.console import Console, Group
from rich.layout import Layout
from rich.panel import Panel
from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn
from rich.table import Table

console = Console()


def make_layout() -> Layout:
    """Define the layout."""
    layout = Layout(name="root")

    layout.split(
        Layout(name="main", ratio=1),
        Layout(name="footer", size=7),
    )
    layout["main"].split_row(
        Layout(name="body", ratio=4, minimum_size=60), Layout(name="side")
    )
    return layout


def make_python_project() -> Panel:
    """Some example content."""
    sponsor_message = Table.grid(padding=1)
    sponsor_message.add_column()
    sponsor_message.add_row(
    )
    sponsor_message.add_row()
    message_panel = Panel(
        Align.center(
            Group("\n", Align.center(sponsor_message)),
            vertical="top",
        ),
        box=box.ROUNDED,
        padding=(1, 2),
        title="[b white]Step 1 - Escaping Astana",
        border_style="bright_blue",
    )
    return message_panel

def new_func():
    return Panel(
            Text.assemble(
                "Astana, Kazakhstan is a country located in Asia and is known for its modernistic and futuristic architecture. Though its beauty is undeniable, the state of living is struggling, as anti-government militias are on the rise in Kazakhstan and placing various cities under strict rule. Astana is one of them.\n\nTo escape, you must ",
                (
                    "hitch a train to the US in the morning to avoid forced labor",
                    "bold purple",
                ),
                justify="center"
            ),
        )


job_progress = Progress(
    "{task.description}",
    SpinnerColumn(),
    BarColumn(),
    TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
)
job_progress.add_task("[green]Cooking")
job_progress.add_task("[magenta]Baking", total=200)
job_progress.add_task("[cyan]Mixing", total=400)

total = sum(task.total for task in job_progress.tasks)
overall_progress = Progress()
overall_task = overall_progress.add_task("All Jobs", total=int(total))

progress_table = Table.grid(expand=True)
progress_table.add_row(
    Panel(
        overall_progress,
        title="Overall Progress",
        border_style="green",
        padding=(2, 2),
    ),
    Panel(job_progress, title="[b]Jobs", border_style="red", padding=(1, 2)),
)


layout = make_layout()

layout["body"].update(make_python_project())
layout["side"].update(Panel(layout.tree, border_style="red"))
layout["footer"].update(progress_table)


from time import sleep

from rich.live import Live


def run():
    with Live(layout, refresh_per_second=10, screen=True):
        while True:
            pass


run()
