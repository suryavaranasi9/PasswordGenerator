from fastapi import FastAPI, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from typing import Union
from PasswordGenerator import pwdg2

description = """
Random Password Generator API. 🚀
## Endpoints
* **password**
* **list of passwords**

You can request a random **password** or **list of passwords** and tweak it with custom parameters.
"""

tags_metadata = [
    {
        "name": "Password Generators",
        "description": "Random Password Generators",
    }
]

app = FastAPI(
    title="Password Generator",
    description=description,
    version="0.2",
    contact={
        "name": "Surya Varanasi",
        "url": "https://www.linkedin.com/in/suryavaranasi9/",
        "email": "suryavaranasi97@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    }, openapi_tags=tags_metadata
)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:4200/",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    return RedirectResponse("/main_page")

@app.get("/main_page", summary="Main Page", tags=['Views'])
async def root():
    """
        Main Page
    """
    html_content = """
        <html>

    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <!-- Tailwind CSS -->
        <link href="https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css" rel="stylesheet">
        <title>Password Generator</title>
    </head>

    <body>
        <main class="min-h-full bg-cover bg-top sm:bg-top"
            style="background-image: url('https://www.w3schools.com/w3images/ocean2.jpg');">
            <div class="max-w-7xl mx-auto px-4 py-16 text-center sm:px-6 sm:py-24 lg:px-8 lg:py-48">
                <p class="text-sm font-semibold text-black text-opacity-50 uppercase tracking-wide">Welcome to Page</p>
                <h1 class="mt-2 text-4xl font-extrabold text-white tracking-tight sm:text-5xl">Click Below options for API Page.
                </h1>
                <p class="mt-2 text-lg font-medium text-black text-opacity-50">
                Welcome to my Random Password API
                </p>
                <div class="mt-6">
                    <a href="docs"
                        class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-black text-opacity-75 bg-white bg-opacity-75 sm:bg-opacity-25 sm:hover:bg-opacity-50">
                        Go to Interactive Page
                    </a>
                </div>

                <div class="mt-6">
                    <a href="redoc"
                        class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-black text-opacity-75 bg-white bg-opacity-75 sm:bg-opacity-25 sm:hover:bg-opacity-50">
                        ReDoc
                    </a>
                </div>
                <div class="mt-6">
                    <a href="http://127.0.0.1:8000/password"
                        class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-black text-opacity-75 bg-white bg-opacity-75 sm:bg-opacity-25 sm:hover:bg-opacity-50">
                        Output API Response Page
                    </a>
                </div>
            </div>
        </main>
    </body>

    </html>
        """

    return HTMLResponse(content=html_content, status_code=200)

@app.get("/password", summary="Get a randomly generated password", tags=['Password Generators'])
async def read_item(pwd_length: Union[int,None] = 5,
                    use_symbols: Union[bool,None] = True,
                    use_numbers: Union[bool,None] = True,
                    use_letters: Union[bool,None] = True,
                    num_of_passwords: Union[int,None] = 3,
                    strange_header: str = Header(None)) -> JSONResponse:
    """
    Requires Params:<br>
    - pwd_length: (int) Length of password to be generated.
    - use_symbols: (bool) Whether or not to use symbols in pwd generation
    - use_symbols: (bool) Whether or not to use symbols in pwd generation
    - use_symbols: (bool) Whether or not to use symbols in pwd generation
    - num_of_passwords: (int) Number of passwords to be generated

    Returns:<br>
    - randomly generated password or a list of passwords

    """

    generator = pwdg2.PasswordGenerator()
    pwd = generator.generate_password(p_length=pwd_length, use_symbols=use_symbols,
                                                     use_numbers=use_numbers, use_letters=use_letters,num_of_pass=num_of_passwords)
    response = {"password": pwd}
    return JSONResponse(response)
