#!/usr/bin/python3
# source: https://wiki.ubuntu.com/DownloadService/DownloadManager#Code_Examples

from gi.repository import GLib
import dbus
from dbus.mainloop.glib import DBusGMainLoop

DBusGMainLoop(set_as_default=True)

MANAGER_PATH = '/'
MANAGER_IFACE = 'com.canonical.applications.DownloadManager'
DOWNLOAD_IFACE = 'com.canonical.applications.Download'
IMAGE_FILE = 'http://i.imgur.com/y51njgu.jpg'


def download_created(path):
    """Deal with the download created signal."""
    print('Download created in %s' % path)


def finished_callback(path, loop):
    """Deal with the finis signal."""
    print('Download performed in "%s"' % path)
    loop.quit()


def progress_callback(total, progress):
    """Deal with the progress signals."""
    print('Progress is %s/%s' % (progress, total))

if __name__ == '__main__':

    bus = dbus.SessionBus()
    loop = GLib.MainLoop()
    manager = bus.get_object('com.canonical.applications.Downloader',
            MANAGER_PATH)
    manager_dev_iface = dbus.Interface(manager, dbus_interface=MANAGER_IFACE)

    # ensure that download created works
    manager_dev_iface.connect_to_signal('downloadCreated', download_created)

    down_path1 = manager_dev_iface.createDownload((IMAGE_FILE, "", "",
        dbus.Dictionary({}, signature="sv"),
        dbus.Dictionary({}, signature="ss")))
    down_path2 = manager_dev_iface.createDownload((IMAGE_FILE, "", "",
        dbus.Dictionary({}, signature="sv"),
        dbus.Dictionary({}, signature="ss")))
    down_path3 = manager_dev_iface.createDownload((IMAGE_FILE, "", "",
        dbus.Dictionary({}, signature="sv"),
        dbus.Dictionary({}, signature="ss")))

    download1 = bus.get_object('com.canonical.applications.Downloader',
            down_path1)
    download2 = bus.get_object('com.canonical.applications.Downloader',
            down_path2)
    download3 = bus.get_object('com.canonical.applications.Downloader',
            down_path3)

    download_dev_iface1 = dbus.Interface(download1, dbus_interface=DOWNLOAD_IFACE)
    download_dev_iface2 = dbus.Interface(download2, dbus_interface=DOWNLOAD_IFACE)
    download_dev_iface3 = dbus.Interface(download3, dbus_interface=DOWNLOAD_IFACE)

    # connect to signals
    download_dev_iface1.connect_to_signal('progress', progress_callback)
    download_dev_iface2.connect_to_signal('progress', progress_callback)
    download_dev_iface3.connect_to_signal('progress', progress_callback)
    download_dev_iface3.connect_to_signal('finished',
            lambda path: finished_callback(path, loop))

    download_dev_iface1.start()
    download_dev_iface2.start()
    download_dev_iface3.start()

    loop.run()

