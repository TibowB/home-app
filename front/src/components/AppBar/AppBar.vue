<template>
  <v-app-bar :elevation="2">
    <template v-slot:prepend>
      <v-btn icon="mdi-home"></v-btn>
    </template>

    <v-app-bar-title>Home App</v-app-bar-title>

    <template v-slot:append>
      <v-btn icon="mdi-magnify"></v-btn>
      <v-btn icon="mdi-dots-vertical"></v-btn>
    </template>
  </v-app-bar>
</template>
