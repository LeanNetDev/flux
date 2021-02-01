import os 
import pynetbox

nb = pynetbox.api(
    'http://localhost:8000',
    token='0123456789abcdef0123456789abcdef01234567'
)

def get_devices():
     devices = nb.dcim.devices.all()
     return devices