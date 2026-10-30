---
schema: qual/card@1
id: P-TOPF19G
kind: problem
title: 'Two maps $T^3\to S^3$ are homotopic if and only if they have the same degree'
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Degree
  - Manifolds
relations: []
review: draft
---

::: {.problem}
Let $f$ and $g$ be two continuous maps from the three-torus $T^3 = S^1 \times S^1 \times S^1$ to the three-sphere $S^3$.
Show that $f$ is homotopic to $g$ if and only if they have the same mapping degree.
:::

::: {.solution}

::: pf

::: {.pf-step #hopf}

For a CW complex $X$ of dimension $n$, the map $[X,S^n]\to H^n(X;\ZZ)$, $[f]\mapsto f^*u$, is a bijection, where $u\in H^n(S^n;\ZZ)$ is a generator.

::: pf-proof

This is the Hopf classification theorem (Hatcher, Corollary 4.57): $S^n$ is $(n-1)$-connected with $\pi_n(S^n)\cong\ZZ$, so maps from an $n$-dimensional complex are classified by obstruction theory through the class $f^*u$.

:::

:::

::: {.pf-step #degree}

For $f:T^3\to S^3$, $f^*u=(\deg f)\,v$, where $v\in H^3(T^3;\ZZ)\cong\ZZ$ is the orientation generator.

::: pf-proof

$T^3$ and $S^3$ are closed connected oriented $3$-manifolds, $v$ and $u$ are dual to the fundamental classes, and $\langle f^*u,[T^3]\rangle=\langle u,f_*[T^3]\rangle=\deg f$.

:::

:::

::: pf-qed

$T^3$ has a CW structure of dimension $3$ (the product of three circles, each with one $0$-cell and one $1$-cell). By Steps [](#hopf){.pf-ref} and [](#degree){.pf-ref}, $f\simeq g$ if and only if $f^*u=g^*u$, which holds if and only if $\deg f=\deg g$.

:::

:::

:::
