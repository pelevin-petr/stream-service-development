<script lang="ts" setup>

import { streamData } from '@/modules/data'

</script>

<template>
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8 mx-8 mt-20">
    <div v-for="video of streamData" :key="video.id"
         class="max-w-[350px] h-[300px] bg-white mx-auto shadow-lg rounded-2xl overflow-hidden dark:bg-neutral-500 dark:text-gray-100">
      <div v-if="video.included">
        <RouterLink :to="{ name: 'Stream', params: { id: video.id } }">
          <img src="../../../../assets/img/dog.jpg" alt="This image don't supported by your browser" class="w-full">
          <label class="block m-4 " for="video">Номер машины: {{ video.description.carNumber }}</label>
        </RouterLink>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>