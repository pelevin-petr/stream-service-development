<script setup lang="ts">
import { useRoute } from 'vue-router'
import { onMounted, ref } from 'vue'
import mpegts from 'mpegts.js'

import { useStreamStore } from '@/stores/stream'

const store = useStreamStore()
const route = useRoute()

const video = ref<HTMLVideoElement | null>(null)

onMounted(() => {
  store.streamId = +route.params.id
  
  if (mpegts.getFeatureList().mseLivePlayback) {
    let player = mpegts.createPlayer({
      type: 'mse',  // could also be mpegts, m2ts, flv
      isLive: true,
      url: `http://127.0.0.1:8080/live/${store.streamId}.flv`
    })
    player.attachMediaElement(video.value!)
    player.load()
    player.play()
  }
})
</script>

<template>
  <div class="flex flex-col items-center">
    <video ref="video" class="w-full bg-gray-600 md:rounded-2xl" controls autoplay muted>
      Your browser does not support the video tag.
    </video>

    <div class="w-full mt-8 bg-white shadow-md rounded-lg p-4 sm:p-6 space-y-4 dark:bg-neutral-500">
      <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center">
        <div class="text-lg font-bold text-gray-900 dark:text-gray-200">Номер машины:</div>
        <div class="text-lg text-gray-700 sm:text-right dark:text-gray-100">{{ store.stream?.title }}</div>
      </div>
      <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center">
        <div class="text-lg font-bold text-gray-900 dark:text-gray-200">Описание:</div>
        <div class="text-lg text-gray-700 sm:text-right dark:text-gray-100">{{ store.stream?.description }}</div>
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
