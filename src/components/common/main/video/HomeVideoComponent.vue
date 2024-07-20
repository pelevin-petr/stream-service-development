<script lang="ts" setup>

import type { Stream } from '@/modules/streamInterface'
import { useStreamStore } from '@/stores/streamStore'

const store = useStreamStore()

// we need to get this info, its example
const streamVideos: Stream[] = [
  {
    id: 1721396986966,
    link: 'https://www.youtube.com/watch?v=DDJ5Qlc6gvg',
      description: {
        carNumber: 'A240РУ-77',
        streamer: 'Ivanov V.V.',
        whenIncluded: new Date(),
        smallDescription: 'Lorem ipsum dolor sit amet.',
        city: 'Moskow'
    },
    included: true
  },
  {
    id: 1721396986966,
    link: 'https://www.youtube.com/watch?v=DDJ5Qlc6gvg',
      description: {
        carNumber: 'A240РУ-77',
        streamer: 'Ivanov V.V.',
        whenIncluded: new Date(),
        smallDescription: 'Lorem ipsum dolor sit amet.',
        city: 'Moskow'
    },
    included: true
  },
  {
    id: 1721396986966,
    link: 'https://www.youtube.com/watch?v=DDJ5Qlc6gvg',
      description: {
        carNumber: 'A240РУ-77',
        streamer: 'Ivanov V.V.',
        whenIncluded: new Date(),
        smallDescription: 'Lorem ipsum dolor sit amet.',
        city: 'Moskow'
    },
    included: true
  }, {
    id: 1721396986966,
    link: 'https://www.youtube.com/watch?v=DDJ5Qlc6gvg',
      description: {
        carNumber: 'A240РУ-77',
        streamer: 'Ivanov V.V.',
        whenIncluded: new Date(),
        smallDescription: 'Lorem ipsum dolor sit amet.',
        city: 'Moskow'
    },
    included: true
  },
  {
    id: 1721396986966,
    link: 'https://www.youtube.com/watch?v=DDJ5Qlc6gvg',
      description: {
        carNumber: 'A240РУ-77',
        streamer: 'Ivanov V.V.',
        whenIncluded: new Date(),
        smallDescription: 'Lorem ipsum dolor sit amet.',
        city: 'Moskow'
    },
    included: true
  },
  {
    id: 1721396986966,
    link: 'https://www.youtube.com/watch?v=DDJ5Qlc6gvg',
      description: {
        carNumber: 'A240РУ-77',
        streamer: 'Ivanov V.V.',
        whenIncluded: new Date(),
        smallDescription: 'Lorem ipsum dolor sit amet.',
        city: 'Moskow'
    },
    included: true
  }, {
    id: 1721396986966,
    link: 'https://www.youtube.com/watch?v=DDJ5Qlc6gvg',
      description: {
        carNumber: 'A240РУ-77',
        streamer: 'Ivanov V.V.',
        whenIncluded: new Date(),
        smallDescription: 'Lorem ipsum dolor sit amet.',
        city: 'Moskow'
    },
    included: true
  },
  {
    id: 1721396986966,
    link: 'https://www.youtube.com/watch?v=DDJ5Qlc6gvg',
      description: {
        carNumber: 'A240РУ-77',
        streamer: 'Ivanov V.V.',
        whenIncluded: new Date(),
        smallDescription: 'Lorem ipsum dolor sit amet.',
        city: 'Moskow'
    },
    included: true
  },
  {
    id: 1721396986966,
    link: 'https://www.youtube.com/watch?v=DDJ5Qlc6gvg',
      description: {
        carNumber: 'A240РУ-77',
        streamer: 'Ivanov V.V.',
        whenIncluded: new Date(),
        smallDescription: 'Lorem ipsum dolor sit amet.',
        city: 'Moskow'
    },
    included: true
  }, {
    id: 1721396986966,
    link: 'https://www.youtube.com/watch?v=DDJ5Qlc6gvg',
      description: {
        carNumber: 'A240РУ-77',
        streamer: 'Ivanov V.V.',
        whenIncluded: new Date(),
        smallDescription: 'Lorem ipsum dolor sit amet.',
        city: 'Moskow'
    },
    included: true
  },
  {
    id: 1721396986966,
    link: 'https://www.youtube.com/watch?v=DDJ5Qlc6gvg',
      description: {
        carNumber: 'A240РУ-77',
        streamer: 'Ivanov V.V.',
        whenIncluded: new Date(),
        smallDescription: 'Lorem ipsum dolor sit amet.',
        city: 'Moskow'
    },
    included: true
  },
  {
    id: 1721396986966,
    link: 'https://www.youtube.com/watch?v=DDJ5Qlc6gvg',
      description: {
        carNumber: 'A240РУ-77',
        streamer: 'Ivanov V.V.',
        whenIncluded: new Date(),
        smallDescription: 'Lorem ipsum dolor sit amet.',
        city: 'Moskow'
    },
    included: true
  }, {
    id: 1721396986966,
    link: 'https://www.youtube.com/watch?v=DDJ5Qlc6gvg',
      description: {
        carNumber: 'A240РУ-77',
        streamer: 'Ivanov V.V.',
        whenIncluded: new Date(),
        smallDescription: 'Lorem ipsum dolor sit amet.',
        city: 'Moskow'
    },
    included: true
  },
  {
    id: 1721396986966,
    link: 'https://www.youtube.com/watch?v=DDJ5Qlc6gvg',
      description: {
        carNumber: 'A240РУ-77',
        streamer: 'Ivanov V.V.',
        whenIncluded: new Date(),
        smallDescription: 'Lorem ipsum dolor sit amet.',
        city: 'Moskow'
    },
    included: true
  },
  {
    id: 1721396986966,
    link: 'https://www.youtube.com/watch?v=DDJ5Qlc6gvg',
      description: {
        carNumber: 'A240РУ-77',
        streamer: 'Ivanov V.V.',
        whenIncluded: new Date(),
        smallDescription: 'Lorem ipsum dolor sit amet.',
        city: 'Moskow'
    },
    included: true
  }, {
    id: 1721396986966,
    link: 'https://www.youtube.com/watch?v=DDJ5Qlc6gvg',
      description: {
        carNumber: 'A240РУ-77',
        streamer: 'Ivanov V.V.',
        whenIncluded: new Date(),
        smallDescription: 'Lorem ipsum dolor sit amet.',
        city: 'Moskow'
    },
    included: true
  },
  {
    id: 1721396986966,
    link: 'https://www.youtube.com/watch?v=DDJ5Qlc6gvg',
      description: {
        carNumber: 'A240РУ-77',
        streamer: 'Ivanov V.V.',
        whenIncluded: new Date(),
        smallDescription: 'Lorem ipsum dolor sit amet.',
        city: 'Moskow'
    },
    included: true
  },
  {
    id: 1721396986966,
    link: 'https://www.youtube.com/watch?v=DDJ5Qlc6gvg',
      description: {
        carNumber: 'A240РУ-77',
        streamer: 'Ivanov V.V.',
        whenIncluded: new Date(),
        smallDescription: 'Lorem ipsum dolor sit amet.',
        city: 'Moskow'
    },
    included: true
  }, {
    id: 1721396986966,
    link: 'https://www.youtube.com/watch?v=DDJ5Qlc6gvg',
      description: {
        carNumber: 'A240РУ-77',
        streamer: 'Ivanov V.V.',
        whenIncluded: new Date(),
        smallDescription: 'Lorem ipsum dolor sit amet.',
        city: 'Moskow'
    },
    included: true
  },
  {
    id: 1721396986966,
    link: 'https://www.youtube.com/watch?v=DDJ5Qlc6gvg',
      description: {
        carNumber: 'A240РУ-77',
        streamer: 'Ivanov V.V.',
        whenIncluded: new Date(),
        smallDescription: 'Lorem ipsum dolor sit amet.',
        city: 'Moskow'
    },
    included: true
  },
  {
    id: 1721396986966,
    link: 'https://www.youtube.com/watch?v=DDJ5Qlc6gvg',
      description: {
        carNumber: 'A240РУ-77',
        streamer: 'Ivanov V.V.',
        whenIncluded: new Date(),
        smallDescription: 'Lorem ipsum dolor sit amet.',
        city: 'Moskow'
    },
    included: true
  }, {
    id: 1721396986966,
    link: 'https://www.youtube.com/watch?v=DDJ5Qlc6gvg',
      description: {
        carNumber: 'A240РУ-77',
        streamer: 'Ivanov V.V.',
        whenIncluded: new Date(),
        smallDescription: 'Lorem ipsum dolor sit amet.',
        city: 'Moskow'
    },
    included: true
  },
  {
    id: 1721396986966,
    link: 'https://www.youtube.com/watch?v=DDJ5Qlc6gvg',
      description: {
        carNumber: 'A240РУ-77',
        streamer: 'Ivanov V.V.',
        whenIncluded: new Date(),
        smallDescription: 'Lorem ipsum dolor sit amet.',
        city: 'Moskow'
    },
    included: true
  },
  {
    id: 1721396986966,
    link: 'https://www.youtube.com/watch?v=DDJ5Qlc6gvg',
      description: {
        carNumber: 'A240РУ-77',
        streamer: 'Ivanov V.V.',
        whenIncluded: new Date(),
        smallDescription: 'Lorem ipsum dolor sit amet.',
        city: 'Moskow'
    },
    included: true
  },
]
</script>

<template>
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8 mx-8 mt-20">
    <div v-for="video of streamVideos" :key="video.id" class="max-w-[350px] h-[300px] bg-white mx-auto shadow-lg rounded-2xl overflow-hidden">
      <div v-if="video.included">
        <RouterLink @click="store.video = video" :to="{ name: 'Stream', params: { id: video.id } }">
          <img src="../../../../assets/img/dog.jpg" alt="This image don't supported by your browser" class="w-full">
          <label class="block m-4 " for="video">Номер машины: {{ video.description.carNumber }}</label>
        </RouterLink>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>