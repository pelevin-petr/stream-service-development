import { createRouter, createWebHistory } from 'vue-router'
import { useKeycloak } from '@josempgon/vue-keycloak'

import HomeView from '@/shared/views/HomeView.vue'
import StreamView from '@/default/views/StreamView.vue'
import CRUDStreams from '@/admin/views/CRUDStreamsView.vue'
import InstructorsView from '@/admin/views/InstructorsView.vue'
import TopView from '@/shared/views/TopView.vue'
import AdminView from '@/admin/views/AdminView.vue'


const routes = [
  { path: '', component: HomeView, name: 'home' },
  { path: 'streams/:id', component: StreamView, name: 'streams' }
]
const adminRoutes = [
  { path: 'streams', component: CRUDStreams, name: 'admin-streams' },
  { path: 'instructors', component: InstructorsView, name: 'instructors' }
]
const topRoutes = [
  {
    path: '/',
    component: TopView,
    children: routes
  },
  {
    path: '/admin',
    component: AdminView,
    children: adminRoutes,
    beforeEnter: () => {
      const { isAuthenticated } = useKeycloak()
      return isAuthenticated.value
    }
  }
]

export const router = createRouter({
  history: createWebHistory(),
  routes: topRoutes
})