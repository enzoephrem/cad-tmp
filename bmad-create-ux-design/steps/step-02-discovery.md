# Step 2: Internal Workflow & Feature Understanding

## MANDATORY EXECUTION RULES:
- 🛑 NEVER generate content without user input
- 📋 YOU ARE A UX FACILITATOR focusing on **Internal Efficiency**
- 💬 FOCUS on how **Actors** (from PRD) perform **Internal Processes**
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style

## PROJECT DISCOVERY SEQUENCE:

### 1. Review Internal Context
"I'm analyzing the internal context for {{project_name}}.

**Internal Actors & Roles:**
{list actors from PRD}

**Features & Business Processes:**
{list Features from PRD/Features.md}

My goal is to design a UX that maximizes productivity for these specific roles within these internal workflows."

### 2. Map Features to UX Goals
For each Feature, identify the UX priority:
- **Efficiency:** How can we reduce the number of clicks to complete this task?
- **Clarity:** How do we present complex internal data without overwhelming the user?
- **Accuracy:** How does the UI prevent data entry errors in this process?

### 3. Identify High-Density Data Needs
"Many internal tools require high information density. 
- Which Features require viewing large data sets (tables, grids)?
- Which Features involve complex multi-step forms?
- Are there specific 'Power User' shortcuts required?"

### 4. Generate Internal Understanding Content
Append to document:
```markdown
## Internal UX Strategy

### Workflow Efficiency Goals
[Goals for reducing task time and cognitive load]

### Role-Based UI Requirements
[Specific UI needs for each Actor/Role]

### Feature-Specific UX Priorities
[Mapping of PRD Features to UX design goals]
```

## NEXT STEP:
Save and load `./step-03-productivity-definition.md` (renamed from core-experience).
