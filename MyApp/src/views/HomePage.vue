<template>
  <div class="iphone-frame">
    <ion-page>
      <ion-header :translucent="true">
        <ion-toolbar>
          <ion-title>iPhone View</ion-title>
        </ion-toolbar>
      </ion-header>

      <ion-content :fullscreen="true">
        <ion-header collapse="condense">
          <ion-toolbar>
            <ion-title size="large">iPhone View</ion-title>
          </ion-toolbar>
        </ion-header>

        <div id="container">
          <strong>Welcome to Your App</strong>
          <p>Start with Ionic 
            <a target="_blank" rel="noopener noreferrer" href="https://ionicframework.com/docs/components">UI Components</a>
          </p>
        </div>
      </ion-content>
    </ion-page>
  </div>
</template>

<script setup lang="ts">
import { IonContent, IonHeader, IonPage, IonTitle, IonToolbar } from '@ionic/vue';
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
  padding: 16px;
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
