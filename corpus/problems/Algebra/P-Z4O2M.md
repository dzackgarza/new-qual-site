---
schema: qual/card@1
id: P-Z4O2M
kind: problem
title: Every nonzero homomorphism from a field is injective, and whether the same
  holds for domains
classification:
  areas:
  - algebra
  topics:
  - Fields
  - Homomorphisms
  - Integral Domains
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Let $R$ and $S$ be commutative rings with multiplicative identity.

(a) Prove that when $R$ is a field, every non-zero ring homomorphism $\phi: R\to S$ is injective.

(b) Does (a) still hold if we only assume that $R$ is a domain?
If so, prove it, and if not provide a counterexample.
:::

::: {.solution}

::: pf

::: pf-step

(a) If $R$ is a field, every nonzero ring homomorphism $\phi\colon R\to S$ is injective.

::: pf-proof

The kernel $\ker\phi$ is an ideal of $R$, and the only ideals of a field are $(0)$ and $R$. Since $\phi\ne0$, $\ker\phi\ne R$, so $\ker\phi=(0)$ and $\phi$ is injective. This argument does not use the convention that ring homomorphisms preserve $1$.

:::

:::

::: pf-step

(b) No: the reduction map $\phi\colon\ZZ\to\ZZ/2\ZZ$, $n\mapsto n\bmod 2$, is a nonzero homomorphism from a domain that is not injective.

::: pf-proof

$\ZZ$ is a domain, $\phi$ is a ring homomorphism with $\phi(1)=1\ne0$, and $\ker\phi=2\ZZ\ne0$.

:::

:::

:::

:::
