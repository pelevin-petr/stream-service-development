<script setup lang="ts">
import { ref } from 'vue'


const title = ref<string>('')
const description = ref<string>('')
const id = ref<number>()
const deleteId = ref<number>()
const isDeleted = ref<boolean>(false)
const isCreated = ref<boolean>(true)
const deletionError = ref<boolean>(false)
const deletedStream = ref()


const createStream = async () => {
  const res = await fetch(`http://127.0.0.1:8000/api/streams`, {
    method: 'POST',
    headers: { 'content-type': 'application/json' },
    body: JSON.stringify({
      title: title.value,
      description: description.value
    })
  })
  
  if (!res.ok) {
    isCreated.value = false
    return
  }
  
  const stream = await res.json()
  id.value = stream.id
  isCreated.value = true
}

const clearCreateForm = () => {
  title.value = ''
  description.value = ''
}
const clearDeleteForm = () => {
  deleteId.value = undefined
}


const deleteStream = async () => {
  const res = await fetch(`http://127.0.0.1:8000/api/streams?stream_id=${deleteId.value}`, {
    method: 'DELETE',
    headers: { 'content-type': 'application/json' },
  })
  
  if (!res.ok) {
    deletionError.value = true
    isDeleted.value = false
    return
  }
  
  deletedStream.value = await res.json()
  isDeleted.value = true
}
</script>
<template>
  <div class="h-[80vh] px-2 flex items-center justify-center">
    <div class="min-w-[350px] max-w-[750px] rounded-2xl shadow-xl flex flex-col p-4">
      <form class="w-full">
        <div class="text-center mb-12">
          <h3 class="text-xl leading-6 text-black">
            Заполните поля, чтобы создать стрим и получить его идентификационный номер
          </h3>
        </div>
        
        <div class="mt-4">
          <label class="block text-sm font-medium leading-6 text-gray-900">Номер машины*</label>
          <input type="text"
                 v-model="title"
                 placeholder="A000AA"
                 class="block w-full rounded-md border-0 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-blue-600 sm:text-sm">
        </div>
        
        <div class="mt-4">
          <label class="block text-sm font-medium leading-6 text-gray-900">Описание</label>
          <input type="text"
                 v-model="description"
                 class="block w-full rounded-md border-0 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-blue-600 sm:text-sm">
        </div>
        
        <div class="flex justify-around w-full mt-4">
          <button type="button"
                  @click="clearCreateForm()"
                  class="px-6 py-1 mt-2 font-medium rounded-lg text-md text-center leading-6 text-gray-900 bg-gray-200 hover:bg-gray-400 focus:ring-4 focus:ring-gray-300">
            Очистить
          </button>
          
          <button type="button"
                  @click="createStream(); clearCreateForm();"
                  :disabled="title == ''"
                  class="px-6 mt-2 py-1 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-md text-center">
            Создать
          </button>
        </div>
        
        <div
          v-if="isCreated"
          class="mt-6 text-center"
        >
          <div class="text-md">
            Ваш идентификационный номер: <span class="text-black font-semibold font-mono">{{ id }}</span>
          </div>
        </div>
        
        <div
          v-else
          class="text-red-600 text-center mt-6 text-md"
        >
          Во время выполнения запроса произошла ошибка. Попробуйте сначала.
        </div>
        
        <div class="mt-16 text-center">
          <h3 class="text-xl leading-6 text-black mb-5">
            Введите идентификационный номер для удаления стрима
          </h3>
          
          <input type="number"
                 v-model="deleteId"
                 class="block mx-auto mb-2 w-full max-w-[400px] rounded-md border-0 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-blue-600 sm:text-sm">
          
          <button
            type="button"
            :disabled="deleteId == undefined"
            class="px-6 mt-2 py-1 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-md text-center"
            @click="deleteStream(); clearDeleteForm()"
          >
            Удалить
          </button>
          
          <div
            class="mt-4"
            v-if="isDeleted">
            Стрим c номером машины «{{ deletedStream.title }}» был успешно удален
          </div>
          
          <div
            v-else-if="deletionError"
            class="text-red-600 text-center mt-4 text-md">
            Во время выполнения запроса произошла ошибка. Попробуйте сначала.
          </div>
        </div>
        
        <div class="pt-6 text-sm italic">
          * — обязательные поля
        </div>
      </form>
    </div>
  </div>

</template>

<style scoped>

</style>