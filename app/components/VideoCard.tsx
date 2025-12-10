'use client'

import { useState } from 'react'
import Image from 'next/image'

interface VideoCardProps {
  video: {
    id: string
    title: string
    description: string
    thumbnail: string
    channel: string
    published_at: string
  }
}

export default function VideoCard({ video }: VideoCardProps) {
  const [showModal, setShowModal] = useState(false)

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

  return (
    <>
      <div 
        className="bg-white rounded-2xl shadow-soft hover:shadow-professional transition-all duration-500 overflow-hidden cursor-pointer group transform hover:-translate-y-2"
        onClick={() => setShowModal(true)}
      >
        <div className="relative h-52 w-full overflow-hidden bg-gradient-to-br from-[#0A1A3A] to-[#1F3F7F]">
          <Image
            src={video.thumbnail}
            alt={video.title}
            fill
            className="object-cover group-hover:scale-110 transition-transform duration-700"
            sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
          />
          <div className="absolute inset-0 bg-gradient-to-t from-black/70 via-transparent to-transparent"></div>
          <div className="absolute inset-0 flex items-center justify-center group-hover:scale-110 transition-transform duration-300">
            <div className="w-20 h-20 rounded-full bg-gradient-to-r from-[#4A6FF3] to-[#1F3F7F] flex items-center justify-center shadow-professional backdrop-blur-sm border-4 border-white/20 group-hover:scale-110 transition-transform duration-300">
              <svg className="w-10 h-10 text-white ml-1" fill="currentColor" viewBox="0 0 24 24">
                <path d="M8 5v14l11-7z"/>
              </svg>
            </div>
          </div>
          <div className="absolute bottom-0 left-0 right-0 p-4">
            <span className="text-xs font-semibold text-white bg-black/40 backdrop-blur-sm px-3 py-1.5 rounded-full">
              {video.channel}
            </span>
          </div>
        </div>
        
        <div className="p-5 bg-white">
          <div className="flex items-center justify-between mb-3">
            <span className="text-xs text-gray-500 font-medium">{formatDate(video.published_at)}</span>
          </div>
          
          <h3 className="font-bold text-[#0A1A3A] mb-3 group-hover:text-[#4A6FF3] transition-colors duration-300 line-clamp-2 leading-tight">
            {video.title}
          </h3>
          
          <p className="text-gray-600 text-sm line-clamp-2 leading-relaxed">
            {video.description}
          </p>
          
          <div className="mt-4 flex items-center text-[#4A6FF3] font-semibold text-xs group-hover:gap-2 transition-all duration-300">
            <span>Watch video</span>
            <span className="transform group-hover:translate-x-1 transition-transform duration-300">→</span>
          </div>
        </div>
      </div>

      {showModal && (
        <div 
          className="fixed inset-0 bg-black/80 backdrop-blur-sm z-50 flex items-center justify-center p-4 animate-fadeIn"
          onClick={() => setShowModal(false)}
        >
          <div 
            className="bg-white rounded-2xl max-w-5xl w-full p-8 shadow-professional animate-slideIn"
            onClick={(e) => e.stopPropagation()}
          >
            <div className="flex justify-between items-center mb-6">
              <h2 className="text-3xl font-bold text-[#0A1A3A] pr-4">{video.title}</h2>
              <button
                onClick={() => setShowModal(false)}
                className="text-gray-500 hover:text-gray-700 text-3xl w-10 h-10 flex items-center justify-center rounded-full hover:bg-gray-100 transition-colors duration-300 flex-shrink-0"
                aria-label="Close modal"
              >
                ×
              </button>
            </div>
            
            <div className="aspect-video w-full rounded-xl overflow-hidden shadow-professional bg-black">
              <iframe
                src={`https://www.youtube.com/embed/${video.id}?autoplay=1`}
                title={video.title}
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowFullScreen
                className="w-full h-full"
              />
            </div>
            
            <div className="mt-6 pt-6 border-t border-gray-200">
              <p className="text-gray-700 leading-relaxed mb-3">{video.description}</p>
              <div className="flex items-center gap-4 text-sm text-gray-500">
                <span className="font-semibold text-[#4A6FF3]">Channel:</span>
                <span>{video.channel}</span>
                <span className="mx-2">•</span>
                <span>{formatDate(video.published_at)}</span>
              </div>
            </div>
          </div>
        </div>
      )}
    </>
  )
}

