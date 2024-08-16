import fastapi


router = fastapi.APIRouter()


@router.get("/sections/{id}")
async def get_section(id: int):
    return {"courses": []}


@router.post("/sections/{id}/content-blocks")
async def read_section_content_blocks():
    return {"courses": []}


@router.post("/content-blocks/{id}")
async def read_content_blocks():
    return {"courses": []}
