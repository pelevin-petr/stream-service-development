import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '@/views/HomeView.vue'
import StreamView from '@/views/StreamView.vue'
import RegisterView from '@/views/RegisterView.vue'
import LoginView from '@/views/LoginView.vue'


const routes = [
  { path: '/', component: HomeView, alias: '/' },
  { path: '/registration', component: RegisterView },
  { path: '/authorization', component: LoginView },
  { path: '/stream/:id', component: StreamView },
]

export const router = createRouter({
  history: createWebHistory(),
  routes
})