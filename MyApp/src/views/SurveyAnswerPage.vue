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
                <ion-card-title>Urban Ninja Warrior Challenge (Go Crazy & Sporty)</ion-card-title>
              </ion-card-header>
              <ion-card-content>
                Combine your sporty side with a \"Go Crazy\" adrenaline rush by tackling Munich's cityscape like an urban ninja warrior!  This isn't a formal event, but a self-guided adventure.\n* *Execution:* Start at the Olympic Park (Olympiapark), using its various structures – stairs, ramps, walls – as obstacles.  Film your progress, turning it into a fun video challenge.  Next, venture into the city center, incorporating creatively chosen spots like the steps of the Deutsches Museum or the Englischer Garten's bridges.  The goal?  Record a dynamic, playful video showcasing your skills and Munich's urban landscape.  (Safety first – avoid dangerous stunts and respect public spaces).\n\n\n*2.  Indoor Rock Climbing & Afterwards, a \"Crazy\" Bavarian Night (Sporty & Go Crazy):\n\n *Concept:*  Get your sporty fix with some indoor rock climbing, then ramp up the craziness with a truly unique Bavarian experience.\n* *Execution:* Head to Boulderwelt München (a popular indoor climbing gym) for an afternoon of exhilarating climbing.  Then, ditch the traditional beer garden for a \"Go Crazy\" twist: find a quirky, less-touristy Bavarian pub (check local listings for live music or themed nights) and embrace the local culture with full gusto. Maybe try a  \"Goaßmaß\" (a large mug of beer) if you're feeling particularly bold! (Remember to drink responsibly).\n\n\n*Note:*  For specific events happening within the next day, check local event listings on websites like muenchen.de or Timeout Munich.  Look for keywords like \"climbing,\" \"events,\" \"concerts,\" or \"parties\" to find something matching your preferences."
              </ion-card-content>
            </ion-card>
  
            <ion-button shape="round" class="button" href='./feed'>Events recommendation</ion-button>  
          </div>
        </ion-content>
      </ion-page>
    </div>
  </template>
  
  <script setup lang="ts">
  import { IonCard, IonCardContent, IonCardHeader, IonCardSubtitle, IonCardTitle, IonContent, IonHeader, IonPage, IonTitle, IonToolbar} from '@ionic/vue';
  import { ref, computed } from 'vue' ;

 // const route = useRoute();
//const answers = ref(route.state?.answers || {});
/*
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
    padding-top: 5rem;
    text-align: center;
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
  