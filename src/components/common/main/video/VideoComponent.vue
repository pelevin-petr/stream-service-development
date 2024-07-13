<script setup lang="ts">
import { type Stream } from './VideoLogic.vue'

// we need to get this info, its example
const streamVideos: Stream[] = [
  {
    id: +(new Date()), link: 'https://www.youtube.com/watch?v=DDJ5Qlc6gvg', description: {
      name: 'some name...',
      strimer: 'Ivanov V.V. car-1234',
      whenIncluded: new Date(),
      smallDescription: 'Lorem ipsum dolor sit amet.'
    }, city: 'Moskow', included: true
  },
  {
    id: +(new Date()), link: 'https://www.youtube.com/watch?v=DDJ5Qlc6gvg', description: {
      name: 'some name...',
      strimer: 'Ivanov V.V. car-1234',
      whenIncluded: new Date(),
      smallDescription: 'Lorem ipsum dolor sit amet.'
    }, city: 'Moskow', included: true
  },
  {
    id: +(new Date()), link: 'https://www.youtube.com/watch?v=DDJ5Qlc6gvg', description: {
      name: 'some name...',
      strimer: 'Ivanov V.V. car-1234',
      whenIncluded: new Date(),
      smallDescription: 'Lorem ipsum dolor sit amet.'
    }, city: 'Moskow', included: true
  },
  {
    id: +(new Date()), link: 'https://www.youtube.com/watch?v=DDJ5Qlc6gvg', description: {
      name: 'some name...',
      strimer: 'Ivanov V.V. car-1234',
      whenIncluded: new Date(),
      smallDescription: 'Lorem ipsum dolor sit amet.'
    }, city: 'Moskow', included: true
  },
  {
    id: +(new Date()), link: 'https://www.youtube.com/watch?v=DDJ5Qlc6gvg', description: {
      name: 'some name...',
      strimer: 'Ivanov V.V. car-1234',
      whenIncluded: new Date(),
      smallDescription: 'Lorem ipsum dolor sit amet.'
    }, city: 'Moskow', included: true
  },
  {
    id: +(new Date()), link: 'https://www.youtube.com/watch?v=DDJ5Qlc6gvg', description: {
      name: 'some name...',
      strimer: 'Ivanov V.V. car-1234',
      whenIncluded: new Date(),
      smallDescription: 'Lorem ipsum dolor sit amet.'
    }, city: 'Moskow', included: true
  },
  {
    id: +(new Date()), link: 'https://www.youtube.com/watch?v=DDJ5Qlc6gvg', description: {
      name: 'some name...',
      strimer: 'Ivanov V.V. car-1234',
      whenIncluded: new Date(),
      smallDescription: 'Lorem ipsum dolor sit amet.'
    }, city: 'Moskow', included: true
  },
  {
    id: +(new Date()), link: 'https://www.youtube.com/watch?v=DDJ5Qlc6gvg', description: {
      name: 'some name...',
      strimer: 'Ivanov V.V. car-1234',
      whenIncluded: new Date(),
      smallDescription: 'Lorem ipsum dolor sit amet.'
    }, city: 'Moskow', included: true
  },
  {
    id: +(new Date()), link: 'https://www.youtube.com/watch?v=DDJ5Qlc6gvg', description: {
      name: 'some name...',
      strimer: 'Ivanov V.V. car-1234',
      whenIncluded: new Date(),
      smallDescription: 'Lorem ipsum dolor sit amet.'
    }, city: 'Moskow', included: true
  },
  {
    id: +(new Date()), link: 'https://www.youtube.com/watch?v=DDJ5Qlc6gvg', description: {
      name: 'some name...',
      strimer: 'Ivanov V.V. car-1234',
      whenIncluded: new Date(),
      smallDescription: 'Lorem ipsum dolor sit amet.'
    }, city: 'Moskow', included: true
  }
]

</script>

<template>
  <div class="mt-16">
    <div v-for="video of streamVideos" :key="video.id" class="inline pt-96 mt-96">
      <div v-if="video.included" class="inline">
        <video class="w-40 inline m-4 mb-8 border border-gray-200 rounded-lg" controls>
          <source :src="video.link" type="video/mp4">
          Your browser does not support the video tag.
        </video>
        <label for="video" class="inline">{{ video.description.name }}</label>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>