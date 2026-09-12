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

::: problem
Let $R$ and $S$ be commutative rings with multiplicative identity.

1. Prove that when $R$ is a field, every non-zero ring homomorphism $\phi: R\to S$ is injective.

2. Does (a) still hold if we only assume that $R$ is a domain?
   If so, prove it, and if not provide a counterexample.
:::

::: {.solution}
Let $R$ be a field and let
\[
\phi:R\to S
\]
be a nonzero ring homomorphism. Its kernel is an ideal of $R$, so
\[
\ker\phi=(0)\quad\text{or}\quad R.
\]
The second possibility would make $\phi$ the zero map. Hence
\[
\ker\phi=(0),
\]
so $\phi$ is injective. This argument does not require a convention that ring homomorphisms preserve $1$.

The statement fails for integral domains. For example,
\[
\mathbb Z\to\mathbb Z/2\mathbb Z,
\qquad n\mapsto n\bmod2,
\]
is a nonzero ring homomorphism, but
\[
\ker\phi=2\mathbb Z\ne0.
\]
Thus a nonzero homomorphism from a domain need not be injective.
:::
