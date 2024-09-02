<script setup lang="ts">
import { ref } from 'vue'
import { useKeycloak } from '@josempgon/vue-keycloak'

import type { Stream } from '@/shared/modules/streamInterface'
import TheModal from '@/shared/components/modals/TheModal.vue'
import CreateDeleteStream from '@/shared/components/modals/TheModalCreate.vue'
import ThePopUpDeleting from '@/shared/components/modals/ThePopUpDeleting.vue'
import LoadingSpinner from '@/shared/modules/LoadingSpinner.vue'
import trashSvg from '@/shared/assets/img/trash.svg'


const streams = ref<Stream[]>([])
const search = ref<string>('')
const model = ref()
const isOpenCreateModal = ref(false)
const loading = ref<boolean>(true)
const { isAuthenticated } = useKeycloak()

const popupModel = ref()


setInterval(async () => {
  const res = await fetch(`http://127.0.0.1:8000/api/instructors?filter_params=${search.value}`)
  
  if (!res.ok) {
    loading.value = false
    streams.value = []
    return
  }
  loading.value = true
  
  streams.value = await res.json()
}, 1000)

const deleteStream = (stream: Stream) => {
  popupModel.value.stream = stream
  popupModel.value.continueDeleting = true
  
  const deleteTimeout = setTimeout(async () => {
    const res = await fetch(`http://127.0.0.1:8000/api/streams?stream_id=${stream.id}`, {
      method: 'DELETE',
      headers: { 'content-type': 'application/json' }
    })
    
    if (!res.ok) {
      return
    }
    streams.value = streams.value.filter((s) => s.id != stream.id)
  }, 7000)
  
  const interval = setInterval(() => {
    if (!popupModel.value.continueDeleting) {
      clearTimeout(deleteTimeout)
      clearInterval(interval)
    }
  })
}

</script>
<template>
  <div class="main">
    <div class="w-full">
      <div class="flex justify-between">
        <form class="min-w-80 ">
          <div class="relative">
            <div class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
              <svg aria-hidden="true" class="w-4 h-4 text-gray-500 dark:text-gray-400"
                   fill="none" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                <path d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z" stroke="currentColor" stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2" />
              </svg>
            </div>
            <input
              class="block w-full h-10 p-4 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              v-model="search"
              placeholder="ФИО инструктора"
              required type="search"
            />
            <button
              class="text-white absolute end-1 bottom-1 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-3.5 py-1.5 dark:bg-gray-800 dark:hover:bg-gray-900 dark:focus:ring-blue-800"
              type="button"
            >
              Поиск
            </button>
          </div>
        </form>
        
        <button
          v-if="isAuthenticated"
          class="text-white end-1 bottom-1 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-6 py-1.5 dark:bg-gray-800 dark:hover:bg-gray-900 dark:focus:ring-blue-800"
          type="button"
          @click="isOpenCreateModal = !isOpenCreateModal">
          Создать
        </button>
      </div>
      
      <div v-if="streams && streams.length > 0">
        <div class="mt-1 grid grid-cols-3 text-xl font-semibold">
          <div class="grid_element titles">Id инструктора</div>
          <div class="grid_element titles">ФИО</div>
          <div class="grid_element titles">Стаж работы</div>
        </div>
        
        <div class="relative grid grid-cols-3" v-for="stream in streams" :key="stream.id">
          <button @click="model.openStreamInfo(stream)">
            <div class="grid_element">{{ stream.id }}</div>
          </button>
          <button @click="model.openStreamInfo(stream)">
            <div class="grid_element">{{ stream.fullname }}</div>
          </button>
          <button @click="model.openStreamInfo(stream)">
            <div class="grid_element">{{ stream.workExperiens }}</div>
          </button>
          <button
            v-if="isAuthenticated"
            class="absolute w-[30px] right-[5px] top-[7px]"
            @click="deleteStream(stream); popupModel!.openPopup()"
          >
            <img :src="trashSvg" alt="" />
          </button>
        </div>
      </div>
      
      <div v-else-if="loading" class="my-[50px]">
        <LoadingSpinner :is-loading="loading" />
      </div>
      
      <div v-else class="text-center my-[50px] text-xl font-semibold text-gray-700">
        Стримов по данному запросу не найдено
      </div>
    </div>
    
    <TheModal v-model="model" />
    <CreateDeleteStream v-model="isOpenCreateModal" />
    <ThePopUpDeleting v-model="popupModel" />
  </div>


</template>

<style scoped>
.grid_element {
  min-height: 45px;
  background: rgb(209 213 219);
  border: 1px solid rgb(107 114 128);
  display: flex;
  justify-content: center;
  align-items: center;
}

.titles {
  background-color: rgb(156 163 175);
}
</style>