<script setup lang="ts">
import { ref, watchEffect } from 'vue'

import NavBar from '@/components/common/header/NavBar.vue'
import SearchBar from '@/components/common/header/SearchBar.vue'
import AuthForm from '@/components/auth/AuthForm.vue'


const windowWidth = ref<number>(window.innerWidth)
const regStatus: boolean = true  //need in some logic

watchEffect(() => {
  const updateWindowSize = () => {
    windowWidth.value = window.innerWidth
  }
  window.addEventListener('resize', updateWindowSize)
  return () => window.removeEventListener('resize', updateWindowSize)
})
</script>

<template>
  <nav class="bg-white dark:bg-gray-900 fixed w-full z-20 top-0 start-0 border-b border-gray-200 dark:border-gray-600">
    <div class="max-w-screen-xxl flex flex-wrap items-center justify-between mx-auto p-4">
      <a href="#" class="flex items-center space-x-3 rtl:space-x-reverse">
        <img src="../../../assets/img/favicon.svg" class="h-8" alt="SSA Logo">
        <span v-if="windowWidth > 1200" class="self-center text-xl font-semibold whitespace-nowrap dark:text-white">Система Стриминга Автомобилей</span>
        <span v-else class="self-center text-xl font-semibold whitespace-nowrap dark:text-white">ССА</span>
      </a>
      <div class="flex lg:order-2 space-x-3 lg:space-x-0 rtl:space-x-reverse">
        <div v-if="regStatus">
          <button type="button"
                  class="mr-1 text-black-50 bg-gray-200 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
            Войти
          </button>
          <button type="button"
                  class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
            Регистрация
          </button>
        </div>
        <AuthForm v-else/>
        <button data-collapse-toggle="navbar-sticky" type="button"
                class="inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg lg:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
                aria-controls="navbar-sticky" aria-expanded="false">
          <span class="sr-only">Open main menu</span>
          <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 17 14">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M1 1h15M1 7h15M1 13h15" />
          </svg>
        </button>
      </div>
      <NavBar v-model:windowWidth="windowWidth">
        <SearchBar />
      </NavBar>
    </div>
  </nav>


</template>
