Goal Manager README

Goal Manager access and uses the goals.db database
This database contains one table: goals
The goals table schema is this:
```
CREATE TABLE goals (
        key INTEGER PRIMARY KEY,
        goal_name VARCHAR(255),
        goal_num INTEGER,
        goal_progress INTEGER,
        start_date DATETIME,
        end_date DATETIME,
        report_period VARCHAR(255),
        goal_per_report_period INTEGER
    );
```
REST endpoints:
* To retrieve all records, use a GET request at /goals
* To retrieve a single record use GET /goals/key
* To create a new goal, use POST /goals/key
* To update one goal use PUT /goals/key
* To delete a single record use DELETE /goals/key

