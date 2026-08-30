---
schema: qual/card@1
id: P-HCAO8
kind: problem
title: Rings in which every prime ideal is maximal
classification:
  areas:
  - algebra
  topics:
  - commutative algebra
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Give a general class of rings in which every prime ideal is maximal.
:::

::: {.solution}
<1>1. **Class 1: Commutative Artinian Rings.** <2>1. A commutative ring $R$ is Artinian if it satisfies the descending chain condition on ideals.
Proof: definition.
<2>2. In any commutative Artinian ring $R$, every prime ideal is maximal (i.e., $\dim R = 0$). Proof: let $\mathfrak{p} \subseteq R$ be a prime ideal; then $D = R/\mathfrak{p}$ is an Artinian integral domain.
For any non-zero element $x \in D$, the descending chain of principal ideals $(x) \supseteq (x^2) \supseteq (x^3) \supseteq \cdots$ must stabilize, so $(x^n) = (x^{n+1})$ for some $n \ge 1$.
Thus $x^n = x^{n+1} y$ for some $y \in D$.
Since $D$ is an integral domain and $x \neq 0$, we may cancel $x^n$ to get $1 = xy$, showing $x$ is invertible.
Hence $D$ is a field, so $\mathfrak{p}$ is maximal.
<2>3. Examples include all finite commutative rings, fields, and finite-dimensional algebras over a field $k[x_1,\dots,x_n]/I$ with $\dim_k < \infty$.
Proof: finite rings and finite-dimensional algebras are Artinian.

<1>2. **Class 2: Boolean Rings and von Neumann Regular Rings.** <2>1. A Boolean ring is a ring $R$ in which $x^2 = x$ for every $x \in R$.
Proof: definition.
<2>2. In a Boolean ring, every prime ideal $\mathfrak{p}$ is maximal.
Proof: let $\mathfrak{p}$ be a prime ideal; then $R/\mathfrak{p}$ is an integral domain in which every element is idempotent: $\bar{x}^2 = \bar{x}$.
In an integral domain, $\bar{x}(\bar{x} - 1) = 0$ implies $\bar{x} = 0$ or $\bar{x} = 1$.
Thus $R/\mathfrak{p} \cong \mathbb{F}_2$, which is a field, so $\mathfrak{p}$ is maximal.
<2>3. More generally, in a commutative von Neumann regular ring (where for each $x \in R$ there is $y \in R$ with $x^2 y = x$), every prime ideal is maximal.
Proof: in $R/\mathfrak{p}$, $\bar{x}^2 \bar{y} = \bar{x} \implies \bar{x}(\bar{x}\bar{y} - 1) = 0$; if $\bar{x} \neq 0$, then $\bar{x}\bar{y} = 1$, so every non-zero element is invertible.

<1>3. **Class 3: Integral Extensions of Fields.** <2>1. If $R$ is an integral extension of a field $k$, then every prime ideal of $R$ is maximal.
Proof: by the Going-Up theorem for integral extensions, $\dim R = \dim k = 0$; directly, for any prime $\mathfrak{p} \subseteq R$, $R/\mathfrak{p}$ is an integral domain that is integral over the field $k \hookrightarrow R/\mathfrak{p}$, and any integral domain that is integral over a field is itself a field.

<1>4. Q.E.D. Proof: <1>1, <1>2, and <1>3 provide general classes of rings with proofs that every prime ideal is maximal.
:::
