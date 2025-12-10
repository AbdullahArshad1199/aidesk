import Link from 'next/link'

export default function Footer() {
  return (
    <footer className="bg-gradient-to-b from-[#0A1A3A] to-[#112B54] text-white mt-20 border-t border-[#1F3F7F]/30">
      <div className="container mx-auto px-8 md:px-12 lg:px-16 py-12">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
          <div className="md:col-span-2">
            <h3 className="text-2xl font-bold mb-4 bg-gradient-to-r from-white to-gray-300 bg-clip-text text-transparent">
              AI News Hub
            </h3>
            <p className="text-gray-300 leading-relaxed max-w-md">
              Your trusted source for the latest AI news, breakthrough research, and insightful videos from leading technology companies and research institutions worldwide.
            </p>
          </div>
          
          <div>
            <h3 className="text-lg font-semibold mb-4 text-white">Quick Links</h3>
            <ul className="space-y-3 text-gray-300">
              <li>
                <Link href="/" className="hover:text-[#4A6FF3] transition-colors duration-300 flex items-center gap-2 group">
                  <span className="w-1 h-1 bg-[#4A6FF3] rounded-full opacity-0 group-hover:opacity-100 transition-opacity"></span>
                  Home
                </Link>
              </li>
              <li>
                <Link href="/news" className="hover:text-[#4A6FF3] transition-colors duration-300 flex items-center gap-2 group">
                  <span className="w-1 h-1 bg-[#4A6FF3] rounded-full opacity-0 group-hover:opacity-100 transition-opacity"></span>
                  All News
                </Link>
              </li>
              <li>
                <Link href="/videos" className="hover:text-[#4A6FF3] transition-colors duration-300 flex items-center gap-2 group">
                  <span className="w-1 h-1 bg-[#4A6FF3] rounded-full opacity-0 group-hover:opacity-100 transition-opacity"></span>
                  Videos
                </Link>
              </li>
              <li>
                <Link href="/sources" className="hover:text-[#4A6FF3] transition-colors duration-300 flex items-center gap-2 group">
                  <span className="w-1 h-1 bg-[#4A6FF3] rounded-full opacity-0 group-hover:opacity-100 transition-opacity"></span>
                  Sources
                </Link>
              </li>
            </ul>
          </div>
          
          <div>
            <h3 className="text-lg font-semibold mb-4 text-white">News Sources</h3>
            <ul className="space-y-2 text-gray-300 text-sm">
              <li className="flex items-center gap-2">
                <span className="w-1.5 h-1.5 bg-[#4A6FF3] rounded-full"></span>
                OpenAI Blog
              </li>
              <li className="flex items-center gap-2">
                <span className="w-1.5 h-1.5 bg-[#4A6FF3] rounded-full"></span>
                DeepMind Blog
              </li>
              <li className="flex items-center gap-2">
                <span className="w-1.5 h-1.5 bg-[#4A6FF3] rounded-full"></span>
                Anthropic Blog
              </li>
              <li className="flex items-center gap-2">
                <span className="w-1.5 h-1.5 bg-[#4A6FF3] rounded-full"></span>
                TechCrunch AI
              </li>
              <li className="flex items-center gap-2">
                <span className="w-1.5 h-1.5 bg-[#4A6FF3] rounded-full"></span>
                Google News
              </li>
            </ul>
          </div>
        </div>
        
        <div className="border-t border-[#1F3F7F]/50 pt-8 mt-8">
          <div className="flex flex-col md:flex-row justify-between items-center gap-4">
            <p className="text-gray-400 text-sm">
              &copy; {new Date().getFullYear()} AI News Hub. All rights reserved.
            </p>
            <div className="flex items-center gap-6 text-sm text-gray-400">
              <span className="hover:text-[#4A6FF3] transition-colors cursor-pointer">Privacy Policy</span>
              <span className="hover:text-[#4A6FF3] transition-colors cursor-pointer">Terms of Service</span>
            </div>
          </div>
        </div>
      </div>
    </footer>
  )
}

