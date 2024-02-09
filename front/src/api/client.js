import axios from 'axios'

export const client = axios.create({
  baseURL: 'http://192.168.1.84:3000/api'
})
