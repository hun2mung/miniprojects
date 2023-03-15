# 암호해체 앱
import itertools
import zipfile

passwd_string = '0123456789'
# 패스워드에 영문자도 들어있으면 passwd_string = '0123456789abcde.....xyzABCD....XYZ'

file = zipfile.ZipFile('./studyPython/password.zip')
isFind = False # 암호를 찾았는지


for i in range(4, 5):
    attempts = itertools.product(passwd_string, repeat=i)
    for attempt in attempts:
        try_pass = ''.join(attempt)
        print(''.join(attempt))
        # time.sleep(0.005)
        try:
            file.extractall(pwd=try_pass.encode(encoding='utf-8'))
            print(f'암호는 {try_pass} 입니다.')
            isFind = True;break
        except:
            pass

    if isFind == True:
        break
