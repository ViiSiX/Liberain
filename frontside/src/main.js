// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import jQuery from 'jquery'
import Vue from 'vue'
import Vuex from 'vuex'
import App from './App.vue'
import router from './router'

window.jQuery = jQuery
window.$ = jQuery

require('what-input')
require('foundation-sites')

Vue.config.productionTip = false
Vue.use(Vuex)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
