import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import './assets/main.css'

import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import Toaster from '@meforma/vue-toaster';


const vuetify = createVuetify({
    components,
    directives,
})

const app = createApp(App)


app.use(createPinia())
app.use(router)
app.use(vuetify)
app.use(Toaster);

app.mount('#app')
