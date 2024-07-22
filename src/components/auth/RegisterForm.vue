<script lang="ts" setup>
import { ref } from 'vue'


const formData = ref({
  email: '',
  password: '',
  confirmPassword: ''
})


const createAccount = () => {

}
</script>

<template>
  <section class="bg-gray-50 dark:bg-extra-neutral-700">
    <div class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
      <RouterLink class="flex items-center mb-6 text-2xl font-semibold text-gray-900 dark:text-white" href="#" to="/">
        <img alt="logo" class="w-8 h-8 mr-2" src="../../assets/img/favicon.svg">
        Система Стриминга Автомобилей
      </RouterLink>
      <div
        class="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-neutral-500 dark:border-gray-700">
        <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
          <h1 class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
            Создайте аккаунт
          </h1>
          <form action="#" class="space-y-4 md:space-y-6">
            <div>
              <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-white" for="email">Ваша почта</label>
              <input id="email"
                     v-model="formData.email"
                     class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-400 dark:border-gray-700 dark:placeholder-gray-800 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                     name="email"
                     placeholder="name@company.com"
                     type="email">
            </div>
            <div>
              <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                     for="password">Пароль</label>
              <input id="password"
                     v-model="formData.password"
                     class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-400 dark:border-gray-700 dark:placeholder-gray-800 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                     name="password" placeholder="••••••••"
                     type="password"
              >
            </div>
            <div>
              <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-white" for="confirm-password">Повторите
                пароль</label>
              <input id="confirm-password"
                     v-model="formData.confirmPassword"
                     class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-400 dark:border-gray-700 dark:placeholder-gray-800 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                     name="confirm-password"
                     placeholder="••••••••"
              >
            </div>
            <div class="flex items-start">
              <div class="flex items-center h-5">
                <input id="terms" aria-describedby="terms"
                       class="w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-primary-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-primary-600 dark:ring-offset-gray-800"
                       type="checkbox"
                >
              </div>
              <div class="ml-3 text-sm">
                <label class="font-light text-gray-500 dark:text-gray-300" for="terms">Я принимаю условия <a
                  class="font-medium text-blue-500 text-primary-600 hover:underline dark:text-extra-neutral-700 " href="#">Пользовательского
                  соглашения</a></label>
              </div>
            </div>
            <button
              class="w-full text-white bg-blue-600  hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-gray-700 dark:hover:bg-gray-800 dark:focus:ring-primary-800"
              type="submit"
              @click.prevent="createAccount">
              Создать аккаунт
            </button>
            <p class="text-sm text-center font-light text-gray-500 dark:text-gray-300">
              Уже есть аккаунт?
              <RouterLink class="font-medium  text-blue-500 text-primary-600 hover:underline dark:text-extra-neutral-700"
                          href="#"
                          to="/authorization">
                Войдите
              </RouterLink>
            </p>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
@media (prefers-color-scheme: dark) {
  .dark\:bg-extra-neutral-700 {
    --tw-bg-opacity: 1;
    background-color: #2C2C2C
  }
  .dark\:text-extra-neutral-700 {
    --tw-bg-opacity: 1;
    color: #2C2C2C
  }
}
</style>