import axios from 'axios'
import { useAuthStore } from '../store/auth'

const api = axios.create({ baseURL: 'http://localhost:8000' })

api.interceptors.request.use(config => {
  const token = useAuthStore.getState().token
  if (token) config.headers = { ...config.headers, Authorization: `Bearer ${token}` }
  return config
})

export default api
