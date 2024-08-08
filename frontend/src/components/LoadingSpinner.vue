<template>
  <div class="spinner border-4 border-gray-200 border-t-blue-500 rounded-full w-10 h-10 mx-auto" v-if="isLoading"></div>
</template>

<script setup>
const props = defineProps({
  isLoading: {
    type: Boolean,
    required: true,
  },
});
</script>

<style scoped>
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
.spinner {
  animation: spin 1s linear infinite;
}
</style>
