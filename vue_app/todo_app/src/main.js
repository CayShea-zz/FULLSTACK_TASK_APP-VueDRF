import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import BoostrapVue from 'bootstrap-vue';

import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

Vue.config.productionTip = false;

Vue.use(BoostrapVue);

new Vue({
  router,
  store,
  render: function(h) {
    return h(App);
  }
}).$mount("#app");
