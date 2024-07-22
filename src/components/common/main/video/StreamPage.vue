<script setup lang="ts">
import { useStreamStore } from '@/stores/streamStore'
import { useRoute } from 'vue-router'
import { computed, onMounted } from 'vue'



const store = useStreamStore()
const route = useRoute()



// const options = {
//   year: 'numeric',
//   month: '2-digit',
//   day: '2-digit',
//   hour: '2-digit',
//   minute: '2-digit',
//   second: '2-digit',
//   hour12: false
// };
// const formatter = new Intl.DateTimeFormat('ru-RU', options);
// const formattedDate = formatter.format(date);

onMounted(() => {
  store.streamId = route.params.id
})

const description = computed(() => store.stream?.description)
</script>

<template>
  <div>
    <div class="flex justify-center items-center  ">
      <video class="w-full md:max-w-3xl lg:max-w-5xl xl:max-w-6xl bg-gray-600 md:rounded-2xl mt-[69px] mb-5" controls>
        <source src="../../../../assets/img/videoplayback%20(1).mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </div>
    <div>
      <div class="max-w-3xl mx-auto bg-white shadow-md rounded-lg p-4 sm:p-6 space-y-4 dark:bg-neutral-500">
        <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center">
          <div class="text-lg font-bold text-gray-900 dark:text-gray-200">Car Number:</div>
          <div class="text-lg text-gray-700 sm:text-right dark:text-gray-100">{{ description?.carNumber }}</div>
        </div>
        <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center">
          <div class="text-lg font-bold text-gray-900 dark:text-gray-200">When Included:</div>
          <div class="text-lg text-gray-700 sm:text-right dark:text-gray-100"></div>
        </div>
        <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center">
          <div class="text-lg font-bold text-gray-900 dark:text-gray-200">Streamer:</div>
          <div class="text-lg text-gray-700 sm:text-right dark:text-gray-100">{{ description?.streamer }}</div>
        </div>
        <div v-if="description?.smallDescription"
             class="flex flex-col sm:flex-row justify-between items-start sm:items-center">
          <div class="text-lg font-bold text-gray-900 dark:text-gray-200">Description:</div>
          <div class="text-lg text-gray-700 sm:text-right dark:text-gray-100">{{ description?.smallDescription }}</div>
        </div>
        <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center">
          <div class="text-lg font-bold text-gray-900 dark:text-gray-200">City:</div>
          <div class="text-lg text-gray-700 sm:text-right dark:text-gray-100">{{ description?.city }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
@media (max-width: 375px) {
  .text-lg {
    font-size: 1rem;
  }
  
  .p-4 {
    padding: 1rem;
  }
  
  .space-y-4 > :not([hidden]) ~ :not([hidden]) {
    --tw-space-y-reverse: 0;
    margin-top: 0.5rem;
  }
}
</style>