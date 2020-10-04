import Vue from 'vue'
import App from './App.vue'

import router from './router'
import store from './store'

Vue.config.productionTip = false
Vue.config.ignoredElements = [/^ion-/]

Vue.filter('formatTime', (data) => {
    let hours = parseInt(data / 3600);
    let minutes = parseInt(data % 3600 / 60);
    let seconds = parseInt(data % 60);

    let res = ''
    if (hours > 0) res += (hours < 10) ? `0${hours}:` : hours
    res += (minutes < 10) ? `0${minutes}:` : minutes
    res += (seconds < 10) ? `0${seconds}` : seconds

    return res;
})


export const playerEventBus = new Vue();

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')
