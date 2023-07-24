import { createWebHistory, createRouter } from 'vue-router';
import Home from '@/components/HomePage.vue';
import StudyRoom from '@/components/StudyRoom.vue';
import StudyTimer from '@/components/StudyTimer.vue';
import profilePage from '@/components/ProfilePage.vue';
import RankingBoard from '@/components/RankingBoard.vue';



const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/StudyRoom',
    name: 'StudyRoom',
    component: StudyRoom
  },
  {
    path: '/StudyTimer',
    name: 'StudyTimer',
    component: StudyTimer
  },
  {
    path: '/profilePage',
    name: 'profilePage',
    component: profilePage
  },
  {
    path: '/RankingBoard',
    name: 'RankingBoard',
    component: RankingBoard
  } 

];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
