#학교 클래스 만들기
#클래스는 이름, 설립연도, 주소라는 정보를 가지고 있어야함.
#클래스 활성화시, 위 3가지 데이터 반드시 입력하도록 처리.

class School:
    founder = "Gwaing"

    def __init__(self, name, year, adress):
        self.name = name
        self.year = year
        self.adress = adress

school1 = School("개발" , "2018", "newyork")

print(school1.name)
print(school1.year)
print(school1.adress)
