<script lang="ts" setup>
import { ref } from 'vue'


const formData = ref({
  email: '',
  password: ''
})

const logIn = () => {

}
</script>

<template>
  <section class="bg-gray-50 dark:bg-gray-900">
    <div class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
      <RouterLink class="flex items-center mb-6 text-2xl font-semibold text-gray-900 dark:text-white" href="#" to="/">
        <img alt="logo" class="w-8 h-8 mr-2" src="../../assets/img/favicon.svg">
        Система Стриминга Автомобилей
      </RouterLink>
      <div
        class="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
        <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
          <h1 class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
            Войдите в аккаунт
          </h1>
          <form action="#" class="space-y-4 md:space-y-6">
            <div>
              <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-white" for="email">Почта</label>
              <input id="email"
                     v-model="formData.email" class="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" name="email"
                     placeholder="name@company.com"
                     type="email">
            </div>
            <div>
              <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                     for="password">Пароль</label>
              <input id="password"
                     v-model="formData.password" class="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" name="password" placeholder="••••••••"
                     type="password"
              >
            </div>
            <div class="flex items-center justify-between">
              <div class="flex items-start">
                <div class="flex items-center h-5">
                  <input id="remember" aria-describedby="remember" class="w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-primary-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-primary-600 dark:ring-offset-gray-800"
                         type="checkbox"
                  >
                </div>
                <div class="ml-3 text-sm">
                  <label class="text-gray-500 dark:text-gray-300" for="remember">Запомнить меня</label>
                </div>
              </div>
              <a class="text-sm font-medium text-primary-600 hover:underline text-blue-500 dark:text-primary-500"
                 href="#">Забыли
                пароль?</a>
            </div>
            <button class="w-full bg-blue-600 text-white bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800"
                    type="submit"
                    @click.prevent="logIn">
              Войти
            </button>
            <p class="text-sm text-center font-light text-gray-500 dark:text-gray-400">
              Ещё нет аккаунта?
              <RouterLink class="font-medium text-blue-500 text-primary-600 hover:underline dark:text-primary-500" href="#"
                          to="/registration">
                Регистрация
              </RouterLink>
            </p>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>

</style>