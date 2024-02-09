<script setup>
import { ref } from 'vue';
import { getRecipes, deleteRecipe, addRecipe } from '@/api/recipes';

const recipes = ref([]);
const newRecipe = ref('');

const onDelete = id =>
  deleteRecipe(id).then(() =>
    getRecipes().then(data => (recipes.value = data))
  );

const onSubmit = () => {
  if (newRecipe.value === '') {
    return;
  }

  addRecipe({ name: newRecipe.value })
    .then(() => getRecipes())
    .then(data => (recipes.value = data))
    .finally(() => (newRecipe.value = ''));
};

recipes.value = [{ name: 'Soupe', id: 4 }];

getRecipes().then(data => (recipes.value = data));
</script>

<template>
  <v-text-field
    label="Nouvelle recette"
    hide-details="auto"
    v-model="newRecipe"
    class="mt-10"
  ></v-text-field>
  <v-btn variant="outlined" @click="onSubmit">Enregistrer</v-btn>
  <v-list lines="one">
    <v-list-item
      v-for="recipe in recipes"
      :key="recipe.id"
      :title="recipe.name"
      append-icon="mdi-close"
      @click.append="onDelete(recipe.id)"
    ></v-list-item>
  </v-list>
</template>

<style>
.recipes {
  margin-bottom: 2em;
}
</style>
