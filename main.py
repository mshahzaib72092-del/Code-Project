
# /// Basic FastApi App (main.py) /// 
 from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# 🔹 In-memory data store (LIST)
users = []

# /// Request Models (Schema) ///
class SignupModel(BaseModel):
    name: str
    email: str
    password: str


class LoginModel(BaseModel):
    email: str
    password: str

# /// Signup API (POST) ///  
@app.post("/signup")
def signup(data: SignupModel):
    # check email already exists
    for user in users:
        if user["email"] == data.email:
            raise HTTPException(status_code=400, detail="Email already registered ❌")

    users.append({
        "name": data.name,
        "email": data.email,
        "password": data.password
    })

    return {"message": "Signup successful ✅"}

# /// login API (POST) ///    
@app.post("/login")
def login(data: LoginModel):
    for user in users:
        if user["email"] == data.email and user["password"] == data.password:
            return {"message": "Login successful ✅ OK"}

    raise HTTPException(status_code=401, detail="Invalid login ❌")

# /// Signup ///    
POST /signup
{
  "name": "Ali",
  "email": "ali@gmail.com",
  "password": "1234"
}

# /// login ///
POST /login
{
  "email": "ali@gmail.com",
  "password": "1234"
}

# /// Users List Structure ///
[
  {
    "name": "Ali",
    "email": "ali@gmail.com",
    "password": "1234"
  }
]
