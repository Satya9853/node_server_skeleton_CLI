import os


class CreateServer:
    def __init__(self, path):
        self.path = f"{path}/server"

    def build(self):
        self.create_folder()
        self.create_app()
        self.create_controller()
        self.create_connectDB()
        self.create_gitignore()
        self.create_router()
        self.create_package()
        self.create_route_not_found()

    def create_folder(self):
        os.mkdir(self.path)
        file_name = ["controller", "model", "router", "db", "middleware"]
        for file in file_name:
            os.mkdir(f"{self.path}/{file}")

    def create_app(self):
        content = open("./required_docs/app.txt", "r").read()
        file = open(f"{self.path}/app.js", "w")
        file.write(content)

    def create_controller(self):
        content = open("./required_docs/controller.txt", "r").read()
        file = open(f"{self.path}/controller/test-controller.js", "w")
        file.write(content)

    def create_connectDB(self):
        content = open("./required_docs/connectDB.txt", "r").read()
        file = open(f"{self.path}/db/connectDB.js", "w")
        file.write(content)

    def create_gitignore(self):
        content = open("./required_docs/gitignore.txt", "r").read()
        file = open(f"{self.path}/.gitignore", "w")
        file.write(content)

    def create_package(self):
        content = open("./required_docs/package.txt", "r").read()
        file = open(f"{self.path}/package.json", "w")
        file.write(content)

    def create_route_not_found(self):
        content = open("./required_docs/route_not_found.txt", "r").read()
        file = open(f"{self.path}/middleware/route-not-found-middleware.js", "w")
        file.write(content)

    def create_router(self):
        content = open("./required_docs/router.txt", "r").read()
        file = open(f"{self.path}/router/test-route.js", "w")
        file.write(content)

    def create_dotenv(self, mongo_uri):
        content = f"MONGO_URI={mongo_uri}"
        file = open(f"{self.path}/.env", "w")
        file.write(content)