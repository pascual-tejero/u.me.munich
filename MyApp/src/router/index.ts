import { createRouter, createWebHistory } from '@ionic/vue-router';
import { RouteRecordRaw } from 'vue-router';
import HomePage from '../views/HomePage.vue';
import SurveyPage from '../views/SurveyPage.vue'; 
import SurveyAnswerPage from '@/views/SurveyAnswerPage.vue';
import SignUpPage from '../views/SignUpPage.vue';

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
    path: '/survey',
    name: 'Survey',
    component: SurveyPage, // Survey Page
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
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;
