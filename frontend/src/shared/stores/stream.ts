import { ref, watch } from 'vue'
import { defineStore } from 'pinia'
import type { BaseStream } from '@/shared/modules/streamInterface'

export const useStreamStore = defineStore('stream', () => {
  const streamId = ref<number>()
  const stream = ref<BaseStream>()

  watch(streamId, async (newStreamId?: number) => {
    if (!newStreamId) {
      stream.value = undefined
      return
    }

    const res = await fetch(`/api/streams/${newStreamId}`)

    if (!res.ok) {
      stream.value = undefined
      return
    }

    stream.value = await res.json()

  })

  return { stream, streamId }
})
