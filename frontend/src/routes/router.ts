import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '@/views/HomeView.vue'
import StreamView from '@/views/StreamView.vue'
import LoginView from '@/views/LoginView.vue'
import CRUDStreams from '@/views/CRUDStreams.vue'
import { useKeycloak } from '@josempgon/vue-keycloak'


const routes = [
  { path: '/', component: HomeView, alias: '/', name: 'home' },
  { path: '/authorization', component: LoginView, name: 'authorization' },
  { path: '/streams/:id', component: StreamView, name: 'streams' },
  { path: '/create-streams', component: CRUDStreams, name: 'create-streams', beforeEnter: () => {
     const {isAuthenticated} = useKeycloak()
      return isAuthenticated.value
    } },
]

export const router = createRouter({
  history: createWebHistory(),
  routes
})