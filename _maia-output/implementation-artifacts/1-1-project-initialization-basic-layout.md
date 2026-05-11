# Story 1.1: Project Initialization & Basic Layout

Status: ready-for-dev

## Story

As a Developer,
I want to set up the React project with the Ambient HUD layout,
so that I have a foundation for the sanctuary.

## Acceptance Criteria

1. **Given** a new project directory, **When** I initialize the project with Vite, TypeScript, and TailwindCSS, **Then** the environment is ready for development. (AC: 1)
2. **Given** the application is loaded, **When** I view the main page, **Then** the basic "Ambient HUD" layout is visible with a centered timer placeholder. (AC: 2)
3. **Given** any layout element, **When** I inspect the spacing, **Then** the 8px grid system is applied (margins, padding). (AC: 3)
4. **Given** the HUD panels, **When** rendered, **Then** they feature glassmorphism effects (backdrop-blur, semi-transparent backgrounds). (AC: 4)
5. **Given** the text elements, **When** rendered, **Then** the Inter typeface is applied with the correct hierarchy. (AC: 5)

## Tasks / Subtasks

- [ ] **Project Setup** (AC: 1)
  - [ ] Initialize Vite project: `npm create vite@latest . -- --template react-ts`
  - [ ] Install dependencies: `npm install`
  - [ ] Install and configure TailwindCSS: `npm install -D tailwindcss postcss autoprefixer && npx tailwindcss init -p`
  - [ ] Configure `tailwind.config.js` to include Inter font and custom spacing.
- [ ] **Base Layout Implementation** (AC: 2, 3, 4)
  - [ ] Create `App.tsx` with a full-screen, relative background.
  - [ ] Implement a centered container for the "Ambient HUD".
  - [ ] Add glassmorphism panel styles to `index.css` or Tailwind classes.
  - [ ] Implement the 8px grid system using Tailwind's spacing scale (e.g., `p-2`, `m-4`).
- [ ] **Placeholder Components** (AC: 2, 5)
  - [ ] Create a `Timer` component placeholder with "25:00" text.
  - [ ] Apply Inter font hierarchy (H1: 3.5rem for timer).
  - [ ] Add basic HUD controls placeholders (Mixer, Themes).

## Dev Notes

- **Tech Stack**: React 18, Vite, TypeScript, TailwindCSS.
- **UI/UX Patterns**:
  - "Ambient HUD" layout: Centered timer, edge-anchored controls.
  - Glassmorphism: `backdrop-blur-md`, `bg-white/10`, `border border-white/20`.
  - 8px Grid: Consistent spacing following the UX spec.
- **Font**: Inter (Sans-serif). Need to import from Google Fonts or local.
- **Colors (Midnight Theme Default)**:
  - Background: `#0F172A`
  - Text: `#F8FAFC`
  - Accents: `#38BDF8`

### Project Structure Notes

- `src/components`: Reusable UI components (Timer, Mixer, ThemeToggle).
- `src/styles`: Custom CSS if needed beyond Tailwind.
- `src/assets`: Audio files and static assets.

### References

- [Source: _maia-output/planning-artifacts/ux-design-specification.md#Visual Design Foundation]
- [Source: _maia-output/planning-artifacts/epics.md#Story 1.1]

## Dev Agent Record

### Agent Model Used

### Debug Log References

### Completion Notes List

### File List
