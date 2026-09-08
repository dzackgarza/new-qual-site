---
schema: qual/card@1
id: P-ALGS13G
kind: problem
title: Finite separable degrees are $p$-powers when all finite degrees are divisible by $p$
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: problem
Let $F$ be a field and $p$ be a prime.
Suppose that the degree of any finite field extension $E/F$ is divisible by $p$.
Prove that the degree of any finite separable extension $E/F$ is a power of $p$.
:::

::: {.solution}
<1>1. Let $E/F$ be a finite separable extension, let $N$ be its normal closure over $F$, and set $G=\operatorname{Gal}(N/F)$.
::: {.proof}
Because $E/F$ is finite separable, its normal closure $N/F$ is finite Galois.
:::

<1>2. The hypothesis implies that $p\mid |G|$.
::: {.proof}
Take the finite extension $N/F$.
Since $N\ne F$ unless the claim is trivial, the hypothesis gives $p\mid [N:F]=|G|$.
:::

<1>3. Let $P$ be a Sylow $p$-subgroup of $G$.
Then $P=G$.
::: {.proof}
Suppose $P<G$.
By the Galois correspondence, the fixed field $N^P$ is a proper finite extension of $F$ and
\[
[N^P:F]=[G:P].
\]
The hypothesis therefore gives $p\mid [G:P]$.
But $P$ is a Sylow $p$-subgroup, so $[G:P]$ is relatively prime to $p$.
This contradiction shows $P=G$.
:::

<1>4. Hence $G$ is a $p$-group.
::: {.proof}
By <1>3, $G=P$, and $P$ has order a power of $p$.
:::

<1>5. Let $H=\operatorname{Gal}(N/E)$.
Then
\[
[E:F]=[G:H],
\]
so $[E:F]$ is a power of $p$.
::: {.proof}
The Galois correspondence gives $[E:F]=[G:H]$.
Since $G$ is a finite $p$-group, every subgroup index is a power of $p$.
:::

<1>6. Therefore every finite separable extension of $F$ has degree a power of $p$.
::: {.proof}
This is exactly <1>5.
:::
:::
