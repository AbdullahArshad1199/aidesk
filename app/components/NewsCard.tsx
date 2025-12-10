'use client'

import Link from 'next/link'
import Image from 'next/image'

interface NewsCardProps {
  article: {
    title: string
    description: string
    link: string
    source: string
    published_at: string
    image?: string
    is_trending?: boolean
    is_important?: boolean
  }
  variant?: 'default' | 'large'
}

export default function NewsCard({ article, variant = 'default' }: NewsCardProps) {
  const formatDate = (dateStr: string) => {
    try {
      const date = new Date(dateStr)
      return date.toLocaleDateString('en-US', { 
        year: 'numeric', 
        month: 'short', 
        day: 'numeric' 
      })
    } catch {
      return 'Recent'
    }
  }

  const isLarge = variant === 'large'
  
  // Generate unique fallback image based on article title
  const getFallbackImage = (title: string) => {
    const aiImages = [
      "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=800&h=600&fit=crop",
      "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=800&h=600&fit=crop",
      "https://images.unsplash.com/photo-1555255707-c07966088b7b?w=800&h=600&fit=crop",
      "https://images.unsplash.com/photo-1488590528505-98d2b5aba04b?w=800&h=600&fit=crop",
      "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&h=600&fit=crop",
      "https://images.unsplash.com/photo-1504639725590-34d0984388bd?w=800&h=600&fit=crop",
      "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&h=600&fit=crop",
      "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=800&h=600&fit=crop",
      "https://images.unsplash.com/photo-1635070041078-e363dbe005cb?w=800&h=600&fit=crop",
      "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=800&h=600&fit=crop",
      "https://images.unsplash.com/photo-1555949963-aa79dcee981c?w=800&h=600&fit=crop",
      "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&h=600&fit=crop",
      "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=800&h=600&fit=crop",
      "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&h=600&fit=crop",
      "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=800&h=600&fit=crop",
    ]
    
    // Simple hash function to get consistent index
    let hash = 0
    for (let i = 0; i < title.length; i++) {
      const char = title.charCodeAt(i)
      hash = ((hash << 5) - hash) + char
      hash = hash & hash // Convert to 32-bit integer
    }
    const index = Math.abs(hash) % aiImages.length
    return aiImages[index]
  }
  
  const imageUrl = article.image || getFallbackImage(article.title)

  return (
    <Link 
      href={`/news/${encodeURIComponent(article.link)}`}
      className={`block bg-white rounded-2xl shadow-soft hover:shadow-professional transition-all duration-500 overflow-hidden group max-w-sm mx-auto transform hover:-translate-y-2 ${
        isLarge ? 'h-full' : ''
      }`}
    >
      <div className={`relative ${isLarge ? 'h-64' : 'h-48'} w-full overflow-hidden bg-gradient-to-br from-[#0A1A3A] via-[#112B54] to-[#1F3F7F]`}>
        <div className="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent z-10"></div>
        <Image
          src={imageUrl}
          alt={article.title}
          fill
          className="object-cover group-hover:scale-110 transition-transform duration-700"
          sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
        />
        {(article.is_trending || article.is_important) && (
          <div className="absolute top-4 right-4 z-20 flex gap-2">
            {article.is_trending && (
              <span className="bg-gradient-to-r from-[#4A6FF3] to-[#1F3F7F] text-white px-3 py-1.5 rounded-full text-xs font-bold shadow-lg backdrop-blur-sm">
                🔥 Trending
              </span>
            )}
            {article.is_important && (
              <span className="bg-gradient-to-r from-yellow-500 to-orange-500 text-white px-3 py-1.5 rounded-full text-xs font-bold shadow-lg backdrop-blur-sm">
                ⭐ Important
              </span>
            )}
          </div>
        )}
        <div className="absolute bottom-0 left-0 right-0 p-4 z-20">
          <span className={`${isLarge ? 'text-sm' : 'text-xs'} font-semibold text-white bg-black/30 backdrop-blur-sm px-3 py-1 rounded-full inline-block`}>
            {article.source}
          </span>
        </div>
      </div>
      
      <div className={`${isLarge ? 'p-6 flex flex-col h-full' : 'p-5'} bg-white`}>
        <div className="flex items-center justify-between mb-3">
          <span className="text-xs text-gray-500 font-medium">{formatDate(article.published_at)}</span>
        </div>
        
        <h3 className={`font-bold text-[#0A1A3A] mb-3 group-hover:text-[#4A6FF3] transition-colors duration-300 ${
          isLarge ? 'text-xl' : 'text-base'
        } line-clamp-2 leading-tight`}>
          {article.title}
        </h3>
        
        <p className={`text-gray-600 ${isLarge ? 'text-sm mb-4 flex-grow leading-relaxed' : 'text-xs leading-relaxed'} line-clamp-2`}>
          {article.description}
        </p>
        
        <div className={`${isLarge ? 'mt-auto pt-4' : 'mt-3'} flex items-center text-[#4A6FF3] font-semibold ${isLarge ? 'text-sm' : 'text-xs'} group-hover:gap-2 transition-all duration-300`}>
          <span>Read more</span>
          <span className="transform group-hover:translate-x-1 transition-transform duration-300">→</span>
        </div>
      </div>
    </Link>
  )
}

