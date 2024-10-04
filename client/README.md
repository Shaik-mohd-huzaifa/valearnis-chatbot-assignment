# Vite + React App

This project is a **Vite** powered **React** application, designed for fast development with modern frontend tooling. Vite provides a lightning-fast development experience with minimal configuration.

## Features

- ⚡ **Vite** for fast development and build process
- ⚛️ **React** for building dynamic user interfaces
- 📦 **ESM-based** project with minimal bundling
- 🚀 Instant hot module replacement (HMR) during development
- 🌈 Easy to extend and configure

## Prerequisites

Make sure you have the following installed on your system:

- **Node.js** (>=14.18.0 or >=16.0.0)
- **npm** or **yarn** package manager

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Shaik-mohd-huzaifa/valearnis-chatbot-assignment.git
cd client
```

### 2. Install Dependencies

Install the required dependencies using your package manager:

```bash
# Using npm
npm install

# OR using yarn
yarn install
```

### 3. Run the Development Server

Start the development server with hot-reloading:

```bash
# Using npm
npm run dev

# OR using yarn
yarn dev
```

Your app should now be running on [http://localhost:5173](http://localhost:5173).

### 4. Build for Production

To create a production-ready build of your app:

```bash
# Using npm
npm run build

# OR using yarn
yarn build
```

The build will be generated in the `dist` folder.

### 5. Preview the Production Build

You can preview the production build locally by running:

```bash
# Using npm
npm run preview

# OR using yarn
yarn preview
```

This will serve the app on [http://localhost:8000](http://localhost:8000) to preview the production build.

## Project Structure

```
├── public              # Static assets
├── src                 # Main source folder
│   ├── assets          # Asset files (images, icons, etc.)
│   ├── components      # React components
|   ├── Store           # Redux Store
|   ├── Utils           # API calling Functions
│   ├── App.jsx         # Root component
│   └── main.jsx        # Entry point of the app
├── index.html          # Main HTML file
├── package.json        # Project dependencies and scripts
└── vite.config.js      # Vite configuration file
```

## Available Scripts

- **`npm run dev`**: Run the development server
- **`npm run build`**: Create a production build
- **`npm run preview`**: Preview the production build locally
- **`npm run lint`**: Lint the code (if applicable)
- **`npm run test`**: Run tests (if applicable)

## Learn More

To learn more about Vite and React, take a look at the following resources:

- [Vite Documentation](https://vitejs.dev/)
- [React Documentation](https://reactjs.org/)
