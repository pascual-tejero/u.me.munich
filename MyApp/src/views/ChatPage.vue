<template>
    <div class="iphone-frame">
      <ion-page>
        <ion-header :translucent="true">
          <ion-toolbar>
            <ion-title>Chat</ion-title>
          </ion-toolbar>
        </ion-header>
  
        <ion-content :fullscreen="true">
          <ion-header collapse="condense">
            <ion-toolbar>
              <ion-title size="large">Chat</ion-title>
            </ion-toolbar>
          </ion-header>
  
          <div id="container">
            <!-- Chat Messages Area -->
            <div class="chat-area">
              <div
                v-for="(message, index) in messages"
                :key="index"
                class="message"
                :class="{ 'sent': message.isSent }"
              >
                {{ message.text }}
              </div>
            </div>
  
            <!-- Input Field for Chat -->
            <div class="chat-input-container">
              <ion-item>
                <ion-input
                  v-model="newMessage"
                  placeholder="Type your message..."
                  clear-input
                ></ion-input>
              </ion-item>
              <ion-button
                expand="block"
                shape="round"
                @click="sendMessage"
                :disabled="!newMessage"
                class="send-btn"
              >
                Send
              </ion-button>
            </div>
          </div>
        </ion-content>
      </ion-page>
    </div>
  </template>
  
  <script setup lang="ts">
import { ref } from "vue";
import {
  IonContent,
  IonHeader,
  IonPage,
  IonTitle,
  IonToolbar,
  IonButton,
  IonItem,
  IonInput,
} from "@ionic/vue";

// Define the type for a message
interface Message {
  text: string;
  isSent: boolean;
}

// Explicitly type the `messages` array
const messages = ref<Message[]>([]);

// New message input field
const newMessage = ref("");

// Predefined responses for the chat
const predefinedAnswers = [
  "Hi Mona, Nice to meet you too! I'm Cabrini. How are you today?",
  "I'm fine, thanks! What are you doing today?",
  "That sounds great! Tell me more about it.",
  "I really enjoy chatting with you.",
  "Goodbye for now! Talk to you soon.",
];

let answerIndex = 0;

// Function to handle sending a new message
const sendMessage = () => {
  if (newMessage.value.trim()) {
    // Add the user's message to the chat
    messages.value.push({ text: newMessage.value, isSent: true });

    // Clear the input field
    const userMessage = newMessage.value.trim();
    newMessage.value = "";

    // Simulate a delay before responding with a predefined answer
    setTimeout(() => {
      if (answerIndex < predefinedAnswers.length) {
        messages.value.push({ text: predefinedAnswers[answerIndex], isSent: false });
        answerIndex++;
      }
    }, 1000); // 1-second delay for realism
  }
};
</script>

  
<style scoped>
/* iPhone frame styling */
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

#container {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100%;
  padding: 16px;
  box-sizing: border-box;
}

/* Chat Area Styles */
.chat-area {
  flex: 1;
  overflow-y: auto;
  padding: 8px;
  width: 100%;
  background-color: #f5f5f5;
  border-radius: 8px;
  margin-bottom: 16px;
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
}

/* General Message Styles */
.message {
  padding: 10px;
  margin: 5px 0;
  border-radius: 12px;
  background-color: #e0e0e0;
  color: #000;
  font-size: 14px;
  max-width: 70%; /* Adjusted to allow space for alignment */
  word-wrap: break-word;
  display: inline-block;
}

/* Sent Messages (Orange, Right-Aligned) */
.message.sent {
  background-color: #ff5d35; /* Custom orange for sent messages */
  color: #fff;
  align-self: flex-end; /* Aligns the message to the right */
}

/* Received Messages (Gray, Left-Aligned) */
.message:not(.sent) {
  align-self: flex-start; /* Aligns the message to the left */
}

/* Chat Input Styles */
.chat-input-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
}

ion-item {
  width: 100%;
  margin-bottom: 8px;
}

ion-button {
  --background: #ff5d35; /* Custom orange for the send button */
  --color: white;
  --border-radius: 16px;
}

ion-button[disabled] {
  opacity: 0.6;
}

ion-header {
  position: sticky;
  top: 0;
  background: #f8f8f8;
}

ion-title {
  font-size: 16px;
}
</style>
