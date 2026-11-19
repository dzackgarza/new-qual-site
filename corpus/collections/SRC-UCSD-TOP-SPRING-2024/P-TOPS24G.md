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
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read in the retained exam assets/attachments/SP24_290_Topology_Qual.pdf,
    problem 7: the CW complex obtained by attaching k two-cells to S^1 by maps
    of degrees n_1,...,n_k, and the request to compute pi_2(X) in terms of those
    degrees. The card agrees.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Both cases are right. With d the gcd of the degrees, the two-cells impose
    t^{n_i} = 1 on the generator of pi_1(S^1), so pi_1(X) = Z/d, and the
    universal cover has d sheets, hence d vertices and d one-cells forming a
    cycle and dk two-cells. Each lift of the i-th two-cell has cellular boundary
    (n_i/d) z on the fundamental cycle of the lifted circle, and since the
    integers n_i/d have gcd 1 those boundaries generate Z z, so the boundary has
    rank 1 and its kernel has rank dk - 1; the cover is simply connected, so
    Hurewicz and the isomorphism of pi_2 with that of the cover give
    pi_2(X) = Z^{dk-1}. When every n_i vanishes the two-cells are attached by
    nullhomotopic maps, X is S^1 wedge k two-spheres, the universal cover is the
    line with k two-spheres over each vertex, and collapsing the contractible
    line gives a wedge of two-spheres indexed by Z times {1,...,k}, whose second
    homology, hence pi_2 by Hurewicz, is the direct sum of that many copies of Z.
    Nothing was changed.
---

::: {.problem}
Let $X$ be the CW complex formed by attaching $k$ two-cells $e^2_1, \ldots, e^2_k$ to the circle $S^1\ (= e^0 \cup e^1)$ via attaching maps with degrees $n_1, n_2, \ldots, n_k$.
Compute $\pi_2(X)$ in terms of $n_1, \ldots, n_k$.
:::

::: {.solution}
Let $d=\gcd(n_1,\dots,n_k)$, taken nonnegative.

::: pf

::: pf-step
If at least one $n_i$ is nonzero, so $d>0$, then
$$
\pi_1(X)\cong\ZZ/d.
$$

::: pf-proof
Starting from $\pi_1(S^1)=\langle t\rangle\cong\ZZ$, attaching the $i$-th $2$-cell imposes $t^{n_i}=1$. Thus
$$
\pi_1(X)\cong \ZZ/\langle n_1,\dots,n_k\rangle\cong\ZZ/d.
$$
:::

:::

::: pf-step
For $d>0$, the universal cover $\widetilde X$ has $d$ vertices, $d$ one-cells forming a cycle, and $dk$ two-cells.

::: pf-proof
The universal cover has $d$ sheets. Each cell of $X$ has $d$ lifts. The lifted $1$-skeleton is the connected $d$-sheeted cover of $S^1$, hence a $d$-edge circle.
:::

:::

::: {.pf-step #boundary-formula}
If $z=e_0+\cdots+e_{d-1}\in C_1(\widetilde X)$ is the fundamental cycle of the lifted circle, then every lift of the $i$-th $2$-cell has cellular boundary $(n_i/d)z$ up to cyclic choice of starting vertex.

::: pf-proof
The attaching loop has degree $n_i$ downstairs. Since $d\mid n_i$, its lift to the $d$-fold circle closes after traversing that lifted circle $n_i/d$ times. A full traversal has cellular chain $z$.
:::

:::

::: {.pf-step #h2-universal-cover}
Hence $\operatorname{im}\partial_2=\ZZ z$ and
$$
H_2(\widetilde X)=\ker\partial_2\cong\ZZ^{dk-1}.
$$

::: pf-proof
The numbers $n_i/d$ have gcd $1$, so the boundaries in step [](#boundary-formula){.pf-ref} generate $\ZZ z$. Thus $\partial_2:\ZZ^{dk}\to\ZZ^d$ has rank $1$. Its kernel is a subgroup of a free abelian group, hence free, and has rank $dk-1$.
:::

:::

::: pf-step
For $d>0$,
$$
\boxed{\pi_2(X)\cong\ZZ^{dk-1}.}
$$

::: pf-proof
The universal covering induces an isomorphism $\pi_2(X)\cong\pi_2(\widetilde X)$. Since $\widetilde X$ is simply connected, the Hurewicz theorem gives $\pi_2(\widetilde X)\cong H_2(\widetilde X)$. Apply step [](#h2-universal-cover){.pf-ref}.
:::

:::

::: pf-step
If all $n_i=0$, then
$$
X\simeq S^1\vee\bigvee_{i=1}^k S^2
$$
and
$$
\boxed{\pi_2(X)\cong\bigoplus_{(m,i)\in\ZZ\times\{1,\dots,k\}}\ZZ.}
$$

::: pf-proof
A degree-$0$ attaching map $S^1\to S^1$ is nullhomotopic, so attaching each $2$-cell wedges on an $S^2$. The universal cover has $1$-skeleton the line $\RR$ with vertices indexed by $m\in\ZZ$, and at every vertex there are $k$ lifted $2$-spheres. Collapsing the contractible lifted $1$-skeleton gives a wedge of countably many $2$-spheres, indexed by $\ZZ\times\{1,\dots,k\}$. Therefore
$$
H_2(\widetilde X)\cong\bigoplus_{\ZZ\times\{1,\dots,k\}}\ZZ,
$$
and Hurewicz gives the same group for $\pi_2$.
:::

:::

:::

:::
