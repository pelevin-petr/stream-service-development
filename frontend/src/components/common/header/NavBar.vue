<script lang="ts" setup>

</script>

<template>
  <div id="navbar-sticky" class="items-center justify-between w-full xl:flex xl:w-auto xl:order-1 ">
    <ul
      class="flex flex-col p-4 xl:p-0 mt-4 font-medium border border-gray-100 rounded-lg bg-gray-50 dark:bg-extra-neutral-700 xl:space-x-8 rtl:space-x-reverse xl:flex-row xl:mt-0 xl:border-0 xl:bg-white dark:bg-gray-800 xl:dark:bg-gray-900 dark:border-gray-700">
      <li class="mt-2">
        <RouterLink to="/">
          <a aria-current="page"
             class="block py-2 px-3 text-white bg-blue-700 rounded xl:bg-transparent xl:text-blue-700 dark:text-white dark:bg-extra-neutral-700 xl:p-0 "
             href="#">Главная</a>
        </RouterLink>
      </li>
      <li class="mt-2">
        <a
          class="block py-2 px-3 text-gray-900 rounded hover:bg-gray-100 xl:hover:bg-transparent xl:hover:text-blue-700 xl:p-0 lg:dark:hover:text-blue-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white xl:dark:hover:bg-transparent dark:border-gray-700"
          href="#">Города</a>
      </li>
      <li class="mt-2">
        <RouterLink to="create-streams"
          class="block py-2 px-3 text-gray-900 rounded hover:bg-gray-100 xl:hover:bg-transparent xl:hover:text-blue-700 xl:p-0 xl:dark:hover:text-blue-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white xlZz:dark:hover:bg-transparent dark:border-gray-700"
          href="#">Создать стрим</RouterLink>
      </li>
      <li>
        <slot></slot>
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