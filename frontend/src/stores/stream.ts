import { ref, watch } from 'vue'
import { defineStore } from 'pinia'
import type { Stream } from '@/modules/streamInterface'

export const useStreamStore = defineStore('stream', () => {
  const streamId = ref<string>('')
  const stream = ref<Stream>()

  watch(streamId, async (newStreamId?: string) => {
    if (!newStreamId) {
      stream.value = undefined
      return
    } 
                                                            //streamId.value(так было изначально)
    const res = await fetch(`/api/streams/${newStreamId}`)

    if (!res.ok) {
      stream.value = undefined
      return
    }

    stream.value = await res.json()

    if (stream.value !== undefined) {
      stream.value = stream.value[streamId.value]
    }
  })

  return { stream, streamId }
})
