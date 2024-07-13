import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '@/views/HomeView.vue'
import AuthForm from '@/components/auth/AuthForm.vue'
import StreamView from '@/views/StreamView.vue'


const routes = [
  { path: '/', component: HomeView, alias: '/' },
  { path: '/authorisation', component: AuthForm },
  { path: '/stream/:id', component: StreamView },
]

export const router = createRouter({
  history: createWebHistory(),
  routes
})