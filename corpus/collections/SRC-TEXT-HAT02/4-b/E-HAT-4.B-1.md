---
schema: qual/card@1
id: E-HAT-4.B-1
kind: problem
title: "Hopf invariant of compositions"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

Show that the Hopf invariant of a composition $S^{2n-1} \xrightarrow{f} S^{2n-1} \xrightarrow{g} S^n$ is given by $H(gf) = (\deg f) H(g)$, and for a composition $S^{2n-1} \xrightarrow{f} S^n \xrightarrow{g} S^n$ the Hopf invariant satisfies $H(gf) = (\deg g)^2 H(f)$.

::: {.solution}
<1>1. The Hopf invariant $H(g)$ is defined via the cohomology of the mapping cone $C_g$: $H(g)$ is the integer such that $\alpha \smile \alpha = H(g)\beta$ in $H^{2n}(C_g)$, where $\alpha \in H^n(C_g)$ and $\beta \in H^{2n}(C_g)$ are generators.
::: {.proof}
definition of the Hopf invariant.
:::

<1>2. First composition: $S^{2n-1} \xrightarrow{f} S^{2n-1} \xrightarrow{g} S^n$.
<2>1. The mapping cone $C_{gf}$ is homotopy equivalent to $C_g$ (since $f$ is a self-map of the domain sphere, and the cone of $gf$ is obtained from the cone of $g$ by precomposing the attaching map with $f$).
::: {.proof}
$C_{gf} = S^n \cup_{gf} e^{2n}$, and $C_g = S^n \cup_g e^{2n}$.
:::
<2>2. The attaching map $gf$ is homotopic to $(\deg f) g$ in $\pi_{2n-1}(S^n)$.
::: {.proof}
precomposition by $f$ multiplies the homotopy class by $\deg f$ (the action of $\pi_{2n-1}(S^{2n-1}) = \ZZ$ on $\pi_{2n-1}(S^n)$).
:::
<2>3. Hence $H(gf) = (\deg f) H(g)$.
::: {.proof}
the Hopf invariant is linear in the attaching map, so scaling the attaching map by $\deg f$ scales the Hopf invariant by $\deg f$.
:::

<1>3. Second composition: $S^{2n-1} \xrightarrow{f} S^n \xrightarrow{g} S^n$.
<2>1. The mapping cone $C_{gf}$ has attaching map $gf$, and $gf$ is homotopic to $(\deg g) f$ in $\pi_{2n-1}(S^n)$.
::: {.proof}
postcomposition by $g$ multiplies the homotopy class by $\deg g$.
:::
<2>2. The Hopf invariant satisfies $H(gf) = (\deg g)^2 H(f)$.
::: {.proof}
the Hopf invariant is a quadratic form on $\pi_{2n-1}(S^n)$ (for $n$ even it is a quadratic form; the general fact is that $H$ is a homomorphism for $n$ odd and a quadratic form for $n$ even, and in both cases postcomposition by a degree-$\deg g$ map multiplies $H$ by $(\deg g)^2$).
:::

<1>4. Q.E.D.
::: {.proof}
<1>2 and <1>3.
:::
:::
