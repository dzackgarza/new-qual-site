---
schema: qual/card@1
id: P-AGXGATHRADICAL
kind: problem
title: Radical of $\generators{x_1^3 - x_2^6,\, x_1x_2 - x_2^3}$ in $\CC[x_1,x_2]$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Radical Ideals
  - Nullstellensatz
  - Vanishing Loci
relations: []
review: draft
---

::: {.problem}
Determine $\sqrt{I}$ for
$$
I\definedas \generators{x_1^3 - x_2^6,\, x_1 x_2 - x_2^3} \normal \CC[x_1, x_2]
.$$
:::

::: {.solution}
Write $x=x_1$, $y=x_2$, and $I=\generators{x^3-y^6,\ xy-y^3}$. For $S\subseteq\AA^2$ let $\mci(S)$ be the ideal of polynomials in $\CC[x,y]$ vanishing on $S$.

::: pf

::: {.pf-step #nss}
For every ideal $J\normal\CC[x,y]$, $\sqrt J=\mci(V(J))$.

::: pf-proof
This is Hilbert's Nullstellensatz over the algebraically closed field $\CC$.
:::

:::

::: {.pf-step #locus}
$V(I)=V(x-y^2)=\theset{(t^2,t)\st t\in\CC}$.

::: pf-proof
Since $xy-y^3=y(x-y^2)$, a point of $V(I)$ has $y=0$ or $x=y^2$. If $y=0$, then $x^3=0$, so the point is $(0,0)$, which satisfies $x=y^2$. Conversely, if $x=y^2$, then $x^3-y^6=0$ and $xy-y^3=0$. Hence $V(I)=V(x-y^2)$, the parabola $\theset{(t^2,t)}$.
:::

:::

::: {.pf-step #prime}
The ideal $\generators{x-y^2}$ is prime, hence radical.

::: pf-proof
The ring map $\CC[x,y]\to\CC[y]$, $x\mapsto y^2$, $y\mapsto y$, is surjective. Its kernel is $\generators{x-y^2}$: dividing by $x-y^2$, which is monic in $x$, writes every polynomial as $(x-y^2)q+r(y)$, and $r(y)$ maps to $r(y)$, which is $0$ only if $r=0$. The image $\CC[y]$ is a domain, so the kernel is prime.
:::

:::

::: pf-qed
By steps [](#nss){.pf-ref} and [](#locus){.pf-ref}, $\sqrt I=\mci(V(I))=\mci(V(x-y^2))=\sqrt{\generators{x-y^2}}$, and by step [](#prime){.pf-ref} this equals $\generators{x-y^2}$. So $\sqrt I=\generators{x_1-x_2^2}$.
:::

:::
:::
