---
schema: qual/card@1
id: P-TOPF08D
kind: problem
title: $\pi_n(\mathbb{RP}^n\vee S^n)$ for $n>1$
classification:
  areas:
  - topology
  topics:
  - Homotopy Groups
  - Projective Spaces
relations: []
review: draft
---

::: {.problem}
Calculate $\pi_n(\mathbb{RP}^n \vee S^n)$ for $n > 1$.
:::

::: {.solution}
<1>1. Let
$$
X=\mathbb{RP}^n\vee S^n,\qquad n>1.
$$
Then $\pi_1(X)\cong\mathbb Z/2$.
::: {.proof}
The sphere $S^n$ is simply connected for $n>1$, while $\pi_1(\mathbb{RP}^n)\cong\mathbb Z/2$.
:::

<1>2. The universal cover $\widetilde X$ is obtained from $S^n\to\mathbb{RP}^n$ by attaching one copy of $S^n$ at each of the two lifts of the wedge point. Hence
$$
\widetilde X\simeq S^n\vee S^n\vee S^n.
$$
::: {.proof}
The fiber over the wedge point has two points. Pulling up the simply connected wedge summand attaches a copy of $S^n$ at each lift. Moving the two attachment points together along an arc in the covering sphere and collapsing the arc yields a wedge of three $n$-spheres up to homotopy.
:::

<1>3. The space $\widetilde X$ is $(n-1)$-connected and
$$
H_n(\widetilde X;\mathbb Z)\cong\mathbb Z^3.
$$
::: {.proof}
A wedge of $n$-spheres has no homotopy below degree $n$ and its $n$th homology is the free abelian group on the sphere summands.
:::

<1>4. By the Hurewicz theorem,
$$
\pi_n(\widetilde X)\cong H_n(\widetilde X)\cong\mathbb Z^3.
$$
::: {.proof}
The first nonzero homotopy group of an $(n-1)$-connected space is identified with its $n$th homology group.
:::

<1>5. Covering maps induce isomorphisms on homotopy groups in degrees at least $2$. Therefore
$$
\boxed{\pi_n(\mathbb{RP}^n\vee S^n)\cong\mathbb Z^3.}
$$
::: {.proof}
Apply the universal covering map $\widetilde X\to X$ to <1>4.
:::
:::
