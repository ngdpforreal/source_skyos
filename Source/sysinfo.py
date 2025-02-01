import os

def get_system_info():
    info = {
        "os_name": os.name,
        "platform": os.sys.platform,
        "release": os.uname().release,
        "version": os.uname().version,
        "machine": os.uname().machine,
        "processor": os.uname().processor
    }
    return info

    system_info = get_system_info()
    for key, value in system_info.items():
        print(f"{key}: {value}")