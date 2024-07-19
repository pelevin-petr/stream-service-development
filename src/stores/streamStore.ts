import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useStreamStore = defineStore('counter', () => {
  const video = ref()
  return { video }

})