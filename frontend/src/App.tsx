import { Routes, Route, Link } from 'react-router-dom'
import Login from './pages/Login'
import Dashboard from './pages/Dashboard'
import CreateEpisode from './pages/CreateEpisode'
import EpisodeView from './pages/Episode'
import Episodes from './pages/Episodes'
import Premium from './pages/Premium'

export default function App() {
  return (
    <div className="p-4">
      <nav className="mb-4 flex gap-4">
        <Link to="/">Dashboard</Link>
        <Link to="/episodes">Episódios</Link>
        <Link to="/new">Novo Episódio</Link>
        <Link to="/premium">Premium</Link>
      </nav>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/" element={<Dashboard />} />
        <Route path="/episodes" element={<Episodes />} />
        <Route path="/new" element={<CreateEpisode />} />
        <Route path="/episodes/:id" element={<EpisodeView />} />
        <Route path="/premium" element={<Premium />} />
      </Routes>
    </div>
  )
}
