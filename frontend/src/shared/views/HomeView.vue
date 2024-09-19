<script lang="ts" setup>
import { onMounted, ref } from 'vue'

import type { BaseStream } from '@/shared/modules/streamInterface'
import loadingWebp from '@/shared/assets/img/loading.webp'

const streams = ref<BaseStream[]>([])

// onMounted(async () => {
//   const response = await fetch('/api/streams')
//   const aboutStreams = await response.json()
//   streams.value = aboutStreams
  // const response = await fetch('http://127.0.0.1:1985/api/v1/streams/')
  // const aboutStreams = await response.json()
  //
  // const streamsIds = aboutStreams.streams.filter((stream: any) => stream.publish.active)
  //                                        .map((s: any) => s.name)
  //
  // const streamsPromises = streamsIds.map(async (id: string) => {
  //   const res = await fetch(`/api/streams/${id}`)
  //   return await res.json()
  // })
  //
  // streams.value = await Promise.all(streamsPromises)
// })
</script>

<template>
  <div class="md:px-8">
    <div class="grid grid-cols-1  md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
      <div v-for="stream of streams" :key="stream.id"
           class="w-auto mx-auto min-w-[300px] max-w-[350px] h-[300px] bg-white shadow-lg rounded-2xl overflow-hidden dark:bg-neutral-500 dark:text-gray-100">
        <RouterLink :to="{ name: 'streams', params: { id: stream.id } }">
          <img :src="loadingWebp" alt="This image don't supported by your browser" class="w-full">
          <label class="block m-4 " for="video">Номер машины: {{ stream.title }}</label>
        </RouterLink>
      </div>
    </div>
  </div>
</template>
