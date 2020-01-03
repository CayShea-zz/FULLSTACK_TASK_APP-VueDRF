<template>
  <div class="home">
    <div>
        <b-button size="sm" v-b-modal.modal-prevent-closing class="mr-2"> New User</b-button>
        <b-button size="sm" v-b-modal.modal-edit-user class="mr-2"> Edit</b-button>
        <b-button size="sm" @click="deleteUser" class="mr-2"> Delete</b-button>
        <b-table 
            :items="users" 
            :fields="fields" 
            striped 
            responsive="lg" 
            ref="selectableTable" 
            selectable
            :select-mode="selectMode" 
            @row-selected="onRowSelected"
        >
            <template v-slot:cell(selected)="{ rowSelected }">
                <template v-if="rowSelected">
                        <span aria-hidden="true">&check;</span>
                        <span class="sr-only">Selected</span>
                </template>
                <template v-else>
                        <span aria-hidden="true">&nbsp;</span>
                        <span class="sr-only">Not selected</span>
                </template>            
            </template>
            <template v-slot:cell(show_details)="row">
                <b-button size="sm" @click="row.toggleDetails" class="mr-2">
                    {{ row.detailsShowing ? 'Hide' : 'Show'}} Tasks
                </b-button>
            </template>
            <template v-slot:row-details="row">
                <b-card>
                    <b-row class="mb-2">
                        <ListTask :userId="row.item"></ListTask>
                        <CreateTask :userId="row.item" v-on:fetchUserTasks="fetchUserTasks"></CreateTask>
                    </b-row>
                </b-card>
            </template>
        </b-table>

        <div class="mt-3">
            <b-modal
                id="modal-prevent-closing"
                ref="modal"
                title="Add New User"
                @hidden="resetModal"
                @ok="handleOk"
            >
                <form ref="form" @submit.stop.prevent="handleSubmit">
                    <b-form-group
                        :state="nameState"
                        label="Name"
                        label-for="name-input"
                        invalid-feedback="Name is required"
                    >
                        <b-form-input
                            id="name-input"
                            v-model="name"
                            :state="nameState"
                            required
                        ></b-form-input>
                    </b-form-group>
                </form>
            </b-modal>
        </div>
        <div class="mt-3">
            <b-modal
                id="modal-edit-user"
                ref="modal"
                title="Edit User"
                @show="showEdit"
                @hidden="resetModal"
                @ok="handleEditOk"
            >
                <form ref="form" @submit.stop.prevent="handleEditSubmit">
                    <b-form-group
                        :state="nameState"
                        label="Name"
                        label-for="name-input"
                        invalid-feedback="Name is required"
                    >
                        <b-form-input
                            id="name-input"
                            v-model="name"
                            :state="nameState"
                            required
                        ></b-form-input>
                    </b-form-group>
                </form>
            </b-modal>
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import CreateTask from '../components/CreateTask';
import ListTask from '../components/ListTask';


  export default {
    name: "home",
    data() {
        return {
          users: [],
          name: '',
          nameState: null,
          selectMode: 'single',
          selected: [],
          fields: ['selected', 'name', 'show_details']
        }
      },
      components: {
          CreateTask,
          ListTask
      },
    mounted: function() {
        this.fetchUsers();
      },
    methods: {
      fetchUsers() {
        axios
          .get("/api/v1/users/")
          .then(response => {
              this.users = response.data;
          })
      },
      onRowSelected(item) {
          this.selected = item
      },
      checkFormValidity() {
          const valid = this.$refs.form.checkValidity()
          this.nameState = valid ? 'valid' : 'invalid'
          return valid
      },
      resetModal() {
          this.name = ''
          this.nameState = null
          this.fetchUsers();
      },
      resetTaskModal() {
          this.fetchUsers();
      },
      handleOk(bvModalEvt) {
          // Prevent modal from closing
          bvModalEvt.preventDefault();
          // Trigger submit handler
          this.handleSubmit();
      },
      handleEditOk(bvModalEvt) {
          bvModalEvt.preventDefault();
          this.handleEditSubmit();
      },
      handleSubmit() {
          if (!this.checkFormValidity()) {
              return
          }
          let user = {
              name: this.name
          };
          axios
              .post("/api/v1/users/", user)
              .catch(error => {
                  console.log(error);
              })
              this.$nextTick(() => {
                  this.$refs.modal.hide()
              })
          },
      handleEditSubmit() {
          if (!this.checkFormValidity()) {
              return
          }
          let user = {
              name: this.name
          };
          axios
              .patch(`/api/v1/users/${this.selected[0].id}/`, user)
              .then(response => {
                  console.log(response.data)
                  this.fetchUsers()
                  this.selected = [];
              }).catch(error => {
                  console.log(error);
              })
              this.$nextTick(() => {
                  this.$refs.modal.hide()
              })
          },
      showEdit () {
          if (!this.selected.length) {
              alert("Please select a User to edit.")
          }
          console.log(this.selected[0].id)
          this.resetModal();
      },
      deleteUser () {
          axios
              .delete(`/api/v1/users/${this.selected[0].id}/`)
              .then(response => {
                  this.selected = [];
                  this.fetchUsers()
              }).catch(error => {
                  console.log(error)
              })
      },
      fetchUserTasks(){
          this.fetchUsers();
      }
  }
};
</script>

<style scoped>
 .icon {
     text-align: right
 }
</style>