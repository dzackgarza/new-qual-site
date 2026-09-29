---
schema: qual/card@1
id: P-AZOFF-E03
kind: problem
title: The ring of analytic functions on a domain has no zero divisors
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Liouville, FTA, and power series, Problem 3, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    If f is not identically zero, continuity makes it nonzero on a
    neighborhood of one point, so fg=0 forces g to vanish on a nonempty open
    set. The identity theorem on the connected domain then forces g to vanish
    identically.
---

::: {.problem}
Suppose $D$ is a domain and $f$ and $g$ are analytic functions on $D$. Prove that if the product $fg = 0$ throughout $D$, then either $f$ or $g$ must vanish identically on $D$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $f$ vanishes identically on $D$, then the required conclusion
holds.

::: pf-proof

This is one of the two alternatives in the conclusion.

:::

:::

::: {.pf-step #s2}

Suppose $f$ does not vanish identically on $D$. Then there is a
nonempty open set $U\subseteq D$ on which $g$ vanishes.

::: pf-proof

Choose $z_0\in D$ with $f(z_0)\neq0$. Since $f$ is continuous, there is an
open neighborhood $U\subseteq D$ of $z_0$ such that
$$
f(z)\neq0
$$
for every $z\in U$. The hypothesis
$$
f(z)g(z)=0
$$
throughout $D$ therefore implies
$$
g(z)=0
$$
for every $z\in U$.

:::

:::

::: {.pf-step #s3}

Under the hypothesis of step [](#s2){.pf-ref}, $g$ vanishes identically on $D$.

::: pf-proof

The analytic function $g$ vanishes on the nonempty open subset $U$ of the
domain $D$. Since a domain is connected, the identity theorem implies that
$g$ vanishes identically on $D$.

:::

:::

::: {.pf-step #s4}

Either $f$ or $g$ vanishes identically on $D$.

::: pf-proof

If $f$ vanishes identically, step [](#s1){.pf-ref} applies. Otherwise step [](#s3){.pf-ref} shows
that $g$ vanishes identically.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the required conclusion.

:::

:::

:::
