import { Link } from 'react-router-dom'

export default function Dashboard() {
  return (
    <div>
      <h1 className="text-2xl mb-4">Eventos recentes</h1>
      <p>Lista de eventos aparecerá aqui.</p>
      <Link to="/new" className="mt-4 inline-block bg-green-500 text-white p-2">Criar Episódio</Link>
    </div>
  )
}
