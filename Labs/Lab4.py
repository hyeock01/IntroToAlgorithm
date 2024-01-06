""" Guessing Game """
import random


def guessing_game():
    """
    단계
    1단계 랜덤 값을 생성한다
    2단계 값을 입력 받는다
    2.5단계 미시오를 보고 당겼는지 확인한다
    3단계 랜덤 값보다 큰지 작은지 정답인지 비교한다
    4단계 오답일때 비교한 결과의 범위를 알려준다 / 정답일때 얼마나 걸렸는지 알려주며 축하해준다
    5단계 2단계로 돌아간다
    """
    low = 1
    high = 100
    cnt = 1
    answer = random.randint(1,100)

    while low <= high:
        innput = get_int(low,high)

        if innput < low or innput > high:
            print('out')
        elif answer > innput:
            low = innput + 1
        elif answer < innput:
            high = innput - 1
        elif answer == innput:
            print(f'good job {cnt} try')
            break
        cnt += 1


def get_int(start, end) -> int:
    while True:
        try:
            ball = int(input(f'Enter your guess from {start} to {end}:'))
        except ValueError as e:
            print(f'입력된 값이 정확하지 않습니다.')
            print(f'{e}')
        except KeyboardInterrupt as e:
            print(f'입력된 값이 없습니다.')
            print(f'{e}')
        except:
            print('알 수 없는 에러')
        else:
            break
    return ball


# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':
    guessing_game()
