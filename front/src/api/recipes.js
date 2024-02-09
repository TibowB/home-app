import { client } from '@/api/client'

export const getRecipes = () => client('recipes').then((data) => data.data)

export const deleteRecipe = (id) => client.delete('recipes/' + id)

export const addRecipe = (recipe) => client.post('recipes', recipe)
