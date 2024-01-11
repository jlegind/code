import os
import threading
import re

import win32file
import win32con

ACTIONS = {
    1 : "Created"
    # 2 : "Deleted",
    # 3 : "Updated",
    # 4 : "Renamed from something",
    # 5 : "Renamed to something"
}

# Thanks to Claudio Grondi for the correct set of numbers
FILE_LIST_DIRECTORY = 0x0001

def watch(path, fn, excludes):
    print("monitoring: %s" % path)
    hdir = win32file.CreateFile (
        path,
        FILE_LIST_DIRECTORY,
        win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
        None,
        win32con.OPEN_EXISTING,
        win32con.FILE_FLAG_BACKUP_SEMANTICS,
        None
        )
    while True:
        #
        # readdirectorychangesw takes a previously-created
        # handle to a directory, a buffer size for results,
        # a flag to indicate whether to watch subtrees and
        # a filter of what changes to notify.
        #
        # nb tim juchcinski reports that he needed to up
        # the buffer size to be sure of picking up all
        # events when a large number of files were
        # deleted at once.
        #
        results = win32file.ReadDirectoryChangesW (
            hdir,
            1024,
            True,
            win32con.FILE_NOTIFY_CHANGE_FILE_NAME |
            win32con.FILE_NOTIFY_CHANGE_DIR_NAME |
            win32con.FILE_NOTIFY_CHANGE_ATTRIBUTES |
            win32con.FILE_NOTIFY_CHANGE_SIZE |
            win32con.FILE_NOTIFY_CHANGE_LAST_WRITE |
            win32con.FILE_NOTIFY_CHANGE_SECURITY,
            None,
            None
        )

        excluded = True

        for action, file in results:
            full_filename = os.path.realpath(os.path.join (path, file))
            print(full_filename, ACTIONS.get (action, "unknown"))

            # find if file and is not excluded by any excludes
            if not os.path.isdir(full_filename):
                if excluded:
                    excluded = any([re.search(e, full_filename) for e in excludes])

        if not excluded:
            fn()

def onchange(path, fn, excludes=[]):
    """ Calls 'fn' when there is any change in the path """
    thread = threading.Thread(target = lambda: watch(path, fn, excludes))
    thread.daemon = True
    thread.start()

if __name__ == '__main__':
    path = r'N:\SCI-SNM-DigitalCollections\DaSSCo\DigiApp\Data\test_monitor'
    # for j in onchange(path, ['pyc$', '.log$']):
    #     print(j)
    ch = onchange(path, lambda: print('i see a change'), ['pyc$', '.log$'])
    # for j in ch:
    #     print(j)
    import time
    time.sleep(40)
