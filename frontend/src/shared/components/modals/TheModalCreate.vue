<script setup lang="ts">
import { nextTick, onMounted, onUnmounted, ref } from 'vue'

import { $vCreate, errorsCreate } from '@/shared/validation/validationCreating'

const id = ref<number>()
const isCreated = ref<boolean>(true)
const submittedCreating = ref<boolean>(false)
const modalOverlay = ref<HTMLDivElement>()

const isOpen = defineModel()
const validateCreating = async () => {
  
  submittedCreating.value = true
  $vCreate.value.$touch()
  
  const result = await $vCreate.value.$validate()

  if (!result) {
    return
  }
  
  await createStream()
  $vCreate.value.title.$model = ''
  $vCreate.value.description.$model = ''
  $vCreate.value.file.$model = undefined
  submittedCreating.value = false
}

const createStream = async () => {
  const formData = new FormData()
  formData.append('title', $vCreate.value.title.$model)
  formData.append('description', $vCreate.value.description.$model)
  
  if ($vCreate.value.file.$model) {
    formData.append('file', $vCreate.value.file.$model)
  }
  
  const res = await fetch(`http://127.0.0.1:8000/api/streams`, {
    method: 'POST',
    body: formData
  })
  
  if (!res.ok) {
    isCreated.value = false
    return
  }

  const stream = await res.json()
  id.value = stream.Stream.id
  isCreated.value = true
}

const clearCreateForm = () => {
  $vCreate.value.title.$model = ''
  $vCreate.value.description.$model = ''
  $vCreate.value.file.$model = undefined
}

const handleFileChange = (event: Event) => {
  const target = event.target as HTMLInputElement
  if (target.files && target.files.length > 0) {
    $vCreate.value.file.$model = target.files[0]
  }
}

const handleOutsideClick = (event: MouseEvent) => {
  if (event.composedPath().includes(modalOverlay.value!)) {
    isOpen.value = false
  }
}

onMounted(() => {
  nextTick(() => {
    document.addEventListener('click', handleOutsideClick)
  })
})

onUnmounted(() => {
  document.removeEventListener('click', handleOutsideClick)
})

const closeModal = () => {
  isOpen.value = !isOpen.value
}
</script>

<template>
  <div v-if="isOpen" class="modal" ref="modalOverlay">
    <div class="relative" @click.stop>
      <button class="absolute right-[18px] top-[-5px] text-md" @click="closeModal">
        <span class="close">&times;</span>
      </button>
      <div class="flex-1 px-2 flex items-center justify-center">
        <div class="min-w-[350px] max-w-[750px] rounded-2xl shadow-xl flex flex-col p-4 bg-white">
          <form @submit.prevent="validateCreating" class="w-full" enctype="multipart/form-data">
            <div class="text-center mb-12">
              <h3 class="text-xl leading-6 text-black mt-[5px]">
                Заполните поля, чтобы создать стрим и получить его идентификационный номер
              </h3>
            </div>
            
            <div class="mt-4">
              <label class="block text-sm font-medium leading-6 text-gray-900">Номер машины</label>
              <input type="text"
                     v-model="$vCreate.title.$model"
                     placeholder="A000AA"
                     class="block w-full rounded-md border-0 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-blue-600 sm:text-sm">
            </div>
            <div v-if="errorsCreate.title && submittedCreating" class="text-red-600 text-sm pl-1 italic">
              {{ errorsCreate.title }}
            </div>
            
            <div class="mt-4">
              <label class="block text-sm font-medium leading-6 text-gray-900">Описание</label>
              <input type="text"
                     v-model="$vCreate.description.$model"
                     class="block w-full rounded-md border-0 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-blue-600 sm:text-sm">
            </div>
            
            <!-- Поле для загрузки файла -->
            <div class="mt-4">
              <label class="block text-sm font-medium leading-6 text-gray-900">Загрузить фото</label>
              <input type="file" @change="handleFileChange"
                     class="block w-full rounded-md border-0 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 sm:text-sm">
            </div>
            <div v-if="errorsCreate.file && submittedCreating" class="text-red-600 text-sm pl-1 italic">
              {{ errorsCreate.file }}
            </div>
            <div class="flex justify-around w-full mt-4">
              <button type="button"
                      @click="clearCreateForm"
                      class="px-6 py-1 mt-2 font-medium rounded-lg text-md text-center leading-6 text-gray-900 bg-gray-200 hover:bg-gray-400 focus:ring-4 focus:ring-gray-300">
                Очистить
              </button>
              
              <button type="submit"
                      class="px-6 mt-2 py-1 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-md text-center"
              >
                Создать
              </button>
            </div>
            
            <div v-if="isCreated" class="mt-6 text-center">
              <div class="text-md">
                Ваш идентификационный номер: <span class="text-black font-semibold font-mono">{{ id }}</span>
              </div>
            </div>
            
            <div v-else class="text-red-600 text-center mt-6 text-md">
              Во время выполнения запроса произошла ошибка. Попробуйте сначала.
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.modal {
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  z-index: 10;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.4);
}

.close {
  display: flex;
  justify-content: end;
  
  color: #aaa;
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
