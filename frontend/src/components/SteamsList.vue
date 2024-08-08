<script setup lang="ts">
import { computed, ref } from 'vue'

import LoadingSpinner from '@/components/LoadingSpinner.vue'
import type { Stream } from '@/modules/streamInterface'

const choice = ref("all")
const isLoading = ref(true)
const streams = ref<Stream[]>([])
const aboutStreams = ref<any>()


setInterval(async () => {
  const response = await fetch('http://127.0.0.1:8000/api/streams')
  streams.value = await response.json()
  
  const res = await fetch('http://127.0.0.1:1985/api/v1/streams/')
  aboutStreams.value = await res.json()

}, 1000)

// const filteredStreams = computed( () => {
//   if (choice.value === 'all')
//     return streams.value
//
//
//   const streamsIds = aboutStreams.value.streams.filter((stream: any) => stream.publish.active)
//     .map((s: any) => s.name)
//
//   const streamsPromises = streamsIds.map(async (id: string) => {
//     const res = await fetch(`/api/streams/${id}`)
//     return await res.json()
//   })
//
//   streams.value = (async () =>  await Promise.all(streamsPromises))()
//   return streams.value
// })

</script>

<template>
    <div v-if="streams.length">
      <h2 class="text-xl text-center font-semibold mb-1">Список стримов</h2>
      <h3 class="text-md font-semibo  ld mb-6 inline">Показать:</h3>
      <div class="ml-4 inline">
        <label>
          <input
            type="radio"
            value="all"
            v-model="choice"
            name="streams"
          />
          Все
        </label>
        <label class="ml-3">
          <input
            type="radio"
            value="online"
            v-model="choice"
            name="streams"
          />
          Онлайн
        </label>
      </div>
      <div
        class="p-4 mt-2 bg-gray-100 rounded-xl min-w-[250px] shadow-md max-h-[300px] md:max-h-[460px] overflow-y-auto whitespace-nowrap">
        <ul class="space-y-2">
          <li v-for="stream in streams" :key="stream.id" class="border-b pb-2 hover:underline">
            <RouterLink :to="`/streams/${stream.id}`">{{ stream.title }} {{}}</RouterLink>
          </li>
        </ul>
      </div>
    </div>
    <div
      v-else
      class="flex items-center justify-center pt-[80px] md:pt-[250px]"
    >
      <LoadingSpinner :isLoading="isLoading"></LoadingSpinner>
    </div>
</template>

