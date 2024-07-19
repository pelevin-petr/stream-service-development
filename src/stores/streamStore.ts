import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useStreamStore = defineStore('stream', () => {
  const video = ref()
  return { video }

})