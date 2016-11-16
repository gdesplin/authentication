from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from datetime import datetime
import json
import sqlite3
from sqlclass import goalsdb

class MyServer(BaseHTTPRequestHandler):
        def createGoal(self):
            sql = goalsdb()
            self.send_response(201)
            self.send_header('Access-Control-Allow-Origin','*')
            self.end_headers()
            length = int(self.headers['Content-Length'])
            data = self.rfile.read(length).decode("utf-8")
            print("start recieved data")
            print(data)
            print('end')
            parsed_data = parse_qs(data, False, True)
            print('parsed')
            print(parsed_data)
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
            print(goal)
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
            print(goallist)
            sql.updateGoal(goal, key)

        def deleteGoal(self, key):
            sql = goalsdb()
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin','*')
            self.end_headers()
            print(key)
            sql.deleteGoal(key)


        def do_GET(self):
            query = parse_qs(urlparse(self.path).query)
            splitq = self.path.split("/")
            if len(splitq) == 3:
                goal = splitq[2]
                self.getGoal(goal)
            elif self.path.startswith("/goals"):
                self.getGoals()
            else:
                self.send_response(404)
                self.send_header('Access-Control-Allow-Origin','*')
                self.end_headers()
                self.wfile.write(bytes("Page not found. 404", "utf-8"))
                return

        def do_POST(self):
            if self.path.startswith("/goals"):
                self.createGoal()   
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(bytes("404", "utf-8"))
                return
        def do_OPTIONS(self):
            self.send_response(200, "ok")
            self.send_header('Access-Control-Allow-Credentials', 'true')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE')
            self.send_header('Access-Control-Allow-Headers', 'Content-type') 
            self.end_headers()

        def do_PUT(self):
            splitq = self.path.split("/")
            if len(splitq) == 3:
                key = splitq[2]
                self.updateGoal(key)
            else:
                self.send_response(404)
                self.send_header('Access-Control-Allow-Origin','*')
                self.end_headers()
                self.wfile.write(bytes("Page not found. 404", "utf-8"))
                return

        def do_DELETE(self):
            splitq = self.path.split("/")
            if len(splitq) == 3:
                goal = splitq[2]
                self.deleteGoal(goal)
            elif self.path.startswith("/goals"):
                self.deleteGoals()
            else:
                self.send_response(404)
                self.send_header('Access-Control-Allow-Origin','*')
                self.end_headers()
                self.wfile.write(bytes("Page not found. 404", "utf-8"))
                return


            
def run():
        listen = ('127.0.0.1', 8080)
        server = HTTPServer(listen,MyServer)
        print ("Listening...")
        server.serve_forever()

run()
