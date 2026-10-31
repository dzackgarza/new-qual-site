---
schema: qual/card@1
id: P-AGH411REGULAROUTSIDEP
kind: problem
title: Existence of a rational function regular away from a single point
classification:
  areas:
  - algebraic-geometry
  topics:
  - Riemann-Roch
  - Linear Systems
  - Divisors
relations: []
review: draft
---

::: {.problem}
Let $X$ be a curve, and let $P \in X$ be a point.
Then there exists a nonconstant rational function $f \in K(X)$, which is regular everywhere except at $P$.
:::

::: {.solution}
Let $g$ be the genus of $X$, and for $n\ge0$ let $\ell(nP)=h^0(X,\mcl(nP))$.

::: pf

::: {.pf-step #s1}

If $n>2g-2$, then $\ell(nP)=n+1-g$.

::: pf-proof

By Riemann-Roch, $\ell(nP)-\ell(K-nP)=\deg(nP)+1-g=n+1-g$. The divisor $K-nP$ has degree $2g-2-n<0$, so $\ell(K-nP)=0$.

:::

:::

::: {.pf-step #s2}

For $n=\max(2g,1)$ one has $\ell(nP)\ge2$.

::: pf-proof

Since $n>2g-2$, step [](#s1){.pf-ref} gives $\ell(nP)=n+1-g$. If $g\ge1$ this is $g+1\ge2$; if $g=0$ it is $2$.

:::

:::

::: pf-qed

Fix $n$ as in step [](#s2){.pf-ref}. The constants form a one-dimensional subspace of $\globsec{X; \mcl(nP)}=\{f\in K(X) \st f=0 \text{ or } (f)+nP\ge0\}$, so this space contains a nonconstant $f$. The condition $(f)+nP\ge0$ says that $f$ is regular at every point other than $P$.

:::

:::

:::
