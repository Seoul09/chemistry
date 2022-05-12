import time # 시간 딜레이를 위해 다른 곳에서 함수를 가져온것
import os 

# element_list는 원자 번호를 저장하는 것 입니다
element_list = { 'H' : 1, 'He' : 2, "Li" : 3, "Be" : 4, "B" : 5,
                 'C' : 6, "N" : 7, 'O' : 8, "F" : 9, "Ne" : 9, "Na" : 10,
                'Mg' : 11 }

electric_list = { 'H' : 2.2, 'He' : 0, "Li" : 1.0, "Be" : 1.6, "B" : 2.0,
                 'C' : 2.6, "N" : 3.0, 'O' : 3.4, "F" : 4.0, "Ne" : 0, "Na" : 0.9,
                'Mg' : 1.3, 'Al' : 1.6, 'Sl' : 1.9, 'P' : 2.2, 'S' : 2.6, 'Cl': 3.2,
                'K' : 0.8, 'Ca' : 1.0}


print("안녕하세요! 화학 I 수업을 듣고 만든 프로그램 입니다.")
print()
time.sleep(2)
print("3초후 프로그램이 실행 됩니다.")
time.sleep(3)

while ( True ) :
    os.system("cls")
    print("----- 화학 계산기 -----")
    print()
    print("1 : 원자 번호를 계산하는 프로그램 입니다.")
    print("2 : 전기 음성도를 계산해 주는 프로그램 입니다.")
    print()
    num = int(input("사용 하고 싶은 프로그램 번호를 입력해주세요! = "))
    
    if (num == 1) : # 원자량 계산 프로그램
        print("----- 원자량 계산 프로그램 -----")
        print( )
        element = input("검색 하고 싶은 원자를 적어주세요 = ")
        print("당신이 검색한 원자의 원자 번호는 " + str(element_list[element]) + "입니다")
        time.sleep(2)
        print("3초 후에 프로그램이 닫힙니다.")
        time.sleep(3)

    if (num == 2) : # 전기 음성도 계산 프로그램
        print("----- 전기 음성도 계산 프로그램 -----")
        print( )
        print("만약 여러가지 원소의 전기 음성도의 대소관계를 비교하고 싶으면 공백으로 입력해주세요 예시 ) H C Na")
        electric = input("검색 하고 싶은 원자를 적어주세요 = ").split(" ")
        if (len(electric) == 1 ) :
            print("당신이 검색한 원자의 전기 음성도는" + str(electric_list[electric]) + "입니다")
        else :
            print("원소를 여러개 입력하셔서 원소의 대소 관계를 구하겠습니다 ! :)")
            electric_big_and_small = [] 
            for i in electric:
                electric_big_and_small.append(electric_list[i])
            print("입력하신 원소의 전기 음성도는 아래를 참고해주세요")
            print(electric)
            print(electric_big_and_small)
            time.sleep(2)
            print("대소 관게를 하겠습니다! 잠시만 기다려주시면 결과를 알려드리겠습니다." )
            sorted(electric_big_and_small)
            time.sleep(2)
            print("대소 관게를 파악하였습니다! 잠시만 기다려주시면 결과를 알려드리겠습니다." )
            time.sleep(2)
            print(electric_big_and_small)
        # print("당신이 검색한 원자의 원자 번호는 " + str(element_list[element]) + "입니다")
        # time.sleep(2)
        # print("3초 후에 프로그램이 닫힙니다.")
        time.sleep(3)
