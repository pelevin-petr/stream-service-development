<script setup lang="ts" defer>
import { ref } from 'vue'

import type { Stream } from '@/modules/streamInterface'


const streams = ref<Stream[]>()
const selectedStream = ref<Stream | null>(null)
const search = ref<string>()


setInterval(async () => {
  const res = await fetch(`http://127.0.0.1:8000/api/streams`)
  
  if (!res.ok) {
    return
  }
  
  streams.value = await res.json()
}, 1000)

const openStreamInfo = (selectedStream: Stream) => {

}
</script>

<template>
  <div class="main ">
    
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
              placeholder="Номер машины, id стрима"
              required type="search"
            />
            <button
              class="text-white absolute end-1 bottom-1 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-3.5 py-1.5 dark:bg-gray-800 dark:hover:bg-gray-900 dark:focus:ring-blue-800"
              type="button">
              Поиск
            </button>
          </div>
        </form>
        
        <button
          class="text-white end-1 bottom-1 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-6 py-1.5 dark:bg-gray-800 dark:hover:bg-gray-900 dark:focus:ring-blue-800"
          type="button">
          Создать
        </button>
      </div>
      
      <div class="mt-1 grid grid-cols-3 text-xl font-semibold">
        <div class="grid_element titles">Номер машины</div>
        <div class="grid_element titles">Описание</div>
        <div class="grid_element titles">Id стрима</div>
      </div>
      
      <div class="grid grid-cols-3" v-for="stream in streams" :key="stream.id">
        <button @click="openStreamInfo(stream)">
          <div class="grid_element">{{ stream.title }}</div>
        </button>
        <button @click="openStreamInfo(stream)">
          <div class="grid_element">{{ stream.description }}</div>
        </button>
        <button @click="openStreamInfo(stream)">
          <div class="grid_element">{{ stream.id }}</div>
        </button>
      </div>
    
    </div>
    
    <div class="modal">
      <div class="modal-content">
        <span class="close">&times;</span>
        <h2>Модальное окно</h2>
        <p>Это пример модального окна.</p>
      </div>
    </div>
  </div>


</template>

<style scoped>
.main {
  display: flex;
  
}

.setka {
  transition: margin-right 0.3s ease;
}

.setka.shifted {
  margin-right: 500px;
}

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

.aside-menu {
  width: 500px;
  height: 620px;
  background: rosybrown;
  position: fixed;
  top: 104px;
  right: -500px;
  transition: right 0.3s ease;
  overflow: auto;
  padding: 20px;
}

.aside-menu.open {
  right: 0;
}

.close-btn {
  background: red;
  color: white;
  border: none;
  font-size: 24px;
  cursor: pointer;
  position: absolute;
  top: 20px;
  right: 20px;
}

.modal {
  display: none; /* Скрыть модальное окно по умолчанию */
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0, 0, 0, 0.4);
}

/* Стиль для содержимого модального окна */
.modal-content {
  background-color: #fefefe;
  margin: 30% auto;
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
}

/* Стиль для кнопки закрытия */
.close {
  color: #aaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: black;
  text-decoration: none;
  cursor: pointer;
}
</style>