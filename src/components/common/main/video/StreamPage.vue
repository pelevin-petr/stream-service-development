<script setup lang="ts">
import { useStreamStore } from '@/stores/streamStore'



const store = useStreamStore()
</script>

<template>
  <div>
    <div>
      <video class="w-full bg-gray-600  mt-16" controls>
        <source src="../../../../assets/img/videoplayback%20(1).mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </div>
    <div>
      <h2 class="">
        {{store.video}}
        <br>
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iste maiores mollitia, nemo officiis unde velit?
      </h2>
      <p>
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. A, maiores?
      </p>
    </div>
  </div>
</template>

<style scoped>

</style>