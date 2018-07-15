# 구현 내용
# - 처음 파이썬 파일을 실행 시키면,
# 한식, 중식, 일식 중 한 가지를 고르라는 내용이 나옵니다.
# - 그 중에서 한 가지를 고르면 식당 이름을 하나 임으로 추천해 줍니다.

# 힌트
# - 리스트를 여러 개 사용하고 사용자의 입력을 받아야 합니다.
# - 리스트에서 데이터를 임으로 하나를 뽑는 방법은 크게 2가지가 있습니다.
# 그 중 어느 걸 사용하셔도 좋습니다.
# - 다만 강의 중에 해당 내용을 배우지 않았기 때문에,
# 인터넷 검색을 통해서 찾아보기시길 바랍니다.
# - 모든 것을 아는 개발자는 존재하지 않고요.
# 검색 능력도 개발자의 꼭 필요한 능력 중에 하나 입니다.
# - 검색 키워드 : random, randit, shuffle

import random

# 1) 리스트를 만든다.
KOREAN_FOOD = ("김치찌개", "비빔밥", "국수")
CHINESE_FOOD = ("짜장면", "탕수육", "짬뽕")
JAPANESE_FOOD = ("라멘", "돈까스", "돈부리")

# 2) 사용자로 부터 입력
user_choice = input("한식, 중식, 일식 중에서 골라주세요:")

# 3) 임의로 추천
if user_choice == "한식":
    choice_result = random.choice(KOREAN_FOOD)
elif user_choice == "중식":
    choice_result = random.choice(CHINESE_FOOD)
elif user_choice == "일식":
    choice_result = random.choice(JAPANESE_FOOD)
else:
    print("한식, 중식, 일식 중에서 선택하셔야 됩니다.")

if choice_result:
    print("{} 중에서 {}이 선택 되었습니다.".format(user_choice, choice_result))
