import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '@/views/HomeView.vue'
import StreamView from '@/views/StreamView.vue'
import RegisterView from '@/views/RegisterView.vue'
import LoginView from '@/views/LoginView.vue'


const routes = [
  { path: '/', component: HomeView, alias: '/', name: 'Home' },
  { path: '/registration', component: RegisterView, name: 'Registration' },
  { path: '/authorization', component: LoginView, name: 'Authorization' },
  { path: '/stream/:id/:city', component: StreamView, name: 'Stream' },
]

export const router = createRouter({
  history: createWebHistory(),
  routes
})