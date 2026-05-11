---
name: bmad-sprint-status
description: 'Summarize sprint status and surface risks. Use when the user says "check sprint status" or "show sprint status"'
---

# Sprint Status Workflow

**Goal:** Summarize sprint status, surface risks, and recommend the next workflow action.

**Your Role:** You are a Developer providing clear, actionable sprint visibility. No time estimates — focus on status, risks, and next steps.

## Conventions

- Bare paths (e.g. `checklist.md`) resolve from the skill root.
- `{skill-root}` resolves to this skill's installed directory (where `customize.toml` lives).
- `{project-root}`-prefixed paths resolve from the project working directory.
- `{skill-name}` resolves to the skill directory's basename.

## On Activation

### Step 1: Resolve the Workflow Block

Run: `python3 {project-root}/_bmad/scripts/resolve_customization.py --skill {skill-root} --key workflow`

**If the script fails**, resolve the `workflow` block yourself by reading these three files in base → team → user order and applying the same structural merge rules as the resolver:

1. `{skill-root}/customize.toml` — defaults
2. `{project-root}/_bmad/custom/{skill-name}.toml` — team overrides
3. `{project-root}/_bmad/custom/{skill-name}.user.toml` — personal overrides

Any missing file is skipped. Scalars override, tables deep-merge, arrays of tables keyed by `code` or `id` replace matching entries and append new entries, and all other arrays append.

### Step 2: Execute Prepend Steps

Execute each entry in `{workflow.activation_steps_prepend}` in order before proceeding.

### Step 3: Load Persistent Facts

Treat every entry in `{workflow.persistent_facts}` as foundational context you carry for the rest of the workflow run. Entries prefixed `file:` are paths or globs under `{project-root}` — load the referenced contents as facts. All other entries are facts verbatim.

### Step 4: Load Config

Load config from `{project-root}/_bmad/bmm/config.yaml` and resolve:

- `project_name`, `user_name`
- `communication_language`, `document_output_language`
- `implementation_artifacts`
- `date` as system-generated current datetime
- YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`

### Step 5: Greet the User

Greet `{user_name}`, speaking in `{communication_language}`.

### Step 6: Execute Append Steps

Execute each entry in `{workflow.activation_steps_append}` in order.

Activation is complete. Begin the workflow below.

## Paths

- `sprint_status_file` = `{implementation_artifacts}/sprint-status.yaml`

## Input Files

| Input | Path | Load Strategy |
|-------|------|---------------|
| Sprint status | `{sprint_status_file}` | FULL_LOAD |

## Execution

<workflow>

<step n="0" goal="Determine execution mode">
  <action>Set mode = {{mode}} if provided by caller; otherwise mode = "interactive"</action>

  <check if="mode == data">
    <action>Jump to Step 20</action>
  </check>

  <check if="mode == validate">
    <action>Jump to Step 30</action>
  </check>

  <check if="mode == interactive">
    <action>Continue to Step 1</action>
  </check>
</step>

<step n="1" goal="Locate sprint status file">
  <action>Load {project_context} for project-wide patterns and conventions (if exists)</action>
  <action>Try {sprint_status_file}</action>
  <check if="file not found">
    <output>sprint-status.yaml not found.
Run `/bmad:bmm:workflows:sprint-planning` to generate it, then rerun sprint-status.</output>
    <action>Exit workflow</action>
  </check>
  <action>Continue to Step 2</action>
</step>

<step n="2" goal="Read and parse sprint-status.yaml">
  <action>Read the FULL file: {sprint_status_file}</action>
  <action>Parse fields: generated, last_updated, project, project_key, tracking_system, ticket_location</action>
  <action>Parse development_status map. Classify keys:</action>
- Features: keys starting with "feature-"
- Tickets: keys matching N-M-L-* (e.g., 1-2-1-backend)
- Stories: keys matching N-M-* but not N-M-L-* (e.g., 1-2-login)
  
  <action>Count ticket statuses: backlog, ready-for-dev, in-progress, review, done</action>
  <action>Count story statuses: backlog, ready-for-dev, in-progress, done</action>
  <action>Count feature statuses: backlog, in-progress, done</action>

<action>Validate all statuses against known values:</action>

- Valid ticket statuses: backlog, ready-for-dev, in-progress, review, done
- Valid story statuses: backlog, ready-for-dev, in-progress, done
- Valid feature statuses: backlog, in-progress, done

  <check if="any status is unrecognized">
    <output>
**Unknown status detected:**
{{#each invalid_entries}}

- `{{key}}`: "{{status}}" (not recognized)
  {{/each}}

**Valid statuses:**

- Tickets: backlog, ready-for-dev, in-progress, review, done
- Stories: backlog, ready-for-dev, in-progress, done
- Features: backlog, in-progress, done
  </output>
  <ask>How should these be corrected?</ask>
<check if="user provided corrections">
<action>Update sprint-status.yaml with corrected values</action>
<action>Re-parse the file with corrected statuses</action>
</check>
</check>

<action>Calculate Aggregation Metrics:</action>
- For each Feature, calculate `% complete` = (Done Tickets for this Feature / Total Tickets for this Feature) * 100

<action>Detect risks:</action>

- IF any ticket has status "review": suggest `/bmad:bmm:workflows:code-review`
- IF any ticket has status "in-progress" AND no tickets have status "ready-for-dev": recommend staying focused on active ticket
- IF all features have status "backlog" AND no stories have status "ready-for-dev": prompt `/bmad:bmm:workflows:create-features-and-stories`
- IF `last_updated` timestamp is more than 7 days old: warn "sprint-status.yaml may be stale"
  </step>

<step n="3" goal="Select next action recommendation">
  <action>Pick the next recommended workflow using priority:</action>
  <note>Sort by feature, then story, then ticket number</note>
  1. If any ticket status == in-progress → recommend `dev-ticket` for the first in-progress ticket
  2. Else if any ticket status == review → recommend `code-review` for the first review ticket
  3. Else if any ticket status == ready-for-dev → recommend `dev-ticket`
  4. Else if any story status == backlog → recommend `create-tickets`
  5. Else if any feature status == backlog → recommend `create-features-and-stories`
  6. Else → All implementation items done; congratulate the user!
  <action>Store selected recommendation as: next_ticket_id, next_workflow_id, next_agent (DEV)</action>
</step>

<step n="4" goal="Display summary">
  <output>
## Sprint Status

- Project: {{project}} ({{project_key}})
- Tracking: {{tracking_system}}
- Status file: {sprint_status_file}

**Features:** backlog {{feature_backlog}}, in-progress {{feature_in_progress}}, done {{feature_done}}
*(Feature Progress: [Show % complete for active features])*

**Stories:** backlog {{story_backlog}}, ready-for-dev {{story_ready}}, in-progress {{story_in_progress}}, done {{story_done}}

**Tickets:** backlog {{ticket_backlog}}, ready-for-dev {{ticket_ready}}, in-progress {{ticket_in_progress}}, review {{ticket_review}}, done {{ticket_done}}

**Next Recommendation:** /bmad:bmm:workflows:{{next_workflow_id}} ({{next_ticket_id}})

{{#if risks}}
**Risks:**
{{#each risks}}
- {{this}}
{{/each}}
{{/if}}

  </output>
  </step>

<step n="5" goal="Offer actions">
  <ask>Pick an option:
1) Run recommended workflow now
2) Show all tickets grouped by status
3) Show raw sprint-status.yaml
4) Exit
Choice:</ask>

  <check if="choice == 1">
    <output>Run `/bmad:bmm:workflows:{{next_workflow_id}}`.
If the command targets a ticket, set `ticket_key={{next_ticket_id}}` when prompted.</output>
  </check>

  <check if="choice == 2">
    <output>
### Tickets by Status
- In Progress: {{tickets_in_progress}}
- Review: {{tickets_in_review}}
- Ready for Dev: {{tickets_ready_for_dev}}
- Backlog: {{tickets_backlog}}
- Done: {{tickets_done}}
    </output>
  </check>

  <check if="choice == 3">
    <action>Display the full contents of {sprint_status_file}</action>
  </check>

  <check if="choice == 4">
    <action>Run: `python3 {project-root}/_bmad/scripts/resolve_customization.py --skill {skill-root} --key workflow.on_complete` — if the resolved value is non-empty, follow it as the final terminal instruction before exiting.</action>
    <action>Exit workflow</action>
  </check>
</step>

<!-- ========================= -->
<!-- Data mode for other flows -->
<!-- ========================= -->

<step n="20" goal="Data mode output">
  <action>Load and parse {sprint_status_file} same as Step 2</action>
  <action>Compute recommendation same as Step 3</action>
  <template-output>next_workflow_id = {{next_workflow_id}}</template-output>
  <template-output>next_story_id = {{next_story_id}}</template-output>
  <template-output>count_backlog = {{count_backlog}}</template-output>
  <template-output>count_ready = {{count_ready}}</template-output>
  <template-output>count_in_progress = {{count_in_progress}}</template-output>
  <template-output>count_review = {{count_review}}</template-output>
  <template-output>count_done = {{count_done}}</template-output>
  <template-output>epic_backlog = {{epic_backlog}}</template-output>
  <template-output>epic_in_progress = {{epic_in_progress}}</template-output>
  <template-output>epic_done = {{epic_done}}</template-output>
  <template-output>risks = {{risks}}</template-output>
  <action>Return to caller</action>
</step>

<!-- ========================= -->
<!-- Validate mode -->
<!-- ========================= -->

<step n="30" goal="Validate sprint-status file">
  <action>Check that {sprint_status_file} exists</action>
  <check if="missing">
    <template-output>is_valid = false</template-output>
    <template-output>error = "sprint-status.yaml missing"</template-output>
    <template-output>suggestion = "Run sprint-planning to create it"</template-output>
    <action>Return</action>
  </check>

<action>Read and parse {sprint_status_file}</action>

<action>Validate required metadata fields exist: generated, project, project_key, tracking_system, story_location (last_updated is optional for backward compatibility)</action>
<check if="any required field missing">
<template-output>is_valid = false</template-output>
<template-output>error = "Missing required field(s): {{missing_fields}}"</template-output>
<template-output>suggestion = "Re-run sprint-planning or add missing fields manually"</template-output>
<action>Return</action>
</check>

<action>Verify development_status section exists with at least one entry</action>
<check if="development_status missing or empty">
<template-output>is_valid = false</template-output>
<template-output>error = "development_status missing or empty"</template-output>
<template-output>suggestion = "Re-run sprint-planning or repair the file manually"</template-output>
<action>Return</action>
</check>

<action>Validate all status values against known valid statuses:</action>

- Tickets: backlog, ready-for-dev, in-progress, review, done
- Stories: backlog, ready-for-dev, in-progress, done
- Features: backlog, in-progress, done
  <check if="any invalid status found">
  <template-output>is_valid = false</template-output>
  <template-output>error = "Invalid status values: {{invalid_entries}}"</template-output>
  <template-output>suggestion = "Fix invalid statuses in sprint-status.yaml"</template-output>
  <action>Return</action>
  </check>

<template-output>is_valid = true</template-output>
<template-output>message = "sprint-status.yaml valid: metadata complete, all statuses recognized"</template-output>
<action>Run: `python3 {project-root}/_bmad/scripts/resolve_customization.py --skill {skill-root} --key workflow.on_complete` — if the resolved value is non-empty, follow it as the final terminal instruction before exiting.</action>
</step>

</workflow>
