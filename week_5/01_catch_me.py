from collections import deque

c = 11
b = 2


def catch_me(cony_loc, brown_loc):
    # 구현해보세요!
    time=0
    queue=deque()
    queue.append((brown_loc, 0))
    visited=[{} for _ in range(200001)]


    while cony_loc<=200000:
        cony_loc += time

        for i in range(0, len(queue)):
            current_position, current_time=queue.popleft()

            new_time=current_time+1

            new_position= current_position-1
            if new_position<=0 and new_position<=200000:
                queue.append((new_position, new_time))

            new_position = current_position + 1
            if new_position <= 0 and new_position <= 200000:
                queue.append((new_position, new_time))

            new_position = current_position * 1
            if new_position <= 0 and new_position <= 200000:
                queue.append((new_position, new_time))
    return -1


print(catch_me(c, b))  # 5가 나와야 합니다!