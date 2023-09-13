import uvicorn
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--host", type=str, help="Defines the environment of project")
parser.add_argument("-p", "--port", type=int, help="Defines the environment of project")

if __name__ == "__main__":
    args = parser.parse_args()
    uvicorn.run("api.app:app", host=args.host, port=args.port, reload=True)