# AI 기반 관광지 개선 솔루션
- 발표 영상: https://youtu.be/oel-aJcP8lI

![image](https://user-images.githubusercontent.com/86218931/144805140-0c0cceec-5ff5-40aa-9cce-b7db9f2e9a16.png)

## 요약
#### 1. 기획 의도
- '트레블 버블(비격리 여행 권역)' 체결과 '위드 코로나'에 따라 해외 여행객의 국내 여행이 점차 늘어날 것으로 예상 
- 관광객들의 실제 경험이 담긴 온라인 리뷰를 수집한 뒤, 리뷰 분석 결과를 바탕으로 기존 관광 시설의 재정비에 필요한 정보를 국내 관광 시설 관계자들에게 제공하고자 함

#### 2. 리뷰 데이터셋 구축
- 신뢰성 있는 리뷰만 게시되도록 자체 검증 시스템을 보유하고 있는 네이버 플레이스, 구글 맵스, 트립어드바이저에서 총 64곳 관광지, 관광지 리뷰 154,449건 수집 (데이터 전처리 후 122,495건 확보)
- 리뷰 수집 대상 관광지: 사전조사 시 3곳 사이트 총 리뷰 합계 3,000건 이상인 관광지 선정
- Fine-tuning을 위한 Data Labeling 12,000건 진행 (긍정 4,000건, 중립 4,000건, 부정 4,000건) 

![image](https://user-images.githubusercontent.com/86218931/144810757-73c74ca8-3c62-491a-8f10-210fd1f0bbc0.png)

#### 3. Fine-tuning
- ETRI(https://aiopen.etri.re.kr/service_dataset.php) 에서 제공하는 한국어 BERT 언어모델 API를 신청하여 의도분류 Fine-tuning을 진행 
- 어절 기반 BERT 학습 모델 - tensorflow 버전 사용(004_bert_eojeol_tensorflow)

![image](https://user-images.githubusercontent.com/86218931/144810643-d5cb6d0b-d093-4216-a68f-8a64de3c4074.png)
![image](https://user-images.githubusercontent.com/86218931/144810676-2b7d7dae-3d1b-4439-bc77-59ceab20a941.png)

#### 4. 대시보드 구축
- Figma로 UI 디자인 작업 후, Django로 웹 구현
- 구글 맵스 API를 통해 관광지의 위치 정보 수집 후 mapping
- 테마별/관광지별 목록을 게시한 후 테마/관광지 선택 시 해당 페이지로 이동
- 테마별/관광지별 리뷰의 긍정/중립/부정 비율 그래프 게시
- 구축된 AI 모델을 직접 시현해 볼 수 있는 리뷰 분석기 창 구현
- 관광지별 대시보드 페이지에서는 관광지별 부정 리뷰에 대한 워드 클라우드와 이를 기반으로한 솔루션 제공  

<테마별 대시보드 페이지>
![image](https://user-images.githubusercontent.com/86218931/144812177-432ee701-6ee2-45c9-8a21-3925d54e9f8a.png)

<관광지별 대시보드 페이지>
![image](https://user-images.githubusercontent.com/86218931/144812245-39b693e9-0768-4834-9299-f8fe1e3f4b67.png)


