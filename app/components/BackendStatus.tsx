'use client'

import { useState, useEffect } from 'react'

interface BackendStatusProps {
  apiUrl: string
}

export default function BackendStatus({ apiUrl }: BackendStatusProps) {
  const [isConnected, setIsConnected] = useState(false)
  const [isChecking, setIsChecking] = useState(true)

  useEffect(() => {
    const checkBackend = async () => {
      try {
        setIsChecking(true)
        const response = await fetch(`${apiUrl}/health`, {
          cache: 'no-store',
          signal: AbortSignal.timeout(3000)
        })
        setIsConnected(response.ok)
      } catch {
        setIsConnected(false)
      } finally {
        setIsChecking(false)
      }
    }

    checkBackend()
    const interval = setInterval(checkBackend, 5000) // Check every 5 seconds

    return () => clearInterval(interval)
  }, [apiUrl])

  if (isConnected || isChecking) {
    return null
  }

  return (
    <div className="mb-6 bg-orange-100 border-l-4 border-orange-500 text-orange-700 p-4 rounded-lg shadow-md">
      <div className="flex items-center">
        <div className="flex-shrink-0">
          <svg className="h-5 w-5 text-orange-500" viewBox="0 0 20 20" fill="currentColor">
            <path fillRule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clipRule="evenodd" />
          </svg>
        </div>
        <div className="ml-3 flex-1">
          <p className="text-sm font-medium">
            Backend server is not connected
          </p>
          <p className="mt-1 text-sm">
            Please start the backend server by running: <code className="bg-orange-200 px-2 py-1 rounded">cd backend && python -m uvicorn main:app --reload --port 8000</code>
          </p>
        </div>
      </div>
    </div>
  )
}

