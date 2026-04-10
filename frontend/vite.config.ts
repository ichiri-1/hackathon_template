import { defineConfig } from 'vite'

export default defineConfig({
    server: {
        proxy: {
            '/api': "http://localhost:8000"
        }
    },
    build: {
        outDir: '../backend/static',
        emptyOutDir: true,
    }
})