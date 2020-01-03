<template>
  <div class="col align-self-center">
    <form class="sign-in" @submit.prevent>
      <div class="form-group todo__row">
        <input
          type="text"
          class="form-control"
          @keypress="typing=true"
          placeholder="Add Tasks for this User"
          v-model="description"
          @keyup.enter="addTask($event)"
        />
        <small class="form-text text-muted" v-show="typing">Hit enter to save</small>
      </div>
    </form>
  </div>
</template>


<script>
import axios from "axios";

export default {
  data() {
    return {
      description: "",
      user: "",
      typing: false
    };
  },
  props: [
    'userId'
  ],
  methods: {
    addTask(event) {
      if (event) event.preventDefault();
      let task = {
        description: this.description,
        state: false,
        user: this.userId.id
      };
      axios
        .post("/api/v1/tasks/", task)
        .then(response => {
          this.clearTask();
          this.refreshTask();
          this.typing = false;
        })
        .catch(error => {
          console.log(error);
        });
    },

    clearTask() {
      this.description = "";
    },

    refreshTask() {
      this.$emit('fetchUserTasks')
    }
  }
};
</script>


<style scoped>
.underline {
  text-decoration: underline;
}
</style>