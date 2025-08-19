import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import api from '../api'

export default function CreateEpisode() {
  const [period, setPeriod] = useState('day')
  const [style, setStyle] = useState('poetic')
  const navigate = useNavigate()

  const submit = async (e: React.FormEvent) => {
    e.preventDefault()
    const res = await api.post('/episodes/create', { period, style })
    navigate(`/episodes/${res.data.id}`)
  }

  return (
    <form onSubmit={submit} className="flex flex-col gap-2 max-w-sm">
      <select className="border p-2" value={period} onChange={e => setPeriod(e.target.value)}>
        <option value="day">Dia</option>
        <option value="week">Semana</option>
        <option value="month">Mês</option>
      </select>
      <select className="border p-2" value={style} onChange={e => setStyle(e.target.value)}>
        <option value="poetic">Poético</option>
        <option value="funny">Engraçado</option>
        <option value="audio">Áudio</option>
        <option value="cartoon">Cartoon</option>
      </select>
      <button className="bg-blue-500 text-white p-2" type="submit">Gerar</button>
    </form>
  )
}
