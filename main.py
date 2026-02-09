from core.sniffer import start
from rich.console import Console
from rich.panel import Panel
import os

console = Console()

def banner():
    console.print(
        Panel.fit(
            "[bold green]ALI ENGINE v2[/bold green]\n\n"
            "✔ Real-Time Firewall Protection\n"
            "✔ DNS & Traffic Monitoring\n"
            "✔ Automatic Threat Blocking\n\n"
            "[yellow]Must be run as Administrator[/yellow]",
            title="Cybersecurity Active",
            border_style="green"
        )
    )

if __name__ == "__main__":
    os.makedirs("logs", exist_ok=True)
    banner()
    start()
