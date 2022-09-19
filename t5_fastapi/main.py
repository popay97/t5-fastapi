from fastapi import FastAPI
import uvicorn
from schemes.translateSchemas import TranslateRequest, TranslateResponse, translateRequestValidator
from api.v1.translate import translate
from fastapi.responses import RedirectResponse
from core.config import apiPrefix, apiDocsUrl

app = FastAPI()

@app.get("/")
async def root():
    response = RedirectResponse(url=apiDocsUrl)
    return response


@app.post("%s/translate" % apiPrefix, response_model=TranslateResponse)
async def requestFunction(request: TranslateRequest):
    if translateRequestValidator(request) != "OK":
        print("validator failed")
        print (translateRequestValidator(request))
        return translateRequestValidator(request)
    else:
        res = await translate(request.text, request.source, request.target)
        return {"translatedText": res}

def start():
    uvicorn.run("t5_fastapi.main:app", host="0.0.0.0", port=8000, reload=True)