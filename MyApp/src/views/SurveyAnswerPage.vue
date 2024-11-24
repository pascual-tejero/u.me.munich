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
            <ion-card>
              <ion-card-header>
                <ion-card-subtitle>That means your vibe is...</ion-card-subtitle>
                <ion-card-title>{{ mood }}</ion-card-title>
              </ion-card-header>
              <ion-card-content>
                Here's a description about the mood you chose.
              </ion-card-content>
            </ion-card>
  
            <ion-button shape="round" class="button" href='./Survey'>Events recommendation</ion-button>  
          </div>
        </ion-content>
      </ion-page>
    </div>
  </template>
  
  <script setup lang="ts">
  import { IonCard, IonCardContent, IonCardHeader, IonCardSubtitle, IonCardTitle, IonContent, IonHeader, IonPage, IonTitle, IonToolbar, IonCheckbox, IonItem, Computed, watchEffect} from '@ionic/vue';
  import { ref } from 'vue' ;

  const route = useRoute();
const answers = ref(route.state?.answers || {});

const mood = computed(() => {
  // Determine mood based on the selected answers
  if (answers.value.sporty) return "Sporty";
  if (answers.value.party) return "Party";
  if (answers.value.nature) return "Nature";
  if (answers.value.cafehopping) return "Cafe Hopping";
  if (answers.value.cooking) return "Cooking";
  if (answers.value.cinema) return "Cinema";
  if (answers.value.walking) return "Walking";
  if (answers.value.gardening) return "Gardening";
  if (answers.value.drinks) return "Drinks";
  if (answers.value.conversation) return "Conversation";
  if (answers.value.gocrazy) return "Go Crazy";
  return "Unknown";
});

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
    padding-top:20rem ;
    justify-content: center;
    justify-items: center;
    align-items: center;
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
    justify-content: center;
    align-items: center;
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
  