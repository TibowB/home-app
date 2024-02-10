<script setup>
import AppBar from '@/components/AppBar/AppBar.vue';
import { RouterView } from 'vue-router';
</script>

<template>
  <v-layout>
    <AppBar />
    <v-main>
      <RouterView />
    </v-main>
  </v-layout>
</template>
