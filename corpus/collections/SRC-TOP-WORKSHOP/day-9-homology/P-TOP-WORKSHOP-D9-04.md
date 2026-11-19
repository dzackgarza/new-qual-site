---
schema: qual/card@1
id: P-TOP-WORKSHOP-D9-04
kind: problem
title: Homology of the unit sphere union the interval from $(0,0,-1)$ to $(0,0,1)$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Mayer-Vietoris
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Lamport structure over the prose that was already there. The homotopy equivalence with the wedge is now
    a step with its two ingredients named (the arc giving a circle with the diameter, and the collapse of a
    complementary tree), and the additivity of reduced homology over a wedge is stated as the second step
    rather than used silently. Not checked: the day-9 sheet, which the collection retains as a problem file
    only; the statement is as transcribed on the card. No retained solution set covers the problem, so the
    argument is the card's own. No statement repair.
---

::: {.problem}
(Michigan Sept ’08) Compute the homology of the space formed as the union of the unit sphere $$\{(x,y,z)\mid x^2+y^2+z^2=1\}$$ and the closed interval along the $z$-axis from $(0,0,-1)$ to $(0,0,1)$.
:::

::: {.solution}
No retained solution set covers this problem: the collection's provenance is the workshop sheets alone, so the argument is the card's own. Let $X=S^2\cup I$ where $I$ is the diameter of the unit sphere $S^2\subset\RR^3$ joining the poles $p=(0,0,1)$ and $q=(0,0,-1)$.

::: pf

::: {.pf-step #wedge}
$X\simeq S^2\vee S^1$.

::: pf-proof
Choose a closed arc $J\subset S^2$ from $p$ to $q$ not equal to the meridian through the diameter; then $I\cup J$ is a circle contained in $X$, and $J\subseteq S^2$. Give $S^2$ a CW structure with $p,q$ as $0$-cells and with $J$ a subcomplex, so that $I$ can be added as a single $1$-cell attached at $p$ and $q$; then $X$ is a CW complex containing the circle $I\cup J$ as a subcomplex. Collapsing a maximal tree of $X$ — a tree containing $J$ and all $0$-cells but none of the $2$-cells of $S^2$ and not the $1$-cell $I$ — is a homotopy equivalence onto the quotient, which is a $2$-sphere (the $2$-cells of $S^2$ with $J$ collapsed) wedged with the circle coming from $I$. So $X$ is homotopy equivalent to $S^2\vee S^1$.
:::

:::

::: {.pf-step #reduced}
$\widetilde H_n(X)\cong\widetilde H_n(S^2)\oplus\widetilde H_n(S^1)$ for all $n$.

::: pf-proof
Homology is a homotopy invariant, so step [](#wedge){.pf-ref} gives $\widetilde H_n(X)\cong\widetilde H_n(S^2\vee S^1)$. For a wedge of pointed CW complexes the reduced homology of the wedge is the direct sum of the reduced homologies: the quotient map from the disjoint union collapses the two basepoints to one, and the long exact sequences of the pairs split because the inclusion of the basepoints is a deformation retract on each summand. Applying this, $\widetilde H_n(S^2\vee S^1)\cong\widetilde H_n(S^2)\oplus\widetilde H_n(S^1)$.
:::

:::

::: {.pf-step #values}
$H_0(X)\cong\ZZ$, $H_1(X)\cong\ZZ$, $H_2(X)\cong\ZZ$, and $H_n(X)=0$ for $n\ge3$.

::: pf-proof
Use $\widetilde H_n(S^2)=\ZZ$ for $n=2$ and $0$ otherwise, and $\widetilde H_n(S^1)=\ZZ$ for $n=1$ and $0$ otherwise. Then step [](#reduced){.pf-ref} gives $\widetilde H_1(X)=\ZZ$, $\widetilde H_2(X)=\ZZ$ and $\widetilde H_n(X)=0$ for $n\ne1,2$. Since $X$ is path connected — it is the union of the connected sphere and the diameter meeting it — $H_0(X)=\ZZ$ with reduced part $\widetilde H_0(X)=0$. So $H_n(X)\cong\ZZ$ for $n=0,1,2$ and vanishes above, as the case distinction on the card records.
:::

:::

::: {.pf-step}
The homology of $S^2$ together with a diameter is $\ZZ$ in dimensions $0,1,2$ and $0$ in dimensions $\ge3$.

::: pf-proof
Step [](#values){.pf-ref} gives the four values, and they are all the values there are because $H_n=0$ for $n\ge3$. This answers the problem. The Mayer--Vietoris route recorded on the card gives the same answer: thickening $S^2$ and the diameter to open sets whose intersection has two contractible components reproduces $\widetilde H_1=\ZZ$, $\widetilde H_2=\ZZ$.
:::

:::

:::

:::
