## Clarifications

### Round 1 — 2026-10-26 · Critic: same session

| REQ | Verdict | Notes |
| --- | --- | --- |
| REQ-EXEC-001 | ok | Stage order, explicit acceptance, failure reporting and one-step boundary covered. |
| REQ-EXEC-002 | issues | F1, F2. |
| REQ-EXEC-003 | issues | F1. |
| REQ-EXEC-004 | issues | F3, F4. |
| REQ-EXEC-005 | issues | F6 / Q1 pending. |
| REQ-EXEC-006 | ok | Four-injection customization remains local and operator-controlled; required negative categories covered. |
| REQ-EXEC-007 | issues | F5 fixed; F6 / Q1 pending. |

- F1 [ambiguity] REQ-EXEC-002, REQ-EXEC-003: selected instruction identity did not explicitly cover the transitive local instruction set and effective configuration, permitting unnoticed dependency drift → fixed: EXEC-002.S1 binds the complete local closure and non-secret configuration; EXEC-003 records those identities and credential references without secret values.
- F2 [coverage] REQ-EXEC-002: no concrete case for request evidence introducing an external instruction chain → fixed: N5 preserves supplied content as data without skill loading, new authority or acceptance bypass.
- F3 [coverage] REQ-EXEC-004: shared-resource contention between different requests was covered, but simultaneous ownership of the same request was not → fixed: N6 requires at most one writer and preserves its journal and other requests.
- F4 [ambiguity] REQ-EXEC-004: release safely did not name its in-flight/uncertainty condition → fixed: S1 requires recorded release only when no effect remains in flight or unresolved; N4/N5 retain reconciliation and stale-owner fencing.
- F5 [coverage] REQ-EXEC-007: past scheduling was covered, but a future request without a usable existing scheduling tool had no explicit outcome → fixed: N6 records a scheduling blocker without immediate posting, a custom scheduler or a false scheduled claim.
- F6 [ambiguity] REQ-EXEC-005, REQ-EXEC-007: missing report configuration blocks readiness and post-success email failure retains notification debt, but temporary mail unavailability before posting has no explicit Facebook decision → Q1.

- Q1 If the email service is temporarily unavailable while Facebook Page/browser/action checks pass, should posting continue? A) continue the authorized post and retain pending email; B) hold posting until email works — recommended: A, keeping independent reporting outages separate from task acceptance unless the service explicitly requires otherwise.

All seven requirements were re-read from disk under the Internal assurance rule. The Spec Author applied F1–F5 without changing the operator's stated scope. No living requirements exist yet in this repository. No implementation, deployment, browser operation or email send was performed. Q1 must be answered and incorporated before the spec gate.
