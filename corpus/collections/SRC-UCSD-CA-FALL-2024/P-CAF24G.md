---
schema: qual/card@1
id: P-CAF24G
kind: problem
title: Bounded harmonic function on the upper half-plane vanishing on the boundary is constant
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked that the odd reflection is well defined because
    u vanishes on the real axis, that it is bounded and odd, that it is continuous on the
    plane (the two branches agreeing on the boundary) and harmonic off the real axis
    including the lower half-plane as a composition with conjugation, that the reflection
    principle gives harmonicity across the boundary, and that Liouville's theorem for
    harmonic functions makes it constant, the oddness forcing the constant to be 0. The
    argument is the card's own; no retained set is cited. No repair needed.
---

::: {.problem}
Let $\halfplane = \{z : \operatorname{Im} z > 0\}$ denote the upper half plane.
Let $u : \overline{\halfplane} \to \RR$ be a continuous bounded function which is harmonic in $\halfplane$ and $u = 0$ on $\partial\halfplane$.
Show that $u$ is constant.
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on it. Write $H=\{z:\operatorname{Im}z>0\}$ for the upper half-plane and $M=\sup_{\overline{H}}\abs{u}<\infty$.

::: pf

::: {.pf-step #define}
The odd reflection $U(z)=u(z)$ for $\operatorname{Im}z\ge0$ and $U(z)=-u(\bar z)$ for $\operatorname{Im}z<0$ is a well-defined function on $\CC$, bounded by $M$, and odd: $U(\bar z)=-U(z)$.

::: pf-proof
On the line $\operatorname{Im}z=0$ one has $\bar z=z$ and $u(z)=0$ by hypothesis, so both formulas give $0$ and $U$ is well defined; and $\abs{U(z)}=\abs{u(z)}$ or $\abs{u(\bar z)}\le M$, so $U$ is bounded. For oddness: if $\operatorname{Im}z\ge0$ then $U(\bar z)=-u(\overline{\bar z})=-u(z)=-U(z)$, and if $\operatorname{Im}z<0$ then $U(\bar z)=u(\bar z)=-U(z)$.
:::

:::

::: {.pf-step #harmonic}
$U$ is continuous on $\CC$ and harmonic off the real axis; being odd and vanishing on $\RR$, it is harmonic across $\RR$ as well, so $U$ is harmonic on $\CC$.

::: pf-proof
Continuity: $U$ is continuous on each closed half-plane by the continuity of $u$ and of conjugation, and the two branches agree on $\RR$, where both equal $0$; a function continuous on two closed sets covering $\CC$ and agreeing on their intersection is continuous. Harmonicity off $\RR$: on $H$ the function $U=u$ is harmonic by hypothesis; on the lower half-plane $U=-u\circ(\text{conjugation})$, and $u\circ(\text{conjugation})$ is harmonic because conjugation is anti-holomorphic and the composition of a harmonic function with an anti-holomorphic map is harmonic. Across $\RR$: the Schwarz reflection principle for harmonic functions says that a function harmonic in $H$, continuous on $H\cup(-\varepsilon,\varepsilon)$-neighbourhoods of the boundary and vanishing on $\RR$, extends to a harmonic function near $\RR$ by odd reflection; that is exactly $U$, so $U$ is harmonic in a neighbourhood of every point of $\RR$.
:::

:::

::: {.pf-step #constant}
$U$ is constant.

::: pf-proof
$U$ is harmonic on all of $\CC$ and bounded, and a bounded harmonic function on $\CC$ is constant — Liouville's theorem in its harmonic form, obtained for instance from the mean value property and the gradient estimate for harmonic functions.
:::

:::

::: {.pf-step #zero}
$U\equiv0$, hence $u\equiv0$ on $H$.

::: pf-proof
$U$ is constant and odd, so $U(0)=-U(0)$ gives $U(0)=0$ and the constant is $0$. Restricting to $H$, where $U=u$, gives $u\equiv0$.
:::

:::

::: {.pf-step}
$u$ is constant.

::: pf-proof
Step [](#zero){.pf-ref} is stronger than required: $u$ vanishes identically on $H$, hence is constant there.
:::

:::

:::
:::
