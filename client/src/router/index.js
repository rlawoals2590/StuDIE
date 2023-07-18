import { createWebHistory, createRouter } from 'vue-router';
import Home from '@/components/HomePage.vue';
import PRoom from '@/components/PRoom.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/PRoom',
    name: 'PRoom',
    component: PRoom
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
