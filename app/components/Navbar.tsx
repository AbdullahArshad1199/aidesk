'use client'

import Link from 'next/link'
import { usePathname, useRouter } from 'next/navigation'
import { useUser } from '../context/UserContext'

export default function Navbar() {
  const pathname = usePathname()
  const router = useRouter()
  const { isLoggedIn, logout } = useUser()

  const isActive = (path: string) => pathname === path || (path === '/news' && pathname.startsWith('/news/'))

  const handleLogout = () => {
    logout()
    router.push('/')
  }

  return (
    <nav className="sticky top-0 z-50 bg-[#0A1A3A] shadow-professional backdrop-blur-md bg-opacity-95 border-b border-[#112B54]/30">
      <div className="container mx-auto px-8 md:px-12 lg:px-16">
        <div className="flex items-center justify-between h-20">
          <Link 
            href="/" 
            className="text-2xl font-bold text-white hover:text-[#4A6FF3] transition-all duration-300 flex items-center gap-2 group"
          >
            <span className="relative">
              <span className="absolute inset-0 bg-gradient-to-r from-[#4A6FF3] to-[#1F3F7F] opacity-0 group-hover:opacity-20 blur-xl transition-opacity duration-300"></span>
              AI News Hub
            </span>
          </Link>
          
          <div className="flex items-center space-x-2">
            <Link
              href="/"
              className={`px-5 py-2.5 rounded-lg font-medium transition-all duration-300 relative overflow-hidden ${
                isActive('/')
                  ? 'bg-gradient-to-r from-[#4A6FF3] to-[#1F3F7F] text-white shadow-lg shadow-[#4A6FF3]/30'
                  : 'text-gray-300 hover:text-white hover:bg-[#112B54]/50'
              }`}
            >
              <span className="relative z-10">Home</span>
            </Link>
            <Link
              href="/news"
              className={`px-5 py-2.5 rounded-lg font-medium transition-all duration-300 relative overflow-hidden ${
                isActive('/news')
                  ? 'bg-gradient-to-r from-[#4A6FF3] to-[#1F3F7F] text-white shadow-lg shadow-[#4A6FF3]/30'
                  : 'text-gray-300 hover:text-white hover:bg-[#112B54]/50'
              }`}
            >
              <span className="relative z-10">All News</span>
            </Link>
            <Link
              href="/videos"
              className={`px-5 py-2.5 rounded-lg font-medium transition-all duration-300 relative overflow-hidden ${
                isActive('/videos')
                  ? 'bg-gradient-to-r from-[#4A6FF3] to-[#1F3F7F] text-white shadow-lg shadow-[#4A6FF3]/30'
                  : 'text-gray-300 hover:text-white hover:bg-[#112B54]/50'
              }`}
            >
              <span className="relative z-10">Videos</span>
            </Link>
            <Link
              href="/sources"
              className={`px-5 py-2.5 rounded-lg font-medium transition-all duration-300 relative overflow-hidden ${
                isActive('/sources')
                  ? 'bg-gradient-to-r from-[#4A6FF3] to-[#1F3F7F] text-white shadow-lg shadow-[#4A6FF3]/30'
                  : 'text-gray-300 hover:text-white hover:bg-[#112B54]/50'
              }`}
            >
              <span className="relative z-10">Sources</span>
            </Link>
            {isLoggedIn ? (
              <button
                onClick={handleLogout}
                className="px-5 py-2.5 rounded-lg font-medium transition-all duration-300 text-gray-300 hover:text-white hover:bg-[#112B54]/50 border border-[#112B54] hover:border-[#4A6FF3]"
              >
                Logout
              </button>
            ) : (
              <Link
                href="/login"
                className={`px-5 py-2.5 rounded-lg font-medium transition-all duration-300 relative overflow-hidden ${
                  isActive('/login')
                    ? 'bg-gradient-to-r from-[#4A6FF3] to-[#1F3F7F] text-white shadow-lg shadow-[#4A6FF3]/30'
                    : 'text-gray-300 hover:text-white hover:bg-[#112B54]/50 border border-[#112B54] hover:border-[#4A6FF3]'
                }`}
              >
                <span className="relative z-10">Login</span>
              </Link>
            )}
          </div>
        </div>
      </div>
    </nav>
  )
}

