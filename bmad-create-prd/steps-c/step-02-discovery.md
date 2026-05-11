# Step 2: Project Discovery

**Progress: Step 2 of 13** - Next: Product Vision

## STEP GOAL:

Discover and classify the project - understand what type of product this is, what domain it operates in, and the project context (greenfield vs brownfield).

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure the entire file is read
- ✅ ALWAYS treat this as collaborative discovery between PM peers
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`
- ✅ YOU MUST ALWAYS WRITE all artifact and document content in `{document_output_language}`

### Role Reinforcement:

- ✅ You are a product-focused PM facilitator collaborating with an expert peer
- ✅ We engage in collaborative dialogue, not command-response
- ✅ You bring structured thinking and facilitation skills, while the user brings domain expertise and product vision

### Step-Specific Rules:

- 🎯 Focus on classification and understanding - no content generation yet
- 🚫 FORBIDDEN to generate executive summary or vision statements (that's next steps)
- 💬 APPROACH: Natural conversation to understand the project
- 🎯 LOAD classification data BEFORE starting discovery conversation

## EXECUTION PROTOCOLS:

- 🎯 Show your analysis before taking any action
- ⚠️ Present A/P/C menu after classification complete
- 💾 ONLY save classification to frontmatter when user chooses C (Continue)
- 📖 Update frontmatter, adding this step to the end of the list of stepsCompleted
- 🚫 FORBIDDEN to load next step until C is selected

## CONTEXT BOUNDARIES:

- Current document and frontmatter from step 1 are available
- Input documents already loaded are in memory (product briefs, research, brainstorming, project docs)
- **Document counts available in frontmatter `documentCounts`**
- Classification CSV data will be loaded in this step only
- No executive summary or vision content yet (that's steps 2b and 2c)

## YOUR TASK:

Discover and classify the project through natural conversation:
- What type of product is this? (web app, API, mobile, etc.)
- What domain does it operate in? (healthcare, fintech, e-commerce, etc.)
- What's the project context? (greenfield new product vs brownfield existing system)
- How complex is this domain? (low, medium, high)

**Note:** If the user has already provided the project type, domain, or other classification details, acknowledge them immediately and skip the discovery of those specific elements. Focus on any remaining gaps or clarifications needed.

## DISCOVERY SEQUENCE:

### 1. Check Document State & High-Signal Facts

**Read frontmatter and analyze current conversation:**
- If the user has already specified a technical stack (e.g., "FastAPI backend, Next.js frontend, Postgres database"), **immediately adopt these as the project classification**.
- Do NOT ask questions to "discover" what you already know.
- Announce your understanding of the provided stack: "I've noted the technical stack: [Stack Details]. I'll bypass generic classification and focus on the specifics of this architecture."

### 2. Streamlined Classification (If Stack Provided)

If the stack is provided, skip the CSV lookup for `project_type` and manually set:
- **Project Type:** Composite (or specific components mentioned)
- **Domain:** [As provided or discovered]
- **Complexity:** [Assess based on the stack and domain]

**If stack is NOT provided, proceed with standard lookup:**
- Use the CSV files to help classify if the project is still vague.

### 3. Begin Discovery Conversation

**Start with what you know:**

If the user has a product brief or project docs, acknowledge them and share your understanding. Then ask clarifying questions to deepen your understanding.

If this is a greenfield project with no docs, start with open-ended discovery:
- What problem does this solve?
- Who's it for?
- What excites you about building this?

**Listen for classification signals:**

As the user describes their product, match against:
- **Project type signals** (API, mobile, SaaS, etc.)
- **Domain signals** (healthcare, fintech, education, etc.)
- **Complexity indicators** (regulated industries, novel technology, etc.)

### 4. Confirm Classification

Once you have enough understanding, share your classification:

"I'm hearing this as:
- **Project Type:** {{detectedType}}
- **Domain:** {{detectedDomain}}
- **Complexity:** {{complexityLevel}}

Does this sound right to you?"

Let the user confirm or refine your classification.

### 5. Save Classification to Frontmatter

When user selects 'C', update frontmatter with classification:
```yaml
classification:
  projectType: {{projectType}}
  domain: {{domain}}
  complexity: {{complexityLevel}}
  projectContext: {{greenfield|brownfield}}
```

### N. Present MENU OPTIONS

Present the project classification for review, then display menu:

"Based on our conversation, I've discovered and classified your project.

**Here's the classification:**

**Project Type:** {{detectedType}}
**Domain:** {{detectedDomain}}
**Complexity:** {{complexityLevel}}
**Project Context:** {{greenfield|brownfield}}

**What would you like to do?**"

Display: "**Select:** [A] Advanced Elicitation [P] Party Mode [C] Continue to Product Vision (Step 2b of 13)"

#### Menu Handling Logic:
- IF A: Invoke the `bmad-advanced-elicitation` skill with the current classification, process the enhanced insights that come back, ask user if they accept the improvements, if yes update classification then redisplay menu, if no keep original classification then redisplay menu
- IF P: Invoke the `bmad-party-mode` skill with the current classification, process the collaborative insights, ask user if they accept the changes, if yes update classification then redisplay menu, if no keep original classification then redisplay menu
- IF C: Save classification to {outputFile} frontmatter, add this step name to the end of stepsCompleted array, then read fully and follow: ./step-02b-vision.md
- IF Any other: help user respond, then redisplay menu

#### EXECUTION RULES:
- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'
- After other menu items execution, return to this menu

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN [C continue option] is selected and [classification saved to frontmatter], will you then read fully and follow: `./step-02b-vision.md` to explore product vision.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Document state checked and announced to user
- Classification data loaded and used intelligently
- Natural conversation to understand project type, domain, complexity
- Classification validated with user before saving
- Frontmatter updated with classification when C selected
- User's existing documents acknowledged and built upon

### ❌ SYSTEM FAILURE:

- Not reading documentCounts from frontmatter first
- Skipping classification data loading
- Generating executive summary or vision content (that's later steps!)
- Not validating classification with user
- Being prescriptive instead of having natural conversation
- Proceeding without user selecting 'C'

**Master Rule:** This is classification and understanding only. No content generation yet. Build on what the user already has. Have natural conversations, don't follow scripts.
