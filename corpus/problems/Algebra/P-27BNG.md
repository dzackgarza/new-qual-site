---
schema: qual/card@1
id: P-27BNG
kind: problem
title: Intermediate fields of a finite cyclic Galois extension
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
relations: []
review: draft
---

::: {.problem}
Let $K/F$ be a finite Galois extension and suppose $\Gal(K/F)$ is cyclic. Let $F\subseteq E\subseteq K$.

(a) Show that both $K/E$ and $E/F$ are cyclic Galois extensions.

(b) If $[K:F]=n$, show that for every divisor $d\mid n$ there is a unique intermediate field $E_d$ with
$$
[E_d:F]=d.
$$
:::

::: {.solution}
Let $G=\Gal(K/F)$ and $H=\Gal(K/E)$.

::: pf

::: pf-step
(a) $K/E$ and $E/F$ are cyclic Galois extensions.

::: pf-proof
Since $K/F$ is Galois, so is $K/E$, with group $H\le G$. A subgroup of a cyclic group is cyclic, so $K/E$ is cyclic Galois.
A subgroup of a cyclic group is normal, so $H\trianglelefteq G$. By the fundamental theorem of Galois theory, $E/F$ is Galois and restriction gives
$$
\Gal(E/F)\cong G/H.
$$
A quotient of a cyclic group is cyclic, so $E/F$ is cyclic Galois.
:::

:::

::: pf-step
(b) For every divisor $d\mid n$ there is a unique intermediate field $E_d$ with $[E_d:F]=d$.

::: pf-proof
Write $G=\langle g\rangle$ with $\abs{G}=n$. For each divisor $d\mid n$, the cyclic group $G$ has a unique subgroup of index $d$, namely
$$
H_d=\langle g^d\rangle,\qquad \abs{H_d}=n/d.
$$
By the Galois correspondence, intermediate fields $E$ with $[E:F]=d$ correspond bijectively to subgroups of index $d$, via $E\mapsto\Gal(K/E)$ and $H\mapsto K^H$. Hence $E_d=K^{H_d}$ is the unique intermediate field with $[E_d:F]=[G:H_d]=d$.
:::

:::

:::

:::

::: {.remark}
The intermediate-field lattice of a finite cyclic Galois extension is therefore the divisor lattice of $[K:F]$.
:::
