from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd
from uvicorn import Config, Server
import nest_asyncio

app = FastAPI()

@app.get("/index")
def read_data():
    data = {
        "Number": [1, 2, 3, 4, 5],
        "Name": ["Mahesh", "Alex", "David", "John", "Chris"],
        "Age": [25, 26, 27, 28, 29],
        "City": ["Bangalore", "London", "San Francisco", "Toronto", "Paris"],
        "Country": ["India", "UK", "USA", "Canada", "France"]
    }
    df = pd.DataFrame(data)
    return JSONResponse(content=df.to_dict(orient="records"))

nest_asyncio.apply()

config = Config(app=app, host="0.0.0.0", port=8000, log_level="info")
server = Server(config=config)

server.run()
