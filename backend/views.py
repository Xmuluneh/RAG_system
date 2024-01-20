from fastapi import APIRouter, HTTPException

main_router = APIRouter()

@main_router.post("/", response_model=dict)
async def index():
    response = {
        "data": None,
        "error": None
    }
    status_code = 404
    try:
        response["data"] = "answer"
        status_code = 200
    except Exception as error:
        response['error'] = {
            'message': str(error)
        }
    if response["error"]:
        raise HTTPException(status_code=status_code, detail=response["error"]["message"])
    return response
