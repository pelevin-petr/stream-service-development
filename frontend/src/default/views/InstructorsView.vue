<script setup lang="ts">
import { ref } from 'vue'

import type { Instructor } from '@/shared/modules/instructorsInterface'
import gerasimchuckJPG from '@/default/assets/img/gerasimchuk.jpg'
import LoadingSpinner from '@/shared/modules/LoadingSpinner.vue'

const instructors = ref<Instructor[]>()
const loading = ref<boolean>(true)


setInterval(async () => {
  const res = await fetch(`http://127.0.0.1:8000/api/instructors?filter_params=`)
  
  if (!res.ok) {
    loading.value = false
    instructors.value = []
    return
  }
  loading.value = true
  
  instructors.value = await res.json()
}, 1000)
</script>

<template>
  <div>
    <div
      v-if="instructors && instructors.length > 0"
      class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 2xl:grid-cols-4"
    >
      <div
        v-for="instructor in instructors"
        :key="instructor.id"
      >
        <RouterLink to="/" class="flex flex-col justify-center items-center m-[20px]">
          <img :src="gerasimchuckJPG" alt="Изображение не поддерживается браузером">
          <div class="text-xl text-blue-500 italic mt-[10px] hover:underline hover:text-blue-800">{{ instructor.fullname }}</div>
        </RouterLink>
      </div>
    </div>
    
    <div v-else-if="loading" class="my-[50px]">
      <LoadingSpinner :is-loading="loading" />
    </div>
    
    <div v-else class="text-center my-[50px] text-xl font-semibold text-gray-700">
      Просмотр инструкторов в данный момент невозможен
    </div>
  </div>
</template>

<style scoped>
</style>