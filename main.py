from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

from modules.netbox import get_devices

devices = get_devices()

print(devices[0])

for key in devices[0]:
    print(key)