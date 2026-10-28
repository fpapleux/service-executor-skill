## Verification — round 1 (historical)

- Date: 2026-10-27 · Verifier: same session (Internal assurance). Round 1; reviewed implementation commit `3c36c1c`.
- Tests: `python3 -m unittest discover -s tests -v` → 52 passed. Breakdown: 44 retained-review evidence checks, seven artifact checks and one actual OS-lock primitive check.
- Check: `sdd.py check --stage verify` → OK, zero errors and 20 pre-existing-evidence warnings. This checks bookkeeping/traceability, not the adequacy of the behavioral evidence.
- Coverage: available `coverage.py`, run with branches over `tests/` → 94% combined statement/branch coverage; 141 statements, five missed, 36 branches and six partially covered branch sites. There is no production Python runtime to measure: the deliverable is Markdown. Uncovered test-harness paths concern external-link/fragment handling, the baseline-review branch during a green run and direct-script entry guards; these are not uncovered executor implementation branches. This metric does not measure instruction compliance.
- Artifact review: ten runtime Markdown artifacts exist; actual linked closure stays local; required four Facebook injections are present. Public runtime text uses configuration placeholders without real provider/account settings. No live publication, communication, installation or account operation was performed.
- Evidence review: opened the generic exercise checker, all guided response artifacts and the baseline assessments. Responses contain proposed actions and records, not observed tool-call transcripts or executed request state. The checker requires a truthy `passed` judgment and matching hashes; it never performs the scenario When or asserts its expected state/effects. This distinction is disclosed in tests/README.md but still falls short of full scenario verification.
- Red/pre-existing review: retained baseline assertion output is real evidence of interpretation-review failures. The 20 pre-existing task groups are credible only as baseline decision answers, not pre-existing executed request behavior. Original task evidence is preserved; corrective tasks below require a behavioral red/green or justified pre-existing application result.
- Retained known gaps: instruction closure is not a sandbox; no live account/browser/transport readiness, custom runtime/recovery service or automatic propagation from old shared sources. Those approved exclusions remain unchanged. The findings below concern offline controlled exercises already in the design, not a demand for live readiness.

| Scenario | Test | Result | Then fully asserted |
| --- | --- | --- | --- |
| REQ-EXEC-001.S1 | tests/test_exercises.py::test_REQ_EXEC_001_S1 | evidence check passes | weak: planned response, no observed application; T43 |
| REQ-EXEC-001.N1 | tests/test_exercises.py::test_REQ_EXEC_001_N1 | evidence check passes | weak: planned response, no observed application; T44 |
| REQ-EXEC-001.N2 | tests/test_exercises.py::test_REQ_EXEC_001_N2 | evidence check passes | weak: planned response, no observed application; T45 |
| REQ-EXEC-001.N3 | tests/test_exercises.py::test_REQ_EXEC_001_N3 | evidence check passes | weak: planned response, no observed application; T46 |
| REQ-EXEC-001.B1 | tests/test_exercises.py::test_REQ_EXEC_001_B1 | evidence check passes | weak: planned response, no observed application; T47 |
| REQ-EXEC-002.S1 | tests/test_exercises.py::test_REQ_EXEC_002_S1 | evidence check passes | weak: planned response, no observed application; T48 |
| REQ-EXEC-002.N1 | tests/test_exercises.py::test_REQ_EXEC_002_N1 | evidence check passes | weak: planned response, no observed application; T49 |
| REQ-EXEC-002.N2 | tests/test_exercises.py::test_REQ_EXEC_002_N2 | evidence check passes | weak: planned response, no observed application; T50 |
| REQ-EXEC-002.N3 | tests/test_exercises.py::test_REQ_EXEC_002_N3 | evidence check passes | weak: planned response, no observed application; T51 |
| REQ-EXEC-002.N4 | tests/test_exercises.py::test_REQ_EXEC_002_N4 | evidence check passes | weak: planned response, no observed application; T52 |
| REQ-EXEC-002.N5 | tests/test_exercises.py::test_REQ_EXEC_002_N5 | evidence check passes | weak: planned response, no observed application; T53 |
| REQ-EXEC-003.S1 | tests/test_exercises.py::test_REQ_EXEC_003_S1 | evidence check passes | weak: planned response, no observed application; T54 |
| REQ-EXEC-003.N1 | tests/test_exercises.py::test_REQ_EXEC_003_N1 | evidence check passes | weak: planned response, no observed application; T55 |
| REQ-EXEC-003.N2 | tests/test_exercises.py::test_REQ_EXEC_003_N2 | evidence check passes | weak: planned response, no observed application; T56 |
| REQ-EXEC-003.N3 | tests/test_exercises.py::test_REQ_EXEC_003_N3 | evidence check passes | weak: planned response, no observed application; T57 |
| REQ-EXEC-003.B1 | tests/test_exercises.py::test_REQ_EXEC_003_B1 | evidence check passes | weak: planned response, no observed application; T58 |
| REQ-EXEC-004.S1 | tests/test_exercises.py::test_REQ_EXEC_004_S1 | evidence check passes | weak: planned response, no observed application; T59 |
| REQ-EXEC-004.N1 | tests/test_exercises.py::test_REQ_EXEC_004_N1 | evidence check passes | weak: planned response, no observed application; T60 |
| REQ-EXEC-004.N2 | tests/test_exercises.py::test_REQ_EXEC_004_N2 | evidence check passes | weak: planned response, no observed application; T61 |
| REQ-EXEC-004.N3 | tests/test_exercises.py::test_REQ_EXEC_004_N3 | evidence check passes | weak: planned response, no observed application; T62 |
| REQ-EXEC-004.N4 | tests/test_exercises.py::test_REQ_EXEC_004_N4 | evidence check passes | weak: planned response, no observed application; T63 |
| REQ-EXEC-004.N5 | tests/test_exercises.py::test_REQ_EXEC_004_N5 | evidence check passes | weak: planned response, no observed application; T64 |
| REQ-EXEC-004.N6 | tests/test_exercises.py::test_REQ_EXEC_004_N6 | evidence check passes | weak: planned response, no observed application; T65 |
| REQ-EXEC-005.S1 | tests/test_exercises.py::test_REQ_EXEC_005_S1 | evidence check passes | weak: planned response, no observed application; T66 |
| REQ-EXEC-005.S2 | tests/test_exercises.py::test_REQ_EXEC_005_S2 | evidence check passes | weak: planned response, no observed application; T67 |
| REQ-EXEC-005.S3 | tests/test_exercises.py::test_REQ_EXEC_005_S3 | evidence check passes | weak: planned response, no observed application; T68 |
| REQ-EXEC-005.N1 | tests/test_exercises.py::test_REQ_EXEC_005_N1 | evidence check passes | weak: planned response, no observed application; T69 |
| REQ-EXEC-005.N2 | tests/test_exercises.py::test_REQ_EXEC_005_N2 | evidence check passes | weak: planned response, no observed application; T70 |
| REQ-EXEC-005.N3 | tests/test_exercises.py::test_REQ_EXEC_005_N3 | evidence check passes | weak: planned response, no observed application; T71 |
| REQ-EXEC-005.N4 | tests/test_exercises.py::test_REQ_EXEC_005_N4 | evidence check passes | weak: planned response, no observed application; T72 |
| REQ-EXEC-006.S1 | tests/test_exercises.py::test_REQ_EXEC_006_S1 | evidence check passes | weak: planned response, no observed application; T73 |
| REQ-EXEC-006.N1 | tests/test_exercises.py::test_REQ_EXEC_006_N1 | evidence check passes | weak: planned response, no observed application; T74 |
| REQ-EXEC-006.N2 | tests/test_exercises.py::test_REQ_EXEC_006_N2 | evidence check passes | weak: planned response, no observed application; T75 |
| REQ-EXEC-006.N3 | tests/test_exercises.py::test_REQ_EXEC_006_N3 | evidence check passes | weak: planned response, no observed application; T76 |
| REQ-EXEC-007.S1 | tests/test_exercises.py::test_REQ_EXEC_007_S1 | evidence check passes | weak: planned response, no observed application; T77 |
| REQ-EXEC-007.S2 | tests/test_exercises.py::test_REQ_EXEC_007_S2 | evidence check passes | weak: planned response, no observed application; T78 |
| REQ-EXEC-007.S3 | tests/test_exercises.py::test_REQ_EXEC_007_S3 | evidence check passes | weak: planned response, no observed application; T79 |
| REQ-EXEC-007.N1 | tests/test_exercises.py::test_REQ_EXEC_007_N1 | evidence check passes | weak: planned response, no observed application; T80 |
| REQ-EXEC-007.N2 | tests/test_exercises.py::test_REQ_EXEC_007_N2 | evidence check passes | weak: planned response, no observed application; T81 |
| REQ-EXEC-007.N3 | tests/test_exercises.py::test_REQ_EXEC_007_N3 | evidence check passes | weak: planned response, no observed application; T82 |
| REQ-EXEC-007.N4 | tests/test_exercises.py::test_REQ_EXEC_007_N4 | evidence check passes | weak: planned response, no observed application; T83 |
| REQ-EXEC-007.N5 | tests/test_exercises.py::test_REQ_EXEC_007_N5 | evidence check passes | weak: planned response, no observed application; T84 |
| REQ-EXEC-007.N6 | tests/test_exercises.py::test_REQ_EXEC_007_N6 | evidence check passes | weak: planned response, no observed application; T85 |
| REQ-EXEC-007.B1 | tests/test_exercises.py::test_REQ_EXEC_007_B1 | evidence check passes | weak: planned response, no observed application; T86 |

Findings:
- F1 (weak tests, all 44 scenarios) The retained responses demonstrate interpretation of the guidance but do not instantiate the Given, perform the When or observe the complete Then. Hash-bound reviewed prose is not proof of stage order, preserved files, exclusive agent behavior, tool selection, communication invocation or absence of extra effects. Add offline application evidence and outcome assertions → T43–T86. This does not require a workflow engine or live service.
- F2 (weak concurrency evidence, REQ-EXEC-004.N2/N6) The OS primitive really excludes a child process, but no two executing agents contend for the same request/profile while using this guidance. There is no observed loser journal, action trace or cross-request preservation check → T61 and T65 within F1.
- F3 (assisted close-out, REQ-EXEC-004.S1) The first guided response omitted ownership disposition; the passing response was prompted to supply the missing element. Preserve that transparent assisted result, but add an unprompted application showing no in-flight operation at release and preserved handover holds → T59 within F1.
- Scope of correction: test evidence only unless a controlled application demonstrates an instruction defect. Do not change the locked requirements, manufacture a pass, alter old evidence or expand the product into an execution framework. No spec gap was identified.

Verdict: GAPS — scenario-level application evidence is insufficient; T43–T86 added, returning to implementation.


## Verification

- Date: 2026-10-28 · Verifier: same session (Internal assurance), round 2. Reviewed implementation commit `2da6dbbd7ad771e6989eb9d798dd7f91048c0f52`. The preceding round is historical; this is the current verdict.
- Tests: `python3 -m unittest discover -s tests -v` → 98 passed: 44 actual-application artifact checks, 44 historical interpretation checks, eight package checks, one live OS-lock primitive check, one passive-native-double check. This rerun inspects retained applications; it does not rerun agents or live services.
- Check: `sdd.py check --stage verify` → OK, zero errors, 20 historical pre-existing-interpretation warnings. These do not establish executed behavior. Corrective T43–T86 provide actual application evidence; T53 still has the weakness below.
- Coverage: coverage.py 7.13.5; `python3 -m coverage run --branch --source=tests -m unittest discover -s tests` then `python3 -m coverage report -m` → 68% combined statement/branch coverage (720 statements, 215 missed; 238 branches, 12 partial sites). Scenario artifact assertions in test_offline_remaining.py have 100% statement/branch coverage, which does not prove assertion adequacy. Fixture generation and the access observer are collection-time utilities, not invoked by replay (0%). The passive double is 56%: its focused unit check does not invoke every export/post, lock-contention or unreadable-journal path. Export/post and contention were exercised during retained applications; unreadable-journal fallback is a test-infrastructure error branch outside the service contract. Other misses are script-entry guards, link fragments/external-link handling and historical baseline selection. No production Python executor exists: the runtime is Markdown. Coverage cannot measure instruction compliance.
- Review: read the approved scenario tables, runtime instructions, named assertions and retained journals/replies/native calls. The suite checks immutable original/configuration/binding hashes, prior-history prefixes and preserved effects. Supplementary inspection verified all ten retained snapshot hashes for each of REQ-EXEC-002.S1 and REQ-EXEC-003.B1. Matrix judgments combine assertions with inspected retained evidence, within the approved offline scope.
- Red evidence: T43's absent export and T44–T86's absent actual observations are real retained assertion failures, primarily demonstrating missing applications rather than defective original guidance. T59 also preserves an actual executor close-out failure, the narrow records-guide correction and a fresh successful application. The original interpretation reds and pre-existing outcomes remain historical; their limitations are disclosed.
- Concurrency: separate-session kernel acquisition/contention/release traces, passive pre-effect lock snapshots, exact effects and request journals establish one business executor in each contention application. The profile contender's assisted recovery of its already-bound snapshot is disclosed in tests/README.md. This is not an external fencing service.
- Close-out: fresh REQ-EXEC-004.S1 records operation completion, owner/resources, explicit empty unresolved/hold/communication lists and next action before release. The failed original remains unchanged. Lock probes on extracted archive copies are only primitive checks; the separately retained original-lock probe is historical cleanup evidence.
- Scope: all four approved known gaps remain. No live account/browser/communication readiness, deployment or certification is claimed. No implementation, tests, existing tasks or historical evidence were changed in this verification.

| Scenario | Test | Result | Then fully asserted |
| --- | --- | --- | --- |
| REQ-EXEC-001.S1 | tests/test_offline_application.py::test_REQ_EXEC_001_S1_actual_export | pass | yes: ordered acceptance/intent, exact export and reports |
| REQ-EXEC-001.N1 | tests/test_offline_remaining.py::test_REQ_EXEC_001_N1 | pass | yes: rejection/report, no task effect, original retained |
| REQ-EXEC-001.N2 | tests/test_offline_remaining.py::test_REQ_EXEC_001_N2 | pass | yes: acceptance-required, no task, history retained |
| REQ-EXEC-001.N3 | tests/test_offline_remaining.py::test_REQ_EXEC_001_N3 | pass | yes: one failed pending action, failure report, prior A retained |
| REQ-EXEC-001.B1 | tests/test_offline_remaining.py::test_REQ_EXEC_001_B1 | pass | yes: one exact export and session reply, no extra task |
| REQ-EXEC-002.S1 | tests/test_offline_remaining.py::test_REQ_EXEC_002_S1 | pass | yes: local snapshot/config hashes verified, credentials referenced |
| REQ-EXEC-002.N1 | tests/test_offline_remaining.py::test_REQ_EXEC_002_N1 | pass | yes: missing injection, requester report, no invented task/procedure |
| REQ-EXEC-002.N2 | tests/test_offline_remaining.py::test_REQ_EXEC_002_N2 | pass | yes: pinned version and completed work retained, report only |
| REQ-EXEC-002.N3 | tests/test_offline_remaining.py::test_REQ_EXEC_002_N3 | pass | yes: dependency blocked, independent inotify audit observes no access |
| REQ-EXEC-002.N4 | tests/test_offline_remaining.py::test_REQ_EXEC_002_N4 | pass | yes: conflict reported, no bypass/effect, immutable package |
| REQ-EXEC-002.N5 | tests/test_offline_remaining.py::test_REQ_EXEC_002_N5 | pass | weak: weak: ineffective path assertion; no independent read observation |
| REQ-EXEC-003.S1 | tests/test_offline_remaining.py::test_REQ_EXEC_003_S1 | pass | yes: same binding/history, only pending B, report obligation retained |
| REQ-EXEC-003.N1 | tests/test_offline_remaining.py::test_REQ_EXEC_003_N1 | pass | yes: missing ID, no replacement/effect |
| REQ-EXEC-003.N2 | tests/test_offline_remaining.py::test_REQ_EXEC_003_N2 | pass | yes: mismatch holds effects, binding/history retained |
| REQ-EXEC-003.N3 | tests/test_offline_remaining.py::test_REQ_EXEC_003_N3 | pass | yes: actual persistence failure, path/operation, no false acknowledgement |
| REQ-EXEC-003.B1 | tests/test_offline_remaining.py::test_REQ_EXEC_003_B1 | pass | yes: one request, exact inputs, snapshot identities, secret reference |
| REQ-EXEC-004.S1 | tests/test_offline_remaining.py::test_REQ_EXEC_004_S1 | pass | yes: fresh attributable completion and durable safe release |
| REQ-EXEC-004.N1 | tests/test_offline_remaining.py::test_REQ_EXEC_004_N1 | pass | yes: unresolved canonical resource, no effect/replacement claim |
| REQ-EXEC-004.N2 | tests/test_offline_remaining.py::test_REQ_EXEC_004_N2 | pass | yes: real sessions, kernel contention, one effect, separate journals |
| REQ-EXEC-004.N3 | tests/test_offline_remaining.py::test_REQ_EXEC_004_N3 | pass | yes: unreadable claim bytes retained, no takeover/effect |
| REQ-EXEC-004.N4 | tests/test_offline_remaining.py::test_REQ_EXEC_004_N4 | pass | yes: same attempt reconciled unknown, no replay/dependent action |
| REQ-EXEC-004.N5 | tests/test_offline_remaining.py::test_REQ_EXEC_004_N5 | pass | yes: stale owner denied, B record and journal unchanged |
| REQ-EXEC-004.N6 | tests/test_offline_remaining.py::test_REQ_EXEC_004_N6 | pass | yes: same-request contention, loser reports outside protected journal |
| REQ-EXEC-005.S1 | tests/test_offline_remaining.py::test_REQ_EXEC_005_S1 | pass | yes: execution/report content and receipt, no delivery/read claim |
| REQ-EXEC-005.S2 | tests/test_offline_remaining.py::test_REQ_EXEC_005_S2 | pass | yes: login blocker promptly reported with required payload |
| REQ-EXEC-005.S3 | tests/test_offline_remaining.py::test_REQ_EXEC_005_S3 | pass | yes: outage precedes export, pending obligations, requester informed |
| REQ-EXEC-005.N1 | tests/test_offline_remaining.py::test_REQ_EXEC_005_N1 | pass | yes: missing config, no guessed recipient/send/task |
| REQ-EXEC-005.N2 | tests/test_offline_remaining.py::test_REQ_EXEC_005_N2 | pass | yes: failed execution and receipt retained, no resend/replay |
| REQ-EXEC-005.N3 | tests/test_offline_remaining.py::test_REQ_EXEC_005_N3 | pass | yes: same uncertain notification reconciled, no resend/replay |
| REQ-EXEC-005.N4 | tests/test_offline_remaining.py::test_REQ_EXEC_005_N4 | pass | yes: same pending incident submitted once, no task replay |
| REQ-EXEC-006.S1 | tests/test_offline_remaining.py::test_REQ_EXEC_006_S1 | pass | yes: actual unactivated export template, local config, generic rules retained |
| REQ-EXEC-006.N1 | tests/test_offline_remaining.py::test_REQ_EXEC_006_N1 | pass | yes: decision injection missing, incomplete/unactivated |
| REQ-EXEC-006.N2 | tests/test_offline_remaining.py::test_REQ_EXEC_006_N2 | pass | yes: separate attributable proposal, immutable instructions/history |
| REQ-EXEC-006.N3 | tests/test_offline_remaining.py::test_REQ_EXEC_006_N3 | pass | yes: missing resource reported, no fallback/readiness claim |
| REQ-EXEC-007.S1 | tests/test_offline_remaining.py::test_REQ_EXEC_007_S1 | pass | yes: synthetic native checks, exact draft, one post and reports |
| REQ-EXEC-007.S2 | tests/test_offline_remaining.py::test_REQ_EXEC_007_S2 | pass | yes: configured Chrome despite unavailable iab, no substitution |
| REQ-EXEC-007.S3 | tests/test_offline_remaining.py::test_REQ_EXEC_007_S3 | pass | yes: portal payload/receipt, no mandatory provider/channel |
| REQ-EXEC-007.N1 | tests/test_offline_remaining.py::test_REQ_EXEC_007_N1 | pass | yes: missing caption rejected/reported, no copy/post |
| REQ-EXEC-007.N2 | tests/test_offline_remaining.py::test_REQ_EXEC_007_N2 | pass | yes: identity mismatch held, approved target retained |
| REQ-EXEC-007.N3 | tests/test_offline_remaining.py::test_REQ_EXEC_007_N3 | pass | yes: upload blocker reported, no post/substitution/security change |
| REQ-EXEC-007.N4 | tests/test_offline_remaining.py::test_REQ_EXEC_007_N4 | pass | yes: prior accepted post retained, reporting pending, no replay |
| REQ-EXEC-007.N5 | tests/test_offline_remaining.py::test_REQ_EXEC_007_N5 | pass | yes: past-time exception reported, original time, no post |
| REQ-EXEC-007.N6 | tests/test_offline_remaining.py::test_REQ_EXEC_007_N6 | pass | yes: scheduling blocker, no post/fallback scheduler |
| REQ-EXEC-007.B1 | tests/test_offline_remaining.py::test_REQ_EXEC_007_B1 | pass | yes: exact caption/media/scope, one post, no added operation |

Findings:
- Round-1 F1: actual application artifacts now exist for all 44 scenarios; 43 are sufficient within the approved scope. One subfinding remains below. F2 (actual concurrency) and F3 (unprompted close-out application) are resolved; original failed/assisted observations remain preserved.
- F4 (weak test/evidence, REQ-EXEC-002.N5, existing T53): tests/test_offline_remaining.py:119 compares literal `outside-skill.md` with full path strings. In a temporary extracted copy only, the verifier added `state/outside-skill.md` and ran the unchanged named test: it still passed. Even a correct file-presence assertion would not establish that outside instructions were never read. This application retains exact business bytes, affirmative acceptance and no extra native operations, but no independent access observation or complete executor read trace. N3's inotify evidence covers a different application and cannot prove N5's data-instruction isolation. The complete N5 Then remains unproven; this is not a demonstrated executor violation.
- Repeated pattern: round 1 rejected asserted compliance without observed behavior. Most corrections now supply actual effects/traces, but N5 retains an unobserved negative claim. The verifier role states: “If a second verify round finds gaps again for the same scenario, stop. Report the pattern to the operator instead of adding a third round of tasks.” No third-round task batch, automatic implementation or waiver is added. Proposed narrow correction: an observable N5 application with an accessible harmless instruction target and access audit, plus an assertion that fails on target access. No new runtime architecture is needed. Await operator direction.

Verdict: GAPS — 98 checks pass; 43 scenario reviews are sufficient, but REQ-EXEC-002.N5 remains weak. Second-round repeat reported to the operator; results are not ready for approval.
