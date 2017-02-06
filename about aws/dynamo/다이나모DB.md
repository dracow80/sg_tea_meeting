다니아모 DB
===========
**for python**

- 설치 모듈: boto3, awscli 모듈
```pip install boto3 awscli```

- aws cli 통한 키 등록(Access key ID, Secret access key, Default region name)
```aws configure ```
- 다이나모 DB 기본 설명 페이지: 
	- https://docs.aws.amazon.com/ko_kr/amazondynamodb/latest/developerguide/Introduction.html
- boto3 기본 사용법
	- https://boto3.readthedocs.io/en/latest/ 
- 테이블 구조
	- 2가지 기본키
		- 파티션키
		- 파티션키 및 정렬키
- 테이블 설계 참고사항
	- https://docs.aws.amazon.com/ko_kr/amazondynamodb/latest/developerguide/GuidelinesForTables.html
	- 테이블의 항목에 대한 균일한 데이터 액세스를 위한 설계
	- 파티션 동작 이해
- 인덱스
	- https://docs.aws.amazon.com/ko_kr/amazondynamodb/latest/developerguide/SecondaryIndexes.html
	- 글로벌 보조 인덱스
	- Local Secondary Index
	- 각 5개씩만 지원
- 테이블 생성 / 데이터 입력 샘플 코드
	- create_dynamo_table.py
	- test_dynamo_table.py
- CloudWatch 사용
- 리전 간 복제
	- https://github.com/awslabs/dynamodb-cross-region-library
	- https://aws.amazon.com/ko/blogs/korea/dynamodb-update-triggers-streams-lambda-cross-region-replication-app/
	- https://aws.amazon.com/ko/blogs/korea/how-to-cross-region-replication-in-dynamodb/

	- 아파치 메이븐 설치
	    - https://maven.apache.org/download.cgi#
    - java se 설치(1.7+)
	    - http://www.oracle.com/technetwork/java/javase/overview/index.html
	- git dynamodb-cross-region-library 소스 저장    
		- https://github.com/awslabs/dynamodb-cross-region-library
	- dynamodb-cross-region-library 설치
	    - mvn install
	- aws 다이나모DB 테이블 스트림 세팅
		- New and old images
	- 컴파일 된 dynamodb-cross-region-replication-1.1.0.jar 실행
		- ```java -jar dynamodb-cross-region-replication-1.1.0.jar --sourceEndpoint dynamodb.ap-northeast-2.amazonaws.com --sourceTable AchievementState --destinationEndpoint dynamodb.ap-northeast-1.amazonaws.com --destinationTable AchievementState-tokyo```
		- ```java -jar dynamodb-cross-region-replication-1.1.0.jar --sourceEndpoint dynamodb.ap-northeast-1.amazonaws.com --sourceTable AchievementState-tokyo --destinationEndpoint dynamodb.ap-northeast-2.amazonaws.com --destinationTable AchievementState```

--------------------------------
**기타**

- 데이터 쓰기상의 주의
	- PutItem — 새 항목을 만듭니다. 동일 키의 항목이 테이블이 이미 존재하는 경우 해당 항목이 새 항목으로 대체됩니다. 테이블 이름과 작성할 항목을 지정해야 합니다.
	- UpdateItem — 이 작업은 해당 항목이 없으면 새 항목을 생성합니다. 그렇지 않으면, 기존 항목의 속성을 수정합니다. 수정할 항목의 키와 테이블 이름을 지정해야 합니다. 업데이트할 각 속성마다 새 값을 지정해야 합니다.
- 이외의 확장 기능들
	- AWS CloudTrail를 사용하여 DynamoDB 작업 로깅
	- AWS Data Pipeline을 사용하여 DynamoDB 데이터 내보내기 및 가져오기
	- Amazon EMR를 사용한 테이블 쿼리 및 조인


---------------
**추가항목**

- 사용 비용 계산
	- 읽기 용량
		- 읽기 용량 단위 1은 초당 strongly consistent read 1 또는 초당 eventually consistent read 2(최대 4 KB 크기 항목의 경우)를 나타냅니다. 4 KB보다 큰 항목을 읽어야 하는 경우, DynamoDB가 추가 읽기 용량 단위를 사용해야 합니다. 필요한 총 읽기 용량 단위 수는 항목 크기 및 eventually consistent read와 strongly consistent read 중 어느 것을 원하는지에 따라 달라집니다.
	- 쓰기 용량
		- 쓰기 용량 단위 1은 최대 크기가 1 KB인 항목에 대해 초당 쓰기 1을 나타냅니다. 1 KB보다 큰 항목을 써야 하는 경우, DynamoDB가 추가 쓰기 용량 단위를 사용해야 합니다. 필요한 총 쓰기 용량 단위 수는 항목 크기에 따라 결정됩니다.
	- 인덱스
		- 보조 인덱스가 있는 테이블의 경우 DynamoDB가 추가 용량 단위를 사용합니다. 예를 들어 단일 1 KB 항목을 테이블에 추가하고 해당 항목에 인덱싱된 속성이 있는 경우, 두 개의 쓰기 용량 단위가 필요합니다. 하나는 테이블 쓰기용이고 다른 하나는 인덱스 쓰기용입니다.
- 원자적 증가값 설정
- 컬럼 최대크기
	- 각 컬럼(항목)은 400KB 를 넘을 수 없다
- 다이나모 네이밍 규칙 
- 읽기 일관성
	- Eventually Consistent Read
		- 최근의 완료된 쓰기 작업이 반영되지 않을 수 있음
	- Strongly Consistent Read
		- 성공한 모든 이전 쓰기 작업의 업데이트를 반영하여 가장 최신 데이터로 응답을 반환