<script setup lang="ts">
const videoArray = [
  { id: 1, link: 'https://www.youtube.com/watch?v=DDJ5Qlc6gvg' },
  { id: 2, link: 'https://www.youtube.com/watch?v=nVWFOtzL7ok' },
  { id: 3, link: 'https://www.youtube.com/watch?v=nVWFOtzL7ok' },
  { id: 4, link: 'https://www.youtube.com/watch?v=nVWFOtzL7ok' },
  { id: 5, link: 'https://www.youtube.com/watch?v=nVWFOtzL7ok' },
  { id: 6, link: 'https://www.youtube.com/watch?v=nVWFOtzL7ok' },
  { id: 7, link: 'https://www.youtube.com/watch?v=nVWFOtzL7ok' },
  { id: 8, link: 'https://www.youtube.com/watch?v=nVWFOtzL7ok' },
  { id: 9, link: 'https://www.youtube.com/watch?v=nVWFOtzL7ok' },
  { id: 10, link: 'https://www.youtube.com/watch?v=nVWFOtzL7ok' },
  { id: 11, link: 'https://www.youtube.com/watch?v=nVWFOtzL7ok' },
  { id: 12, link: 'https://www.youtube.com/watch?v=nVWFOtzL7ok' },
  { id: 13, link: 'https://www.youtube.com/watch?v=nVWFOtzL7ok' },
  { id: 14, link: 'https://www.youtube.com/watch?v=nVWFOtzL7ok' },
  { id: 15, link: 'https://www.youtube.com/watch?v=nVWFOtzL7ok' },
  { id: 16, link: 'https://www.youtube.com/watch?v=QDrBOVU5yGo' }
]

</script>

<template>
  <div class="mt-16">
    <div v-for="video of videoArray" :key="video.id" class="inline pt-96 mt-96">
      <video class="w-40 inline m-4 mb-8 border border-gray-200 rounded-lg" controls>
        <source :src="video.link" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    
    </div>
  </div>
</template>

<style scoped>

</style>