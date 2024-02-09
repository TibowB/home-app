<script setup>
import AppBar from '@/components/AppBar/AppBar.vue';
import { RouterView } from 'vue-router';
</script>

<template>
  <v-app>
    <AppBar />
    <RouterView />
  </v-app>
</template>
