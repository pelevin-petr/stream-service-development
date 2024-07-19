<script setup lang="ts">
import { useStreamStore } from '@/stores/streamStore'



const store = useStreamStore()

const description = store.video.description
const date = description.whenIncluded

const options = {
  year: 'numeric',
  month: '2-digit',
  day: '2-digit',
  hour: '2-digit',
  minute: '2-digit',
  second: '2-digit',
  hour12: false
};
const formatter = new Intl.DateTimeFormat('ru-RU', options);
const formattedDate = formatter.format(date);
</script>

<template>
  <div>
    <div>
      <video class="w-full bg-gray-600  mt-16" controls>
        <source src="../../../../assets/img/videoplayback%20(1).mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </div>
    <div>
      <div class="max-w-3xl mx-auto bg-white shadow-lg rounded-lg p-4 sm:p-6 space-y-4">
        <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center">
          <div class="text-lg font-bold text-gray-900">Car Number:</div>
          <div class="text-lg text-gray-700 sm:text-right">{{ description.carNumber }}</div>
        </div>
        <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center">
          <div class="text-lg font-bold text-gray-900">When Included:</div>
          <div class="text-lg text-gray-700 sm:text-right">{{ formattedDate }}</div>
        </div>
        <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center">
          <div class="text-lg font-bold text-gray-900">Streamer:</div>
          <div class="text-lg text-gray-700 sm:text-right">{{ description.streamer }}</div>
        </div>
        <div v-if="description.smallDescription"
             class="flex flex-col sm:flex-row justify-between items-start sm:items-center">
          <div class="text-lg font-bold text-gray-900">Description:</div>
          <div class="text-lg text-gray-700 sm:text-right">{{ description.smallDescription }}</div>
        </div>
        <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center">
          <div class="text-lg font-bold text-gray-900">City:</div>
          <div class="text-lg text-gray-700 sm:text-right">{{ description.city }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
@media (max-width: 375px) {
  .text-lg {
    font-size: 1rem; /* Уменьшение размера шрифта для небольших экранов */
  }
  
  .p-4 {
    padding: 1rem; /* Уменьшение внутреннего отступа */
  }
  
  .space-y-4 > :not([hidden]) ~ :not([hidden]) {
    --tw-space-y-reverse: 0;
    margin-top: 0.5rem; /* Уменьшение вертикального расстояния между элементами */
  }
}
</style>