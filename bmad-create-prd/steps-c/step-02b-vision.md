# Step 2b: Purpose and Product Vision Discovery

**Progress: Step 2b of 13** - Next: Executive Summary

## STEP GOAL:

Discover the core purpose and vision for this internal product. Understand why the company needs it and what success looks like for internal stakeholders.

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

- 🎯 Focus on discovering purpose, vision and value to the company — no content generation yet
- 🚫 FORBIDDEN to generate executive summary content (that's the next step)
- 🚫 FORBIDDEN to append anything to the document in this step
- 💬 APPROACH: Natural conversation to understand the business need and vision
- 🎯 BUILD ON classification insights from step 2

## EXECUTION PROTOCOLS:

- 🎯 Show your analysis before taking any action
- ⚠️ Present A/P/C menu after vision discovery is complete
- 📖 Update frontmatter, adding this step to the end of the list of stepsCompleted
- 🚫 FORBIDDEN to load next step until C is selected

## CONTEXT BOUNDARIES:

- Current document and frontmatter from steps 1 and 2 are available
- Project classification exists from step 2 (project type, domain, complexity, context)
- Input documents already loaded are in memory (product briefs, research, brainstorming, project docs)
- No executive summary content yet (that's step 2c)
- This step ONLY discovers — it does NOT write to the document

## YOUR TASK:

Discover the product purpose and vision through natural conversation. Understand the internal business value before any content is written.

## VISION DISCOVERY SEQUENCE:

### 1. Acknowledge Classification Context

Reference the classification from step 2 and use it to frame the conversation:

"We've established this is a {{projectType}} in the {{domain}} domain. Now let's explore the core purpose and vision for this internal product."

### 2. Explore the Core Purpose

Guide the conversation to uncover why this product is being built for the company:

- **Business Need:** "What's the primary problem this solves for the company?"
- **Internal Impact:** "How will this change the way internal teams work?"
- **Efficiency/Value:** "What's the main efficiency gain or value this brings to our internal operations?"
- **Purpose Statement:** "If you had one sentence to explain why the company is investing in this, what would it be?"

### 3. Understand the Vision

Dig deeper into the long-term goal:

- **Future State:** "When this product is fully operational, what does success look like for our internal processes?"
- **Alignment:** "How does this align with our broader company goals or department objectives?"
- **Why Now:** "Why is this the priority for the company at this moment?"

### 4. Validate Understanding

Reflect back what you've heard and confirm:

"Here's what I'm hearing about the purpose and vision:

**Purpose:** {{summarized_purpose}}
**Vision:** {{summarized_vision}}
**Core Internal Value:** {{summarized_value}}

Does this capture it? Anything I'm missing?"

Let the user confirm or refine your understanding.

### N. Present MENU OPTIONS

Present your understanding for review, then display menu:

"Based on our conversation, I have a clear picture of the purpose and vision. I'll use these insights to draft the Executive Summary in the next step.

**What would you like to do?**"

Display: "**Select:** [A] Advanced Elicitation [P] Party Mode [C] Continue to Executive Summary (Step 2c of 13)"

#### Menu Handling Logic:
- IF A: Invoke the `bmad-advanced-elicitation` skill with the current vision insights, process the enhanced insights that come back, ask user if they accept the improvements, if yes update understanding then redisplay menu, if no keep original understanding then redisplay menu
- IF P: Invoke the `bmad-party-mode` skill with the current vision insights, process the collaborative insights, ask user if they accept the changes, if yes update understanding then redisplay menu, if no keep original understanding then redisplay menu
- IF C: Update {outputFile} frontmatter by adding this step name to the end of stepsCompleted array, then read fully and follow: ./step-02c-executive-summary.md
- IF Any other: help user respond, then redisplay menu

#### EXECUTION RULES:
- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'
- After other menu items execution, return to this menu

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN [C continue option] is selected and [stepsCompleted updated], will you then read fully and follow: `./step-02c-executive-summary.md` to generate the Executive Summary.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Classification context from step 2 acknowledged and built upon
- Natural conversation to understand purpose and vision
- User's existing documents leveraged for insights
- Purpose and vision validated with user before proceeding
- Clear focus on internal business value
- Frontmatter updated with stepsCompleted when C selected

### ❌ SYSTEM FAILURE:

- Using "market" or "public" facing terminology
- Generating executive summary or any document content (that's step 2c!)
- Appending anything to the PRD document
- Not building on classification from step 2
- Being prescriptive instead of having natural conversation
- Proceeding without user selecting 'C'

**Master Rule:** This step is purpose and vision discovery only. Focus on internal value. No content generation, no document writing.
