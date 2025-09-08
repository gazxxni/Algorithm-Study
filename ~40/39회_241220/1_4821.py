import sys

while True:
    total_page = int(input())

    if total_page == 0:  # 입력이 0이면 루프 종료
        break

    visited = [False] * (total_page + 1)  # 각 페이지가 인쇄 대상인지 기록 / O(n)

    print_list = input().rstrip().split(',')  # 쉼표로 나눠 리스트 저장

    for print_range in print_list:  # print_list의 크기가 m이면 O(m)

        if '-' in print_range:  # '-' 이 포함된 경우

            low, high = map(int, print_range.split('-'))

            for i in range(low, high + 1):  # 가장 큰 페이지의 범위는 total_page 크기로 n -> O(n)
                if i <= total_page:  # 전체 페이지를 넘지 않는 경우
                    visited[i] = True 

            continue 
        
        # 단일 페이지 지정인 경우
        page = int(print_range)

        if page <= total_page:  # 전체 페이지를 넘지 않는 경우
            visited[page] = True

    # 이중 for문으로 O(mn)
    
    print(visited.count(True))

