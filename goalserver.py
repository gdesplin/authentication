from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from datetime import datetime
import json
import sqlite3
from sqlclass import goalsdb, usersdb

class MyServer(BaseHTTPRequestHandler):
#goals
        def createGoal(self):
            sql = goalsdb()
            self.send_response(201)
            self.send_header('Access-Control-Allow-Origin','*')
            self.end_headers()
            length = int(self.headers['Content-Length'])
            data = self.rfile.read(length).decode("utf-8")
            parsed_data = parse_qs(data, False, True)
            sql.sqlCreateGoal(parsed_data)

        def getGoals(self):
            sql = goalsdb()
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin','*')
            self.end_headers()
            goals = sql.getGoals()
            self.wfile.write(bytes(str.encode(goals)))

        def getGoal(self, key):
            sql = goalsdb()
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin','*')
            self.end_headers()
            goal = sql.getGoal(key)
            self.wfile.write(bytes(str.encode(goal)))

        def updateGoal(self, key):
            sql = goalsdb()
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin','*')
            self.end_headers()
            length = int(self.headers['Content-Length'])
            data = self.rfile.read(length).decode("utf-8")
            goal = parse_qs(data)
            goallist = sql.dictToList(goal)
            sql.updateGoal(goal, key)

        def deleteGoal(self, key):
            sql = goalsdb()
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin','*')
            self.end_headers()
            sql.deleteGoal(key)

        def check_key_goals(self, key):
            sql = goalsdb()
            return sql.check_key_goals(key)

        def createUser(self):
            sql = usersdb()
            self.send_response(201)
            self.send_header('Access-Control-Allow-Origin','*')
            self.end_headers()
            length = int(self.headers['Content-Length'])
            data = self.rfile.read(length).decode("utf-8")
            parsed_data = parse_qs(data, False, True)
            sql.sqlCreateUser(parsed_data)
#users
        def getUsers(self):
            sql = usersdb()
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin','*')
            self.end_headers()
            users = sql.getUsers()
            self.wfile.write(bytes(str.encode(users)))

        def getUser(self, key):
            sql = usersdb()
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin','*')
            self.end_headers()
            goal = sql.getUser(key)
            self.wfile.write(bytes(str.encode(goal)))

        def updateUser(self, key):
            sql = usersdb()
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin','*')
            self.end_headers()
            length = int(self.headers['Content-Length'])
            data = self.rfile.read(length).decode("utf-8")
            goal = parse_qs(data)
            goallist = sql.dictToList(goal)
            sql.updateUser(goal, key)

        def deleteUser(self, key):
            sql = usersdb()
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin','*')
            self.end_headers()
            sql.deleteUser(key)
        
        def check_key_users(self, key):
            sql = usersdb()
            return sql.check_key_users(key)

        def send_404(self):
            self.send_response(404)
            self.send_header('Access-Control-Allow-Origin','*')
            self.end_headers()
            self.wfile.write(bytes("Page not found. 404", "utf-8"))

#Do Routes
        def do_GET(self):
            query = parse_qs(urlparse(self.path).query)
            splitq = self.path.split("/")
            if splitq[1] == "goals":
                if len(splitq) == 3:
                    key = splitq[2]
                    if self.check_key_goals(key):
                        self.getGoal(key)
                    else:
                        self.send_404()
                elif self.path.startswith("/goals"):
                    self.getGoals()
            elif sqlitq[1] == "users":
                if len(splitq) == 3:
                    key = splitq[2]
                    if self.check_key_users(key):
                        self.getUser(key)
                    else:
                        self.send_404()
                elif len(splitq) == 2:
                    self.getUsers()
            else:
                self.send_404()

        def do_POST(self):
            query = parse_qs(urlparse(self.path).query)
            splitq = self.path.split("/")
            if len(splitq) == 2:
                if splitq[1] == "goals":
                    self.createGoal()   
                elif splitq[1] == "users":
                    self.createUser()
                else:
                    self.send_404()
            else:
                self.send_404()

        def do_OPTIONS(self):
            self.send_response(200, "ok")
            self.send_header('Access-Control-Allow-Credentials', 'true')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE')
            self.send_header('Access-Control-Allow-Headers', 'Content-type') 
            self.end_headers()

        def do_PUT(self):
            splitq = self.path.split("/")
            if splitq[1] == 'goals':
                if len(splitq) == 3:
                    key = splitq[2]
                    if self.check_key_goals(key):
                        self.updateGoal(key)
                    else:
                        self.send_404()
            elif splitq[1] == 'users':
                if len(splitq) == 3:
                    key = splitq[2]
                    if self.check_key_users(key):
                        self.updateUser(key)
                    else:
                        self.send_404()
            else:
                self.send_404()

        def do_DELETE(self):
            splitq = self.path.split("/")
            if splitq[1] == "goals":
                if len(splitq) == 3:
                    key = splitq[2]
                    if self.check_key_goals(key):
                        self.deleteGoal(key)
                    else:
                        self.send_404()
                elif splitq[1] == "goals":
                    self.deleteGoals()
            elif splitq[1] == "users":
                if len(splitq) == 3:
                    key = splitq[2]
                    if self.check_key_users(key):
                        self.deleteUser(key)
                    else:
                        self.send_404()
            else:
               self.send_404()

            
def run():
        listen = ('127.0.0.1', 8080)
        server = HTTPServer(listen,MyServer)
        print ("Listening...")
        server.serve_forever()

run()
