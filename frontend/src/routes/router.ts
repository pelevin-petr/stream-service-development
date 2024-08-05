import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '@/views/HomeView.vue'
import StreamView from '@/views/StreamView.vue'
import RegisterView from '@/views/RegisterView.vue'
import LoginView from '@/views/LoginView.vue'
import CreateStream from '@/views/CreateDeleteStream.vue'


const routes = [
  { path: '/', component: HomeView, alias: '/', name: 'home' },
  { path: '/registration', component: RegisterView, name: 'registration' },
  { path: '/authorization', component: LoginView, name: 'authorization' },
  { path: '/streams/:id', component: StreamView, name: 'streams' },
  { path: '/create-streams', component: CreateStream, name: 'create-streams' },
]

export const router = createRouter({
  history: createWebHistory(),
  routes
})