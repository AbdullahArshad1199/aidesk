/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        'navy-primary': '#0A1A3A',
        'navy-secondary': '#112B54',
        'navy-tertiary': '#1F3F7F',
        'accent-blue': '#4A6FF3',
        'light-bg': '#EEF2FF',
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
      },
      animation: {
        'fade-in': 'fadeIn 0.6s ease-out',
        'slide-in': 'slideIn 0.5s ease-out',
        'shimmer': 'shimmer 2s infinite',
      },
      boxShadow: {
        'soft': '0 2px 15px -3px rgba(0, 0, 0, 0.07), 0 10px 20px -2px rgba(0, 0, 0, 0.04)',
        'professional': '0 10px 40px -10px rgba(10, 26, 58, 0.2)',
      },
    },
  },
  plugins: [],
}

