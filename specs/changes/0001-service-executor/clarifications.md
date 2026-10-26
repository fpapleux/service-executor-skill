## Clarifications

### Round 1 — 2026-10-26 · Critic: same session

| REQ | Verdict | Notes |
| --- | --- | --- |
| REQ-EXEC-001 | ok | Stage order, explicit acceptance, failure reporting and one-step boundary covered. |
| REQ-EXEC-002 | issues | F1, F2. |
| REQ-EXEC-003 | issues | F1. |
| REQ-EXEC-004 | issues | F3, F4. |
| REQ-EXEC-005 | issues | F6 / Q1 resolved. |
| REQ-EXEC-006 | ok | Four-injection customization remains local and operator-controlled; required negative categories covered. |
| REQ-EXEC-007 | issues | F5 fixed; F6 / Q1 resolved. |

- F1 [ambiguity] REQ-EXEC-002, REQ-EXEC-003: selected instruction identity did not explicitly cover the transitive local instruction set and effective configuration, permitting unnoticed dependency drift → fixed: EXEC-002.S1 binds the complete local closure and non-secret configuration; EXEC-003 records those identities and credential references without secret values.
- F2 [coverage] REQ-EXEC-002: no concrete case for request evidence introducing an external instruction chain → fixed: N5 preserves supplied content as data without skill loading, new authority or acceptance bypass.
- F3 [coverage] REQ-EXEC-004: shared-resource contention between different requests was covered, but simultaneous ownership of the same request was not → fixed: N6 requires at most one writer and preserves its journal and other requests.
- F4 [ambiguity] REQ-EXEC-004: release safely did not name its in-flight/uncertainty condition → fixed: S1 requires recorded release only when no effect remains in flight or unresolved; N4/N5 retain reconciliation and stale-owner fencing.
- F5 [coverage] REQ-EXEC-007: past scheduling was covered, but a future request without a usable existing scheduling tool had no explicit outcome → fixed: N6 records a scheduling blocker without immediate posting, a custom scheduler or a false scheduled claim.
- F6 [ambiguity] REQ-EXEC-005, REQ-EXEC-007: missing report configuration blocks readiness and post-success email failure retains notification debt, but temporary mail unavailability before posting has no explicit Facebook decision → fixed: Sam answered Q1; EXEC-005 now owns customer communication and continuation during a temporary channel outage, while EXEC-007 accepts the adopter's chosen communication procedure without mandating a communication channel or provider.

- Q1 If the email service is temporarily unavailable while Facebook Page/browser/action checks pass, should posting continue? A) continue the authorized post and retain pending email; B) hold posting until email works — recommended: A, keeping independent reporting outages separate from task acceptance unless the service explicitly requires otherwise.
  - Answer: "continue posting but that is not a facebook injection. That is part of the process of executing a service." Sam further states that communication is a generic duty to keep the customer informed; email is his proposed channel and every adopter of this public skill implements their own way. (operator, 2026-10-26)

All seven requirements were re-read from disk under the Internal assurance rule. The Spec Author applied F1–F5 without changing the operator's stated scope. No living requirements exist yet in this repository. No implementation, deployment, browser operation or email send was performed. Q1 is answered and incorporated. A second round audits the generic-policy correction and its ownership/recovery implications before the spec gate.

### Round 2 — 2026-10-26 · Critic: same session

| REQ | Verdict | Notes |
| --- | --- | --- |
| REQ-EXEC-001 | ok | Acceptance still gates task execution; existing N1/N3 cover rejection/failure reporting. |
| REQ-EXEC-002 | ok | Complete local instruction/configuration binding and explicit service procedure remain channel-neutral. |
| REQ-EXEC-003 | ok | Original decisions, execution evidence and outstanding communication survive a fresh session. |
| REQ-EXEC-004 | issues | F7 fixed. |
| REQ-EXEC-005 | issues | F8 and F9 fixed; Q1 is incorporated as generic policy, not a Facebook option. |
| REQ-EXEC-006 | ok | Operator selects the channel/procedure while preserving the generic communication duty and nonblocking outage rule. |
| REQ-EXEC-007 | ok | Public template uses configured browser and communication tools; no mandatory communication channel, provider, transport or sender identity. |

- F7 [contradiction] REQ-EXEC-004, REQ-EXEC-005: the blanket no-unresolved-effect release condition could prevent safe handover with a retained uncertain communication obligation → fixed: EXEC-004.S1 requires that no prior-owner operation can still mutate the released resource, while preserving unresolved outcomes and their replay/dependency holds; EXEC-005.N4 proves reporting-only continuation without task replay. Unknown outcomes never become permission to resend or repeat a business action.
- F8 [untestable] REQ-EXEC-005: the revised intervention row combined rejection, task failure and login blockers, and the outage row combined multiple timings → fixed: S2 now names one interactive-login blocker and S3 one pre-execution portal failure; EXEC-001.N1/N3 already cover rejection/failure reporting and EXEC-007.N4 covers a post-execution communication outage.
- F9 [coverage] REQ-EXEC-005: Sam's generic nonblocking outage decision also requires retained reporting recovery after the business task finishes → fixed: S3 exercises an otherwise executable non-Facebook service during a pre-execution reporting outage; N4 requires fresh-session communication-only recovery, preserving the original execution and incident evidence.

The Critic re-read all seven revised requirements from disk, including the operator's Q1 answer and the local public template brief. Required Internal categories are covered without exemptions. No new requirement or unanswered product decision resulted. No implementation, deployment or live service action occurred. This round is ready for the operator's spec approval.
