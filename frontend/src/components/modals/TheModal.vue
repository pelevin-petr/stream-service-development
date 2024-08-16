<script setup lang="ts">
import { onUnmounted, ref, nextTick, onMounted } from 'vue'

import type { Stream } from '@/modules/streamInterface'
import { $vCreate, errorsCreate } from '@/validation/validationCreating'


const isOpen = ref(false)
const newImage = ref<HTMLImageElement | null>()
const updatedStreamClass = ref<string>('hidden')
const defaultStreamClass = ref<string>('inline')
const selectedStream = ref<Stream>()
const submittedCreating = ref(false)
const modalOverlay = ref<HTMLDivElement>()

const model = defineModel()

const validateCreating = async () => {
  submittedCreating.value = true
  $vCreate.value.$touch()
  
  const result = await $vCreate.value.$validate()
  
  if (!result) {
    return
  }
  
  await updateStream()
  $vCreate.value.title.$model = ''
  $vCreate.value.description.$model = ''
  submittedCreating.value = false
}

const openStreamInfo = (stream: Stream) => {
  isOpen.value = !isOpen.value
  selectedStream.value = stream
}
model.value = {
  openStreamInfo: openStreamInfo
}
const handleOutsideClick = (event: MouseEvent) => {
  if (event.composedPath().includes(modalOverlay.value!)) {
    isOpen.value = false
    cancelUpdate()
    
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

const changeStream = () => {
  updatedStreamClass.value = 'inline'
  defaultStreamClass.value = 'hidden'
}

const cancelUpdate = () => {
  updatedStreamClass.value = 'hidden'
  defaultStreamClass.value = 'inline'
  $vCreate.value.title.$model = ''
  $vCreate.value.description.$model = ''
}
const updateStream = async () => {
  const res = await fetch(`http://127.0.0.1:8000/api/streams?stream_id=${selectedStream.value?.id}`, {
    method: 'PUT',
    headers: { 'content-type': 'application/json' },
    body: JSON.stringify({
      title: $vCreate.value.title.$model,
      description: $vCreate.value.description.$model
    })
  })
  
  if (!res.ok) {
    return
  }
  
  selectedStream.value = await res.json()
  
  cancelUpdate()
}
const closeModal = () => {
  isOpen.value = !isOpen.value
  cancelUpdate()
}
</script>

<template>
  <div v-if="isOpen" class="modal" ref="modalOverlay">
    <div class="modal-content relative rounded-xl" @click.stop>
      <button class="absolute right-3 top-0" @click="closeModal">
        <span class="close">&times;</span>
      </button>
      <div class="wrapper">
        
        <div>
          <img src="../../assets/img/modal-car.png" alt="Это изображение не поддерживается вашим браузером"
               class="w-[170px] md:w-[200px] rounded-xl " />
          <div :class="updatedStreamClass">
            <label
              class="upload-label block cursor-pointer p-[5px] text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium text-center mt-[15px]">
              <span>Выберите фотографию</span>
              <input type="file" class="hidden" accept="image/*" ref="newImage">
            </label>
          </div>
        </div>
        
        <div class="flex flex-col justify-around items-center text-center">
          <h2 class="font-semibold">Номер машины:
            <span class=""
                  :class="defaultStreamClass"
            >
                {{ selectedStream?.title }}
              </span>
            
            <input
              class="w-[60px] h-[25px]"
              :class="updatedStreamClass"
              type="text"
              v-model="$vCreate.title.$model">
            <div v-if="errorsCreate.title && submittedCreating" class="text-red-600 text-sm pl-1 italic">
              {{ errorsCreate.title }}
            </div>
          </h2>
          <h2 class="font-semibold">Описание:
            <span
              class=""
              :class="defaultStreamClass"
            >
                {{ selectedStream?.description }}
              </span>
            <input
              class="w-[100px] h-[25px]"
              :class="updatedStreamClass"
              type="text"
              v-model="$vCreate.description.$model">
          </h2>
        </div>
        <div>
          <button
            class="w-[100px] absolute bottom-[8px] right-[8px] text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-3.5 py-1.5"
            :class="updatedStreamClass"
            @click="validateCreating">
            Сохранить
          </button>
          <button
            class="w-[100px] absolute bottom-[8px] right-[115px] text-white bg-red-600 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm px-3.5 py-1.5"
            :class="updatedStreamClass"
            @click="cancelUpdate"
          >
            Отменить
          </button>
        </div>
        <button
          class="w-[100px] absolute bottom-[8px] right-[115px] text-white bg-red-600 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm px-3.5 py-1.5"
          :class="defaultStreamClass"
        >
          Удалить
        </button>
        <button
          class="w-[100px] absolute bottom-[8px] right-[8px] text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-3.5 py-1.5"
          :class="defaultStreamClass"
          @click="changeStream">
          Изменить
        </button>
      
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

.modal-content {
  background-color: #fefefe;
  margin: auto;
  padding: 20px;
  border: 1px solid #888;
  width: 70%;
  max-width: 600px;
  max-height: 80%;
}

@media (max-width: 640px) {
  .modal-content {
    width: 90%;
  }
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

.wrapper {
  display: grid;
  grid-template-columns: 1fr 2fr;
}


.upload-label {
  border: 2px solid transparent;
  border-radius: 8px;
  font-size: 12px;
  transition: background-color 0.3s;
}
</style>