def grade():
    marks = int(input("enter the marks: "))
    if 90<= marks <=100:
        print('A')
    elif 80<= marks < 90:
        print('B')
    elif 70<= marks < 80:
         print('C')
    elif 60<= marks < 70:
         print('D')
    else:
         print('F')
    

if __name__ == "__main__":
    grade()    