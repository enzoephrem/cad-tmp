# Step 9: Functional Requirements & Feature Synthesis

**Progress: Step 9 of 11** - Next: Non-Functional Requirements

## MANDATORY EXECUTION RULES (READ FIRST):

- 🛑 NEVER generate content without user input

- 📖 CRITICAL: ALWAYS read the complete step file before taking any action - partial understanding leads to incomplete decisions
- 🔄 CRITICAL: When loading next step with 'C', ensure the entire file is read and understood before proceeding
- ✅ ALWAYS treat this as collaborative discovery between PM peers
- 📋 YOU ARE A FACILITATOR, not a content generator
- 💬 FOCUS on creating a comprehensive inventory of Features and their Functional Requirements
- 🎯 CRITICAL: This is THE CAPABILITY CONTRACT for all downstream work (Architecture, Stories, Tickets)
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`
- ✅ YOU MUST ALWAYS WRITE all artifact and document content in `{document_output_language}`

## EXECUTION PROTOCOLS:

- 🎯 Show your analysis before taking any action
- ⚠️ Present A/P/C menu after generating features and functional requirements
- 💾 ONLY save when user chooses C (Continue)
- 📖 Update output file frontmatter, adding this step name to the end of the list of stepsCompleted
- 🚫 FORBIDDEN to load next step until C is selected

## CONTEXT BOUNDARIES:

- Current document and frontmatter from previous steps are available
- ALL previous content (executive summary, purpose, journeys, internal processes) must be referenced
- Focus on Features as modules of value proposition

## CRITICAL IMPORTANCE:

**This section defines THE CAPABILITY CONTRACT for the entire product:**

- Architects will map these **Features** to components and boundaries
- **Features** will be broken down into **User Stories**
- **User Stories** will be broken down into **Implementation Tickets**
- If a capability is missing from the FRs within a Feature, it will NOT exist in the final product

## FEATURE & FR SYNTHESIS SEQUENCE:

### 1. Understand Feature-Driven Requirements

Start by explaining the role of Features and Functional Requirements:

**Feature:**
A Feature is a logical grouping of Functional Requirements that represents a specific module of value proposition for the internal user or the company.

**Functional Requirement (FR):**
FRs define the specific testable capabilities within a Feature. They specify WHO and WHAT, not HOW.

**How They Will Be Used:**
1. Architect reads **Features** → maps them to components/modules
2. PM/Strategist reads **Features** → breaks them into **User Stories**
3. Dev Architect reads **User Stories** → breaks them into **Implementation Tickets**

### 2. Review Existing Content for Feature Extraction

Systematically review all previous sections to extract Features and their underlying FRs:

**Extract From:**
- Purpose & Vision → Core high-level Features
- User Journeys & Internal Processes → Workflow-based Features
- Actors & Roles → Role-specific Features and FRs
- Internal Innovation & Efficiency → Performance and automation Features

### 3. Organize Requirements by Feature

Group FRs by logical **Features** (modules of value proposition):

**Target 5-10 Features** for typical projects. Each Feature should have a clear "Value Proposition" for the company.

### 4. Generate Comprehensive Feature & FR List

Create the list using this format:

**Format:**
**Feature: [Feature Name]**
*Value Proposition: [One sentence on the business value]*
- FR1: [Actor] can [capability] [context/constraint]
- FR2: [Actor] can [capability]
- ...

### 5. Self-Validation Process

Before presenting to user, validate:
1. "Does every FR belong to a Feature that delivers clear value?"
2. "Are the Features distinct enough to be mapped to architectural components?"
3. "Could a User Story be derived from these FRs without ambiguity?"

### 6. Generate Feature & FR Content

Prepare the content to append to the document:

#### Content Structure:

```markdown
## Features & Functional Requirements

### Feature: [Feature Name]
**Value Proposition:** [One sentence business value]

- FR1: [Specific Actor] can [specific capability]
- FR2: [Specific Actor] can [specific capability]

### Feature: [Another Feature]
**Value Proposition:** [One sentence business value]

- FR3: [Specific Actor] can [specific capability]
```

### 7. Present MENU OPTIONS

Present the content for review:
- Show synthesized Features and FRs
- Emphasize this is the foundation for User Stories and Tickets

Display: "**Select:** [A] Advanced Elicitation [P] Party Mode [C] Continue to Non-Functional Requirements (Step 10 of 11)"

#### Menu Handling Logic:
- IF A: Invoke the `bmad-advanced-elicitation` skill with the current FR list, process the enhanced capability coverage that comes back, ask user if they accept the additions, if yes update content then redisplay menu, if no keep original content then redisplay menu
- IF P: Invoke the `bmad-party-mode` skill with the current FR list, process the collaborative capability validation and additions, ask user if they accept the changes, if yes update content then redisplay menu, if no keep original content then redisplay menu
- IF C: Append the final content to {outputFile}, update frontmatter by adding this step name to the end of the stepsCompleted array, then read fully and follow: ./step-10-nonfunctional.md
- IF Any other: help user respond, then redisplay menu

#### EXECUTION RULES:
- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'
- After other menu items execution, return to this menu

## APPEND TO DOCUMENT:

When user selects 'C', append the content directly to the document using the structure from step 6.

## SUCCESS METRICS:

✅ All previous discovery content synthesized into Features and FRs
✅ Each Feature represents a clear value proposition
✅ Each FR states WHAT capability exists, not HOW to implement
✅ Altitude validation ensures implementation-agnostic requirements
✅ A/P/C menu presented and handled correctly
✅ Content properly appended to document when C selected

## FAILURE MODES:

❌ Missing capabilities from previous discovery sections
❌ Organizing by technology instead of Features
❌ Including implementation details or UI specifics in FRs
❌ Not presenting A/P/C menu after content generation
❌ Appending content without user selecting 'C'

## NEXT STEP:

After user selects 'C' and content is saved to document, load ./step-10-nonfunctional.md to define non-functional requirements.

Remember: Do NOT proceed to step-10 until user explicitly selects 'C' from the A/P/C menu and content is saved!
