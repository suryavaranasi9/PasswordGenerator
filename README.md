# Password Manager 🗃

## What is this all about? 💬
This is a small scale OSS project to practice with and make something that might look cool on a resume 📝.<br>


## What you need to know:
- This app is written in Python 3.9. 
- Main purpose of this program \[currently\] is to act as a web integrated and mobile, random password generator. (Just for fun why not? 🙈)
 
- I've chosen to use [`FastApi`](https://fastapi.tiangolo.com/) as our API framework for the backend python functionality. but at some point Id like to make a [GraphQl](https://graphql.org/) version too. (Maybe someone can commit? 👥)

- ***<span style="color:red; ">Important 💥</span>***
Please see the [`CONTRIBUTING.md`](docs/CONTRIBUTING.md) guidelines before pushing to any branches on this repo.

### Usage:
- see [`FastApi`](https://fastapi.tiangolo.com/) for in depth api details.
- Ensure you have a *local virtual environment* setup and `pip install -r requirements`.
- navigate to the **src** folder and run the following command:
    - `uvicorn main2:app --reload`
- This will start a locally hosted server at **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**
- Google Chrome or Firefox can be used to open the above URL.
- you can then make requests to the api by specifying a url with parameters if need be.
- To see what requests can be made navigate to the `/docs` page where you will be greeted with the beautiful **swaggerUI**.
- To see the endpoints navigate to to the `/password` page where you will find the API output
- If you are curious about how the raw OpenAPI schema looks like, FastAPI automatically generates a JSON (schema) with the descriptions of all your API.
**[http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json)**



### References:

- [FastApi](https://fastapi.tiangolo.com/)
- [Swagger UI](https://github.com/swagger-api/swagger-ui)
- [Contributing guidelines](docs/CONTRIBUTING.md)
- [Security](docs/CONTRIBUTING.md)
- [License](docs/CONTRIBUTING.md)


