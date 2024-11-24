import { createRouter, createWebHistory } from '@ionic/vue-router';
import { RouteRecordRaw } from 'vue-router';
import HomePage from '../views/HomePage.vue';
import SurveyPage from '../views/SurveyPage.vue'; 
import SurveyAnswerPage from '@/views/SurveyAnswerPage.vue';
import SignUpPage from '../views/SignUpPage.vue';
import SyncSharePage from '@/views/SyncSharePage.vue';
import ChatPage from '@/views/ChatPage.vue';
import FeedPage from '@/views/FeedPage.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    redirect: '/home',
  },
  {
    path: '/home',
    name: 'Home',
    component: HomePage, // Login/Register
  },
  {
    path: '/survey/',
    name: 'Survey',
    component: SurveyPage,
  },
  {
    path: '/surveyanswer',
    name: 'SurveyAnswer',
    component: SurveyAnswerPage, // Survey Answer Page
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUpPage,
  },
  {
    path: '/sync',
    name: 'Sync',
    component: SyncSharePage,
  },
  {
    path: '/chat',
    name: 'Chat',
    component: ChatPage,
  },
  {
    path: '/feed',
    name: 'Feed',
    component: FeedPage
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;
