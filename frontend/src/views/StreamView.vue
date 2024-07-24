<script setup lang="ts">
import { useRoute } from 'vue-router'
import { onMounted } from 'vue'

import { useStreamStore } from '@/stores/stream'
import { dateFormatter } from '@/modules/convertDate'


const store = useStreamStore()
const route = useRoute()


onMounted(() => {
  store.streamId = route.params.id
})
</script>

<template>
  <div class="flex flex-col items-center">
    <video class="w-full bg-gray-600 md:rounded-2xl" controls>
      <source src="@/assets/img/videoplayback%20(1).mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>

    <div class="w-full mt-8 bg-white shadow-md rounded-lg p-4 sm:p-6 space-y-4 dark:bg-neutral-500">
      <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center">
        <div class="text-lg font-bold text-gray-900 dark:text-gray-200">Номер машины:</div>
        <div class="text-lg text-gray-700 sm:text-right dark:text-gray-100">{{ store.stream?.title }}</div>
      </div>
<!--      <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center">-->
<!--        <div class="text-lg font-bold text-gray-900 dark:text-gray-200">Начало стрима:</div>-->
<!--        <div class="text-lg text-gray-700 sm:text-right dark:text-gray-100">{{ dateFormatter(description?.whenTurnOn)-->
<!--          }}-->
<!--        </div>-->
<!--      </div>-->
      <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center">
        <div class="text-lg font-bold text-gray-900 dark:text-gray-200">Описание:</div>
        <div class="text-lg text-gray-700 sm:text-right dark:text-gray-100">{{ store.stream?.description }}</div>
      </div>
<!--      <div v-if="description?.smallDescription"-->
      <!--           class="flex flex-col sm:flex-row justify-between items-start sm:items-center">-->
      <!--        <div class="text-lg font-bold text-gray-900 dark:text-gray-200">Описание:</div>-->
      <!--        <div class="text-lg text-gray-700 sm:text-right dark:text-gray-100">{{ description?.smallDescription }}</div>-->
      <!--      </div>-->
      <!--      <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center">-->
      <!--        <div class="text-lg font-bold text-gray-900 dark:text-gray-200">Город:</div>-->
      <!--        <div class="text-lg text-gray-700 sm:text-right dark:text-gray-100">{{ description?.city }}</div>-->
      <!--      </div>-->
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
