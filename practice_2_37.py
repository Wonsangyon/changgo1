# def profile(name, age, lang1, lang2, lang3, lang4, lang5) :
#     print("이름 : {0}\t 나이 : {1}\t".format(name, age), end=" ") #end확장자를 이용하여 두줄의 프린트문을 하나로 이음.
#     print(lang1, lang2, lang3, lang4, lang5)
#  
def profile(name, age, *language) :
    print("이름 : {0}\t 나이 : {1}\t".format(name, age), end=" ") #end확장자를 이용하여 줄바꿈을 하지 않음.
    for lang in language:
        print(lang, end=" ") #end확장자를 이용하여 줄바꿈을 하지 않음.
    print()
        
profile("유재석", 20, "python", "java", "c", "c++", "c#", "javascript")
profile("김태호", 25, "kotlin", "swift",)
profile("홍길동", 20, "python", "java", "c", "c++", "c#")


