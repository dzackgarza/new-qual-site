---
schema: qual/card@1
id: T-IJW1K
kind: theorem
title: The cohomology of $\OO_{\PP^n}(d)$
slogan: 'Twists on projective space have cohomology only at the ends: $H^0$ for nonnegative degree, $H^n$ for sufficiently negative degree, and nothing in between.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cohomology
  - Twisting Sheaves
  - Serre Duality
relations:
- kind: uses
  target: D-CB9XS
- kind: uses
  target: D-PTIW0
review: draft
prompts:
- Compute $H^*(\PP^n, \OO(d))$.
- What is $H^0(\PP^1, \Omega^1)$?
---

::: {.theorem}
Let $A$ be a ring, let $n\ge1$, put $S=A[x_0,\ldots,x_n]$, and write $\PP^n=\PP_A^n$.
Then

- $H^0(\PP^n, \OO(d)) = S_d$, a free $A$-module of rank $\binom{n+d}{n}$ for $d \geq 0$, and $0$ for $d < 0$;

- $H^n(\PP^n,\OO(d))$ is the free $A$-module on the monomials $x_0^{a_0}\cdots x_n^{a_n}$ with every $a_i\le-1$ and $\sum_i a_i=d$.
  It is zero for $d>-n-1$ and has rank $\binom{-d-1}{n}$ for $d\le-n-1$.
  It is $A$-linearly dual to $S_{-d-n-1}$;

- $H^p(\PP^n, \OO(d)) = 0$ for $0 < p < n$ and for $p > n$, for every $d$.

[@Har10a, Theorem III.5.1] The [projective-space cohomology calculation](https://stacks.math.columbia.edu/tag/01XS) gives these formulas over every ring $A$.
:::

::: {.remark title="Projective dimension zero"}
For $n=0$, the scheme $\PP_A^0$ is $\Spec A$, and every $\OO(d)$ is trivial.
Thus $H^0(\PP_A^0,\OO(d))\cong A$ for every integer $d$, and all positive-degree cohomology groups vanish.
The negative-degree sections are represented on its single standard chart by $Ax_0^d$, as in [[P-AGH2510SATIDEAL]], step 4.1.
:::

::: {.remark title="Consequences over a field"}
For $n\ge2$, $H^1(\PP_k^n,\OO(d))=0$ for every integer $d$.
On $\PP_k^1$, one has
$$
h^0(\OO(d))=\max\{d+1,0\},\qquad
h^1(\OO(d))=\max\{-d-1,0\}=h^0(\OO(-d-2)).
$$
In particular $h^1(\OO(-2))=1$.
The [[T-MODEULER|Euler sequence]] gives $\Omega_{\PP_k^1/k}^1\cong\OO(-2)$, so the projective line has no nonzero global regular differentials.
The duality between the top and bottom groups is [[T-COHSD|Serre duality]], with canonical sheaf $\omega_{\PP_k^n}=\OO(-n-1)$.
:::
