<script lang="ts" setup>

</script>

<template>
  <form class="min-w-80">
    <label class="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white"
           for="default-search">Search</label>
    <div class="relative">
      <div class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
        <svg aria-hidden="true" class="w-4 h-4 text-gray-500 dark:text-gray-400"
             fill="none" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
          <path d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z" stroke="currentColor" stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2" />
        </svg>
      </div>
      <input id="default-search"
             class="block w-full h-10 p-4 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
             placeholder="Город, номер стрима..."
             required type="search" />
      <button
        class="text-white absolute end-1 bottom-1 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-3.5 py-1.5 dark:bg-gray-800 dark:hover:bg-gray-900 dark:focus:ring-blue-800"
        type="submit">
        Поиск
      </button>
    </div>
  </form>
</template>
