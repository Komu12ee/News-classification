import logging
import os
from datetime import datetime
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path=os.path.join(os.getcwd(),"log",LOG_FILE)
os.makedirs(log_path,exist_ok=True)


LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,

)

#  ................GPT CODE ................................
# import os
# import logging
# from datetime import datetime

# # Use a writable location
# LOG_DIR = os.path.join("/tmp", "log")
# os.makedirs(LOG_DIR, exist_ok=True)

# LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# LOG_PATH = os.path.join(LOG_DIR, LOG_FILE)

# logging.basicConfig(
#     filename=LOG_PATH,
#     level=logging.INFO,
#     format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"
# )

# logger = logging.getLogger(__name__)