<template>
  <div>
				<ul v-bind:show="tasks.length>0" class="col align-self-center">
					<li v-for="task in tasks" :class="{done: isChecked(task)}" :key="task.id">

            <p>{{task}}</p>
						<button class="button" @click="deleteTask">X</button>
					</li>			
				</ul>		
    <div
        class="alert alert-primary todo__row"
        v-if="tasks.length==0 && doneLoading"
    ><p>No Tasks for this User</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import bus from "./../bus.js";

export default {
  data() {
    return {
      tasks: [],
      doneLoading: false,
      editingTask: {}
    };
  },
  props: [
    'userId'
  ],
  mounted: function() {
    this.fetchTask();
    this.listenToEvents();
  },
  watch: {
    $route: function() {
      this.doneLoading = false;
      this.fetchTask().then(function() {
        this.doneLoading = true;
      });
    }
  },
  methods: {
    // Currently getting tasks from the /users/
    // NEXT--> 
    // 1) need to switch to getting tasks from /tasks/
    // 2) need to filter tasks by user id (backend)
    // 3) need to add in new RESTful calls: DELETE
    fetchTask() {
      axios.get(`/api/v1/users/${this.userId.id}/`).then(response => {
        this.tasks = this.userId.tasks;
      })
  },
    deleteTask() {
      console.log("Oh my! We are not hooked up to anything yet.")
    },
    listenToEvents() {
      bus.$on("refreshTask", $event => {
        this.fetchTask(); 
      });
    },

    check: function (task) {
        // ***** need to UPDATE!
        // need a PATCH to BE to update the task.state
				task.state = true;
		},

    isChecked: function (task) {
				return task.state;
		}
  }
};
</script>

<style scoped>
.todo__done {
  text-decoration: line-through !important;
}

.no_border_left_right {
  border-left: 0px;
  border-right: 0px;
}

.flat_form {
  border-radius: 0px;
}

.mrb-10 {
  margin-bottom: 10px;
}

.addon-left {
  background-color: none !important;
  border-left: 0px !important;
  cursor: pointer !important;
}

.addon-right {
  background-color: none !important;
  border-right: 0px !important;
}

/* Relevant resets */

ul, li {
	margin: 0;
	padding: 0;
	border: 0;
}

/* Global Styles */

body {
	line-height: 1;
	font-family: "Lato", sans-serif;
	background-color: #EFF1F2;
}

.container {
	width: 70%;
	margin: 1em auto 3em;
	border: 1px solid #efefef;
}

.panel, li {
	display: flex;
	align-items: center;
	justify-content: space-between;
	list-style-type: none;
	padding: 10px;
	border-bottom: 1px solid #efefef;
	background-color: #E7E8EB;
}

.text-input {
	border: 1px solid #dedede;
	padding-left: 10px;
	width: 70%;
	height: 35px;
	color: #555;
}


button {
	color: #555;
	background-color: #FFFFFF;
	border: 1px solid #bbb;
	outline: 0;
	width: 100px;
	height: 38px;
	cursor: pointer;
	font-size: 14px;
}

/* Task  area */

.list li {
	background-color: #3465A4;
}

.list li button {
	background-color: transparent;
	border: 1px solid #3465A4;
	color: #ddd;
	visibility: hidden;
	font-size: 20px;
	font-weight: bold;
}

.list li:hover > button {
	visibility: visible;
}

.list label {
	padding-right: 10px;
	display: inline-block;
	width: 70%;
	font-size: 18px;
	line-height: 24px;
	color: #fcfcfc;
	z-index: 2;
	overflow: hidden;
}

.list li.done label {
	color: #d9d9d9;
	text-decoration: line-through;
}
</style>
