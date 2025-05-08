# 표준체중 구하는 프로그램
#
def std_weight(height, gender) :
     if gender == '남자':
        return (height/100)*(height/100)*22
     else :
        return (height/100)*(height/100)*21

ht = float(input("키를 입력하세요 (cm) : ")) #input()으로 입력받은 값은 문자열이므로 float로 변환
gd = input("남자이면 남자, 여자이면 여자를 입력하세요 : ")
weight = round(std_weight(ht, gd),2)
print("키 {0}cm {1}의 표준 체중은 {2}kg입니다.".format(ht, gd, weight))

# for num in range(1,21) :
#     print("대기번호 : "+ str(num).zfill(3))

# answer = input("아무 값이나 입력하세요 : ") # input으로 받게 되면 항상 문자열로 받음
# print(type(answer))  
# print("입력한 값은 : "+ answer +"입니다.")
