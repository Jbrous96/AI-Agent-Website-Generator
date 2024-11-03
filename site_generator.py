import os
import time
import subprocess
from dataclasses import dataclass

@dataclass
class SiteConfig:
    name: str
    type: str

class TestedGenerator:
    def __init__(self):
        self.types = ["portfolio", "dashboard", "landing"]
    
    def create_website(self, site_type: str):
        name = f"{site_type}-{int(time.time())}"
        print(f"\n🚀 Creating {site_type} website: {name}")
        
        try:
            # Create Next.js project
            subprocess.run([
                'npx',
                'create-next-app@latest',
                name,
                '--typescript',
                '--tailwind',
                '--eslint',
                '--app',
                '--src-dir'
            ], check=True)
            
            os.chdir(name)
            
            # Install framer-motion
            print("\n📦 Installing dependencies...")
            subprocess.run([
                'npm',
                'install',
                'framer-motion@latest',
                '--legacy-peer-deps'
            ], check=True)
            
            # Create component directory
            os.makedirs('src/components', exist_ok=True)
            
            # Create the page component
            with open('src/app/page.tsx', 'w') as f:
                f.write('''
import MainContent from '@/components/MainContent'

export default function Home() {
  return (
    <MainContent />
  )
}
''')

            # Create the main content component
            with open('src/components/MainContent.tsx', 'w') as f:
                f.write('''
'use client'

import { motion } from 'framer-motion'

export default function MainContent() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-600 to-blue-600">
      <main className="container mx-auto px-4 py-20">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          className="text-center"
        >
          <h1 className="text-6xl md:text-8xl font-bold text-white mb-8">
            Creative Vision
          </h1>
          <p className="text-xl md:text-2xl text-white/80 mb-12">
            Experience the future of web design
          </p>
        </motion.div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mt-20">
          <motion.div
            whileHover={{ scale: 1.05 }}
            className="bg-white/10 backdrop-blur-lg rounded-lg p-8 text-white"
          >
            <h3 className="text-2xl font-bold mb-4">Modern Design</h3>
            <p className="text-white/80">Clean, beautiful, and responsive interfaces.</p>
          </motion.div>

          <motion.div
            whileHover={{ scale: 1.05 }}
            className="bg-white/10 backdrop-blur-lg rounded-lg p-8 text-white"
          >
            <h3 className="text-2xl font-bold mb-4">Animation</h3>
            <p className="text-white/80">Smooth, engaging motion design.</p>
          </motion.div>

          <motion.div
            whileHover={{ scale: 1.05 }}
            className="bg-white/10 backdrop-blur-lg rounded-lg p-8 text-white"
          >
            <h3 className="text-2xl font-bold mb-4">Performance</h3>
            <p className="text-white/80">Lightning-fast load times and interactions.</p>
          </motion.div>
        </div>

        <motion.div
          whileHover={{ scale: 1.05 }}
          className="mt-20 text-center"
        >
          <button className="bg-white text-black px-8 py-4 rounded-full text-xl font-bold hover:bg-opacity-90 transition-all">
            Get Started
          </button>
        </motion.div>
      </main>
    </div>
  )
}
''')
            
            print(f"\n✅ Website {name} created successfully!")
            print(f"\nTo view your site:")
            print(f"1. cd {name}")
            print(f"2. npm run dev")
            print(f"3. Open http://localhost:3000")
            
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return False
        
        return True

def main():
    generator = TestedGenerator()
    
    print("🎨 Website Generator")
    print("\nChoose website type:")
    print("1. Portfolio")
    print("2. Dashboard")
    print("3. Landing Page")
    
    choice = input("\nEnter number (1-3): ")
    site_type = generator.types[int(choice) - 1]
    
    generator.create_website(site_type)

if __name__ == "__main__":
    main()