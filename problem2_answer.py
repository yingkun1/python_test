"""
写一个函数将 ipv4 地址字符串 (仅包含数字，点) 转化成 32 位整数，要求输出合法地址的 32 位整型结果。
"""


def ipv4_to_int(address: str) -> int:
    iResult = 0
    str = ''
    i = 1
    bLastIsSpace = False
    bAfterDot = False
    setNumbers = set(['0','1','2','3','4','5','6','7','8','9'])
    for s in address:
        if s == ' ':
            bLastIsSpace = True
        elif (not bAfterDot) and bLastIsSpace and (s != ' ' and s != '.'):
            raise NameError('Error spaces')
        elif bAfterDot and s == ' ':
            bAfterDot = True
        elif s == '.':
            bLastIsSpace = False
            bAfterDot = True
            if str == '':
                raise NameError('Each address number should not be null')
            if len(str) > 3:
                raise NameError('Each address number should be 3-digits')
            iStr = int(str)
            if iStr > 255 :
                raise NameError('Each address number should in [0,255]')
            iResult = iResult << 8 ^ iStr
            i += 1
            str = ''
        elif s not in setNumbers:
            raise NameError('Each number should in [0-9]')
        else :
            bLastIsSpace = False
            bAfterDot = False
            str += s
    iResult = iResult << 8 ^ int(str)
    if i != 4:
        raise NameError('Invalid format of string, please make sure 4 address numbers are given')
    return iResult


if __name__ == "__main__":
    assert ipv4_to_int("0.0.0.0") == 0
    assert ipv4_to_int("192.168.0.0") == 3232235520
    assert ipv4_to_int("255.255.255.255") == 4294967295
    print('OK')
