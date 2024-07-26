<script lang="ts" setup>

import type { Stream } from '@/modules/streamInterface'
import { onMounted, ref } from 'vue'

const streams = ref<Stream[]>()

onMounted(async () => {
  const res = await fetch('/api/streams')
  streams.value = await res.json()
})

</script>

<template>
  <div>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
      <div v-for="stream of streams" :key="stream.id"
           class="w-[300px] max-w-[350px] h-[300px] bg-white shadow-lg rounded-2xl overflow-hidden dark:bg-neutral-500 dark:text-gray-100">
        <RouterLink :to="{ name: 'stream', params: { id: stream.id } }">
          <img src="@/assets/img/dog.jpg" alt="This image don't supported by your browser" class="w-full">
          <label class="block m-4 " for="video">Номер машины: {{ stream.title }}</label>
        </RouterLink>
      </div>
    </div>
  </div>
</template>
