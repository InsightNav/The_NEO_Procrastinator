import sys
from colorama import Fore, init

from core import fetch_data, extract_metrics, get_urgency

init(autoreset=True)


METER_WIDTH = 10


def build_meter(level: int) -> str:
    """Return ASCII urgency meter."""
    filled = level * 3
    empty = METER_WIDTH - filled
    return f"[{'■' * filled}{'□' * empty}] Level {level}"

#bit of ui ;)
def get_color(level: int):
    """Return terminal color based on urgency level."""
    colors = {
        1: Fore.GREEN,
        2: Fore.YELLOW,
        3: Fore.RED,
    }
    return colors.get(level, Fore.WHITE)


def display(metrics, level: int, message: str) -> None:
    """Render output to terminal."""
    color = get_color(level)

    asteroid_count, diameter, distance, hazardous = metrics

    print("\n=== CELESTIAL CLOCK ===")
    print("-" * 40)

    print(f"Asteroids Today  : {asteroid_count}")
    print(f"Closest Distance : {distance:.2f} LD")
    print(f"Largest Size     : {diameter:.2f} m")
    print(f"Hazardous        : {'Yes' if hazardous else 'No'}")

    print("\nURGENCY")
    print(color + build_meter(level))

    print("\nVERDICT")
    print(color + message)

    print("-" * 40)


def main():
    """Application entry point."""
    force_refresh = "--refresh" in sys.argv

    data = fetch_data(force_refresh)
    metrics = extract_metrics(data)

    asteroid_count, diameter, distance, hazardous = metrics
    level, message = get_urgency(distance, diameter, hazardous)

    display(metrics, level, message)


if __name__ == "__main__":
    main()