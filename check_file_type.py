def check_file_type(file_name):
    try:
        f = open(file_name, "rb")
        line1 = f.readline()
        line2 = f.readline()
        line3 = f.readline()

        print(get_file_type(line1, line2, line3))
    except FileNotFoundError as rnf:
        return rnf


def get_file_type(line1, line2, line3):
    #\x89PNG\r\n
    if line1[0:6] == b'\x89\x50\x4E\x47\x0D\x0A' and line2[0:2] == b'\x1A\x0A':
        return 'PNG'
    # 8BPS
    elif line1[0:4] == b'\x38\x42\x50\x53':
        return 'PSD'
    elif line1[0:2] == b'\xFF\xD8':
        return 'JPG'
    elif line1[0:2] == b'\x42\x4D':
        return 'BMP'
    elif line1[0:4] == b'\x00\x00\x01\x00':
        return 'ICO'
    elif line1[0:4] == b'\x00\x00\x01\xBA':
        return 'MPG'
    else:
        print(line1)
        print(line2 == b'\x1A\x0A')

    return None


check_file_type("D:\\ERP 원본 다운로드\\20210114_210001501_2.pdf")
#check_file_type("D:\\ERP 원본 다운로드\\20200713_171227567_2.psd")
#check_file_type("C:\\Esko\\bg_prog_egsis_v010\\uninstall\\esko.ico")
#check_file_type("C:\\ImageMagick\\1111.jpg")
#check_file_type("C:\\LEADTOOLS 20\\Bin\\Common\\JobProcessor\\Media\\Input\\DaDa_DVD_MPEG2.mpg")
