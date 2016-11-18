var writeSuccUC = function () {
    var  submitButtonUser = document.getElementById('submit_su');
    submitButtonUser.value = "Success!";
    submitButtonUser.setAttribute("class", "success");
}

var writeFailUC = function () {
    var  submitButtonUser = document.getElementById('submit_su');
    submitButtonUser.value = "Already Exists";
    submitButtonUser.setAttribute("class", "fail");
}

var userPostRequest = function () {
	var request = new XMLHttpRequest();
	request.onreadystatechange = function () {
        if (request.readyState === XMLHttpRequest.DONE) {
            if (request.status >= 200 && request.status < 400) {
                writeSuccUC()
            }
            else if (request.status = 400 ) {
                
            }
            else {
                alert("Uh");
            }
        }
	};
    serialize = function(obj) {
      var str = [];
      for(var p in obj)
        if (obj.hasOwnProperty(p)) {
          str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
        }
      return str.join("&");
    }
    var email = document.getElementById("email_su");
    var f_name = document.getElementById("f_name_su");
    var l_num = document.getElementById("l_name_su");
    var password = document.getElementById("password_su");
    
    var postuser= {};
    postuser[email.name] = email.value;
    postuser[f_name.name] = f_name.value;
    postuser[l_num.name] = l_num.value;
    postuser[password.name] = password.value;

    var encodedData = serialize(postuser);
    console.log(postuser);
    console.log(encodedData);
    
    request.open("POST", "http://localhost:8080/users");
    request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    request.send(encodedData);
    
};

var  submitButtonUser = document.getElementById('submit_su');
submitButtonUser.onclick = function () {
    console.log("Submit Pressed");
    userPostRequest();
    console.log("User Created Successfully");
};

var close_btn_su = document.getElementById('close_su');
function signUpClick() {
    signUpModal.style.display = 'block'; 
}
close_btn_su.onclick = function() {
    signUpModal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == signUpModal) {
        signUpModal.style.display = "none";
    }
}
var nameSections = function (i) {
    var nme = '';
    if (i == 1) {nme = 'Goal Name: ';}
    else if (i == 2) {nme = 'Goal Number: ';}
    else if (i == 3) {nme = 'Progress: ' ;}
    else if (i == 4) {nme = 'Start Date: ';}
    else if (i == 5) {nme = 'End Date: ';}
    else if (i == 6) {nme = 'Reporting: ';}
    else if (i == 7) {nme = 'Goal Per: ';}
    return nme;
}
var displayGoals = function (goals) {
	var goalDiv = document.getElementById("goals");
	goalDiv.innerHTML = "";
	gslen = goals.length;
	for (i = 0; i < gslen; i++) {
        var goal_key = goals[i][0];
        var newul = document.createElement("ul");
        newul.className = "goal";
        newul.setAttribute("id", "goal_"+goal_key);
        newul.setAttribute("name", goal_key);
        goalDiv.appendChild(newul);
        
        
        goal = goals[i]
//        console.log(goal);
        glen = goal.length;
        for (a = 1; a < glen; a++) {
            var newli = document.createElement("li");
            newul.appendChild(newli);
            newli.innerHTML = nameSections(a)+goal[a]; 
        }
        var button = document.createElement("button");
        newul.appendChild(button);
        button.setAttribute("id", "goal_update_"+i);
        button.setAttribute("class", "update_btns");
        button.setAttribute("onclick", "update_click("+i+','+goal_key+")");
        button.innerHTML = ("Update");
        var button = document.createElement("button");
        newul.appendChild(button);
        button.setAttribute("id", "delete"+i);
        button.setAttribute("class", "delete_btns");
        button.setAttribute("onclick", "delete_click("+goal_key+")");
        button.innerHTML = ("Delete");
        var button = document.createElement("button");
        newul.appendChild(button);
        button.setAttribute("id", "plus_one"+i);
        button.setAttribute("class", "plus_one_btn");
        button.setAttribute("onclick", "plus_one("+i+','+goal_key+")");
        button.innerHTML = ("+1");
        
	}
}
var getRequest = function () {
    var request = new XMLHttpRequest();
    request.onreadystatechange = function () {
        if (request.readyState == XMLHttpRequest.DONE) {
            if (request.status >= 200 && request.status < 400) {
                goals = JSON.parse(request.responseText);
//                console.log(goals);
                displayGoals(goals)
            }
            else {
                alert("Not Worky")
            }
        }
    };

    request.open("GET", "http://localhost:8080/goals");
    request.send();
};

var goalsPostRequest = function () {
	var request = new XMLHttpRequest();
	request.onreadystatechange = function () {
        if (request.readyState === XMLHttpRequest.DONE) {
            if (request.status >= 200 && request.status < 400) {
                getRequest();
            }
            else {
                alert("Uh");
            }
        }
	};
    serialize = function(obj) {
      var str = [];
      for(var p in obj)
        if (obj.hasOwnProperty(p)) {
          str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
        }
      return str.join("&");
    }
    var goal_name = document.getElementById("goal_name");
    var goal_num = document.getElementById("goal_num");
    var goal_progress = document.getElementById("goal_progress");
    var start_date = document.getElementById("start_date");
    var end_date = document.getElementById("end_date");
    var report_period = document.getElementById("report_period");
    var goal_per_report_period = document.getElementById("goal_per_report_period");
    
    var postgoal= {};
    postgoal[goal_name.name] = goal_name.value;
    postgoal[goal_num.name] = goal_num.value;
    postgoal[goal_progress.name] = goal_progress.value;
    postgoal[start_date.name] = start_date.value;
    postgoal[end_date.name] = end_date.value;
    postgoal[report_period.name] = report_period.value;
    postgoal[goal_per_report_period.name] = goal_per_report_period.value;
    var encodedData = serialize(postgoal);
    console.log(postgoal);
    console.log(encodedData);
    
    request.open("POST", "http://localhost:8080/goals");
    request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    request.send(encodedData);
};

getRequest();
var  submitButton = document.getElementById('submit');
submitButton.onclick = function () {
    console.log("Submit Pressed");
    goalsPostRequest();
    console.log("Goal Created Successfully");
};

var updateGoal = function (key) {
    var request = new XMLHttpRequest();
	request.onreadystatechange = function () {
        if (request.readyState === XMLHttpRequest.DONE) {
            if (request.status >= 200 && request.status < 400) {
                getRequest();
            }
            else {
                alert("Uh");
            }
        }
	};
    serialize = function(obj) {
      var str = [];
      for(var p in obj)
        if (obj.hasOwnProperty(p)) {
          str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
        }
      return str.join("&");
    }
    
    get_update_goal_form();
    var updateGoal= {};
    updateGoal[goal_name_u.name] = goal_name_u.value;
    updateGoal[goal_num_u.name] = goal_num_u.value;
    updateGoal[goal_progress_u.name] = goal_progress_u.value;
    updateGoal[start_date_u.name] = start_date_u.value;
    updateGoal[end_date_u.name] = end_date_u.value;
    updateGoal[report_period_u.name] = report_period_u.value;
    updateGoal[goal_per_report_period_u.name] = goal_per_report_period_u.value;
    var encodedData = serialize(updateGoal);
    console.log(updateGoal);
    console.log(encodedData);
    
    request.open("PUT", "http://localhost:8080/goals/"+key);
    request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    request.send(encodedData);
};

//update modal
var modal = document.getElementById('form-goals-modal');
var modal_btn = document.getElementById('submit-u');
var update_buttons = document.getElementsByClassName('update_btns');
var close_btn = document.getElementById('close');
var get_update_goal_form = function () {
    var goal_name_u = document.getElementById("goal_name_u");
    var goal_num_u = document.getElementById("goal_num_u");
    var goal_progress_u = document.getElementById("goal_progress_u");
    var start_date_u = document.getElementById("start_date_u");
    var end_date_u = document.getElementById("end_date_u");
    var report_period_u = document.getElementById("report_period_u");
    var goal_per_report_period_u = document.getElementById("goal_per_report_period_u");
    
}

function update_click(goal_num,goal_key) {
    modal.style.display = 'block';
    console.log("clicked");
    
    get_update_goal_form();
    goal_name_u.value = goals[goal_num][1];
    goal_num_u.value = goals[goal_num][2];
    goal_progress_u.value = goals[goal_num][3]
    start_date_u.value = goals[goal_num][4];
    end_date_u.value = goals[goal_num][5];
    report_period_u.value = goals[goal_num][6];
    goal_per_report_period_u.value = goals[goal_num][7];
    modal.setAttribute("data-key", goal_key);
    
}
close_btn.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

var submitUpdate = document.getElementById("submit_u");
submitUpdate.onclick = function() {
    key = document.getElementById('form-goals-modal').getAttribute("data-key")
    updateGoal(key);
    
}


//delete stuff

var deleteRecord = function (key) {
    var request = new XMLHttpRequest();
    request.onreadystatechange = function () {
        if (request.readyState == XMLHttpRequest.DONE) {
            if (request.status >= 200 && request.status < 400) {
                getRequest()
            }
            else {
                alert("Not Worky")
            }
        }
    };
    
    request.open("DELETE", "http://localhost:8080/goals/"+key);
    request.send();
};

function delete_click(key) {
    if (confirm("Are you sure you want to delete this record?") == true) {
        deleteRecord(key);}
}

//Plus one
function plus_one(goal_num,goal_key) {
    get_update_goal_form();
    goal_name_u.value = goals[goal_num][1];
    goal_num_u.value = goals[goal_num][2];
    goal_progress_u.value = goals[goal_num][3]+1;
    start_date_u.value = goals[goal_num][4];
    end_date_u.value = goals[goal_num][5];
    report_period_u.value = goals[goal_num][6];
    goal_per_report_period_u.value = goals[goal_num][7];
    modal.setAttribute("data-key", goal_key);
    key = goal_key;
    updateGoal(key);
}