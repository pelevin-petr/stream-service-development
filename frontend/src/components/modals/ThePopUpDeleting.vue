<script setup>
import { ref } from 'vue'


const isPopupVisible = ref(false)
const isVisible = ref(false)
const popupModel = defineModel()


const openPopup = () => {
  isVisible.value = true
  setTimeout(() => {
    isPopupVisible.value = true
  }, 10)
  setTimeout(closePopup, 7000)
}

popupModel.value = {
  openPopup: openPopup
}

const closePopup = () => {
  isPopupVisible.value = false
  setTimeout(() => {
    isVisible.value = false
  }, 300)
}
</script>
<template>
  <div v-if="isVisible"
       class="popup border border-rose-500"
       :class="{ show: isPopupVisible }">
    
    <div class="text-center font-bold mb-[11px]">Стрим успешно удален!</div>
    <div>Id: {{ popupModel.stream.id }}</div>
    <div>Номер машины: {{ popupModel.stream.title }}</div>
    <div>Описание: {{ popupModel.stream.description }}</div>
    
    <button @click="closePopup">
      <span class="close">&times;</span>
    </button>
  
  </div>
</template>
<style scoped>
.popup {
  position: fixed;
  bottom: 20px;
  right: 20px;
  width: 300px;
  padding: 20px 20px 0;
  background-color: rgba(228, 184, 184, 0.34);
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  z-index: 20;
  transition: transform 0.7s ease, opacity 0.5s ease;
  transform: translateY(100%);
  opacity: 0;
}

.popup.show {
  transform: translateY(0);
  opacity: 1;
}

.close {
  position: absolute;
  top: 0;
  right: 12px;
  color: #686868;
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
