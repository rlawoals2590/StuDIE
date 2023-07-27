import { createWebHistory, createRouter } from 'vue-router';
import Home from '@/components/HomePage.vue';
import StudyRoom from '@/components/StudyRoom.vue';
import StudyTimer from '@/components/StudyTimer.vue';
import profilePage from '@/components/ProfilePage.vue';
import RankingBoard from '@/components/RankingBoard.vue';
import LoginPage from '@/components/LoginPage.vue';
import SignUp from '@/components/SignUp.vue';
import Cookies from 'js-cookie';




const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: { authorization: ["client"] }
  },
  {
    path: '/StudyRoom',
    name: 'StudyRoom',
    component: StudyRoom,
    meta: { authorization: ["client"] }
  },
  {
    path: '/StudyTimer',
    name: 'StudyTimer',
    component: StudyTimer,
    meta: { authorization: ["client"] }
  },
  {
    path: '/profilePage',
    name: 'profilePage',
    component: profilePage,
    meta: { authorization: ["client"] }
  },
  {
    path: '/RankingBoard',
    name: 'RankingBoard',
    component: RankingBoard,
    meta: { authorization: ["client"] }
  },
  {
    path: '/LoginPage',
    name : 'LoginPage',
    component : LoginPage,
    meta: { authorization: ["guest"] }
  },    
  {
     path: '/signup',
    component: SignUp ,
    meta: { authorization: ["guest"] }
  },



];




const router = createRouter({
  history: createWebHistory(),
  routes
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.authorization.includes("client")) && !Cookies.get('user_access_token')) {
    next('/LoginPage');
  } else if(to.matched.some(record => record.meta.authorization.includes("guest")) && Cookies.get('user_access_token')) {
    next('/');
  } else {
    next();
  }
});

export default router;
