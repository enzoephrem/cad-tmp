# Step 6: Internal Innovation & Efficiency Discovery

**Progress: Step 6 of 11** - Next: Project Type Analysis

## MANDATORY EXECUTION RULES (READ FIRST):

- 🛑 NEVER generate content without user input

- 📖 CRITICAL: ALWAYS read the complete step file before taking any action - partial understanding leads to incomplete decisions
- 🔄 CRITICAL: When loading next step with 'C', ensure the entire file is read and understood before proceeding
- ✅ ALWAYS treat this as collaborative discovery between PM peers
- 📋 YOU ARE A FACILITATOR, not a content generator
- 💬 FOCUS on detecting and exploring innovative aspects that drive internal efficiency and company value
- 🎯 OPTIONAL STEP: Only proceed if innovation or efficiency signals are detected
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`
- ✅ YOU MUST ALWAYS WRITE all artifact and document content in `{document_output_language}`

## EXECUTION PROTOCOLS:

- 🎯 Show your analysis before taking any action
- ⚠️ Present A/P/C menu after generating innovation content
- 💾 ONLY save when user chooses C (Continue)
- 📖 Update output file frontmatter, adding this step name to the end of the list of stepsCompleted
- 🚫 FORBIDDEN to load next step until C is selected

## CONTEXT BOUNDARIES:

- Current document and frontmatter from previous steps are available
- Focus on internal company innovation and operational efficiency

## OPTIONAL STEP CHECK:

Before proceeding with this step, scan for efficiency or innovation signals:
- Listen for language like "automating manual work", "massive time savings", "rethinking internal workflow"
- Look for novel internal approaches or unique combinations of internal tools
- If no significant innovation or efficiency gains detected, skip this step

## YOUR TASK:

Detect and explore innovation patterns that drive internal efficiency and create value for the company.

## DISCOVERY SEQUENCE:

### 1. Listen for Internal Efficiency Signals

Monitor conversation for signals of internal transformation:
- "This will save hours of manual work"
- "We're automating a process that currently takes days"
- "This combines data from [System A] and [System B] in a way we never have before"
- "Novel approach to an internal bottleneck"

### 2. Deep Efficiency Exploration (If Detected)

If efficiency/innovation signals are found, explore deeply:
- **Value Projection:** "What's the estimated impact on team productivity?"
- **Novelty:** "How is this different from how other departments or companies handle this?"
- **Sustainability:** "How does this scale as the company grows?"
- **Validation:** "How will we measure the actual efficiency gain?"

### 3. Generate Innovation & Efficiency Content

Prepare the content to append to the document:

#### Content Structure:

When saving to document, append these Level 2 and Level 3 sections:

```markdown
## Internal Innovation & Efficiency

### Efficiency Gains

[Description of automation and productivity improvements based on conversation]

### Novel Internal Patterns

[Innovative internal approaches identified based on conversation]

### Validation & Metrics

[How efficiency will be measured and validated based on conversation]

### Risk Mitigation

[Internal risks and fallbacks for new processes based on conversation]
```

### 4. Present MENU OPTIONS

Present the content for review, then display menu:

Display: "**Select:** [A] Advanced Elicitation [P] Party Mode [C] Continue to Project Type Analysis (Step 7 of 11)"

#### Menu Handling Logic:
- IF A: Invoke the `bmad-advanced-elicitation` skill, process insights, update then redisplay menu
- IF P: Invoke the `bmad-party-mode` skill, process insights, update then redisplay menu
- IF C: Append final content to {outputFile}, update frontmatter, then read fully and follow: ./step-07-project-type.md
- IF Any other: help user respond, then redisplay menu

#### EXECUTION RULES:
- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'

## NO INNOVATION DETECTED:

If no significant efficiency or innovation signals are found:
- Acknowledge that the focus is on solid execution of established internal patterns
- Offer to skip: "**Select:** [C] Continue - Skip innovation section and move to Project Type Analysis (Step 7 of 11)"

## APPEND TO DOCUMENT:

When user selects 'C', append the content directly to the document using the structure from step 3.

## SUCCESS METRICS:

✅ Internal efficiency gains clearly identified and projected
✅ Novel internal workflows explored and documented
✅ Validation metrics defined for productivity impact
✅ A/P/C menu presented and handled correctly

## FAILURE MODES:

❌ Including "Market Context" or "Competitive Landscape" (irrelevant for internal tools)
❌ Forced innovation when the goal is simple automation
❌ Missing clear metrics for measuring success
❌ Appending content without user selecting 'C'

**Master Rule:** Focus on internal company value. How does this make the company faster, better, or more efficient?
