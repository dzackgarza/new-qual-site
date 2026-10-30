---
schema: qual/card@1
id: P-UCTOP-FA11-5
kind: problem
title: 'No free $\ZZ/2$ action on a $4$-manifold with $H_2$ of rank $1$'
classification:
  areas:
  - topology
  topics:
  - Manifolds
relations: []
review: draft
---

::: {.problem}
Let $M$ be a closed oriented 4-manifold whose second homology $H_2(M; \ZZ)$ has rank 1. Show that there does not exist a free action of the group $\ZZ_2$ on $M$.
:::

::: {.solution}

::: pf

::: pf-step
Suppose a free $\ZZ/2$-action existed and let $N=M/(\ZZ/2)$.

::: pf-proof
A free action of a finite group on a manifold gives a covering map $M\to N$ of degree $2$.
:::

:::

::: {.pf-step #euler-char-even}
Euler characteristic would satisfy
$$
\chi(M)=2\chi(N),
$$
so $\chi(M)$ would be even.

::: pf-proof
Euler characteristic multiplies by the degree of a finite covering of finite CW complexes; closed manifolds have finite CW type.
:::

:::

::: {.pf-step #euler-char-odd}
On the other hand, $\chi(M)$ is odd.

::: pf-proof
Since $M$ is closed and oriented of dimension $4$, Poincaré duality over $\QQ$ gives
$$
b_4=b_0,\qquad b_3=b_1.
$$
The hypothesis says $b_2=1$. Hence
$$
\chi(M)=b_0-b_1+b_2-b_3+b_4=2b_0-2b_1+1,
$$
which is odd.
:::

:::

::: pf-step
This contradiction proves that no free $\ZZ/2$-action exists on $M$.

::: pf-proof
Steps [](#euler-char-even){.pf-ref} and [](#euler-char-odd){.pf-ref} give incompatible parities for $\chi(M)$.
:::

:::

:::

:::

::: {.remark title="Variations"}
The Fall 2014 exam asks the same question with $M$ also assumed connected.
:::
