<template>
  <div class="iphone-frame">
    <ion-page>
      <ion-header :translucent="true">
        <ion-toolbar>
          <ion-title>Sign Up</ion-title>
        </ion-toolbar>
      </ion-header>

      <ion-content :fullscreen="true">
        <ion-header collapse="condense">
          <ion-toolbar>
            <ion-title size="large">Sign Up</ion-title>
          </ion-toolbar>
        </ion-header>

        <div id="container">
          <strong>Create Your Account</strong>

          <!-- Full Name Input -->
          <ion-item>
            <ion-label position="stacked">Full Name</ion-label>
            <ion-input v-model="fullname" type="text" placeholder="Enter your full name"></ion-input>
          </ion-item>

          <!-- Email Input -->
          <ion-item>
            <ion-label position="stacked">Email</ion-label>
            <ion-input v-model="email" type="email" placeholder="Enter your email"></ion-input>
          </ion-item>

          <!-- Error Message for Invalid Email -->
          <ion-text color="danger" v-if="emailErrorMessage" class="error-message">
            {{ emailErrorMessage }}
          </ion-text>

          <!-- Password Input -->
          <ion-item>
            <ion-label position="stacked">Password</ion-label>
            <ion-input v-model="password" type="password" placeholder="Create a password"></ion-input>
          </ion-item>

          <!-- Repeat Password Input -->
          <ion-item>
            <ion-label position="stacked">Repeat Password</ion-label>
            <ion-input v-model="repeatPassword" type="password" placeholder="Repeat your password"></ion-input>
          </ion-item>

          <!-- Error Message for Password Mismatch -->
          <ion-text color="danger" v-if="errorMessage" class="error-message">
            {{ errorMessage }}
          </ion-text>

          <!-- Sign Up Button -->
          <ion-button expand="block" shape="round" @click="handleSignUp" class="sign-up-btn">Sign Up</ion-button>

          <!-- Success Message -->
          <ion-text color="success" v-if="successMessage">{{ successMessage }}</ion-text>

          <!-- Sign In Link -->
          <ion-text class="sign-in-link">
            <span class="have-account-text"> Already have an account? </span>
            <a href="#" @click="goToSignIn">Sign In</a>
          </ion-text>
        </div>
      </ion-content>
    </ion-page>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue';
import { IonContent, IonHeader, IonPage, IonTitle, IonToolbar, IonButton, IonItem, IonLabel, IonInput, IonText } from '@ionic/vue';
import { useRouter } from 'vue-router';

const fullname = ref('');
const email = ref('');
const password = ref('');
const repeatPassword = ref('');
const errorMessage = ref('');
const successMessage = ref('');
const emailErrorMessage = ref('');
const router = useRouter();

// Email validation function using regex
const isValidEmail = (email: string) => {
  const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  return emailRegex.test(email);
};

// Watcher to check if the passwords match as the user types
watch([password, repeatPassword], () => {
  if (repeatPassword.value && repeatPassword.value !== password.value) {
    errorMessage.value = 'Passwords do not match.';
  } else {
    errorMessage.value = ''; // Clear error when they match
  }
});

// Watcher to check if email is valid as the user types
watch(email, (newEmail) => {
  if (newEmail && !isValidEmail(newEmail)) {
    emailErrorMessage.value = 'Please enter a valid email address.';
  } else {
    emailErrorMessage.value = ''; // Clear error if email is valid
  }
});

// Simulate an email sending function
const sendVerificationEmail = (email: string) => {
  // Replace with your backend email sending logic
  console.log(`Verification email sent to ${email}`);
};

// Handle sign up logic
const handleSignUp = () => {
  if (fullname.value && email.value && password.value && repeatPassword.value) {
    // If there is an email error, prevent sign up
    if (emailErrorMessage.value) {
      return;
    }

    if (errorMessage.value === '') {
      // Simulate sending a verification email
      sendVerificationEmail(email.value);
      successMessage.value = 'Account created successfully! Please check your email to verify your account.';
      // You can redirect the user to the login page after successful sign up
      // router.push('/login'); (if using Vue Router)
    }
  } else {
    errorMessage.value = 'Please fill in all fields.';
  }
};

const goToSignIn = () => {
  router.push('/home');
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

/* Main iPhone container */
.iphone-frame {
  position: relative;
  width: 402px; /* Approx width of iPhone */
  height: 874px; /* Approx height of iPhone */
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
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100%; /* Take full height of the parent (iphone-frame) */
  padding: 16px;
  box-sizing: border-box;
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
  color: var(--ion-color-primary); /* Use the primary color for the link, which adapts in dark mode */
  text-decoration: none;
}

.no-account-text {
  color: var(--ion-text-color); /* This will adapt based on the theme (dark/light) */
}

/* Dark mode customization */
body {
  --ion-background-color: #121212; /* Dark background */
  --ion-text-color: #ffffff; /* Light text color for dark mode */
}

ion-text {
  --color: var(--ion-text-color); /* Ensure ion-text inherits the correct text color */
}

ion-item {
  margin-bottom: 15px;
  width: 100%; /* Make inputs fill the width */
}

ion-button {
  margin-top: 20px;
  --border-radius: 16px; /* Round the corners for iOS-style */
  --padding-start: 24px; /* Padding for left */
  --padding-end: 24px; /* Padding for right */
  --padding-top: 12px; /* Padding for top */
  --padding-bottom: 12px; /* Padding for bottom */
  font-weight: bold;
  --background: #ff5d35; /* Custom color for the button */
  --color: white; /* Text color white for contrast */
}

/* Style for disabled button */
ion-button[disabled] {
  opacity: 0.6; /* Faded look when disabled */
}

/* Sign Up link styling */
.sign-in-link {
  margin-top: 10px;
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

ion-text {
  display: block;
  margin-top: 10px;
}

/* Error message styling */
.error-message {
  margin-bottom: 16px;
  color: #ff3b30;
}
</style>
