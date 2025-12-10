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
    },
  },
  plugins: [],
}

