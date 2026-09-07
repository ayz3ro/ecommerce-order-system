from fastapi import FastAPI
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware

from api.v1.auth import router as auth_router

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"],
                   allow_headers=["*"], )

app.include_router(auth_router)



@app.get("/")
async def read_headers(request: Request):
    headers = dict(request.headers)
    cookies = dict(request.cookies)
    return headers, cookies

# Future will be added request handler for not allowed origins
# @app.middleware("http")
# async def check_origin(request: Request, call_next):
#     origin = request.headers.get("origin")
#     allowed_origins = {"http://localhost:5173", "http://127.0.0.1:5173"}
#     try:
#         if not origin:
#             return HTTPException(status_code=403, detail="Requests without Origin are not allowed")
#         if origin not in allowed_origins:
#             return HTTPException(status_code=403, detail=f"Origin {origin} is not allowed")
#     except HTTPException:
#         raise HTTPException(status_code=403, detail="Requests without Origin are not allowed")