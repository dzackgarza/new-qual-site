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
Suppose D is a domain and f and g are analytic functions on D. Prove that if the product $f g = 0$ throughout D, then either f or g must vanish identically on D.
:::

::: {.solution}
<1>1. If $f$ vanishes identically on $D$, then the required conclusion
holds.

::: {.proof}
This is one of the two alternatives in the conclusion.
:::

<1>2. Suppose $f$ does not vanish identically on $D$. Then there is a
nonempty open set $U\subseteq D$ on which $g$ vanishes.

::: {.proof}
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

<1>3. Under the hypothesis of step <1>2, $g$ vanishes identically on $D$.

::: {.proof}
The analytic function $g$ vanishes on the nonempty open subset $U$ of the
domain $D$. Since a domain is connected, the identity theorem implies that
$g$ vanishes identically on $D$.
:::

<1>4. Either $f$ or $g$ vanishes identically on $D$.

::: {.proof}
If $f$ vanishes identically, step <1>1 applies. Otherwise step <1>3 shows
that $g$ vanishes identically.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
