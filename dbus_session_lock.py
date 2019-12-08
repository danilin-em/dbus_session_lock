"""DBus Display Manager Session Lock

File: dbus_session_lock.py

@author Evgenii Danilin <evgenii.danilin.m@gmail.com

"""

import dbus  # type: ignore


SERVICE_NAME = 'org.freedesktop.DisplayManager'
SERVICE_PATH = '/org/freedesktop/DisplayManager/Session0'


def get_session_iface():
    bus = dbus.SystemBus()
    proxy = bus.get_object(SERVICE_NAME, SERVICE_PATH)
    return dbus.Interface(proxy, dbus_interface=SERVICE_NAME+'.Session')


def lock():
    session_iface = get_session_iface()
    session_iface.Lock()


def main():
    lock()


if __name__ == '__main__':
    main()
