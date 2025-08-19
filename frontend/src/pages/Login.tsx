import { useState } from 'react'
import axios from 'axios'
import { useNavigate } from 'react-router-dom'
import { useAuthStore } from '../store/auth'

export default function Login() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const navigate = useNavigate()
  const setToken = useAuthStore(s => s.setToken)

  const submit = async (e: React.FormEvent) => {
    e.preventDefault()
    const form = new URLSearchParams()
    form.append('username', email)
    form.append('password', password)
    const res = await axios.post('/auth/login', form)
    setToken(res.data.access_token)
    navigate('/')
  }

  return (
    <form onSubmit={submit} className="flex flex-col gap-2 max-w-sm mx-auto">
      <input className="border p-2" placeholder="Email" value={email} onChange={e => setEmail(e.target.value)} />
      <input className="border p-2" type="password" placeholder="Senha" value={password} onChange={e => setPassword(e.target.value)} />
      <button className="bg-blue-500 text-white p-2" type="submit">Entrar</button>
    </form>
  )
}
