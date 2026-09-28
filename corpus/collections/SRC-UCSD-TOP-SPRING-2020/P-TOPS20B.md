---
schema: qual/card@1
id: P-TOPS20B
kind: problem
title: "No map from S^{2n} to itself avoiding both x and -x"
classification:
  areas:
  - topology
  topics:
  - Fixed Point Theory
  - Antipodal Map
  - Spheres
relations: []
review: draft
---

::: {.problem}
Let $n$ be a positive even number.
Show that there does not exist a continuous map $f : S^n \to S^n$ such that for any $\vec{x} \in S^n$, we have $f(\vec{x}) \neq \vec{x}$ and $f(\vec{x}) \neq -\vec{x}$.
:::

::: {.solution}
<1>1. If a map $f:S^n\to S^n$ has no fixed point, then it is homotopic to the antipodal map.
::: {.proof}
The normalized straight-line homotopy
$$H_t(x)=\frac{(1-t)f(x)-tx}{\|(1-t)f(x)-tx\|}$$
is well-defined: the denominator could vanish only when $f(x)=x$. At $t=0$ it is $f$ and at $t=1$ it is $-x$.
:::

<1>2. Hence, for even $n$,
$$\deg f=\deg(-\operatorname{id})=(-1)^{n+1}=-1.$$
::: {.proof}
Degree is invariant under homotopy, and the antipodal map on $S^n$ has degree $(-1)^{n+1}$.
:::

<1>3. If also $f(x)\ne-x$ for every $x$, then $f$ is homotopic to the identity.
::: {.proof}
Now use
$$K_t(x)=\frac{(1-t)f(x)+tx}{\|(1-t)f(x)+tx\|}.$$
Its denominator could vanish only if $f(x)=-x$. Thus it gives a homotopy from $f$ to $\operatorname{id}$.
:::

<1>4. This would force $\deg f=1$, contradicting <1>2. Therefore no such map exists.
::: {.proof}
Homotopic maps have equal degree, while $1\ne-1$ in $\mathbb Z$.
:::
:::
