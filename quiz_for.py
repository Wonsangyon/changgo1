from random import *
cnt = 0 #총 탑승 승객 수
for i in range(1,51): # 1~50까지 수 i 생성 (승객)
     time = randrange(5,51) # 5분에서 50분 소요 시간을 랜덤으로 정함
     if 5 <= time <=15 : # 5분에서 15분이내의 손님 (매칭 성공), 탑승 승객 수 증가 처리
          print("[o] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
          cnt += 1
     else : # 매칭 실패한 경우 cnt증가 안 됌.
          print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

print("총 탑승 승객 : {0} 명".format(cnt))
print("github활용에 대하여 알아보자")
