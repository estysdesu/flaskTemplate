import os
import sys
import server


def main():
    server.app.logger.info("server starting")
    server.app.run()


if __name__ == "__main__":
    sys.exit(main())
