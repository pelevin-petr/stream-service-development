<script lang="ts" setup>
import { useKeycloak } from '@josempgon/vue-keycloak'


const { isAuthenticated } = useKeycloak()
const visible = defineModel()
</script>
<template>
  <div class="w-full">
    <ul
      class="flex flex-col justify-between p-4 xl:p-0 mt-4 font-medium border border-gray-100 rounded-lg bg-gray-50 dark:bg-extra-neutral-700 xl:space-x-8 rtl:space-x-reverse xl:flex-row xl:mt-0 xl:border-0 xl:bg-white dark:bg-gray-800 xl:dark:bg-gray-900 dark:border-gray-700">
      <li class="mt-2">
        <RouterLink
          to="/"
          class="block py-2 px-3 text-white xl:text-gray-900 bg-blue-600 rounded xl:bg-transparent xl:hover:text-blue-700 dark:text-white dark:bg-extra-neutral-700 xl:p-0 "
          @click="visible = !visible"
        >
          Главная
        </RouterLink>
      </li>
      <li class="mt-2">
        <RouterLink
          to="/instructors"
          class="block py-2 px-3 text-gray-900 rounded hover:bg-gray-100 xl:hover:bg-transparent xl:hover:text-blue-700 xl:p-0 lg:dark:hover:text-blue-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white xl:dark:hover:bg-transparent dark:border-gray-700"
          @click="visible = !visible"
        >
          Инструкторы
        </RouterLink>
      </li>
      <li class="mt-2" v-if="isAuthenticated">
        <RouterLink
          to="/create-streams"
          class="block py-2 px-3 text-gray-900 rounded hover:bg-gray-100 xl:hover:bg-transparent xl:hover:text-blue-700 xl:p-0 xl:dark:hover:text-blue-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white xlZz:dark:hover:bg-transparent dark:border-gray-700"
          @click="visible = !visible"
        >
          Стримы
        </RouterLink>
      </li>
    </ul>
  </div>
</template>

<style scoped>
@media (prefers-color-scheme: dark) {
  .dark\:bg-extra-neutral-700 {
    --tw-bg-opacity: 1;
    background-color: #2C2C2C
  }
}
</style>