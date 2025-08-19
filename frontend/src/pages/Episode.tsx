import { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import api from '../api'

interface Episode {
  id: number
  text?: string
  audio_path?: string
  video_path?: string
}

export default function EpisodeView() {
  const { id } = useParams()
  const [episode, setEpisode] = useState<Episode | null>(null)

  useEffect(() => {
    api.get(`/episodes/${id}`).then(res => setEpisode(res.data))
  }, [id])

  if (!episode) return <p>Carregando...</p>

  return (
    <div className="space-y-4">
      <p>{episode.text}</p>
      {episode.audio_path && (
        <audio controls src={`/${episode.audio_path}`}></audio>
      )}
      {episode.video_path && (
        <video controls width="320" src={`/${episode.video_path}`}></video>
      )}
    </div>
  )
}
