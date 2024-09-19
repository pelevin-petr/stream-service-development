<script setup lang="ts">
import { useInstructorStore } from '@/shared/stores/instructor'

const store = useInstructorStore()
const { instructor } = store
</script>

<template>
<div class="">
  <div class="w-full bg ">
    <div class="flex justify-center items-end text-white text-3xl pb-[110px] z-10 h-[100vh]">{{ instructor?.fullname }}</div>
  </div>
</div>
</template>

<style scoped>
.bg {
  background-image: url('@/default/assets/img/gerasimchuk_large.jpg');
  background-repeat: no-repeat;
  background-position: center center;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
}
</style>