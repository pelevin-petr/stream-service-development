import { ref, watch } from 'vue'
import { defineStore } from 'pinia'
import type { Stream } from '@/shared/modules/streamInterface'

export const useStreamStore = defineStore('stream', () => {
  const streamId = ref<number>()
  const stream = ref<Stream>()

  watch(streamId, async (newStreamId?: number) => {
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

  })

  return { stream, streamId }
})
