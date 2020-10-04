import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from './views/Home.vue'
import Library from './views/Library.vue'
import Charts from './views/Charts.vue'
import ArtistPage from './views/ArtistPage.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/library/',
        name: 'Library',
        component: Library
    },
    {
        path: '/charts/',
        name: 'Charts',
        component: Charts
    },
    {
        path: '/artist/:id',
        name: 'Artist',
        component: ArtistPage
    }
    //   {
    //     path: '/about',
    //     name: 'About',
    //     // route level code-splitting
    //     // this generates a separate chunk (about.[hash].js) for this route
    //     // which is lazy-loaded when the route is visited.
    //     component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
    //   }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
