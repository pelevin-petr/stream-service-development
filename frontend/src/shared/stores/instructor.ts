import { ref } from 'vue'
import { defineStore } from 'pinia'
import type { Instructor } from '@/shared/modules/instructorsInterface'

export const useInstructorStore = defineStore('instructor', () => {
  const instructor = ref<Instructor>()
  return { instructor }
})
