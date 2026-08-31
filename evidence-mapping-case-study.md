# Security Control Evidence Mapping Case Study

> Demonstration portfolio artifact. The organization and evidence below are fictional. The purpose is to show a defensible GRC review method, not to represent a certification or client engagement.

## Scenario

A healthcare technology vendor receives a customer security review covering identity, encryption, vulnerability management, incident response, and business continuity. The vendor has policies and technical controls, but its questionnaire responses need to be tied to evidence before submission.

## Review method

For each control statement:

1. Identify exactly what the question requires.
2. Separate policy intent from implemented technical control.
3. Identify evidence that could substantiate the response.
4. Record evidence owner and freshness.
5. Mark gaps or ambiguity instead of filling them with assumptions.
6. Draft the external response only from verified facts.

## Evidence map

| Control area | Proposed control statement | Evidence requested | Evidence owner | Review result |
| --- | --- | --- | --- | --- |
| Identity | MFA is required for privileged administrative access | IdP configuration export, privileged role list, access policy | IAM owner | Supported pending freshness check |
| Encryption | Customer data is encrypted in transit | TLS configuration, architecture diagram, approved crypto standard | Infrastructure | Supported for documented application paths |
| Vulnerability management | Critical findings are remediated under defined timelines | Vulnerability policy, recent scan, remediation tickets | Security operations | Partial, SLA compliance must be sampled |
| Incident response | Security incidents follow a documented response process | IR plan, exercise record, incident ticket template | Security lead | Supported at process level |
| Continuity | Critical services have recovery objectives | BCP, BIA, recovery test evidence | Business continuity owner | Gap, recovery objectives not evidenced for all services |

## Example: converting a weak answer into a defensible answer

### Customer question

Do you require multi-factor authentication for privileged access?

### Weak response

Yes, MFA is required for all administrative accounts.

### Why that is risky

The answer makes an absolute claim before scope and evidence are checked. A single unmanaged administrative path would make the response inaccurate.

### Evidence-aware working draft

Available identity documentation indicates MFA is required for privileged access through the primary identity provider. Before external submission, validate that all privileged access paths are federated through the documented control and confirm whether any emergency or local administrative accounts require separate treatment.

### Evidence status

**Validation required before submission.**

## Gap handling

A mature questionnaire process does not turn missing evidence into polished fiction. When evidence is incomplete, the reviewer should identify:

- the unsupported portion of the claim
- the evidence needed to close the gap
- the person responsible for providing it
- whether compensating controls exist
- whether the final answer needs narrower wording

## Deliverable structure

A useful internal review package would include:

- questionnaire response
- response status: verified, partial, gap, not applicable
- mapped evidence
- evidence owner
- evidence date or version
- reviewer notes
- external wording approved for submission

## What this demonstrates

This case study demonstrates security questionnaire review, control-to-evidence mapping, careful treatment of absolute claims, gap identification, and the distinction between having a policy and proving that a control is implemented.