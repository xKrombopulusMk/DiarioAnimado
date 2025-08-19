import { render, screen } from '@testing-library/react'
import { BrowserRouter } from 'react-router-dom'
import Login from '../Login'

it('renderiza formulário de login', () => {
  render(<BrowserRouter><Login /></BrowserRouter>)
  expect(screen.getByPlaceholderText('Email')).toBeDefined()
})
