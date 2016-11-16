import json
import sqlite3

class goalsdb:
        def __init__(self):
             self.conn = sqlite3.connect("goals.db")
             self.cursor = self.conn.cursor()
        def dictToList(self, mydict):
            print('mydict')
            print(mydict)
            row = [
                mydict.get('goal_name'),
                mydict.get('goal_num'),
                mydict.get('goal_progress'),
                mydict.get('start_date'),
                mydict.get('end_date'),
                mydict.get('report_period'),
                mydict.get('goal_per_report_period')
            ]
            print(row)
            mylist = [item for sublist in row for item in sublist]
            print('made list')
            return mylist
    
        def sqlCreateGoal(self, goal):
            print(goal)
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
            print(goal)
            print(key)
            goalList = self.dictToList(goal)
            print(goalList)
            self.cursor.execute("UPDATE goals SET goal_name = ?, goal_num = ?,goal_progress = ?, start_date = ?, end_date = ?, report_period = ?,goal_per_report_period = ? WHERE key = ?", (goalList[0] ,goalList[1],goalList[2],goalList[3],goalList[4],goalList[5],goalList[6],key))
            print("updated goal")
            self.conn.commit()
            self.conn.close()
        
        def deleteGoal(self, key):
            self.cursor.execute("DELETE FROM goals WHERE key = ?", (key,))
            self.conn.commit()
            self.conn.close()

