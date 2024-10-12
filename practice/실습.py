# 사용자에게 수학 점수를 입력받아
# 상/중/하 반으로 분류
# 90점 이상
# 70점 이상
# 나머지

size = int(input())
print(size)

if size > 100:
    print("잘못된 점수입니다.")
elif size >= 90:
    print("상")
elif size >= 70:
    print("중")
else:
    print("하")