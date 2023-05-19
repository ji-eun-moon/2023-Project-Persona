import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import CommunityView from '../views/CommunityView.vue'
import ProfileView from '../views/ProfileView.vue'
import movies from './movies'
import community from './community'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/community',
    name: 'community',
    component: CommunityView
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView
  },
  ...movies,
  ...community

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
