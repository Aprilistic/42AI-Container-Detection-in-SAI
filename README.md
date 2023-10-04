# 42AI

##한국항공우주연구원(KARI) 에서 주최한 위성영상을 활용한 컨테이너 탐지 경진대회의 흔적입니다

https://aifactory.space/task/2455/overview

주최측에서 매우 적은 데이터(200장)과 낮은 라벨링 품질의 데이터로 제한을 두어서 고민을 정말 많이 했습니다.

해결 아이디어는 
Oriented Bounding Box(OBB) + Image Segmentation 
두 모델의 결과를 Nom-maximum Suppression(NMS) 알고리즘을 통해 합치는 방법입니다.

42서울에서 모인 4명이 한 팀으로 참가했습니다.
모두 첫 인공지능 경진대회 참가였는데요, 8위라는 꽤 괜찮은 성적을 받았습니다.
리더보드에서 4224팀을 확인하실 수 있습니다.
https://aifactory.space/task/2455/leaderboard
