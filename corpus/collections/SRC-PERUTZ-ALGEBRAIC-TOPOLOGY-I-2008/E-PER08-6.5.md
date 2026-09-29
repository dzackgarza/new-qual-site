---
schema: qual/card@1
id: E-PER08-6.5
kind: problem
title: Deck group of a covering is $N_G(H)/H$
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
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Retyped the mathematics against Exercise 6.5 of the Perutz 2008 notes.
---

::: {.problem}
Let $p\colon Y\to X$ be a covering (with $Y$ path connected and $X$ locally path connected) such that $p_*\pi_1(Y,y)=H\subset G=\pi_1(X,p(y))$.
Show that $\operatorname{Aut}(\widetilde X/X)\cong(N_GH)/H$, where $N_GH=\{g\in G:gHg^{-1}=H\}$.
:::

::: {.solution}
We prove
\[
\operatorname{Aut}(Y/X)\cong N_G(H)/H,
\qquad
N_G(H)=\{g\in G:gHg^{-1}=H\}.
\]

::: pf

::: pf-step

A deck transformation determines a coset in $N_G(H)/H$.

::: pf-proof

Fix $y\in p^{-1}(x)$.
The fibre can be identified with the coset $G/H$ by lifting loops at $x$.
A deck transformation $\varphi$ is determined by $\varphi(y)$, say the point represented by $gH$.
Because $\varphi$ is an isomorphism of the based covering after moving the basepoint, the corresponding subgroup must remain $H$; the change-of-basepoint formula gives $gHg^{-1}=H$.
Thus $g\in N_G(H)$.
Replacing $g$ by $gh$ with $h\in H$ gives the same point of the fibre, so only the coset $gH$ matters.

:::

:::

::: pf-step

Every coset in $N_G(H)/H$ gives a deck transformation.

::: pf-proof

If $g\in N_G(H)$, the lifting criterion gives a unique map of coverings $Y\to Y$ sending $y$ to the point $gH$ in the fibre, because the subgroup condition is exactly $gHg^{-1}=H$.
Applying the same construction to $g^{-1}$ gives its inverse, so this map is a deck transformation.

:::

:::

::: pf-step

The correspondence is a group isomorphism.

::: pf-proof

Composition sends the image of $y$ according to multiplication of cosets, and the kernel consists exactly of $g\in H$.
Hence the deck group is canonically $N_G(H)/H$ after the chosen basepoint identification.

:::

:::

:::

:::

::: {.remark}
The group $\operatorname{Aut}(\widetilde X/X)$ is printed as in the source; since the covering in the statement is $p\colon Y\to X$, the group meant is $\operatorname{Aut}(Y/X)$.
:::
