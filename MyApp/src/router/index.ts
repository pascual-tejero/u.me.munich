import { createRouter, createWebHistory } from '@ionic/vue-router';
import { RouteRecordRaw } from 'vue-router';
import HomePage from '../views/HomePage.vue';
import SurveyPage from '../views/SurveyPage.vue'; 

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    redirect: '/home', // Redirect to homepage initially
  },
  {
    path: '/home',
    name: 'Home',
    component: HomePage, // Home page route (could be after login)
  },
  {
    path: '/survey',
    name: 'Survey',
    component: SurveyPage, // Main survey page route
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;
