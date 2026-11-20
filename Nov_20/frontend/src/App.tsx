import { useState, useEffect } from 'react'
import './App.css'

const API_BASE = 'http://localhost:8000'

type Student = {
  id: number
  name: string
  email: string
  course: string
  grade: string
}

type View = 'login' | 'dashboard'

function App() {
  const [view, setView] = useState<View>('login')
  const [adminKey, setAdminKey] = useState('')
  const [token, setToken] = useState('')

  const [students, setStudents] = useState<Student[]>([])
  const [newStudent, setNewStudent] = useState({ name: '', email: '', course: '', grade: '' })

  const [notes, setNotes] = useState('')
  const [aiResult, setAiResult] = useState('')

  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  // ---------- Login ----------
  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)
    setError('')
    try {
      const res = await fetch(`${API_BASE}/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ admin_key: adminKey }),
      })
      const data = await res.json()
      if (!res.ok) throw new Error(data.detail || 'Login failed')
      setToken(data.token)
      setView('dashboard')
      fetchStudents()
    } catch (err: any) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  // ---------- Students ----------
  const fetchStudents = async () => {
    try {
      const res = await fetch(`${API_BASE}/students`)
      const data = await res.json()
      setStudents(data)
    } catch (err) {
      console.error(err)
    }
  }

  const addStudent = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)
    setError('')
    try {
      const res = await fetch(`${API_BASE}/students`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-Admin-Key': adminKey,
        },
        body: JSON.stringify(newStudent),
      })
      const data = await res.json()
      if (!res.ok) throw new Error(data.detail || 'Failed to add student')
      setStudents([data.student, ...students])
      setNewStudent({ name: '', email: '', course: '', grade: '' })
    } catch (err: any) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  // ---------- AI ----------
  const runAi = async (endpoint: string) => {
    setLoading(true)
    setError('')
    setAiResult('')
    try {
      const res = await fetch(`${API_BASE}/ai/${endpoint}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-Admin-Key': adminKey,
        },
        body: JSON.stringify({ notes }),
      })
      const data = await res.json()
      if (!res.ok) throw new Error(data.detail || 'AI request failed')
      setAiResult(data.summary || data.quiz || '')
    } catch (err: any) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app">
      <header>
        <h1>🎓 AI Student Portal</h1>
        <p>FastAPI • React • MySQL • Gemini AI</p>
      </header>

      {view === 'login' ? (
        <section className="card login-card">
          <h2>Admin Login</h2>
          {error && <div className="error">{error}</div>}
          <form onSubmit={handleLogin}>
            <label>Admin Key</label>
            <input
              type="password"
              value={adminKey}
              onChange={(e) => setAdminKey(e.target.value)}
              placeholder="Enter admin key"
              required
            />
            <button type="submit" disabled={loading}>
              {loading ? 'Signing in...' : 'Sign In'}
            </button>
          </form>
        </section>
      ) : (
        <>
          <nav>
            <button onClick={() => setView('login')}>Logout</button>
            <span>Signed in as admin</span>
          </nav>

          <section className="grid">
            {/* Student list */}
            <div className="card">
              <h2>Students</h2>
              <button
                className="btn"
                onClick={() => (document.getElementById('add-form') as HTMLElement | null)?.scrollIntoView()}
              >
                + Add Student
              </button>
              <table>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Course</th>
                    <th>Grade</th>
                  </tr>
                </thead>
                <tbody>
                  {students.map((s) => (
                    <tr key={s.id}>
                      <td>{s.name}</td>
                      <td>{s.email}</td>
                      <td>{s.course}</td>
                      <td>{s.grade}</td>
                    </tr>
                  ))}
                  {students.length === 0 && <tr><td colSpan="4">No students yet.</td></tr>}
                </tbody>
              </table>
            </div>

            {/* Add student form */}
            <div className="card" id="add-form">
              <h2>Add Student</h2>
              {error && <div className="error">{error}</div>}
              <form onSubmit={addStudent}>
                <label>Name</label>
                <input
                  value={newStudent.name}
                  onChange={(e) => setNewStudent({ ...newStudent, name: e.target.value })}
                  placeholder="Name"
                  required
                />
                <label>Email</label>
                <input
                  value={newStudent.email}
                  onChange={(e) => setNewStudent({ ...newStudent, email: e.target.value })}
                  placeholder="email@example.com"
                  type="email"
                  required
                />
                <label>Course</label>
                <input
                  value={newStudent.course}
                  onChange={(e) => setNewStudent({ ...newStudent, course: e.target.value })}
                  placeholder="Course"
                  required
                />
                <label>Grade</label>
                <input
                  value={newStudent.grade}
                  onChange={(e) => setNewStudent({ ...newStudent, grade: e.target.value })}
                  placeholder="A"
                  required
                />
                <button type="submit" disabled={loading} className="btn">
                  {loading ? 'Adding...' : 'Add Student'}
                </button>
              </form>
            </div>

            {/* AI Summarize */}
            <div className="card">
              <h2>AI Summarize Notes</h2>
              <textarea
                value={notes}
                onChange={(e) => setNotes(e.target.value)}
                placeholder="Paste your study notes here..."
                rows={6}
              />
              <button onClick={() => runAi('summarize')} disabled={loading} className="btn">
                {loading ? 'Summarizing...' : 'Summarize'}
              </button>
              {aiResult && <div className="result"><strong>Summary:</strong><br />{aiResult}</div>}
            </div>

            {/* AI Quiz */}
            <div className="card">
              <h2>AI Quiz Generator</h2>
              <p>Generate 5 MCQs from your notes.</p>
              <button onClick={() => runAi('quiz')} disabled={loading} className="btn">
                {loading ? 'Generating...' : 'Generate Quiz'}
              </button>
              {aiResult && <div className="result"><strong>Quiz:</strong><br />{aiResult}</div>}
            </div>
          </section>

          {error && <div className="error">{error}</div>}
        </>
      )}

      <footer>
        AI Student Portal — built with React, FastAPI, MySQL, and Gemini AI
      </footer>
    </div>
  )
}

export default App
