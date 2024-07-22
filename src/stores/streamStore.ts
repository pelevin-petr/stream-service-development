import { computed, ref } from 'vue'
import { defineStore } from 'pinia'
import { streamData } from '@/modules/data'

export const useStreamStore = defineStore('stream', () => {
  const streamId = ref()
  const stream = computed(() => {
    return streamData.find((s) => s.id == streamId.value)
  })

  return { stream, streamId }
})