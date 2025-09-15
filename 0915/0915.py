# select python interpreter -> 아나콘다 가상환경 설정 (base)

# 필요 패키지 설치
# pip install -r requirements.txt

import os
import langchain
import yaml
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# api_key.yml 파일에서 API 키를 로드
with open('api_key.yml', 'r') as file:
    config = yaml.safe_load(file)

os.environ["OPENAI_API_KEY"] = config['api_key']

# llm 호출 테스트
llm = ChatOpenAI(
    model_name="gpt-4o", # 모델명
    max_tokens = 5000, # 최대 출력 토큰 수
    temperature = 1 # 답변의 창의성(0에 가까울수록 일관된 답변, 0~2)
    )

response = llm.invoke("저는 중요한 발표를 앞두고 너무 긴장돼서 아무것도 손에 잡히지 않습니다. 머릿속에는 '내가 실수하면 어떡하지?'라는 생각만 가득해요. 이 불안감을 어떻게 다스려야 할까요?")

# response를 그대로 print할 경우 AIMessage 객체 형태로서 llm 응답과 함꼐 메타 데이터도 같이 출력됨
# response.content 하면 메타 데이터를 제외한 응답 텍스트만 출력할 수 있음
# print(response)
# print('*'*100)
print(response.content)

# llm 체인 만들기
# llm 체인 = 프롬프트 + llm

# 프롬프트 정의
prompt = ChatPromptTemplate.from_template("당신은 20년 경력의 저명한 임상 심리학자입니다. 당신은 사람들이 겪는 복잡한 감정과 관계 문제를 깊이 이해하고 있습니다. 당신의 목표는 단순한 조언이 아닌, 내담자의 심리를 근본적으로 파악하고 변화를 위한 통찰력을 제공하는 것입니다. 항상 공감적이고 전문적인 언어를 사용하며, 내담자의 상황에 맞는 구체적인 심리학적 개념(예: 인지 왜곡, 방어기제, 애착 유형 등)을 들어 설명합니다.")
chain = prompt | llm

response = llm.invoke("저는 중요한 발표를 앞두고 너무 긴장돼서 아무것도 손에 잡히지 않습니다. 머릿속에는 '내가 실수하면 어떡하지?'라는 생각만 가득해요. 이 불안감을 어떻게 다스려야 할까요?")
print('*'*100)
print(response.content)