---
schema: qual/card@1
id: P-TOP-WORKSHOP-D9-01
kind: problem
title: Homology of $T\times[-1,1]$ with each end $T\times\{\pm 1\}$ collapsed to a
  point
classification:
  areas:
  - topology
  topics:
  - Homology
  - Quotient Spaces
  - Surfaces
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
    Restructured into a structured proof under #2. Re-checked: the relation collapses $T\times\{-1\}$
    and $T\times\{1\}$ each to a point and leaves $T\times(-1,1)$ alone, so $X$ is the unreduced
    suspension; the suspension isomorphism $\widetilde H_n(\Sigma T)\cong\widetilde H_{n-1}(T)$
    follows from Mayer--Vietoris on the two cones; $H_*(T)$ is $\ZZ,\ZZ^2,\ZZ$ in degrees $0,1,2$;
    and the shift gives $\ZZ$ in $0$, $0$ in $1$, $\ZZ^2$ in $2$, $\ZZ$ in $3$, zero above. Added:
    the identity $\widetilde H_0(\Sigma T)=0$ (from $\widetilde H_0(T)=0$), which the earlier text
    passed over and which is what makes $H_1(X)=0$ rather than $\ZZ$, and the conversion from
    reduced to unreduced homology in degree $0$. No defect found in the statement. The collection's
    provenance is the worksheet, so no retained solution set covers the item.
---

::: {.problem}
(Michigan Sept ’10) Consider the 2-dimensional torus $T$ and the topological space $$X=T\times[-1,1]/\sim$$ where $(x,t)\sim(x',t')$ if either $(x,t)=(x',t')$ or $t=t'\in\{-1,1\}$.
Compute $H_*(X,\ZZ)$.
:::

::: {.solution}
No retained solution set covers this item, the collection's provenance being the worksheet, so the computation is the card's own; it identifies $X$ as a suspension and uses the suspension isomorphism.

::: pf

::: {.pf-step #suspension}
$X=T\times[-1,1]/\!\sim$ is the unreduced suspension $\Sigma T$ of the torus.

::: pf-proof
The relation identifies $(x,t)$ with $(x',t')$ whenever $t=t'\in\{-1,1\}$, and otherwise only a point with itself. So each of $T\times\{-1\}$ and $T\times\{1\}$ is collapsed to a single point, while $T\times(-1,1)$ is embedded unchanged; that is exactly the quotient by collapsing $T\times\{-1\}$ and $T\times\{1\}$ to two cone points, namely $\Sigma T=T\times[-1,1]/(T\times\{\pm1\})$.
:::

:::

::: {.pf-step #shift}
$\widetilde H_n(\Sigma T;\ZZ)\cong\widetilde H_{n-1}(T;\ZZ)$ for all $n$.

::: pf-proof
The unreduced suspension of a space is the union of two cones on it meeting in a copy of the space, and the Mayer--Vietoris sequence of that cover, together with contractibility of the cones, gives the suspension isomorphism $\widetilde H_n(\Sigma T)\cong\widetilde H_{n-1}(T)$ for every $n$. Equivalently the suspension is the reduced suspension up to homotopy and the shift is the standard one.
:::

:::

::: {.pf-step #torus}
$H_0(T)=\ZZ$, $H_1(T)=\ZZ^2$, $H_2(T)=\ZZ$, and $H_k(T)=0$ for $k\ge3$.

::: pf-proof
$T=S^1\times S^1$ with the product CW structure of one $0$-cell, two $1$-cells and one $2$-cell; its cellular chain complex has zero boundary maps because the attaching maps have degree $0$ in the relevant degrees, so the homology is $\ZZ$ in degrees $0,2$ and $\ZZ^2$ in degree $1$, nothing above. Equivalently Künneth gives $H_*(S^1)\otimes H_*(S^1)$.
:::

:::

::: {.pf-step}
$\boxed{H_n(X;\ZZ)=\ZZ,\ 0,\ \ZZ^2,\ \ZZ$ for $n=0,1,2,3$ and $0$ for $n\ge4$.

::: pf-proof
$X$ is connected, so $H_0(X)=\ZZ$ and $\widetilde H_0(X)=0$. For $n\ge1$, step [](#shift){.pf-ref} gives $\widetilde H_n(X)=\widetilde H_{n-1}(T)$, which by step [](#torus){.pf-ref} is $\ZZ$ for $n-1=0$ or $2$ and $\ZZ^2$ for $n-1=1$, and vanishes otherwise; since $\widetilde H_0(T)=0$, we get $\widetilde H_1(X)=0$. Converting to unreduced homology, which differs from reduced only in degree $0$, gives the stated table: $H_1(X)=0$, $H_2(X)=\ZZ^2$, $H_3(X)=\ZZ$, and $0$ beyond. Step [](#suspension){.pf-ref} identifies $X$ with $\Sigma T$.
:::

:::

:::
:::
