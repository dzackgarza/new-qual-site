---
schema: qual/card@1
id: P-NL22Q
kind: problem
title: The ring of analytic functions on a domain is an integral domain
classification:
  areas:
  - complex-analysis
  topics:
  - Identity Theorem
  - Zeros
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Suppose $D$ is a domain and $f, g$ are analytic on $D$.

Prove that if $fg = 0$ on $D$, then either $f \equiv 0$ or $g\equiv 0$ on $D$.
:::

::: {.solution}
**Goal:** Prove that if $f, g$ are analytic on a domain $D$ and $fg \equiv 0$ on $D$, then either $f \equiv 0$ or $g \equiv 0$ on $D$.

::: pf

::: {.pf-step #s1}
Assume $f \not\equiv 0$; it suffices to show $g \equiv 0$.

::: pf-proof
By symmetry between $f$ and $g$.
:::

:::

::: pf-step
The zero set $Z \definedas \theset{z \in D \suchthat f(z) = 0}$ is a closed subset of $D$ with no accumulation point in $D$.

::: pf-proof

::: {.pf-step #s2-1}
$Z$ is closed in $D$.

::: pf-proof
$f$ is continuous, and $Z$ is the preimage of the closed set $\theset{0}$.
:::

:::

::: pf-step
$Z$ has empty interior.

::: pf-proof
If $Z$ contained a nonempty open set $U$, then $f \equiv 0$ on $U$, and by the identity theorem $f \equiv 0$ on $D$, contradicting step [](#s1){.pf-ref}.
:::

:::

:::

:::

::: {.pf-step #s3}
$D \setminus Z$ is nonempty and open in $D$.

::: pf-proof
$Z \neq D$ (else $f \equiv 0$, contradicting step [](#s1){.pf-ref}) and $Z$ is closed by step [](#s2-1){.pf-ref}.
:::

:::

::: pf-step
$g \equiv 0$ on $D \setminus Z$.

::: pf-proof
For $z \in D \setminus Z$, $f(z) \neq 0$, so $fg(z) = 0$ forces $g(z) = 0$.
:::

:::

::: {.pf-step #s5}
$g \equiv 0$ on $D$.

::: pf-proof
step [](#s3){.pf-ref} gives a nonempty open set (e.g. a disk contained in $D \setminus Z$) on which $g$ vanishes; by the identity theorem, $g$ vanishes on all of $D$.
:::

:::

::: pf-qed
steps [](#s1){.pf-ref} through [](#s5){.pf-ref} show that if $f \not\equiv 0$ then $g \equiv 0$; the alternative case is symmetric.
:::

:::

:::
