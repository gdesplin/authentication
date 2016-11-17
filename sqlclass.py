import json
import sqlite3
from passlib.hash import bcrypt

class goalsdb:
        def __init__(self):
             self.conn = sqlite3.connect("goals.db")
             self.cursor = self.conn.cursor()
        def dictToList(self, mydict):
            row = [
                mydict.get('goal_name'),
                mydict.get('goal_num'),
                mydict.get('goal_progress'),
                mydict.get('start_date'),
                mydict.get('end_date'),
                mydict.get('report_period'),
                mydict.get('goal_per_report_period')
            ]
            mylist = [item for sublist in row for item in sublist]
            return mylist
    
        def sqlCreateGoal(self, goal):
            mylist = self.dictToList(goal)
            self.cursor.execute("INSERT INTO goals VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)", (mylist))
            self.conn.commit()
            self.conn.close()

        def getGoals(self):
            self.cursor.execute("SELECT * FROM goals")
            all_goals = self.cursor.fetchall()
            json_goals = json.dumps(all_goals)
            self.conn.commit()
            self.conn.close()
            return json_goals
        
        def getGoal(self, key):
            self.cursor.execute("SELECT * FROM goals WHERE key = ?", (key))
            goal = self.cursor.fetchone()
            json_goal = json.dumps(goal)
            self.conn.commit()
            self.conn.close()
            return json_goal
    
        def updateGoal(self, goal, key):
            goalList = self.dictToList(goal)
            self.cursor.execute("UPDATE goals SET goal_name = ?, goal_num = ?,goal_progress = ?, start_date = ?, end_date = ?, report_period = ?,goal_per_report_period = ? WHERE key = ?", (goalList[0] ,goalList[1],goalList[2],goalList[3],goalList[4],goalList[5],goalList[6],key))
            self.conn.commit()
            self.conn.close()
        
        def deleteGoal(self, key):
            self.cursor.execute("DELETE FROM goals WHERE key = ?", (key,))
            self.conn.commit()
            self.conn.close()
        
        def check_key_goals(self, key):
            self.cursor.execute("select exists (select key from goals where key = ?)", (key,))
            checker = self.cursor.fetchone()
            if checker[0] == 1:
                print("true")
                print(checker[0])
                return True
            return False

class usersdb:
        def __init__(self):
             self.conn = sqlite3.connect("goals.db")
             self.cursor = self.conn.cursor()
        def dictToList(self, mydict, hashed):
            row = [
                mydict.get('email'),
                mydict.get('f_name'),
                mydict.get('l_name'),
                hashed
            ]
            mylist = [item for sublist in row for item in sublist]
            return mylist

        def hashPass(self, password):
            return hashed = bcrypt.encrypt(password)

        def sqlCreateUser(self, user):
            hashed = hashPass(user.get('password'))
            mylist = self.dictToList(user, hashed)
            self.cursor.execute("INSERT INTO users VALUES (NULL, ?, ?, ?, ?)", (mylist))
            self.conn.commit()
            self.conn.close()

        def getUsers(self):
            self.cursor.execute("SELECT * FROM users")
            all_users = self.cursor.fetchall()
            json_users = json.dumps(all_users)
            self.conn.commit()
            self.conn.close()
            return json_users
        
        def getUser(self, key):
            self.cursor.execute("SELECT * FROM users WHERE key = ?", (key))
            user = self.cursor.fetchone()
            json_user = json.dumps(user)
            self.conn.commit()
            self.conn.close()
            return json_user
    
        def updateUser(self, user, key):
            userList = self.dictToList(user)
            self.cursor.execute("UPDATE users SET email = ?, f_name = ?, l_name = ?, password = ?, WHERE key = ?", (userList[0] ,userList[1],userList[2],userList[3],key))
            self.conn.commit()
            self.conn.close()
        
        def deleteUser(self, key):
            self.cursor.execute("DELETE FROM users WHERE key = ?", (key,))
            self.conn.commit()
            self.conn.close()
        
        def check_key_users(self, key):
            self.cursor.execute("select exists (select key from users where key = ?)", (key,))
            checker = self.cursor.fetchone()
            if checker[0] == 1:
                print("true")
                print(checker[0])
                return True
            return False
                et('password'),

        def check_key_users(self, key):
            self.cursor.execute("select exists (select key from users where key = ?)", (key,))
            checker = self.cursor.fetchone()
            if checker[0] == 1:
                return True
            return False

