# Step 4: User Journey and Internal Process Mapping

**Progress: Step 4 of 11** - Next: Actors, Roles & Domain Requirements

## MANDATORY EXECUTION RULES (READ FIRST):

- 🛑 NEVER generate content without user input

- 📖 CRITICAL: ALWAYS read the complete step file before taking any action - partial understanding leads to incomplete decisions
- 🔄 CRITICAL: When loading next step with 'C', ensure the entire file is read and understood before proceeding
- ✅ ALWAYS treat this as collaborative discovery between PM peers
- 📋 YOU ARE A FACILITATOR, not a content generator
- 💬 FOCUS on mapping ALL internal user types and business processes
- 🎯 CRITICAL: No journey/process = no functional requirements = product doesn't exist
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`
- ✅ YOU MUST ALWAYS WRITE all artifact and document content in `{document_output_language}`

## EXECUTION PROTOCOLS:

- 🎯 Show your analysis before taking any action
- ⚠️ Present A/P/C menu after generating journey content
- 💾 ONLY save when user chooses C (Continue)
- 📖 Update output file frontmatter, adding this step name to the end of the list of stepsCompleted
- 🚫 FORBIDDEN to load next step until C is selected

## CONTEXT BOUNDARIES:

- Current document and frontmatter from previous steps are available
- Purpose, vision, and scope already defined
- Focus on internal company workflows and users

## YOUR TASK:

Create compelling narrative user journeys and map internal business processes that reveal how the product will be used within the company.

## JOURNEY & PROCESS MAPPING SEQUENCE:

### 1. Identify Internal Users & Roles

**Discovery of Actors:**
Guide exploration of ALL internal roles that interact with the system:
- Primary internal users (employees, staff)
- Operational roles (admins, support, IT)
- Management/Stakeholders (viewers, approvers)
- Automated actors (internal integrations, cron jobs)

### 2. Map Internal Business Processes

Explore the "Process" — how work flows through the system:
- **Current State:** "How is this process handled today without the product?"
- **Future State:** "How will the product transform this internal workflow?"
- **Decision Points:** "Where are the critical human-in-the-loop decisions?"
- **Handoffs:** "How does work move from one role to another?"

### 3. Create Narrative Story-Based Journeys

For each key role, create narrative journeys that illustrate the process:

#### Narrative Journey Creation Process:
- **Role/Actor:** Who is performing the action?
- **Business Goal:** What internal objective are they trying to achieve?
- **Workflow Steps:** What are the specific actions they take in the system?
- **Outcome:** How does this step contribute to the overall business process?

### 4. Guide Journey Exploration

For each journey, facilitate detailed exploration:
- What happens at each step specifically?
- What internal rules or policies apply?
- What information do they need to see/hear to make decisions?
- Where are the potential bottlenecks in the process?

### 5. Connect Journeys/Processes to Requirements

Explicitly state:
- These journeys reveal requirements for specific internal capabilities
- Connect process needs to concrete features (audit logs, approval workflows, internal dashboards)

### 6. Generate Journey & Process Content

Prepare the content to append to the document:

#### Content Structure:

When saving to document, append these Level 2 and Level 3 sections:

```markdown
## User Journeys & Internal Processes

### Key Internal Workflows

[Description of mapped business processes based on conversation]

### Role-Based Narratives

[Journey narratives for each internal actor based on conversation]

### Process Requirements Summary

[Summary of capabilities revealed by processes/journeys]
```

### 7. Present MENU OPTIONS

Present the content for review, then display menu:

Display: "**Select:** [A] Advanced Elicitation [P] Party Mode [C] Continue to Actors, Roles & Domain Requirements (Step 5 of 11)"

#### Menu Handling Logic:
- IF A: Invoke the `bmad-advanced-elicitation` skill, process insights, update then redisplay menu
- IF P: Invoke the `bmad-party-mode` skill, process insights, update then redisplay menu
- IF C: Append final content to {outputFile}, update frontmatter, then read fully and follow: ./step-05-domain.md
- IF Any other: help user respond, then redisplay menu

#### EXECUTION RULES:
- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'

## APPEND TO DOCUMENT:

When user selects 'C', append the content directly to the document using the structure from step 6.

## SUCCESS METRICS:

✅ Internal roles and actors clearly identified
✅ Business processes mapped from current to future state
✅ Narrative journeys tell the story of internal work
✅ Process bottlenecks and decision points identified
✅ Minimum 3-4 journeys covering different internal roles
✅ A/P/C menu presented and handled correctly

## FAILURE MODES:

❌ Focus on external/public users instead of internal staff
❌ Missing operational or management roles
❌ Generic journeys that don't reflect actual business processes
❌ Not addressing how work flows between roles
❌ Not presenting A/P/C menu after content generation
❌ Appending content without user selecting 'C'

**Master Rule:** Focus on internal business processes and the people who run them. Narrative storytelling is key to revealing requirements.
