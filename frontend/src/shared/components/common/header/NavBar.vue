<script lang="ts" setup>
import type { NavTab } from '@/shared/modules/nav-tab'

const visible = defineModel()
const isSmallScreen = window.innerWidth <= 1280
const props = defineProps<{ routes: NavTab[] }>()
</script>
<template>
  <div class="w-full">
    <ul
      class="flex flex-col justify-center p-4 xl:p-0 mt-4 font-medium border border-gray-100 rounded-lg bg-gray-50 dark:bg-extra-neutral-700 xl:space-x-8 rtl:space-x-reverse xl:flex-row xl:mt-0 xl:border-0 xl:bg-white dark:bg-gray-800 xl:dark:bg-gray-900 dark:border-gray-700">
      <li class="mt-2" v-for="{to, title} in routes" :key="to">
        <RouterLink
          :to="to"
          class="block py-2 px-3 xl:text-gray-900 bg-gray-100 hover:bg-gray-200 xl:hover:bg-white xl:hover:border-white hover:border hover:border-gray-300 rounded xl:bg-transparent xl:hover:text-blue-700 dark:text-white dark:bg-extra-neutral-700 xl:p-0 "
          @click="isSmallScreen ? visible = !visible : null"
        >
          {{ title }}
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