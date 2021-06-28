import requests
from notify import TelegramBot
from datetime import date, datetime
from time import sleep
import logging

from config import config

telegram_bot = TelegramBot(
    token=config["telegram"]["token"],
    chat_id=config["telegram"]["chat_id"])


# Configure loggers
logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('application.log')
fh.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.addHandler(fh)


def check_appointments() -> None:
    """ Access appointment endpoint and check if an earlier appointment
        exists than specified in configuration """

    current_date = date.today()
    start_date = current_date.strftime("%Y-%m-%d")

    appointment_endpoint = config["target"]["appointment_url"].format(
        start_date=start_date, end_date=config["target"]["latest_data"])

    result = requests.get(appointment_endpoint, cookies=get_cookies()).json()

    for available_date in result["available_days"]:
        logger.info(available_date)
        appointment_date = available_date["day"]
        telegram_bot.send_message(f"Earlier appointment available at \
            {appointment_date}!")


def get_cookies() -> requests.sessions.RequestsCookieJar:
    """ Access the main page and return regular cookies """
    result = requests.get(config["target"]["start_url"])
    return result.cookies


while True:
    check_appointments()

    current_hour = datetime.now().hour
    night_start = config["interval"]["night_start"]
    night_end = config["interval"]["night_end"]
    night_enabled = config["interval"]["night_enabled"]

    if night_enabled and (
        (night_start > night_end and
            (current_hour < night_end or current_hour >= night_start)) or
        (night_start < night_end and
            current_hour >= night_start and current_hour < night_end)):
        logger.info(f"Next check in {config['interval']['night']} minutes")
        sleep(config['interval']['night'] * 60)
    else:
        logger.info(f"Next check in {config['interval']['day']} minutes")
        sleep(config['interval']['day'] * 60)
