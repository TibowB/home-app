<script setup>
import { ref } from 'vue'
import { getRecipes, deleteRecipe, addRecipe } from '@/api/recipes'

const recipes = ref([])
const newRecipe = ref('')

const onDelete = (id) =>
  deleteRecipe(id).then(() => getRecipes().then((data) => (recipes.value = data)))

const onSubmit = () => {
  addRecipe({ name: newRecipe.value })
    .then(() => getRecipes())
    .then((data) => (recipes.value = data))
    .finally(() => (newRecipe.value = ''))
}

getRecipes().then((data) => (recipes.value = data))
</script>

<template>
  <div v-for="recipe in recipes" :key="recipe.id" class="recipes">
    <div>
      <h3>{{ recipe.name }}</h3>
      <button @click="onDelete(recipe.id)">Supprimer</button>
    </div>
  </div>
  <form @submit.prevent="onSubmit" @keyup.enter="onSubmit">
    <input type="text" v-model="newRecipe" name="newRecipe" />
    <button type="submit">Envoyer</button>
  </form>
</template>

<style>
.recipes {
  margin-bottom: 2em;
}
</style>
