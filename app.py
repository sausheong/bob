import logging
from dotenv import load_dotenv
load_dotenv()

from server import server

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    # start server
    server.run("127.0.0.1", 3721, debug=True)
