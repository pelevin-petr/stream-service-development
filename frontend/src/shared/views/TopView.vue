<script lang="ts" setup>
import FooterComponent from '@/shared/components/common/footer/FooterComponent.vue'
import HeaderComponent from '@/shared/components/common/header/HeaderComponent.vue'
const nav = [
  {
    to: '/',
    title: 'Главная'
  },
  {
    to: '/instructors',
    title: 'Инстукторы'
  },
  {
    to: '/streams',
    title: 'Стримы'
  }
]

</script>

<template>
  <div class="flex flex-col min-h-full justify-between">
    <div class="flex flex-col items-center">
     <HeaderComponent class="w-full" :routes="nav"/>
      <RouterView class="dark:bg-gray-800 mt-8 md:px-8 w-full"/>
    </div>
    
    <FooterComponent class="mt-8" />
  </div>
</template>
