---
schema: qual/card@1
id: P-UCTOP-SU01-1
kind: problem
title: Fundamental theorem of algebra by topological argument
classification:
  areas:
  - topology
  topics:
  - Degree
relations: []
review: draft
---

::: {.problem}
Let $p(z) = a_n z^n + a_{n-1} z^{n-1} + \cdots + a_0$ (where $a_n \neq 0$, and $n \geq 1$) be a complex polynomial.
Prove by a topological argument that $p$ must have a root in the complex plane.
:::

::: {.solution}

::: pf

::: {.pf-step #suppose-no-root}
Suppose, for contradiction, that $p(z)\ne0$ for every $z\in\mathbb C$.

::: pf-proof
Then the normalized map
$$
F(z)=\frac{p(z)}{|p(z)|}
$$
is a continuous map $\mathbb C\to S^1$.
:::

:::

::: {.pf-step #degree-zero}
For every $R>0$, the restriction
$$
F_R:S^1\to S^1,\qquad F_R(\zeta)=\frac{p(R\zeta)}{|p(R\zeta)|}
$$
has degree $0$.

::: pf-proof
The map $F_R$ extends over the disk $D^2$ by
$$
\widetilde F_R(w)=\frac{p(Rw)}{|p(Rw)|},\qquad |w|\le1,
$$
which is well-defined by step [](#suppose-no-root){.pf-ref}. Any map $S^1\to S^1$ extending to the disk is null-homotopic, hence has degree $0$.
:::

:::

::: {.pf-step #homotopic-to-leading-term}
For all sufficiently large $R$, the loop $\zeta\mapsto p(R\zeta)$ in $\mathbb C\setminus\{0\}$ is homotopic to $\zeta\mapsto a_nR^n\zeta^n$.

::: pf-proof
Choose $R$ so large that
$$
\sum_{j=0}^{n-1}|a_j|R^j<|a_n|R^n.
$$
For $0\le t\le1$ set
$$
H_t(\zeta)=a_nR^n\zeta^n+t\sum_{j=0}^{n-1}a_jR^j\zeta^j.
$$
On $|\zeta|=1$,
$$
|H_t(\zeta)|\ge |a_n|R^n-\sum_{j<n}|a_j|R^j>0,
$$
so $H_t$ is a homotopy through loops in $\mathbb C\setminus\{0\}$.
:::

:::

::: pf-step
For such $R$, the map $F_R$ has degree $n$.

::: pf-proof
Normalizing the homotopy in step [](#homotopic-to-leading-term){.pf-ref} gives a homotopy in $S^1$ from $F_R$ to
$$
\zeta\longmapsto \frac{a_n}{|a_n|}\zeta^n.
$$
Multiplication by the constant $a_n/|a_n|$ has degree $1$ on the target and does not alter the winding number, while $\zeta\mapsto\zeta^n$ has degree $n$. Hence $\deg F_R=n$.
:::

:::

::: pf-step
This contradicts step [](#degree-zero){.pf-ref} because $n\ge1$.

::: pf-proof
The same map $F_R$ cannot simultaneously have degree $0$ and degree $n\ne0$.
:::

:::

::: pf-step
Therefore $p$ has a root in $\mathbb C$.

::: pf-proof
The assumption in step [](#suppose-no-root){.pf-ref} is false.
:::

:::

:::

:::

