# OIDC: a concept demonstration, not a deployment lab

OpenID Connect lets a GitHub Actions job obtain short-lived cloud credentials by presenting its identity, instead of storing a long-lived cloud key.

```text
Workflow job → signed GitHub OIDC token → cloud verifies trust → limited temporary access
```

The cloud checks issuer, audience and subject against a preconfigured trust relationship.

Job permissions may include:

```yaml
permissions:
  contents: read
  id-token: write
```

**This is not a complete login workflow.** `id-token: write` allows token issuance. It does not grant Azure, AWS or Google Cloud resource access.

You must separately configure:

1. A supported cloud identity and federation relationship.
2. Trust restricted to the approved owner/repository and branch or GitHub environment.
3. A least-privilege cloud role.
4. A supported login action and appropriate environment protections.

Example **alternative** GitHub subject patterns:

```text
repo:OWNER/REPO:ref:refs/heads/main
repo:OWNER/REPO:environment:staging
```

Use the subject appropriate to the actual job configuration; do not copy both into every trust policy.

OIDC is distinct from `gh auth login` and does not replace every application-level API credential.

No cloud resource or paid deployment is required in this workshop.

Reference: [GitHub OpenID Connect documentation](https://docs.github.com/en/actions/concepts/security/openid-connect).
