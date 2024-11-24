<template>
  <div class="iphone-frame">
    <ion-page>
      <!-- Header Section -->
      <ion-header :translucent="true">
        <ion-toolbar>
          <!-- Title aligned to the left -->
          <ion-title slot="start" class="profile-title">Profile</ion-title>
        </ion-toolbar>
      </ion-header>

      <ion-content :fullscreen="true">
        <div id="container">
          <!-- Sponsor and Points Section -->
          <div class="sponsor-points">
            <ion-button expand="block" shape="round" class="sponsor-btn" @click="goToSponsor">
              Sponsor
            </ion-button>
            <div class="points-display">
              <ion-icon name="wallet-outline"></ion-icon>
              {{ userPoints }} Points
            </div>
          </div>

          <!-- My Profile Title -->
          <h1 class="main-title">My Profile</h1>

          <!-- Profile Picture Placeholder -->
          <div class="profile-picture">
            <ion-avatar>
              <div class="placeholder-icon">
                <ion-icon name="person-circle-outline"></ion-icon>
                <div class="plus-icon">+</div>
              </div>
            </ion-avatar>
          </div>

          <!-- Welcome Message -->
          <h2 class="description-title">Welcome to Your Profile</h2>

          <!-- Action Buttons -->
          <ion-button expand="block" shape="round" class="action-btn" @click="goToHost">
            Host
          </ion-button>

          <ion-button expand="block" shape="round" class="action-btn" @click="goToMyEvents">
            My Events
          </ion-button>

          <ion-button expand="block" shape="round" class="action-btn" @click="redeemPoints">
            Redeem Points
          </ion-button>
        </div>
      </ion-content>
    </ion-page>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { IonContent, IonHeader, IonPage, IonTitle, IonToolbar, IonButton, IonAvatar, IonIcon } from "@ionic/vue";

// User Points (can be dynamically fetched later)
const userPoints = ref(1200);

// Navigation Methods
const goToSponsor = () => {
  console.log("Navigating to Sponsor Page");
  // Add routing logic here
};

const goToHost = () => {
  console.log("Navigating to Host Page");
  // Add routing logic here
};

const goToMyEvents = () => {
  console.log("Navigating to My Events Page");
  // Add routing logic here
};

const redeemPoints = () => {
  console.log("Redeeming Points");
  // Add redemption logic here
};
</script>

<style scoped>
/* Center the iPhone frame */
/* Main Body */
body {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0;
  height: 100vh;
  background-color: var(--ion-background-color); /* Dynamically changes based on mode */
}

/* Main iPhone container */
.iphone-frame {
  position: relative;
  width: 402px;
  height: 874px;
  background: var(--ion-item-background-color); /* Dynamic background for dark/light */
  border-radius: 40px;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
  overflow: hidden;
  border: 2px solid var(--ion-border-color); /* Border color adjusts with theme */
}

/* Container inside the "screen" */
#container {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  height: 100%;
  padding: 16px;
  box-sizing: border-box;
}

/* Profile title aligned to the left */
.profile-title {
  text-align: left;
  margin-left: 16px;
  font-weight: bold;
  color: var(--ion-text-color); /* Text color adjusts with theme */
}

/* Sponsor and Points Section */
.sponsor-points {
  display: flex;
  justify-content: space-between; /* Align items to the left and right */
  align-items: center;
  width: 100%;
  margin-bottom: 16px;
  margin-top: -10px; 
}

/* Sponsor button styling */
.sponsor-btn {
  --background: #ff5d35;
  --color: white;
  --border-radius: 16px;
  width: auto;
  margin-right: 16px; /* Add space between button and points display */
  flex-shrink: 0; /* Prevent the button from shrinking */
}

/* Points display styling */
.points-display {
  font-size: 16px;
  display: flex;
  align-items: center;
  gap: 8px;
  font-weight: bold;
  color: var(--ion-text-color); /* Text color adjusts with theme */
  flex-grow: 1;  /* Allow the points display to take available space */
  justify-content: flex-end;  /* Align to the right */
}

.points-display ion-icon {
  font-size: 20px;
}

/* Main title: My Profile */
.main-title {
  font-size: 22px;
  font-weight: bold;
  margin-bottom: 24px;
  text-align: center;
  color: var(--ion-text-color); /* Text color adjusts with theme */
}

/* Profile picture styling */
.profile-picture {
  margin-bottom: 16px;
}

ion-avatar {
  width: 180px;
  height: 180px;
  border-radius: 50%;
  background-color: var(--ion-item-background-color); /* Avatar background color */
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
  position: relative;
  overflow: hidden;
}

.placeholder-icon {
  font-size: 60px;
  color: var(--ion-text-color); /* Placeholder icon color */
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}

.plus-icon {
  position: absolute;
  bottom: 15px;
  right: 15px;
  font-size: 24px;
  color: #fff;
  background-color: #ff5d35;
  border-radius: 50%;
  width: 36px;
  height: 36px;
  display: flex;
  justify-content: center;
  align-items: center;
}

/* Description Title */
.description-title {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 24px;
  text-align: center;
  color: var(--ion-text-color); /* Text color adjusts with theme */
}

/* Buttons styling */
ion-button {
  margin-top: 20px;
  --border-radius: 16px;
  font-weight: bold;
  --background: #ff5d35; /* Custom orange color */
  --color: white; /* Text color white for contrast */
}

/* Action Buttons */
.action-btn {
  --padding-start: 24px;
  --padding-end: 24px;
  --padding-top: 12px;
  --padding-bottom: 12px;
}

/* Top header buttons styling */
ion-buttons ion-button {
  --color: var(--ion-text-color); /* Button text color */
  font-size: 14px;
  font-weight: bold;
}

ion-buttons ion-button ion-icon {
  margin-right: 4px;
  font-size: 18px;
}

/* Media Query for Dark Mode */
@media (prefers-color-scheme: dark) {
  body {
    background-color: var(--ion-background-color-dark);
  }
  .iphone-frame {
    background-color: var(--ion-item-background-color-dark);
    border: 2px solid var(--ion-border-color-dark);
  }
  .profile-title,
  .main-title,
  .description-title,
  .points-display {
    color: var(--ion-text-color-dark);
  }
  ion-avatar {
    background-color: var(--ion-item-background-color-dark);
  }
  .plus-icon {
    background-color: #ff5d35;
  }
}
</style>
