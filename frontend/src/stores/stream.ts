import { ref, watch } from 'vue'
import { defineStore } from 'pinia'
import type { Stream } from '@/modules/streamInterface'

export const useStreamStore = defineStore('stream', () => {
  const streamId = ref<string>()
  const stream = ref<Stream>()

  watch(streamId, async (newStreamId?: string) => {
    if (!newStreamId) {
      stream.value = undefined
      return
    }

    const res = await fetch(`/api/streams/${streamId.value}`)

    if (!res.ok) {
      stream.value = undefined
      return
    }

    stream.value = await res.json()
  })

  return { stream, streamId }
})
