import os
import subprocess 
import time

from django.conf import settings
from pathlib import Path
from stats.logger import logger
from stats.models import CurrentMission

GAME_SERVER_PATH = settings.GAME_SERVER_PATH
GAME_SDS_PATH = '_wings_of_liberty.sds'
GAME_SERVER_BIN = 'DServer.exe'
GAME_BANLIST_BIN = 'RConGen.exe'
FAILURE_TIME_OUT = 3 * 60
MAX_DURATION = 3 * 3600 + FAILURE_TIME_OUT

def stop_server():
    os.system('taskkill /im ' + GAME_BANLIST_BIN)
    os.system('taskkill /im ' + GAME_SERVER_BIN)

def start_server():
    startup_path = Path(GAME_SERVER_PATH).joinpath('bin', 'game')
    binary_path = startup_path.joinpath(GAME_SERVER_BIN)
    subprocess.Popen([binary_path.as_posix(), GAME_SDS_PATH], cwd=startup_path.as_posix())
    return True

def check_server(server_failure_timestamp):
    try:
        current_mission = CurrentMission.objects.all()[0]
    except IndexError:
        current_mission = None

    if current_mission is None or current_mission.duration > MAX_DURATION:
        if server_failure_timestamp == 0:
           return time.time()
        elif time.time() - server_failure_timestamp > FAILURE_TIME_OUT:
           logger.info('restarting the server...')
           stop_server()
           time.sleep(60)
           start_server()
           return 0

    return server_failure_timestamp