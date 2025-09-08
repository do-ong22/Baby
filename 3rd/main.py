# main.py
# 필요한 도구들을 가져오기
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 서버 만들기 (마치 가게를 차리는 것과 같아요)
app = FastAPI(title="내가 만든 첫 번째 서버", version="1.0.0")

# CORS 설정 (다른 웹사이트에서도 우리 서버를 쓸 수 있게 해주는 설정)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],# 모든 사이트에서 접근 허용
    allow_credentials=True,
    allow_methods=["*"],# 모든 방식의 요청 허용
    allow_headers=["*"],# 모든 종류의 데이터 허용
)

# 메인 페이지 만들기
@app.get("/")
# "/"는 메인 주소를 의미해요
def 메인페이지():
    return {"message": "안녕하세요! 제 서버에 오신 걸 환영합니다! 🎉"}

# 이 코드를 @app.get("/") 아래에 추가해주세요
@app.get("/ping")
def 서버_상태_확인():
    """서버가 살아있는지 확인하는 창구예요"""
    return {
        "message": "pong! 서버가 살아있어요! 🏓",
        "status": "정상 작동 중"
    }
    
    
# 이 코드를 ping 함수 아래에 추가해주세요
@app.get("/items")
def 상품_목록_가져오기():
    """우리 가게의 모든 상품을 보여주는 창구예요"""

# 우리 가게의 상품들 (진짜 데이터베이스 대신 임시로 만든 목록)
    우리가게_상품들 = [
        {"id": 1, "name": "게이밍 노트북", "price": 1200000, "category": "전자제품"},
        {"id": 2, "name": "기계식 키보드", "price": 150000, "category": "전자제품"},
        {"id": 3, "name": "게이밍 마우스", "price": 80000, "category": "전자제품"},
        {"id": 4, "name": "모니터 27인치", "price": 300000, "category": "전자제품"},
        {"id": 5, "name": "높이조절 책상", "price": 200000, "category": "가구"}
    ]

# 상품 목록과 개수를 함께 보내주기
    return {
        "items": 우리가게_상품들,
        "count": len(우리가게_상품들),# len()은 리스트의 개수를 세어주는 함수
        "message": f"총 {len(우리가게_상품들)}개의 상품이 있어요!"
    }
    

# 이 코드를 items 함수 아래에 추가해주세요
@app.get("/items/{item_id}")
def 특정_상품_찾기(item_id: int):
    """특정 번호의 상품만 찾아주는 창구예요"""

# 같은 상품 목록 (나중에 실제 데이터베이스에서 가져올 거예요)
    우리가게_상품들 = [
        {"id": 1, "name": "게이밍 노트북", "price": 1200000, "category": "전자제품"},
        {"id": 2, "name": "기계식 키보드", "price": 150000, "category": "전자제품"},
        {"id": 3, "name": "게이밍 마우스", "price": 80000, "category": "전자제품"},
        {"id": 4, "name": "모니터 27인치", "price": 300000, "category": "전자제품"},
        {"id": 5, "name": "높이조절 책상", "price": 200000, "category": "가구"}
    ]

# 요청받은 번호와 같은 상품 찾기
    for 상품 in 우리가게_상품들:
        if 상품["id"] == item_id:
            return {
                "item": 상품,
                "message": f"{상품['name']}을(를) 찾았어요!"
            }

# 찾는 상품이 없으면
    return {
        "error": f"{item_id}번 상품을 찾을 수 없어요 😅",
        "message": "다른 번호로 다시 시도해보세요!"
    }
    
# 이 코드를 위 함수들 아래에 추가해주세요
@app.get("/search")
def 상품_검색하기(q: str = ""):
    """상품 이름으로 검색하는 창구예요"""

    모든_상품들 = [
        {"id": 1, "name": "게이밍 노트북", "price": 1200000},
        {"id": 2, "name": "기계식 키보드", "price": 150000},
        {"id": 3, "name": "게이밍 마우스", "price": 80000},
        {"id": 4, "name": "모니터 27인치", "price": 300000},
        {"id": 5, "name": "높이조절 책상", "price": 200000}
    ]

# 검색어가 없으면 모든 상품 보여주기
    if not q:# q가 비어있으면
        return {
            "items": 모든_상품들,
            "message": "모든 상품을 보여드릴게요!",
            "search_term": "전체"
        }

# 상품 이름에 검색어가 포함된 것들만 찾기
    찾은_상품들 = []
    for 상품 in 모든_상품들:
        if q in 상품["name"]:# 검색어가 상품 이름에 포함되어 있나?
            찾은_상품들.append(상품)# 포함되어 있으면 결과에 추가

    return {
        "items": 찾은_상품들,
        "count": len(찾은_상품들),
        "search_term": q,
        "message": f"'{q}'(으)로 검색한 결과 {len(찾은_상품들)}개를 찾았어요!"
    }
