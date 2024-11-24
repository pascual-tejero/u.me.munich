<template>
    <div class="iphone-frame">
      <ion-page>
        <ion-header :translucent="true"></ion-header>
  
        <ion-content :fullscreen="true">
          <ion-header collapse="condense">
            <ion-toolbar>
              <ion-title size="large">U, Me, Munich</ion-title>
            </ion-toolbar>
          </ion-header>
  
          <div id="container">
            <h1>I am feeling...</h1>
            <div class="checkbox-list">
              <ion-item v-for="(label, key) in options" :key="key">
                <ion-checkbox v-model="answers[key]">{{ label }}</ion-checkbox>
              </ion-item>
            </div>
            <ion-button 
              class="button" 
              shape="round" 
              :disabled="isLoading" 
              @click="submitAnswers">
              <span v-if="!isLoading">Submit</span>
              <ion-spinner v-else></ion-spinner>
            </ion-button>
          </div>
        </ion-content>
      </ion-page>
    </div>
  </template>
  
  <script setup lang="ts">
import { useRouter } from 'vue-router';
import { ref } from 'vue';
import { IonCheckbox, IonItem, IonButton, IonContent, IonPage, IonTitle, IonToolbar, IonHeader, IonSpinner } from '@ionic/vue';
import axios from 'axios';

const router = useRouter();
const email = ref(router.currentRoute.value.query.email || '');  // Retrieve email from query params

// Survey options
const options = {
  sporty: "Sporty",
  party: "Party",
  nature: "Nature",
  cafehopping: "Cafe Hopping",
  cooking: "Cooking",
  cinema: "Cinema",
  walking: "Walking",
  gardening: "Gardening",
  drinks: "Drinks",
  conversation: "Conversation",
  gocrazy: "Go Crazy"
};

const answers = ref(
  Object.fromEntries(Object.keys(options).map((key) => [key, false]))
);

const isLoading = ref(false);

const submitAnswers = async () => {
  const apiEndpoint = `http://localhost:8100/surveyanswer/`;

  try {
    isLoading.value = true;
    // Send answers to the backend
    const response = await axios.post(apiEndpoint, answers.value);

    // Handle backend response
    console.log(response.data.message);
    alert("Survey submitted successfully!");

    // Navigate to SurveyAnswer page, passing answers in route state
    router.push({ 
      path: '/surveyanswer', 
      state: { answers: answers.value } 
    });
  } catch (error) {
    console.error("Error submitting answers:", error);
    alert("Failed to submit survey. Please try again later.");
  } finally {
    isLoading.value = false;
  }
};
</script>

  
  <style scoped>
  /* Body to center the iPhone frame */
  body {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 0;
    height: 100vh;
    background-color: #f0f0f5;
  }
  
  .custom-line-break {
    height: 20px; /* Adjust the height to set the space between elements */
  }
  
  /* Main iPhone container */
  .iphone-frame {
    position: relative;
    width: 390px; /* Approx width of iPhone */
    height: 844px; /* Approx height of iPhone */
    background: #ffffff;
    border-radius: 40px;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
    overflow: hidden;
    border: 2px solid #e0e0e0;
  }
  
  /* Mock camera notch (for top center) */
  .iphone-frame::before {
    content: "";
    position: absolute;
    top: 8px;
    left: 50%;
    transform: translateX(-50%);
    width: 120px;
    height: 30px;
    background: #000000;
    border-radius: 20px;
    z-index: 10;
  }
  
  /* Container inside the "screen" */
  #container {
    text-align: center;
    padding-top: 5rem;
  }
  
  .checkbox-list {
    text-align: left;
    margin: 0 auto;
    width: 90%;
  }
  
  #container strong {
    font-size: 18px;
    line-height: 24px;
    margin-bottom: 12px;
    display: block;
  }
  
  #container p {
    font-size: 14px;
    line-height: 20px;
    color: #8c8c8c;
    margin: 0;
  }
  
  #container a {
    color: #007aff;
    text-decoration: none;
  }
  
  .button {
    --background: rgb(255, 94, 53);
    text-align: center;
    color: white;
  }
  
  ion-header {
    position: sticky;
    top: 0;
    width: 100%;
    background: #f8f8f8;
    z-index: 100;
  }
  
  ion-title {
    font-size: 16px;
  }
  </style>