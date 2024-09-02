<script lang="ts" setup>
import { useKeycloak } from '@josempgon/vue-keycloak'


const { isAuthenticated } = useKeycloak()
</script>

<template>
  <footer class="bg-gray-100 text-gray-700 mt-2 dark:bg-extra-neutral-700 dark:text-white">
    <div class="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8 text-center">
      <p class="text-sm">&copy; 2024 Система Стриминга Автомобилей. Все права защищены.</p>
      <nav class="mt-2">
        <RouterLink to="/" class="text-blue-500 hover:underline mx-2 text-sm">Главная</RouterLink>
        <RouterLink to="" class="text-blue-500 hover:underline mx-2 text-sm">Инструкторы</RouterLink>
        <span v-if="isAuthenticated">
          <RouterLink to="create-streams" class="text-blue-500 hover:underline mx-2 text-sm">Стримы</RouterLink>
        </span>
      </nav>
    </div>
  </footer>
</template>

<style scoped>
@media (prefers-color-scheme: dark) {
  .dark\:bg-extra-neutral-700 {
    --tw-bg-opacity: 1;
    background-color: #2C2C2C
  }
}
</style>
