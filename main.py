import eyed3
import os
import sys
from collections import UserDict


def strip_nulls(data):
    """strip whitespace and nulls"""
    #return str(object=data.strip(), encoding='utf-8', errors='strict')
    return str(object=data.strip(), encoding='euc_kr', errors='strict')


class FileInfo(UserDict):
    """store file metadata"""
    def __init__(self, filename=None):
        UserDict.__init__(self)
        self["name"] = filename


class MP3FileInfo(FileInfo):
    """store ID3v1.0 MP3 tags"""
    tagDataMap = {"title": (3,  33, strip_nulls),
                  "artist": (33,  63, strip_nulls),
                  "album": (63,  93, strip_nulls),
                  "year": (93,  97, strip_nulls),
                  "comment": (97, 126, strip_nulls),
                  "genre": (127, 128, ord)}

    def __parse(self, filename):
        """parse ID3v1.0 tags from MP3 file"""
        self.clear()
        try:
            f_sock = open(filename, "rb", 0)
            try:
                f_sock.seek(-128, 2)
                tag_data = f_sock.read(128)
            finally:
                f_sock.close()

            #if tag_data[:3] == "TAG":
            for tag, (start, end, parse_func) in self.tagDataMap.items():
                try:
                    self[tag] = parse_func(tag_data[start:end])
                except Exception as ex:
                    self[tag] = 'exception: %s' % ex
        except IOError:
            pass

    def __setitem__(self, key, item):
        if key == "name" and item:
            self.__parse(item)
        FileInfo.__setitem__(self, key, item)


def list_directory(directory, file_ext_list):
    """get list of file info objects for files of particular extensions"""
    file_list = [os.path.normcase(f) for f in os.listdir(directory)]
    file_list = [os.path.join(directory, f) for f in file_list if os.path.splitext(f)[1] in file_ext_list]

    def get_file_info_class(filename, module=sys.modules[FileInfo.__module__]):
        """get file info class from filename extension"""
        subclass = "%sFileInfo" % os.path.splitext(filename)[1].upper()[1:]
        return hasattr(module, subclass) and getattr(module, subclass) or FileInfo

    result = []

    return [get_file_info_class(f)(f) for f in file_list]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for info in list_directory("D:\\Musics\\20190402 - 4월 2주\\", [".mp3"]):
        print("\n".join(["%s=%s" % (k, v) for k, v in info.items()]))
        print()
