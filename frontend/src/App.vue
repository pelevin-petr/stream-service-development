<script lang="ts" setup>
import FooterComponent from '@/components/common/footer/FooterComponent.vue'
import HeaderComponent from '@/components/common/header/HeaderComponent.vue'
</script>

<template>
  <div class="flex flex-col min-h-full justify-between ">
    <div class="flex flex-col items-center">
      <HeaderComponent class="w-full" />

      <RouterView class="dark:bg-gray-800 mt-8 md:px-8 w-full flex flex-col items-center"/>
    </div>

    <FooterComponent class="mt-8" />
  </div>
</template>
