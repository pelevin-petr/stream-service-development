<script lang="ts" setup>
const windowWidth = defineModel<number>()

const calcWindowWidth = (windowWidth: number | undefined): string => {
  if (!windowWidth) {
    return ''
  }
  if (windowWidth > 1500) {
    return 'margin-right: 256px'
  } else {
    return 'margin-left: 0px'
  }
}
</script>

<template>
  <div id="navbar-sticky" class="items-center justify-between hidden w-full lg:flex lg:w-auto lg:order-1">
    <ul
      :style="calcWindowWidth(windowWidth)"
      class="flex flex-col p-4 lg:p-0 mt-4 font-medium border border-gray-100 rounded-lg bg-gray-50 lg:space-x-8 rtl:space-x-reverse lg:flex-row lg:mt-0 lg:border-0 lg:bg-white dark:bg-gray-800 lg:dark:bg-gray-900 dark:border-gray-700">
      <li class="mt-2">
        <RouterLink to="/">
          <a aria-current="page"
             class="block py-2 px-3 text-white bg-blue-700 rounded lg:bg-transparent lg:text-blue-700 lg:p-0 lg:dark:text-blue-500"
             href="#">Главная</a>
        </RouterLink>
      </li>
      <li class="mt-2">
        <a
          class="block py-2 px-3 text-gray-900 rounded hover:bg-gray-100 lg:hover:bg-transparent lg:hover:text-blue-700 lg:p-0 lg:dark:hover:text-blue-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white lg:dark:hover:bg-transparent dark:border-gray-700"
          href="#">Города</a>
      </li>
      <li class="mt-2">
        <a
          class="block py-2 px-3 text-gray-900 rounded hover:bg-gray-100 lg:hover:bg-transparent lg:hover:text-blue-700 lg:p-0 lg:dark:hover:text-blue-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white lg:dark:hover:bg-transparent dark:border-gray-700"
          href="#">Автошколы</a>
      </li>
      <li>
        <slot></slot>
      </li>
    </ul>
  </div>
</template>
