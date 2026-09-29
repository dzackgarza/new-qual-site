---
schema: qual/card@1
id: P-TOPS01A
kind: problem
title: "Topological proof of the fundamental theorem of algebra"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Covering Spaces
relations: []
review: draft
---

::: {.problem}
Let $p(z) = a_n z^n + a_{n-1} z^{n-1} + \cdots + a_0$ (where $a_n \neq 0$, and $n \geq 1$) be a complex polynomial.
Prove by a topological argument that $p$ must have a root in the complex plane.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Suppose, for contradiction, that $p(z)$ has no zero in $\mathbb C$.

::: pf-proof

Then $p$ defines a continuous map $\mathbb C\to\mathbb C^*$.

:::

:::

::: {.pf-step #s2}

Choose $R>0$ so large that on $|z|=R$,
$$
|a_{n-1}z^{n-1}+\cdots+a_0|<|a_nz^n|.
$$

::: pf-proof

After dividing by $R^n$, the lower-degree terms tend uniformly to zero on the circle as $R\to\infty$, while $|a_nz^n|=|a_n|R^n$.

:::

:::

::: pf-step

The loop $p|_{|z|=R}:S^1\to\mathbb C^*$ is homotopic in $\mathbb C^*$ to the loop $z\mapsto a_nz^n$.

::: pf-proof

Use the straight-line homotopy
$$
H_t(z)=a_nz^n+t(a_{n-1}z^{n-1}+\cdots+a_0).
$$
By step [](#s2){.pf-ref},
$$
|H_t(z)-a_nz^n|<|a_nz^n|,
$$
so $H_t(z)\ne0$ for every $t\in[0,1]$ and $|z|=R$.

:::

:::

::: {.pf-step #s4}

Hence the winding number of $p|_{|z|=R}$ about $0$ is $n$.

::: pf-proof

The loop $z\mapsto a_nz^n$ winds exactly $n$ times around the origin, and winding number is invariant under homotopy in $\mathbb C^*$.

:::

:::

::: {.pf-step #s5}

But $p|_{|z|=R}$ extends over the disk $|z|\le R$ as a map into $\mathbb C^*$, so it must be null-homotopic and have winding number $0$.

::: pf-proof

Under the assumption in step [](#s1){.pf-ref}, $p$ never vanishes on the whole disk. The boundary of a disk represents the trivial element of the fundamental group after extending across the disk.

:::

:::

::: pf-step

Since $n\ge1$, steps [](#s4){.pf-ref} and [](#s5){.pf-ref} contradict each other. Therefore $p$ has a zero in $\mathbb C$.

::: pf-proof

A loop in $\mathbb C^*$ cannot simultaneously have winding numbers $n\ne0$ and $0$.

:::

:::

:::

:::
