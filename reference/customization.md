# Operator customization

This guide is for operators defining services in later sessions. Executing agents do not edit their own skill, injections, templates or helpers, including when an improvement has been approved in principle. Record an attributable change request (request ID, bound version, problem/evidence, proposed change and impact) separately through the configured operator route; the operator evaluates and implements it in a separate change context. Preserve the running request's history and binding.

## Create or adapt a service

1. State the exact service effect, input contract, authority boundary and native evidence of success. Copy the bundled [Facebook template declaration](../templates/facebook-posting/README.md) as a structural example; replace domain content rather than inheriting its actions.
2. Supply four local files: `validate.md` for requirements/checks, `decision.md` for accept/reject constraints, `execute.md` for task steps, and `report.md` for the chosen customer communication procedure. Declare all four paths and supporting local instruction resources in the template README.
3. Put tool access/how-to and identity/recipient requirements in local tool configuration. Keep business conditions in injections. Each adopter chooses a communication channel; preserve the generic duty to keep the customer informed and to continue independent authorized work during a transient reporting outage. Missing required configuration is a distinct validation failure.
4. Import necessary domain guidance locally. Resolve the full instruction closure including links/symlinks; remove outside skill/procedure references. Use current tool documentation for tool operation without importing workflow policy. Check that injections cannot override acceptance, scope, ownership, continuity or reporting rules.
5. Declare canonical shared resources, private record location, configuration fields, authority sources and reporting/reconciliation capabilities. Never place private credentials, provider/account identities, requests, logs or media in a public release. Keep secret access as private references.
6. Exercise nominal work, missing inputs, wrong state, dependency outages, uncertain effects, fresh-session resume and contention with another request/owner. Verify that a report-only recovery cannot replay the task. An untested capability is not ready by declaration alone.
7. Review/publish an identifiable operator-controlled version. Keep old bound content available for existing requests. Publishing artifacts does not install/activate a service or grant action authority. Deployment is a separate authorized operation.

## Four-injection review checklist

| Injection | Must define | Incomplete when |
| --- | --- | --- |
| Validate | Required exact inputs, configuration and capability checks, errors | Required checks or inputs are unspecified |
| Decision | Acceptance/rejection constraints and task authority | Decision constraints are missing |
| Execute | Exact domain task and native evidence/reconciliation | Task, side-effect scope or success evidence is unclear |
| Report | Customer channel/procedure, event triggers, payload, acknowledgement/reconciliation | Required route or procedure is missing |

Keep an incomplete template visibly incomplete; never claim ready-for-execution or activate it. If this guide or a required bundled resource is missing, report `missing-customization-resource`. Do not load another skill or invent substitute instructions to complete the review.

## Small non-Facebook example: document export

This illustrates injection content for an operator; it is not a second deployed service.

- Validate: require explicit source document, output format and authorized destination; confirm source readability and existing export capability. Require a configured customer-portal reporting procedure.
- Decision: accept only when source/destination authority and all required configuration are established. Temporary portal unavailability alone does not reject an independently executable export.
- Execute: record intent, export the specified source once with the existing tool, verify the resulting artifact and retain its reference. Preserve confirmed output on resume; reconcile uncertain export outcomes.
- Report: submit the request outcome, artifact reference or blocker to the configured portal, retain its request-specific submission receipt and pending obligations if unavailable. Never infer customer reading from a receipt.

Give the service its own local four files, explicit tool configuration and canonical shared-resource keys. Do not copy social posting actions or introduce a mandatory email route into the generic lifecycle.
