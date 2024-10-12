# 사용자에게 수학 점수를 입력받아
# 상/중/하 반으로 분류
# 90점 이상
# 70점 이상
# 나머지



# size = int(input())
# print(size)
#
# if size > 100:
#     print("잘못된 점수입니다.")
# elif size >= 90:
#     print("상")
# elif size >= 70:
#     print("중")
# else:
#     print("하")

#예제 1번

# a = int(input())
#
#
# if a % 2 != 0:
#     print("홀수입니다.")
# else:
#     print("짝수입니다.")


# 예제 2번



# 예제 3번



print("당신은 주말에 보통 무엇을 하며 시간을 보내세요?\n1. 집에서 쉬는 편이다\n2. 친구들과 약속을 잡아 나가는 편이다")
a = input()
if a == 1:
    M = "I"
    print("갑자기 상공에 외계인이 나타난다면?\n1. 어쩌면 인간 친화적인 외계인일지도..?\n2. 외계인이 왜 나타나냐")
    b = input()
    if b == 1:
        B = "N"
        print("슬픔을 둘로 나누면?\n1. 슬과 픔 \n2. 슬픔이 떨어진다")
        c = input()
        if c == 1:
            T = "T"
            print("계획했던 식당이 갑자기 휴무면?\n1. 근처 아무 식당이나 간다 \n2. 이미 Plan B가 있다")
            d = input()
            if d == 1:
                I = "P"
            elif d == 2:
                I = "J"
            else:
                print("1번 혹은 2번만 골라주세요")

        elif c == 2:
            T = "F"
            print("계획했던 식당이 갑자기 휴무면?\n1. 근처 아무 식당이나 간다 \n2. 이미 Plan B가 있다")
            d = input()
            if d == 1:
                I = "P"
            elif d == 2:
                I = "J"
            else:
                print("1번 혹은 2번만 골라주세요")
        else:
            print("1번 혹은 2번만 골라주세요")

    elif b == 2:
        B = "T"
        print("슬픔을 둘로 나누면?\n1. 슬과 픔 \n2. 슬픔이 떨어진다")
        c = input()
        if c == 1:
            T = "T"
            print("계획했던 식당이 갑자기 휴무면?\n1. 근처 아무 식당이나 간다 \n2. 이미 Plan B가 있다")
            d = input()
            if d == 1:
                I = "P"
            elif d == 2:
                I = "J"
            else:
                print("1번 혹은 2번만 골라주세요")

        elif c == 2:
            T = "F"
            print("계획했던 식당이 갑자기 휴무면?\n1. 근처 아무 식당이나 간다 \n2. 이미 Plan B가 있다")
            d = input()
            if d == 1:
                I = "P"
            elif d == 2:
                I = "J"
            else:
                print("1번 혹은 2번만 골라주세요")
        else:
            print("1번 혹은 2번만 골라주세요")
    else:
        print("1번 혹은 2번만 골라주세요")


elif a == 2:
    M = "I"
    print("갑자기 상공에 외계인이 나타난다면?\n1. 어쩌면 인간 친화적인 외계인일지도..?\n2. 외계인이 왜 나타나냐")
    b = input()
    if b == 1:
        B = "N"
        print("슬픔을 둘로 나누면?\n1. 슬과 픔 \n2. 슬픔이 떨어진다")
        c = input()
        if c == 1:
            T = "T"
            print("계획했던 식당이 갑자기 휴무면?\n1. 근처 아무 식당이나 간다 \n2. 이미 Plan B가 있다")
            d = input()
            if d == 1:
                I = "P"
            elif d == 2:
                I = "J"
            else:
                print("1번 혹은 2번만 골라주세요")

        elif c == 2:
            T = "F"
            print("계획했던 식당이 갑자기 휴무면?\n1. 근처 아무 식당이나 간다 \n2. 이미 Plan B가 있다")
            d = input()
            if d == 1:
                I = "P"
            elif d == 2:
                I = "J"
            else:
                print("1번 혹은 2번만 골라주세요")
        else:
            print("1번 혹은 2번만 골라주세요")

    elif b == 2:
        B = "T"
        print("슬픔을 둘로 나누면?\n1. 슬과 픔 \n2. 슬픔이 떨어진다")
        c = input()
        if c == 1:
            T = "T"
            print("계획했던 식당이 갑자기 휴무면?\n1. 근처 아무 식당이나 간다 \n2. 이미 Plan B가 있다")
            d = input()
            if d == 1:
                I = "P"
            elif d == 2:
                I = "J"
            else:
                print("1번 혹은 2번만 골라주세요")

        elif c == 2:
            T = "F"
            print("계획했던 식당이 갑자기 휴무면?\n1. 근처 아무 식당이나 간다 \n2. 이미 Plan B가 있다")
            d = input()
            if d == 1:
                I = "P"
            elif d == 2:
                I = "J"
            else:
                print("1번 혹은 2번만 골라주세요")
        else:
            print("1번 혹은 2번만 골라주세요")
    else:
        print("1번 혹은 2번만 골라주세요")

mbti = M+B+T+I

print(mbti)