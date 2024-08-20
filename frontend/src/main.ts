import { createApp } from 'vue'
import { createPinia } from 'pinia'

import './main.css'
import App from './App.vue'
import { router } from '@/routes/router'
import { vueKeycloak } from '@josempgon/vue-keycloak'


(async () => {
  const app = createApp(App)
  await vueKeycloak.install(app, {
    config: {
      url: `http://127.0.0.1:9080/`,
      realm: 'myrealm',
      clientId: 'myclient'
    },
    initOptions: {
      onLoad: 'check-sso',
      silentCheckSsoRedirectUri: window.location.origin+ '/silent-check-sso.html',
    }
  })
  app.use(createPinia())
  app.use(router)
  app.mount('#app')
})()

// const app = createApp(App)
// app.use(createPinia())
// app.use(router)
// app.mount('#app')