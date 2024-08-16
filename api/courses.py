import fastapi


router = fastapi.APIRouter()


@router.get("/courses")
async def get_courses():
    return {"courses": []}


@router.post("/courses")
async def create_course():
    return {"courses": []}