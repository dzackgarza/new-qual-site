---
schema: qual/card@1
id: P-TOPS24G
kind: problem
title: Second homotopy group of a circle with 2-cells attached
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Let $X$ be the CW complex formed by attaching $k$ two-cells $e^2_1, \ldots, e^2_k$ to the circle $S^1\ (= e^0 \cup e^1)$ via attaching maps with degrees $n_1, n_2, \ldots, n_k$.
Compute $\pi_2(X)$ in terms of $n_1, \ldots, n_k$.
:::

::: {.solution}
Let $d=\gcd(n_1,\dots,n_k)$, taken nonnegative.

<1>1. If at least one $n_i$ is nonzero, so $d>0$, then
$$
\pi_1(X)\cong\mathbb Z/d.
$$
::: {.proof}
Starting from $\pi_1(S^1)=\langle t\rangle\cong\mathbb Z$, attaching the $i$-th $2$-cell imposes $t^{n_i}=1$. Thus
$$
\pi_1(X)\cong \mathbb Z/\langle n_1,\dots,n_k\rangle\cong\mathbb Z/d.
$$
:::

<1>2. For $d>0$, the universal cover $\widetilde X$ has $d$ vertices, $d$ one-cells forming a cycle, and $dk$ two-cells.
::: {.proof}
The universal cover has $d$ sheets. Each cell of $X$ has $d$ lifts. The lifted $1$-skeleton is the connected $d$-sheeted cover of $S^1$, hence a $d$-edge circle.
:::

<1>3. If $z=e_0+\cdots+e_{d-1}\in C_1(\widetilde X)$ is the fundamental cycle of the lifted circle, then every lift of the $i$-th $2$-cell has cellular boundary $(n_i/d)z$ up to cyclic choice of starting vertex.
::: {.proof}
The attaching loop has degree $n_i$ downstairs. Since $d\mid n_i$, its lift to the $d$-fold circle closes after traversing that lifted circle $n_i/d$ times. A full traversal has cellular chain $z$.
:::

<1>4. Hence $\operatorname{im}\partial_2=\mathbb Z z$ and
$$
H_2(\widetilde X)=\ker\partial_2\cong\mathbb Z^{dk-1}.
$$
::: {.proof}
The numbers $n_i/d$ have gcd $1$, so the boundaries in <1>3 generate $\mathbb Z z$. Thus $\partial_2:\mathbb Z^{dk}\to\mathbb Z^d$ has rank $1$. Its kernel is a subgroup of a free abelian group, hence free, and has rank $dk-1$.
:::

<1>5. For $d>0$,
$$
\boxed{\pi_2(X)\cong\mathbb Z^{dk-1}.}
$$
::: {.proof}
The universal covering induces an isomorphism $\pi_2(X)\cong\pi_2(\widetilde X)$. Since $\widetilde X$ is simply connected, the Hurewicz theorem gives $\pi_2(\widetilde X)\cong H_2(\widetilde X)$. Apply <1>4.
:::

<1>6. If all $n_i=0$, then
$$
X\simeq S^1\vee\bigvee_{i=1}^k S^2
$$
and
$$
\boxed{\pi_2(X)\cong\bigoplus_{(m,i)\in\mathbb Z\times\{1,\dots,k\}}\mathbb Z.}
$$
::: {.proof}
A degree-$0$ attaching map $S^1\to S^1$ is nullhomotopic, so attaching each $2$-cell wedges on an $S^2$. The universal cover has $1$-skeleton the line $\mathbb R$ with vertices indexed by $m\in\mathbb Z$, and at every vertex there are $k$ lifted $2$-spheres. Collapsing the contractible lifted $1$-skeleton gives a wedge of countably many $2$-spheres, indexed by $\mathbb Z\times\{1,\dots,k\}$. Therefore
$$
H_2(\widetilde X)\cong\bigoplus_{\mathbb Z\times\{1,\dots,k\}}\mathbb Z,
$$
and Hurewicz gives the same group for $\pi_2$.
:::
:::
