### 문제 정의

OBB(Oriented Bounding Boxes)를 구현하기 위해 백본 모델로는 transformer를 이용하는 DETR를 고려했으나, 해당 모델은 크기가 큰 객체를 탐지할 때 성능이 좋고 학습하는데 오랜시간이 걸린다. 또한 Boundling boxes의 모양과 각도를 함께 학습하는 기존 OBB model들은 추론해야 할 값이 많기 때문에 많은 데이터와 오랜 학습시간이 걸린다. 따라서 해당 공모전을 해결하기 위해서 두가지의 문제를 해결해야 한다.

- 크기가 작은 객체를 탐지할 수 있어야 한다.
- 학습시간이 적어야 한다.

위의 두 문제를 동시에 해결하기 위해 도입된 모델은 Single-Stage Rotation-Decoupled Detector for Oriented Object라는 논문에서 소개한 모델이다.

### 논문 리뷰

- transformers를 사용하지 않기 때문에 학습시간이 적게 들고 작은 객체를 탐지할 수 있다. 또한 각도(Rotation)와 Bounding Boxes를 분리하여 학습하기 때문에 학습시간이 적게 들고 Bounding Boxes의 모양을 탐지하는데 유리하다.

### 데이터 시각화
detect_nms.ipynb

### 데이터 증강
data_augumentation.ipynb

### 앙상블
detect_nms.ipynb
