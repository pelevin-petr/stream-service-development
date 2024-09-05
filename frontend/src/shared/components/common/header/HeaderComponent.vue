<script lang="ts" setup>
import { ref } from 'vue'
import { useKeycloak } from '@josempgon/vue-keycloak'

import NavBar from '@/shared/components/common/header/NavBar.vue'
import faviconSVG from '@/shared/assets/img/favicon.svg'
import type { NavTab } from '@/shared/modules/nav-tab'
import { useRouter } from 'vue-router'


const { isAuthenticated } = useKeycloak()
const visible = ref(window.innerWidth >= 1280)
const headerClass = ref(window.innerWidth >= 1280)
const { keycloak, roles, hasRoles } = useKeycloak()
const router = useRouter()

const props = defineProps<{routes: NavTab[]}>()
</script>

<template>
  <nav
    class="bg-white dark:bg-extra-neutral-700 border-b border-gray-200 dark:border-gray-600">
    <div class="grid mx-auto p-4"
         :class="{'grid-cols-3': headerClass, 'grid-cols-2': !headerClass}"
    >
      <RouterLink
        class="flex items-center space-x-3 rtl:space-x-reverse"
        to="/"
        @click="visible = !visible"
      >
        <img alt="SSA Logo" class="h-8" :src="faviconSVG">
        <span class=" hidden md:block self-center text-xl font-semibold whitespace-nowrap dark:text-white">Система Стриминга Автомобилей</span>
        <span class=" block md:hidden self-center text-xl font-semibold whitespace-nowrap dark:text-white">ССА</span>
      </RouterLink>
      
      <div class="flex justify-end xl:order-2 space-x-3 xl:space-x-0 rtl:space-x-reverse">
        <div v-if="hasRoles(['my-admin-role'])">
            <button
              class="mr-1 text-black-50 bg-gray-200 hover:bg-gray-400 focus:ring-4 focus:outline-none focus:bg-gray-200 font-medium rounded-lg text-sm px-5 py-2 text-center dark:bg-gray-700 dark:hover:bg-gray-800 dark:focus:ring-blue-800 dark:text-white"
              type="button"
              @click="router.push('/admin')"
            >
              Панель администратора
            </button>
        </div>
        <div v-if="!isAuthenticated">
          <span @click="keycloak?.login">
            <button
              class="mr-1 text-black-50 bg-gray-200 hover:bg-gray-400 focus:ring-4 focus:outline-none focus:bg-gray-200 font-medium rounded-lg text-sm px-5 py-2 text-center dark:bg-gray-700 dark:hover:bg-gray-800 dark:focus:ring-blue-800 dark:text-white"
              type="button">
              Войти
            </button>
          </span>
        </div>
        <div v-else
             class="my-auto font-medium text-green-600 bg-green-200 py-1 px-2 rounded-lg border border-green-600"
        >
          Вы авторизованы
        </div>
        <button @click="visible = !visible"
                aria-controls="navbar-sticky" aria-expanded="false"
                class="inline-flex justify-center items-center p-2 w-10 h-10  text-sm text-gray-500 rounded-lg xl:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
                data-collapse-toggle="navbar-sticky" type="button">
          <span class="sr-only">Open main menu</span>
          <svg aria-hidden="true" class="w-5 h-5" fill="none" viewBox="0 0 17 14" xmlns="http://www.w3.org/2000/svg">
            <path d="M1 1h15M1 7h15M1 13h15" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
                  stroke-width="2" />
          </svg>
        </button>
      </div>
      <div class="flex justify-center" :class="{'col-span-full': !headerClass}">
        <NavBar v-show="visible" v-model="visible" :routes="routes" >
        </NavBar>
      </div>
    </div>
  </nav>
</template>

<style scoped>
@media (prefers-color-scheme: dark) {
  .dark\:bg-extra-neutral-700 {
    --tw-bg-opacity: 1;
    background-color: #2C2C2C
  }
}
</style>
