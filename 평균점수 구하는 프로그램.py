#평균 점수 구하는 프로그램 
subject =int(input("과목 수를 입력 하세요"))
#과목의 수를 입력 
subjectsum = 0

for repetition in range(subject):
    score = input("과목의 점수를 입력하세요")
#과목 수 만큼 점수를 입력
    subjectsum = int(score)+int(subjectsum)
#입력한 점수들의 합
print("당신의 평균 점수는",subjectsum // subject,"입니다.")
#입력한 점수들의 합을 입력한 과목의 수로 나눔
