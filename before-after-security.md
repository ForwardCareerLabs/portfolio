# Security Documentation Before and After

Clearer language is useful only when the supporting facts and evidence are equally clear. The examples below show how to improve vague statements without turning uncertainty into an unsupported compliance claim.

## Example 1 Encryption

### Before

> We use encryption to protect data and secure our systems.

### Improved draft

> Sensitive data is encrypted in transit using approved protocols. Encryption at rest is enabled for the production data stores identified in the current system inventory. Exceptions require documented review and approval.

### Evidence needed before approval

- Approved encryption standard
- Current system and data inventory
- Production storage configuration
- TLS configuration
- Exception register
- Control owner validation

### Why this is stronger

The improved version defines the type and scope of encryption. It still remains a draft until the inventory, configuration, exceptions, and responsible owner support the wording.

## Example 2 Incident response

### Before

> We have processes in place for handling security issues.

### Improved draft

> The organization maintains an incident response process covering identification, escalation, containment, investigation, recovery, communications, and post incident review. Response roles and escalation criteria are documented and tested through exercises or actual incidents.

### Evidence needed before approval

- Current incident response plan
- Severity and escalation criteria
- Role and contact list
- Recent exercise or incident record
- After action documentation
- Open corrective actions

### Why this is stronger

The improved version explains the expected lifecycle and introduces operational testing. A written plan alone does not support the claim that the process is tested.

## Example 3 Access reviews

### Before

> User access is reviewed regularly.

### Improved draft

> Application owners review user and privileged access at the frequency defined in the access control standard. Identified exceptions are assigned to an owner and tracked through remediation or approved risk acceptance.

### Evidence needed before approval

- Access control standard
- Application and privileged account inventory
- Defined review frequency
- Recent completed review
- Exception and remediation records
- Risk acceptance record when applicable

### Why this is stronger

The improved version identifies who performs the review and how exceptions are handled. The word regularly is replaced with a frequency that must be supported by the governing standard.

## Example 4 Vendor recovery

### Before

> Our critical vendors have strong disaster recovery plans.

### Improved draft

> Critical vendors are assigned recovery requirements based on the services they support. Recovery objectives and recent test evidence are reviewed against internal continuity needs, and unresolved gaps are documented for treatment or acceptance.

### Evidence needed before approval

- Critical vendor inventory
- Business impact analysis
- Contracted recovery objectives
- Vendor recovery plans
- Recent recovery test results
- Documented gaps and treatment decisions

### Why this is stronger

The improved version avoids declaring a vendor strong without a defined standard. It connects vendor evidence to the organization’s actual continuity requirements.

## Review rule

An improved sentence is not automatically a true sentence. Before approval, the reviewer should confirm:

1. The systems and processes covered by the statement
2. The evidence supporting each material claim
3. Known exceptions and limitations
4. The accountable control owner
5. The time period represented by the evidence
6. The person authorized to approve the final response

## Portfolio note

These examples demonstrate documentation methodology using fictional information. They are not statements about a real organization’s controls, compliance status, or certification.
