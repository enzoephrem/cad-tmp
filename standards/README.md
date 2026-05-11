# Company Standards Knowledge Base

This directory contains the definitive, company-wide standards for architectures, best practices, validated code snippets, and operational guidelines. Everything lives here in the monorepo, making it instantly accessible to developers, AI agents, and internal scripts.

## How It Works

Every standard in this directory is written in Markdown and MUST include a YAML frontmatter block. This structured metadata allows our scaffolding scripts and AI agents (like Maia/BMAD) to query, filter, and apply the rules precisely where they belong, without overwhelming the context window.

### Directory Structure

- **`/cross-cutting/`**: Universal standards applicable to any project (e.g., Git strategies, CI/CD, Secrets, Error Handling).
- **`/stacks/`**: Language/framework-specific implementations (e.g., FastAPI, .NET, React).
- **`/integrations/`**: Specific third-party or infrastructure patterns (e.g., Azure OpenAI, Azure Search, Database ORMs).

### The Standard Template

If you are adding a new standard, copy the frontmatter format below:

```yaml
---
id: unique-standard-identifier
title: Human Readable Title
tags: [fastapi, backend, security, azure]
applies_to_phase: [architecture, implementation, testing, review]
version: 1.0
---
```

## Usage in Workflows

1. **AI Context (Agentic Use):** When an agent is asked to "add an API in FastAPI", it will automatically parse the `standards/stacks/fastapi/` directory and inject the relevant constraints into its system prompt before writing code.
2. **Scaffolding:** Internal scripts can parse the YAML tags to copy relevant snippets or generate specific `.cursorrules` payloads for different modules of the codebase.
