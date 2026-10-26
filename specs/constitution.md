---
assurance: internal
approved: yes
fingerprint: 3b88f781b59d
approved_level: internal
---

# Constitution

Non-negotiable rules for this project. Every SDD phase checks against them.
The operator approves this file and every change to it.

## Assurance level: `internal`

Used by you or your team, with real data and a small blast radius. Every scenario is test-first; bad input, wrong state and dependency failures are covered.

This is set once for the project. A single change may raise its own level
(for example, payment code inside an internal tool). Lowering it needs a
recorded operator waiver.

## Article 1 — Test-first

No production code without a failing test that names the scenario it proves
(e.g. `test_REQ_CHK_007_S1_guest_pays`). Every task records its failing (red)
run and its passing (green) run. At `prototype`, this applies to happy-path
scenarios.

## Article 2 — Negative coverage

Every requirement covers the failure categories its assurance level requires,
or records `N/A <category>: <reason>`. At `prototype`, every change keeps a
Known gaps list instead.

## Article 3 — The spec is the contract

Behavior changes only through an approved change in `specs/changes/`. If
implementation shows the spec is wrong or incomplete, work stops and the
operator decides.

## Project rules
- Deliver an agent-interpreted skill, not a custom execution engine or service.
- The generic lifecycle is validate → accept/reject → execute → report. Each service supplies explicit requirements, decision constraints, task instructions and reporting procedure.
- Runtime instructions are self-contained within the skill package and selected local service template. Import necessary guidance; never load another skill or shared operating procedure implicitly. Configured tools and their API documentation remain usable.
- Service-specific browser, email and account choices belong in the service injections/configuration, not the generic skill. The first template is templates/facebook-posting/.
- Preserve durable request records, concurrent-request ownership and reconciliation before retrying uncertain effects. Customization instructions serve operators; executing agents never amend themselves.
- Keep credentials, private connection settings, requests, logs and media out of this public repository. Repository publication does not deploy or activate a live executor.

## Approvals
| Gate | Date | Evidence |
| --- | --- | --- |
| constitution | 2026-10-26 | Sam in Operations Codex chat 01a1686e-0119-7580-8cd7-58c77204142b, 2026-10-26 Europe/Brussels: "$sdd approve constitution". · fingerprint 3b88f781b59d · level internal |
