<script lang="ts" setup>
import type { Stream } from '@/modules/streamInterface'


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
  }, {
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
  }, {
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
  }, {
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
  }, {
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
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mt-16">
    <div v-for="video of streamVideos" :key="video.id" class="w-[350px] h-[300px] bg-gray-600 mx-auto">
      <div v-if="video.included">
        <RouterLink :to="{ name: 'Stream', params: { id: video.id, link: video.link, city: 'Moskow' } }">
          <img src="../../../../assets/img/favicon.svg" alt="This image don't supported by your browser" class="max-w-[150px]">
          <br>
          <label class="inline pl-5" for="video">{{ video.description.name }}</label>
        </RouterLink>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>