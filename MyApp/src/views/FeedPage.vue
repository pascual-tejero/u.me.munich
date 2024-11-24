<template>
    <div class="iphone-frame">
      <ion-page>
        <ion-header :translucent="true">
          <ion-toolbar>
            <ion-title>U, Me, Munich</ion-title>
          </ion-toolbar>
        </ion-header>
  
        <ion-content :fullscreen="true">
          <ion-list>
            <!-- Loop through each event -->
            <ion-item v-for="(event, index) in events" :key="index">
              <ion-avatar slot="start">
                <img :src="event.images[0]" alt="Event Image" />
              </ion-avatar>
              <ion-label>
                <h2>{{ event.name }}</h2>
              </ion-label>
            </ion-item>
          </ion-list>
          <ion-infinite-scroll threshold="100px" @ionInfinite="loadData">
            <ion-infinite-scroll-content
              loading-spinner="crescent"
              loading-text="Loading more data..."
            ></ion-infinite-scroll-content>
          </ion-infinite-scroll>
        </ion-content>
        <ion-page>
            <ion-tabs>
      <ion-router-outlet></ion-router-outlet>
      <ion-tab-bar slot="bottom">
        <ion-tab-button tab="home" href="/home">
            <img src="/src/assets/today-outline.svg">
          <ion-label>Events</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="radio" href="/radio">
          <img src="/src/assets/U-Me-Munich-Logo.png">
        </ion-tab-button>

        <ion-tab-button tab="library" href="/library">
            <img src="/src/assets/people-outline.svg">
          <ion-label>Sync & Share</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="search" href="/search">
          <ion-icon :icon="Profile" />
          <ion-label>Profile</ion-label>
        </ion-tab-button>
      </ion-tab-bar>
    </ion-tabs>
        </ion-page>
      </ion-page>
    </div>
  </template>
  
  
  
  <script lang="ts">
import {
  IonContent,
  IonInfiniteScroll,
  IonInfiniteScrollContent,
  IonList,
  IonItem,
  IonAvatar,
  IonImg,
  IonLabel,
  IonTabs, IonRouterOutlet, IonTabBar, IonTabButton, IonIcon
} from "@ionic/vue";
import { defineComponent, ref } from "vue";
import { playCircle, people-outline, profile } from 'ionicons/icons';

export default defineComponent({
  components: {
    IonContent,
    IonInfiniteScroll,
    IonInfiniteScrollContent,
    IonList,
    IonItem,
    IonAvatar,
    IonImg,
    IonLabel,
    IonTabs, IonRouterOutlet, IonTabBar, IonTabButton, IonIcon
  },
  setup() {
    // Initial events with multiple images
    const events = ref([
      {
        name: "Hackatum 2024",
        images: ["./src/assets/Hackatum.jpg"],
      },
      {
        name: "Basketball Friendly",
        images: ["./src/assets/Basketball.jpg"],
      },
      {
        name: "Starnberger See Boat Tour",
        images: ["./src/assets/BoatTour.jpg"],
      },
      {
        name: "English Garden Walk",
        images: ["./src/assets/Nature.jpg"],
      },
      {
        name: "Baking class",
        images: ["./src/assets/Dessert.jpg"],
      },
      {
        name: "Munich Motorbikes Tour",
        images: ["./src/assets/Rides.jpg"],
      },
    ]);

    // Infinite scroll to load more events
    const loadData = (event: any) => {
      setTimeout(() => {
        const newEvents = [
          {
            name: `Event ${events.value.length + 1}`,
            images: [
              "./src/assets/Event1.jpg",
              "./src/assets/Event2.jpg",
              "./src/assets/Event3.jpg",
            ],
          },
          {
            name: `Event ${events.value.length + 2}`,
            images: [
              "./src/assets/Event4.jpg",
              "./src/assets/Event5.jpg",
              "./src/assets/Event6.jpg",
            ],
          },
        ];
        events.value.push(...newEvents);

        event.target.complete();

        if (events.value.length >= 20) {
          event.target.disabled = true;
        }
      }, 1000);
    };

    return {
      events,
      loadData,
    };
  },
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