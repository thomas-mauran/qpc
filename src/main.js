import { createApp } from 'vue';
import './style.css';
// import { createRouter, createWebHistory } from 'vue-router';

import kuzzle from './services/kuzzle';

// Vues pages
import App from './vues/App.vue';

createApp(App).mount('#app');
