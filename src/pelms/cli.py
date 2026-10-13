import argparse
from .core import preview


def main():

    parser = argparse.ArgumentParser(
        description="CLI to interact with the PELMS module"
    )

    subparsers = parser.add_subparsers()
    preview_parser = subparsers.add_parser("preview", help="Preview camera output")
    preview_parser.add_argument(
        "-t",
        "--time",
        default=0,
        type=int,
        help="Time to keep the preview open, 0 is forever",
    )

    args = parser.parse_args()
    preview(args.t)


if __name__ == "__main__":
    main()
