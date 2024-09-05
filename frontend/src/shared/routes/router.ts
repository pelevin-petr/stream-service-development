import { createRouter, createWebHistory } from 'vue-router'
import { useKeycloak } from '@josempgon/vue-keycloak'


import TopView from '@/shared/views/TopView.vue'
import AdminView from '@/admin/views/AdminView.vue'
import { adminRoutes } from '@/admin/routes/router'
import { routes } from '@/default/routes/router'


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
      const { hasRoles } = useKeycloak()
      return hasRoles(['my-admin-role'])
    }
  }
]

export const router = createRouter({
  history: createWebHistory(),
  routes: topRoutes
})