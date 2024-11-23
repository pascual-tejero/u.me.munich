<template>
  <ion-page>
    <ion-header :translucent="true">
      <ion-toolbar>
        <ion-title>Blank</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content :fullscreen="true">
      <ion-header collapse="condense">
        <ion-toolbar>
          <ion-title size="large">Blank</ion-title>
        </ion-toolbar>
      </ion-header>

      <div id="container">
        <strong>Ready to create an app?</strong>
        <p>Start with Ionic <a target="_blank" rel="noopener noreferrer" href="https://ionicframework.com/docs/components">UI Components</a></p>
      </div>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import { IonContent, IonHeader, IonPage, IonTitle, IonToolbar } from '@ionic/vue';
</script>

<style scoped>
/* Set up the screen to look like an iPhone 16 Pro */
body {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0;
  background-color: #f0f0f5; /* Light background */
}

#container {
  text-align: center;
  position: relative;
  width: 402px; /* iPhone 16 Pro width */
  height: 874px; /* iPhone 16 Pro height */
  background-color: #ffffff; /* White background */
  border-radius: 35px; /* Rounded corners to match iPhone screen */
  box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1); /* Soft shadow for depth */
  overflow: hidden; /* Prevent content from overflowing the rounded corners */
}

#container strong {
  font-size: 20px;
  line-height: 26px;
}

#container p {
  font-size: 16px;
  line-height: 22px;
  
  color: #8c8c8c;
  
  margin: 0;
}

#container a {
  text-decoration: none;
}

ion-header {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  background: #f8f8f8;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Add shadow for header */
}

ion-title {
  font-size: 18px;
}
</style>
