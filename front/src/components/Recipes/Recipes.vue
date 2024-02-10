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
  addRecipe({ name: newRecipe.value })
    .then(() => getRecipes())
    .then(data => (recipes.value = data))
    .finally(() => (newRecipe.value = ''));
};

getRecipes().then(data => (recipes.value = data));
</script>

<template>
  <v-text-field
    label="Nouvelle recette"
    hide-details="auto"
    v-model="newRecipe"
    class="my-4"
  ></v-text-field>
  <v-btn
    variant="outlined"
    width="100%"
    @click="onSubmit"
    :disabled="!newRecipe"
    >Enregistrer</v-btn
  >
  <p class="text-h4 mt-4">Recettes</p>
  <v-list lines="one" v-if="recipes.length !== 0">
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
