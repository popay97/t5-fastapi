from pydantic import BaseModel
from core.config import supportedLanguages 

class TranslateRequest(BaseModel):
    text: str
    source: str
    target: str

class TranslateResponse(BaseModel):
    translatedText: str

def translateRequestValidator(request: TranslateRequest):
    if request.source == request.target:
        return ValueError("Source and target languages are the same")
    elif request.source.lower() not in [x.lower() for x in supportedLanguages]:
        return ValueError("Source language is not supported")
    elif request.target.lower() not in [x.lower() for x in supportedLanguages]:
        return ValueError("Target language is not supported")
    else:
        return "OK"