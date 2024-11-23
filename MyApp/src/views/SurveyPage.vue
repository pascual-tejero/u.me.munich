<template>
    <div class="iphone-frame">
      <ion-page>
        <ion-header :translucent="true">
        </ion-header>
  
        <ion-content :fullscreen="true">
          <ion-header collapse="condense">
            <ion-toolbar>
              <ion-title size="large">U, Me, Munich</ion-title>
            </ion-toolbar>
          </ion-header>
  
          <div id="container">
            <h1>I am feeling...</h1>
            <ion-item>
                <ion-checkbox v-model="answers.sporty">Sporty</ion-checkbox>
            </ion-item>
            <ion-item>
                <ion-checkbox v-model="answers.party">Party</ion-checkbox>
            </ion-item>
            <ion-item>
                <ion-checkbox v-model="answers.nature">Nature</ion-checkbox>
            </ion-item>
            <ion-item>
                <ion-checkbox v-model="answers.cafehopping">Cafe Hopping</ion-checkbox>
            </ion-item>
            <ion-item>
                <ion-checkbox v-model="answers.cooking">Cooking</ion-checkbox>
            </ion-item>
            <ion-item>
                <ion-checkbox v-model="answers.cinema">Cinema</ion-checkbox>
            </ion-item>
            <ion-item>
                <ion-checkbox v-model="answers.walking">Walking</ion-checkbox>
            </ion-item>
            <ion-item>
                <ion-checkbox v-model="answers.gardening">Gardening</ion-checkbox>
            </ion-item>
            <ion-item>
                <ion-checkbox v-model="answers.drinks">Drinks</ion-checkbox>
            </ion-item>
            <ion-item>
                <ion-checkbox v-model="answers.conversation">Conversation</ion-checkbox>
            </ion-item>
            <ion-item>
                <ion-checkbox v-model="answers.gocrazy">Go Crazy</ion-checkbox>
            </ion-item>
          <ion-button class="button" shape="round" @click="submitAnswers">Submit</ion-button>
          </div>
        </ion-content>
      </ion-page>
    </div>
  </template>
  
  <script setup lang="ts">
  import { IonContent, IonHeader, IonPage, IonTitle, IonToolbar, IonCheckbox, IonItem } from '@ionic/vue';
  import { ref } from 'vue';
  //import axios from 'axios';

  const answers = ref({
  sporty: false,
  party: false,
  nature: false,
  cafehopping: false,
  cooking: false,
  cinema: false,
  walking: false,
  gardening: false,
  drinks: false,
  conversation: false,
  gocrazy: false
});

/*
const submitAnswers = async () => {
  try {
    // Send the collected answers to the backend
    const response = await axios.post('API', {
      answers: answers.value
    });

    // Handle the response from the AI API
    console.log(response.data);
  } catch (error) {
    console.error('Error submitting answers:', error);
  }
};
*/

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
    padding-top:5rem ;
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
    --background: rgb(255, 94,53);
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
  