# Service executor skill development

- Build the generic validate → accept/reject → execute → report skill and explicit service injections.
- Keep runtime instruction dependencies inside the skill package and the explicitly selected local service template. Import needed guidance locally; do not route runtime execution through other skills or shared procedures.
- Keep generic orchestration separate from service-specific requirements, decisions, task procedures and reports.
- Customization is operator-controlled. Executors never rewrite their own instructions, injections, templates or helpers.
- Preserve separate request records, exclusive ownership of shared effects and reconciliation before retrying uncertain effects.
- This is a public repository. Never commit credentials, private connection settings, live request records, logs or media.
- No worker launch, Facebook action, email send or installation into existing agents is authorized by repository development alone.

<!-- sdd:begin -->
## Spec-driven development (SDD)

This repository uses SDD. Specs in `specs/` are the contract for behavior.

- Don't change behavior without an approved change in `specs/changes/`
  (status `planned` or later). Tiny fixes are the exception, but a behavior
  change still needs a failing test first.
- Tests name the scenario they prove, e.g. `test_REQ_CHK_007_N1_invalid_email`.
- Current behavior: `specs/capabilities/`. Project rules and assurance level:
  `specs/constitution.md`.
- When something breaks: stop, analyze, think, plan, execute. No blind
  retries. After two failed fixes for the same problem, report to the operator.
- Work on changes with the `sdd` skill: `/sdd` in Claude Code, `$sdd` in Codex.
<!-- sdd:end -->
