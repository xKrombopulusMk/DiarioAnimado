import { create } from 'zustand'

interface AuthState {
  token: string | null
  setToken: (t: string) => void
}

export const useAuthStore = create<AuthState>(set => ({
  token: null,
  setToken: (t) => set({ token: t })
}))
