<script setup lang="ts">
import { ref } from 'vue'

import RegisterForm from '@/components/auth/RegisterForm.vue'
import LoginForm from '@/components/auth/LoginForm.vue'


const isRegistered = ref<boolean>(true)
</script>

<template>
    <LoginForm v-if="isRegistered"/>
    <RegisterForm v-else/>
</template>

<style scoped>

</style>