---
id: 0001-service-executor
title: Self-contained four-stage service executor and Facebook template
type: feature
size: standard
assurance: internal
status: clarifying
capabilities: service-executor=EXEC
created: 2026-10-26
---

# 0001-service-executor — Self-contained four-stage service executor and Facebook template

<!-- A standard change is this folder: proposal.md (this file), spec-delta.md,
design.md, tasks.md and verification.md. sdd.py reads them as one spec.
Gates: spec (locks Intent, Defect, Scope, Requirements, Known gaps) → plan → results. -->

## Intent
Build a generic, self-contained service-executor skill that guides an agent through validate → accept/reject → execute → report. A service supplies requirements for validation, constraints for the acceptance decision, task instructions for execution and a reporting procedure, without changing the generic lifecycle. Facebook posting is the first complete service template.

The operator must be able to define more services in fresh sessions with predictable behavior, durable request continuity and concurrent requests. Previously developed guidance may be imported into the package, but runtime execution must not discover or inherit instructions by chaining other skills or shared operating procedures. Customization belongs to operators, not executing agents.

## Scope
- In:
  - An agent-interpreted generic skill with the four explicit stages and four service-specific injection areas. Execution is conditional on acceptance. Keeping the customer informed is a generic responsibility; temporary communication outages retain reporting obligations without blocking otherwise accepted, authorized and independently executable work. Each adopter supplies its communication channel and procedure.
  - An instruction boundary consisting of the skill's bundled files and the explicitly selected local service template. Necessary prior guidance is imported locally, without runtime references that load other skills or shared operating procedures. Explicit request inputs, local tool configuration and current tool/API documentation remain usable.
  - Durable records sufficient to recover exact inputs, decisions, versions, authority, progress, effects and reporting in a new session. Separate concurrent requests retain independent records; shared effects require exclusive ownership and uncertain effects require reconciliation before retry.
  - The four Facebook posting injections under templates/facebook-posting/, including local domain guidance, browser configuration and the adopter's chosen customer communication procedure. Service-specific destinations, channel choices, sender settings and tool settings do not become generic executor rules; neither the skill nor the public template requires email or a particular provider.
  - Bundled operator-facing instructions for creating, adapting and reviewing another service's injections, with the generic skill pointing to that local customization guidance. Executors may report improvements but never amend their own process.
  - Documentation and scoped verification of the package, its instruction boundary, lifecycle, continuity and Facebook template. Publish repository artifacts through the existing public GitHub remote.
- Out:
  - A custom execution engine, workflow service, scheduler, queue, supervisor, automatic retry system, browser adapter or email implementation.
  - Replacing the currently installed execute skill, migrating existing requests, changing legacy releases, updating the MCP launcher or deploying into the live Facebook agent. Publishing the Facebook template here means delivering its injections in this repository.
  - Live Facebook posts, uploads, comments, shares, crossposts, boosts, email sends, account changes or spending. Template availability does not grant authority for these actions.
  - Credentials, private connection settings, live request histories, logs or media in the public repository.

## Open questions
- Q1 resolved by Sam, 2026-10-26: "continue posting but that is not a facebook injection. That is part of the process of executing a service." Keeping the customer informed and continuing independent accepted work during communication outages belong to the generic executor. Public adopters implement their own communication channel/procedure; email is only one option.
- A missing or malformed required reporting definition/configuration remains a definition/validation issue; the nonblocking rule concerns temporary unavailability of an otherwise configured communication channel.

## Amendments
<!-- Spec changes after the spec gate, one line each, then `sdd.py approve amend`:
- A1 2026-10-08: <reason> → <what changed> -->

## Approvals
| Gate | Date | Evidence |
| --- | --- | --- |
