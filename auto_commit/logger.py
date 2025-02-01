import logging

def setup_logger():
    """
    Set up a basic logger. (editted).
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    return logging.getLogger()