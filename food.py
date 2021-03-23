# 로또를  산다
# 번호 1, 2, 3 아무꺼나 정해서
# 당첨 번호를 선택 해서 결과를 출력

### 아래 전체를 반복 ###
for i in range(1,4):
    print("로또를 사자")
    print("번호는? ")
    print("1.당첨 2.2등 3.꽝")
    menu = input(i + ".입력: ")
    if menu == '1':
        print("당첨")
    if menu == '2':
        print("2등")
    if menu == '3':
        print("꽝")
### 여기까지 반복 ###