<script setup lang="ts">
import { ref } from 'vue'


const title = ref<string>('')
const description = ref<string>('')
const id = ref<number>()


const createStream = async () => {
  const res = await fetch(`http://127.0.0.1:8000/api/streams`, {
    method: 'POST',
    headers: { 'content-type': 'application/json' },
    body: JSON.stringify({
      title: title.value,
      description: description.value
    })
  })
  
  const stream = await res.json()
  id.value = stream.id
}

const clear = () => {
  title.value = ''
  description.value = ''
}
</script>
<template>
  <div class="h-[70vh] px-2">
    <div class="min-w-[350px] max-w-[750px] rounded-2xl shadow-xl flex flex-col items-center justify-center p-4">
      <form class="w-full">
        <div class="">
          <div class="">
            <div class="">
              <h3 class="text-xl text-center leading-6 text-black mb-12">
                Заполните поля, чтобы создать стрим и получить его
                идентификационный номер
              </h3>
              <div class="mt-4">
                <label class="block text-sm font-medium leading-6 text-gray-900">Номер машины*</label>
                <div class="mt-2">
                  <input type="text"
                         v-model="title"
                         placeholder="A000AA"
                         class="block w-full rounded-md border-0 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                </div>
              </div>
              
              <div class="mt-4">
                <label class="block text-sm font-medium leading-6 text-gray-900">Описание</label>
                <div class="mt-2">
                  <input type="text"
                         v-model="description"
                         class="block w-full rounded-md border-0 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                </div>
              </div>
            </div>
            
            <div class="flex justify-around w-full mt-4">
              <button type="button"
                      @click="clear"
                      class="px-6 py-1 mt-2 font-medium rounded-lg text-md text-center leading-6 text-gray-900 bg-gray-200 hover:bg-gray-400 focus:ring-4 focus:outline-none focus:ring-gray-300">
                Очистить
              </button>
              <button type="button"
                      @click="createStream(); clear(); "
                      :disabled="title == ''"
                      class="px-6 mt-2 py-1 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-md text-center">
                Создать
              </button>
            </div>
            
            <div class="pt-3 text-sm italic">
              * — обязательные поля
            </div>
            
            <div class="mt-[25px] md:mt-[60px] text-center">
              <div class="sm:text-xl text-md">
                Ваш идентификационный номер: <span class=" text-black font-semibold font-mono">{{ id }}</span>
              </div>
            </div>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<style scoped>

</style>