## Description

This is the documentation for setting up [melanoma-scan](https://github.com/melanoma-scan-site/melanoma-scan/) for development and production deployment.

The purpose of the frontend is to serve a web application ([melanoma-scan.site](https://melanoma-scan.site/)) that allows people to upload or take a picture with their phone, have an AI predict whether the person has melanoma, and then view the AI results along with a disclaimer and an option to download the results as a PDF.

## Tech stack

- [Svelte](https://svelte.dev/) - Framework for building fast and reactive web applications.
- [SvelteKit](https://kit.svelte.dev/) - Full-stack framework for Svelte with routing and SSR.
- [Tailwind CSS](https://tailwindcss.com/) - CSS framework for easier and better CSS styling.
- [shadcn-svelte](https://www.shadcn-svelte.com/) - shadcn UI component library ported to Svelte, styled with Tailwind CSS.
- [Lucide icons](https://lucide.dev/) - Open-source, customizable, icon library.
- [jsPDF](https://github.com/parallax/jsPDF) - JavaScript library for generating PDF documents.
- [LayerChart](https://www.layerchart.com/) - Interactive charting library for visualizing data.

## File structure

```
├── components.json        # UI component configurations for shadcn
├── jsconfig.json          # JavaScript configuration for editor/IDE settings
├── package.json           # Project dependencies and scripts
├── package-lock.json      # Lock file for npm dependencies
├── pnpm-lock.yaml         # Lock file for pnpm dependencies
├── postcss.config.js      # PostCSS configuration for CSS processing
├── README.md              # Project documentation
├── src                    # Source code directory
│   ├── app.css            # Global CSS styles
│   ├── app.html           # Main HTML template
│   ├── lib                # Library/shared code directory
│   │   ├── components     # Reusable components directory
│   │   │   ├── app        # Application-specific components
│   │   │   └── ui         # shadcn UI components
│   │   └── utils.js       # Utility/helper functions
│   └── routes             # SvelteKit routing directory
│       ├── +layout.svelte # Root layout component
│       └── +page.svelte   # Root page component
├── static                 # Static assets directory
│   └── favicon.png        # Browser favicon/icon
├── svelte.config.js       # SvelteKit configuration
├── tailwind.config.js     # Tailwind CSS configuration
└── vite.config.js         # Vite bundler configuration

```

## Setup for development

To clone the project in order to get the files onto your computer:

> **Note:** If you don't have Node.js installed, you can download and install it from [here](https://nodejs.org/en/download/).

```bash
git clone https://github.com/melanoma-scan-site/melanoma-scan
cd melanoma-scan/frontend/app/
npm install
```

```bash
npm run dev
```

## Setup for production

To clone the project in order to get the files onto your computer:

> **Note:** If you don't have Node.js installed, you can download and install it from [here](https://nodejs.org/en/download/).

```bash
git clone https://github.com/melanoma-scan-site/melanoma-scan
cd melanoma-scan/frontend/app/
npm install
```

To create a compiled version of the project:

```bash
npm run build
```

Run the compiled version of the project

```bash
node index.js
```

## Miscellaneous

> Authors:

- [Jesper Nielsen](mailto:jeni.skp@edu.mercantec.dk?subject=melanoma-scan)
