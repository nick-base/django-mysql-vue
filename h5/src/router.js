import Vue from 'vue'
import Router from 'vue-router'
import Page1 from './views/Page1.vue'
import Page2 from './views/Page2.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'page1',
      component: Page1
    },
    {
      path: '/page2',
      name: 'page2',
      component: Page2
    }
  ]
})
