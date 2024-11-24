<template>
    <div class="iphone-frame">
      <ion-page>
        <ion-header :translucent="true">
          <ion-toolbar>
            <ion-title>Search Users</ion-title>
          </ion-toolbar>
        </ion-header>
  
        <ion-content :fullscreen="true">
          <ion-header collapse="condense">
            <ion-toolbar>
              <ion-title size="large">Search Users</ion-title>
            </ion-toolbar>
          </ion-header>
  
          <div id="container">
            <!-- Description Title -->
            <h2 class="description-title">Search for Users</h2>
  
            <!-- Search Bar with Custom Icon -->
            <ion-searchbar
              v-model="searchQuery"
              :search-icon="searchCircle"
              placeholder="Search by email"
              clear-input
            ></ion-searchbar>
  
            <!-- Error Message for Invalid Email -->
            <ion-text color="danger" v-if="emailErrorMessage" class="error-message">
              {{ emailErrorMessage }}
            </ion-text>
  
            <!-- Action Buttons -->
            <ion-button
              expand="block"
              shape="round"
              :disabled="!isValidEmail(searchQuery)"
              @click="inviteToEvent"
              class="action-btn"
            >
              Invite to Event
            </ion-button>
  
            <ion-button
              expand="block"
              shape="round"
              :disabled="!isValidEmail(searchQuery)"
              @click="openChatInNewTab"
              class="action-btn"
            >
              Chat
            </ion-button>
          </div>
        </ion-content>
      </ion-page>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref, watch } from "vue";
  import {
    IonContent,
    IonHeader,
    IonPage,
    IonTitle,
    IonToolbar,
    IonButton,
    IonText,
    IonSearchbar,
  } from "@ionic/vue";
  import { searchCircle } from "ionicons/icons"; // Import the search icon from ionicons
  
  const searchQuery = ref("");
  const emailErrorMessage = ref("");
  
  // Email validation function using regex
  const isValidEmail = (email: string) => {
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return emailRegex.test(email);
  };
  
  // Watcher for live email validation
  watch(searchQuery, (newQuery) => {
    if (newQuery && !isValidEmail(newQuery)) {
      emailErrorMessage.value = "Please enter a valid email address.";
    } else {
      emailErrorMessage.value = ""; // Clear error message
    }
  });
  
  // Button Actions
  const inviteToEvent = () => {
    console.log(`Inviting ${searchQuery.value} to the event.`);
    // Your event invitation logic here
  };
  
  // Open the chat page in a new tab
  const openChatInNewTab = () => {
    console.log(`Opening chat for ${searchQuery.value}.`);
    // Open the chat page in a new tab
    window.open('/chat', '_blank');  // This will open the chat page in a new tab
  };
  </script>
  
  <style scoped>
  /* Center the iPhone frame */
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
    width: 402px;
    height: 874px;
    background: #ffffff;
    border-radius: 40px;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
    overflow: hidden;
    border: 2px solid #e0e0e0;
  }
  
  /* Container inside the "screen" */
  #container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100%;
    padding: 16px;
    box-sizing: border-box;
  }
  
  /* Description Title */
  .description-title {
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 16px;
    text-align: center;
    color: #333; /* Default light mode color */
  }
  
  /* Dark Mode Styling for Description Title */
  @media (prefers-color-scheme: dark) {
    .description-title {
      color: #fff; /* White text in dark mode */
    }
  }
  
  /* Custom search bar styling */
  ion-searchbar {
    width: 100%;
    --padding-start: 12px;
    --border-radius: 8px;
    --background: #f7f7f7; /* Light gray background */
    --icon-color: #8c8c8c; /* Gray color for the icon */
    --color: #333; /* Darker text color */
    margin-bottom: 12px;
  }
  
  /* Buttons styling */
  ion-button {
    margin-top: 20px;
    --border-radius: 16px;
    font-weight: bold;
    --background: #ff5d35; /* Custom orange color */
    --color: white; /* Text color white for contrast */
  }
  
  .action-btn {
    --padding-start: 24px;
    --padding-end: 24px;
    --padding-top: 12px;
    --padding-bottom: 12px;
  }
  
  /* Error message styling */
  ion-text.error-message {
    margin-bottom: 16px;
    --color: #ff3b30; /* Error text color */
  }
  </style>
  