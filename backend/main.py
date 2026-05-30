from fastapi import FastAPI
from pydantic import BaseModel
from afri_auth.otp import OTPAuth

app = FastAPI()

otp = OTPAuth()


class RegisterRequest(BaseModel):
    phone: str

class VerifyRequest(BaseModel):
    phone: str
    code: str


@app.post("/register")
async def register(data: RegisterRequest):

    result = await otp.send_otp(
        data.phone
    )

    return result


@app.post("/verify")
async def verify(data: VerifyRequest):

    result = await otp.verify_otp(
        data.phone,
        data.code
    )

    return result