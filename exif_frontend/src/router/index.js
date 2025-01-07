import {createRouter, createWebHistory} from 'vue-router'
import ExifHandle from "@/views/ExifHandle.vue";
import Policy from "@/views/Policy.vue";
import Terms from "@/views/Terms.vue";

const routes = [
    {
        path: '/',
        name: 'home',
        component: ExifHandle
    }, {
        path: '/policy',
        name: 'Policy',
        component: Policy
    }, {
        path: '/terms',
        name: 'Terms',
        component: Terms
    }
]

const router = createRouter({
    history: createWebHistory(),
    mode: 'history',
    routes
})

export default router
