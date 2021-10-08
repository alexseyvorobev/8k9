def convert(chis):
            b=''
            while chis>0:
                    b=str(chis % x) + b
                    chis=chis//x
            print(b)
try:
    print("Введите нужную систему счисления до девятиричной")
    x=int(input())
    print("Введите число для перевода в другую систему счисления")
    chis=int(input())
except ValueError:
    print("Incorrect value")
    exit()
if (x<10) & (chis> -1):
    convert(chis)
else:
    print("Данная система счисления или число пока что не добавлены в систкму, введите другое значение")
