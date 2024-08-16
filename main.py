from fastapi import FastAPI, Path, Query

from api import users, sections, courses

app = FastAPI(
    title="FastAPI LMS",
    description="A simple LMS",
    version="0.0.1",
    contact={
        "name": "Tanvir Reza",
        "email": "mail@tanvirreza.me",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT"
    }

)

app.include_router(users.router)
app.include_router(sections.router)
app.include_router(courses.router)



