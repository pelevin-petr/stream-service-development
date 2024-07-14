<script setup lang="ts">
import { ref } from 'vue'

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
  },{
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
  },{
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
  },{
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
  },{
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
const viewMoreValue = ref<number>(17)

const viewMore = (): void => {
  viewMoreValue.value = streamVideos.length
}
</script>

<template>
  <div class="mt-16">
    <div v-for="(video, index) of streamVideos" :key="video.id" class="inline pt-96 mt-96">
      <span v-if="index<=viewMoreValue">
        <div v-if="video.included" class="inline-block">
          <video class="w-40 inline mx-4 mt-4 border border-gray-200 rounded-lg" controls>
            <source :src="video.link" type="video/mp4">
            Your browser does not support the video tag.
          </video>
          <br>
          <label for="video" class="inline pl-5">{{ video.description.name }}</label>
        </div>
      </span>
    </div>
    <div v-if="viewMoreValue==17"
         class=" bg-blue-200  text-center text-black">
      <button @click="viewMore">Показать больше &#8659;</button>
    </div>
  </div>
</template>

<style scoped>

</style>