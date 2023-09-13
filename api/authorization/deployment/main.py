import uvicorn
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--host", type=str, help="Defines the host")
parser.add_argument("-p", "--port", type=int, help="Defines the port")
parser.add_argument("-e", "--env", type=str, help="Defines the environment of project")

if __name__ == "__main__":
    args = parser.parse_args()
    uvicorn.run("api.app:app", host=args.host, port=args.port, reload=True, env_file=args.env)