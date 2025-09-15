# select python interpreter -> 아나콘다 가상환경 설정 (base)

# 필요 패키지 설치
# pip install -r requirements.txt

import os
import langchain
import yaml
from langchain_openai import ChatOpenAI

# api_key.yml 파일에서 API 키를 로드
with open('api_key.yml', 'r') as file:
    config = yaml.safe_load(file)

os.environ["OPENAI_API_KEY"] = config['api_key']

# llm 호출 테스트
llm = ChatOpenAI(
    model_name="gpt-4o-mini", # 모델명
    max_tokens = 512, # 최대 출력 토큰 수
    temperature = 0.5 # 답변의 창의성(0에 가까울수록 일관된 답변, 0~2)
    )

response = llm.invoke("버터쿠키 만드는 법 알려줘.")

# response를 그대로 print할 경우 AIMessage 객체 형태로서 llm 응답과 함꼐 메타 데이터도 같이 출력됨
# response.content 하면 메타 데이터를 제외한 응답 텍스트만 출력할 수 있음
# print(response)
# print('*'*100)
print(response.content)
