---
schema: qual/card@1
id: P-JHUSP02CAA
kind: problem
title: "Entire functions whose image omits a ray"
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Open Mapping Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

1. Let f be an entire function such that the image of f does not intersect $\{ z \in \mathbb { R } : z \geq 5 \}$ . Prove that $f$ is a constant.

::: {.solution}
<1>1. $f(\C)$ omits $[5,\infty)$, so $\sqrt{5-f}$ entire omitting upper half-plane? Compose to bounded.
::: {.proof}
$5-f$ omits $(-\infty,0]$, so $h=\sqrt{5-f}$ entire and $\operatorname{Re}h>0$? Actually $5-f$ omits $[0,\infty)$? Wait $f$ omits $[5,\infty)$, so $5-f$ omits $(-\infty,0]$.
:::

<1>2. $g=\sqrt{5-f}$ maps $\C$ into right half-plane, then $\phi=(g-1)/(g+1)$ bounded by $1$.
::: {.proof}
Cayley.
:::

<1>3. $\phi$ entire bounded, so constant by Liouville, hence $f$ constant.
::: {.proof}
<1>2.
:::

<1>4. Q.E.D.
::: {.proof}
<1>3.
:::
:::
