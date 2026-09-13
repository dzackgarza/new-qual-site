---
schema: qual/card@1
id: E-PER08-6.5
kind: problem
title: Perutz Algebraic Topology I Exercise 6.5
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Completed from the retained Perutz Algebraic Topology I source and checked against the stated hypotheses.
---

::: {.problem}
Let p: Y $\\to$ X be a covering (with Y path connected and X locally path connected) such that p$\\ast$π1(Y, y) = H $\\subset$ G = π1(X, p(y)). Show that Aut( ˜X/X) $\\cong$ (NGH)/H, where NGH = {g $\\in$ G : gHg$^{-1}$ = H}.
:::

::: {.solution}
The intended statement is
\[
\operatorname{Aut}(Y/X)\cong N_G(H)/H,
\qquad
N_G(H)=\{g\in G:gHg^{-1}=H\}.
\]

<1>1. A deck transformation determines a coset in $N_G(H)/H$.
::: {.proof}
Fix $y\in p^{-1}(x)$.
The fibre can be identified with the coset $G/H$ by lifting loops at $x$.
A deck transformation $\varphi$ is determined by $\varphi(y)$, say the point represented by $gH$.
Because $\varphi$ is an isomorphism of the based covering after moving the basepoint, the corresponding subgroup must remain $H$; the change-of-basepoint formula gives $gHg^{-1}=H$.
Thus $g\in N_G(H)$.
Replacing $g$ by $gh$ with $h\in H$ gives the same point of the fibre, so only the coset $gH$ matters.
:::

<1>2. Every coset in $N_G(H)/H$ gives a deck transformation.
::: {.proof}
If $g\in N_G(H)$, the lifting criterion gives a unique map of coverings $Y\to Y$ sending $y$ to the point $gH$ in the fibre, because the subgroup condition is exactly $gHg^{-1}=H$.
Applying the same construction to $g^{-1}$ gives its inverse, so this map is a deck transformation.
:::

<1>3. The correspondence is a group isomorphism.
::: {.proof}
Composition sends the image of $y$ according to multiplication of cosets, and the kernel consists exactly of $g\in H$.
Hence the deck group is canonically $N_G(H)/H$ after the chosen basepoint identification.
:::
:::
