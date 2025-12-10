import TrendingSlider from './components/TrendingSlider'
import NewsGrid from './components/NewsGrid'
import NewsList from './components/NewsList'
import BackendStatus from './components/BackendStatus'

export default async function Home() {
  const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

  let trending = { articles: [], error: '' }
  let important = { articles: [], error: '' }
  let all = { articles: [], error: '' }
  let backendConnected = false

  try {
    // First check if backend is reachable
    try {
      const controller = new AbortController()
      const timeoutId = setTimeout(() => controller.abort(), 5000)
      const healthCheck = await fetch(`${apiUrl}/health`, { 
        cache: 'no-store',
        signal: controller.signal
      })
      clearTimeout(timeoutId)
      backendConnected = healthCheck.ok
    } catch {
      backendConnected = false
    }

    if (backendConnected) {
      // Fetch data with better error handling
      const createFetchWithTimeout = (url: string, timeout: number = 10000) => {
        const controller = new AbortController()
        const timeoutId = setTimeout(() => controller.abort(), timeout)
        return fetch(url, { 
          next: { revalidate: 300 },
          signal: controller.signal
        }).finally(() => clearTimeout(timeoutId))
      }

      const [trendingRes, importantRes, allRes] = await Promise.allSettled([
        createFetchWithTimeout(`${apiUrl}/news/trending`),
        createFetchWithTimeout(`${apiUrl}/news/important`),
        createFetchWithTimeout(`${apiUrl}/news/all`),
      ])

      if (trendingRes.status === 'fulfilled' && trendingRes.value.ok) {
        trending = await trendingRes.value.json().catch(() => ({ articles: [], error: 'Failed to parse trending news' }))
      } else if (trendingRes.status === 'rejected') {
        trending.error = trendingRes.reason?.message || 'Failed to fetch trending news'
      }
      
      if (importantRes.status === 'fulfilled' && importantRes.value.ok) {
        important = await importantRes.value.json().catch(() => ({ articles: [], error: 'Failed to parse important news' }))
      } else if (importantRes.status === 'rejected') {
        important.error = importantRes.reason?.message || 'Failed to fetch important news'
      }
      
      if (allRes.status === 'fulfilled' && allRes.value.ok) {
        all = await allRes.value.json().catch(() => ({ articles: [], error: 'Failed to parse all news' }))
      } else if (allRes.status === 'rejected') {
        all.error = allRes.reason?.message || 'Failed to fetch all news'
      }
    }
  } catch (error: any) {
    console.error('Error fetching news:', error)
    if (!trending.error) trending.error = error.message || 'Unknown error'
    if (!important.error) important.error = error.message || 'Unknown error'
    if (!all.error) all.error = error.message || 'Unknown error'
  }

  return (
    <div className="container mx-auto px-8 md:px-12 lg:px-16 py-8">
      {/* Backend Status Banner */}
      {!backendConnected && (
        <BackendStatus apiUrl={apiUrl} />
      )}

      {/* Hero Section - Always visible */}
      <div className="text-center mb-16 animate-fadeIn">
        <div className="inline-block mb-6">
          <span className="text-sm font-semibold text-[#4A6FF3] bg-[#EEF2FF] px-4 py-2 rounded-full">
            Latest AI Intelligence
          </span>
        </div>
        <h1 className="text-6xl md:text-7xl font-extrabold mb-6 bg-gradient-to-r from-[#0A1A3A] via-[#1F3F7F] to-[#4A6FF3] bg-clip-text text-transparent leading-tight">
          AI News Hub
        </h1>
        <p className="text-xl md:text-2xl text-[#1F3F7F] max-w-3xl mx-auto leading-relaxed font-light">
          Stay updated with the latest AI news, breakthroughs, and research from top sources around the world
        </p>
      </div>

      {/* Trending Slider */}
      <section className="mb-20 animate-slideIn">
        <div className="flex items-center gap-3 mb-8">
          <div className="h-1 w-12 bg-gradient-to-r from-[#4A6FF3] to-[#1F3F7F] rounded-full"></div>
          <h2 className="text-4xl font-bold text-[#0A1A3A]">🔥 Trending Now</h2>
          <div className="flex-1 h-1 bg-gradient-to-r from-[#4A6FF3] to-transparent rounded-full"></div>
        </div>
        {trending.articles && trending.articles.length > 0 ? (
          <TrendingSlider articles={trending.articles.slice(0, 15)} />
        ) : (
          <div className="text-center py-12 bg-white rounded-xl shadow-md">
            <div className="inline-block animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-[#4A6FF3] mb-4"></div>
            <p className="text-gray-600">Loading trending news...</p>
            {trending.error && (
              <p className="text-sm text-red-500 mt-2">Error: {trending.error}</p>
            )}
            {!backendConnected && (
              <p className="text-sm text-orange-500 mt-2">⚠️ Backend server not connected. Please start the backend server.</p>
            )}
          </div>
        )}
      </section>

      {/* Important News Grid */}
      <section className="mb-20 animate-slideIn">
        <div className="flex items-center gap-3 mb-8">
          <div className="h-1 w-12 bg-gradient-to-r from-yellow-500 to-orange-500 rounded-full"></div>
          <h2 className="text-4xl font-bold text-[#0A1A3A]">⭐ Important News</h2>
          <div className="flex-1 h-1 bg-gradient-to-r from-yellow-500 to-transparent rounded-full"></div>
        </div>
        {important.articles && important.articles.length > 0 ? (
          <NewsGrid articles={important.articles.slice(0, 6)} />
        ) : (
          <div className="text-center py-12 bg-white rounded-xl shadow-md">
            <div className="inline-block animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-[#4A6FF3] mb-4"></div>
            <p className="text-gray-600">Loading important news...</p>
            {important.error && (
              <p className="text-sm text-red-500 mt-2">Error: {important.error}</p>
            )}
          </div>
        )}
      </section>

      {/* All News List */}
      <section className="mb-20 animate-slideIn">
        <div className="flex items-center gap-3 mb-8">
          <div className="h-1 w-12 bg-gradient-to-r from-[#4A6FF3] to-[#1F3F7F] rounded-full"></div>
          <h2 className="text-4xl font-bold text-[#0A1A3A]">📰 All News</h2>
          <div className="flex-1 h-1 bg-gradient-to-r from-[#4A6FF3] to-transparent rounded-full"></div>
        </div>
        {all.articles && all.articles.length > 0 ? (
          <NewsList articles={all.articles} />
        ) : (
          <div className="text-center py-12 bg-white rounded-xl shadow-md">
            <div className="inline-block animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-[#4A6FF3] mb-4"></div>
            <p className="text-gray-600">Loading news articles...</p>
            {all.error && (
              <p className="text-sm text-red-500 mt-2">Error: {all.error}</p>
            )}
            {!backendConnected && (
              <p className="text-sm text-orange-500 mt-2">⚠️ Backend server not connected. Please start the backend server on port 8000</p>
            )}
          </div>
        )}
      </section>
    </div>
  )
}

