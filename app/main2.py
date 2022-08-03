from fastapi import FastAPI, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from typing import Union
from PasswordGenerator import pwdg2

description = """
Random Password Generator API. 🚀
## Endpoints
* **password / list of passwords**

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
                Welcome to my Random Password Generator API
                </p>
                <div class="mt-6">
                    <a href="docs"
                        class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-black text-opacity-75 bg-white bg-opacity-75 sm:bg-opacity-25 sm:hover:bg-opacity-50">
                        Go to Interactive API
                    </a>
                </div>

                <div class="mt-6">
                    <a href="redoc"
                        class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-black text-opacity-75 bg-white bg-opacity-75 sm:bg-opacity-25 sm:hover:bg-opacity-50">
                        ReDocly Page
                    </a>
                </div>
                <div class="mt-6">
                    <a href="http://127.0.0.1:8000/password"
                        class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-black text-opacity-75 bg-white bg-opacity-75 sm:bg-opacity-25 sm:hover:bg-opacity-50">
                        Default API Response Page
                    </a>
                </div>
                <div class="mt-6">
                    <a href="http://127.0.0.1:8000/uiform"
                        class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-black text-opacity-75 bg-white bg-opacity-75 sm:bg-opacity-25 sm:hover:bg-opacity-50">
                        GUI Form for API Inputs
                    </a>
                </div>
                </div>                
            </div>
        </main>
    </body>

    </html>
        """

    return HTMLResponse(content=html_content, status_code=200)

@app.get("/uiform", summary="UI Representation with Actions")
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
            
<div class="flex flex-col text-center">
    <h1 class="text-2xl font-bold text-blue-600 dark:text-green-100">Password Generator</h1>
    <h2 class="text-lg font-semibold text-gray-600 dark:text-green-200">A random Password Generation API built using
        Python and FastAPI.</h2>
</div>
<div class="flex-column mx-auto mt-8 flex">
    <div>
        <form>
            <fieldset class="text-center">
                <legend class="text-base font-medium text-gray-900 dark:text-blue-100">Configure Your Password</legend>
                <div class="mt-4 space-y-4">
                    <div class="flex items-center">
                        <div class="ml-3 text-sm"><label for="password_length"
                                class="font-medium text-gray-700 dark:text-blue-200">Password Length</label></div>
                        <div class="ml-2 flex h-auto items-center"><input id="password_length" name="password_length"
                                type="number" min="1"
                                class="form-input h-fit w-16 rounded border-gray-300 p-1 text-center font-semibold text-gray-800 focus:ring-blue-500 dark:bg-black/60 dark:text-slate-100 md:text-left"
                                value="5"></div>
                    </div>
                    <div class="ml-8 flex items-start md:ml-12">
                        <div class="flex h-5 items-center"><input id="use_letters" name="use_letters" type="checkbox"
                                class="h-4 w-4 rounded border-gray-300 text-blue-600 focus:ring-blue-500">
                        </div>
                        <div class="ml-3 text-sm"><label for="use_letters"
                                class="font-medium text-gray-700 dark:text-blue-200">Use Letters</label></div>
                    </div>
                    <div class="ml-8 flex items-start md:ml-12">
                        <div class="flex h-5 items-center"><input id="use_numbers" name="use_numbers" type="checkbox"
                                class="h-4 w-4 rounded border-gray-300 text-blue-600 focus:ring-blue-500">
                        </div>
                        <div class="ml-3 text-sm"><label for="use_numbers"
                                class="font-medium text-gray-700 dark:text-blue-200">Use Numbers</label></div>
                    </div>
                    <div class="ml-8 flex items-start md:ml-12">
                        <div class="flex h-5 items-center"><input id="use_symbols" name="use_symbols" type="checkbox"
                                class="h-4 w-4 rounded border-gray-300 text-blue-600 focus:ring-blue-500">
                        </div>
                        <div class="ml-3 text-sm"><label for="use_symbols"
                                class="font-medium text-gray-700 dark:text-blue-200">Use Symbols</label></div>
                    </div>
                    <div class="flex items-center">
                        <div class="ml-3 text-sm"><label for="number_of_passwords"
                                class="font-medium text-gray-700 dark:text-blue-200">Number of Passwords</label></div>
                        <div class="ml-2 flex h-auto items-center"><input id="number_of_passwords" name="number_of_passwords"
                                type="number" min="1"
                                class="form-input h-fit w-16 rounded border-gray-300 p-1 text-center font-semibold text-gray-800 focus:ring-blue-500 dark:bg-black/60 dark:text-slate-100 md:text-left"
                                value="3"></div>
                    </div>                    
                </div>
            </fieldset>
            <div class="my-4 flex justify-center"><button type="submit" onclick="PasswordCall()"
                    class="
            w-full md:w-auto items-center px-4 py-2 text-white
            border drop-shadow-xl text-base font-medium rounded-md 
            focus:outline-none focus:ring-2 focus:ring-offset-2 border-transparent disabled:opacity-50 disabled:text-slate-600focus:ring-blue-600 bg-blue-500/75 hover:bg-blue-500 dark:bg-blue-900 dark:hover:bg-blue-700">
                    <div class="align-middle">Get Password</div>
                </button></div>
        </form>
    </div>
</div>
<div class="my-4 mx-4 flex flex-row justify-center break-all px-2">
    <div></div>
</div>    
    <script type="text/javascript">
        function PasswordCall(){
            let plength = document.getElementById("password_length").value;
            var usymbol_T = document.getElementById("use_symbols");
            if (usymbol_T.checked) {
                usymbol=true;
            } else {
                alert("Symbol CheckBox not checked.");
                usymbol=false;
            }
            var uletter_T = document.getElementById("use_letters");
            if (uletter_T.checked) {
                uletter=true;
            } else {
                alert("Letter CheckBox not checked.");
                uletter=false;
            }
            var unumber_T = document.getElementById("use_numbers");
            if (unumber_T.checked) {
                unumber=true;
            } else {
                alert("Number CheckBox not checked.");
                unumber=false;
            }            
            let numpass = document.getElementById("number_of_passwords").value;
            let url = 'http://127.0.0.1:8000/password?pwd_length=' + plength + '&use_letters=' + uletter + '&use_numbers=' + unumber + '&use_symbols=' + usymbol + '&num_of_passwords=' + numpass ;
            window.open(url, '_blank');
        }
    </script>
    
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
