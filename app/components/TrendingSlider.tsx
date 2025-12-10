'use client'

import { useRef } from 'react'
import NewsCard from './NewsCard'

interface TrendingSliderProps {
  articles: Array<{
    title: string
    description: string
    link: string
    source: string
    published_at: string
    image?: string
    is_trending?: boolean
    is_important?: boolean
  }>
}

export default function TrendingSlider({ articles }: TrendingSliderProps) {
  const scrollRef = useRef<HTMLDivElement>(null)

  const scroll = (direction: 'left' | 'right') => {
    if (scrollRef.current) {
      const scrollAmount = 400
      scrollRef.current.scrollBy({
        left: direction === 'left' ? -scrollAmount : scrollAmount,
        behavior: 'smooth'
      })
    }
  }

  return (
    <div className="relative group">
      <div 
        ref={scrollRef}
        className="flex gap-6 overflow-x-auto scrollbar-hide pb-6 scroll-smooth px-2"
        style={{ scrollbarWidth: 'none', msOverflowStyle: 'none' }}
      >
        {articles.slice(0, 10).map((article, index) => (
          <div 
            key={index} 
            className="flex-shrink-0 w-80 animate-fadeIn"
            style={{ animationDelay: `${index * 0.1}s` }}
          >
            <NewsCard article={article} variant="large" />
          </div>
        ))}
      </div>
      
      <button
        onClick={() => scroll('left')}
        className="absolute left-0 top-1/2 -translate-y-1/2 -translate-x-6 bg-gradient-to-r from-[#4A6FF3] to-[#1F3F7F] text-white p-4 rounded-full shadow-professional hover:shadow-lg hover:scale-110 transition-all duration-300 z-10 backdrop-blur-sm border-2 border-white/20 opacity-0 group-hover:opacity-100"
        aria-label="Scroll left"
      >
        <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M15 19l-7-7 7-7" />
        </svg>
      </button>
      
      <button
        onClick={() => scroll('right')}
        className="absolute right-0 top-1/2 -translate-y-1/2 translate-x-6 bg-gradient-to-r from-[#4A6FF3] to-[#1F3F7F] text-white p-4 rounded-full shadow-professional hover:shadow-lg hover:scale-110 transition-all duration-300 z-10 backdrop-blur-sm border-2 border-white/20 opacity-0 group-hover:opacity-100"
        aria-label="Scroll right"
      >
        <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M9 5l7 7-7 7" />
        </svg>
      </button>
    </div>
  )
}

