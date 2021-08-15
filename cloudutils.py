import pymem
import win32gui

class NeteaseMusicUtils:
    """
    Helper class to retrieve info about current song
    """
    def __init__(self, currOffset=0x93EB38, maxLenOffset=0x967DA8):
        """Initialize the helper class with current version offsets

        Args:
            currOffset (hexadecimal, optional): Address offset for current time of song. Defaults to 0x93EB38.
            maxLenOffset (hexadecimal, optional): Address offset for length of song. Defaults to 0x967DA8.
        """
        self.currOffset = currOffset
        self.maxLenOffset = maxLenOffset
        self.pm = pymem.Pymem('cloudmusic.exe')
        self.EntryPoint = self.getEntryPoint()

    def getEntryPoint(self):
        """Get entry point for cloudmusic.dll

        Returns:
            int: EntryPoint
        """
        modules = list(self.pm.list_modules())
        for module in modules:
            if module.name == 'cloudmusic.dll':
                return module.lpBaseOfDll

    def getTime(self) -> dict:
        """Get timings of song

        Returns:
            dict: A dictionary of current, length and difference of playing song
        """
        curr = self.pm.read_double(self.EntryPoint + self.currOffset)
        maxlen = self.pm.read_double(self.EntryPoint + self.maxLenOffset)
        diff = maxlen - curr
        return {"curr": curr, "maxlen": maxlen, "diff": diff}

    def getCurrentSong(self) -> str:
        """Returns title of current song

        Returns:
            str: Song title
        """
        return win32gui.GetWindowText(win32gui.FindWindow('OrpheusBrowserHost', None))

