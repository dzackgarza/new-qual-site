---
schema: qual/card@1
id: E-HAT-3.3-28
kind: problem
title: "Nondegeneracy on large subspaces"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

Show that a nonsingular symmetric or skew-symmetric bilinear pairing over a field $F$, of the form $F^n \times F^n \to F$, cannot be identically zero when restricted to all pairs of vectors $\nu, w$ in a $k$-dimensional subspace $V \subset F^n$ if $k > n/2$.

::: {.solution}
<1>1. Let $B:F^n\times F^n\to F$ be nonsingular, with matrix $A$ ($B(x,y)=x^tAy$).
::: {.proof}
choose basis.
:::

<1>2. Suppose $V\subset F^n$ is $k$-dimensional and $B|_{V\times V}=0$.
::: {.proof}
assume for contradiction $k>n/2$.
:::

<1>3. The map $F^n\to V^*$ given by $x\mapsto B(x,\cdot)|_V$ has kernel $V^\perp$.
::: {.proof}
definition of orthogonal.
:::

<1>4. $\dim V^\perp = n-\dim V = n-k$ (nonsingularity).
::: {.proof}
<1>3.
:::

<1>5. $V\cap V^\perp=0$ would imply $B|_{V\times V}$ nondegenerate, but $B|_{V\times V}=0$.
::: {.proof}
<1>2.
:::

<1>6. $\dim(V+V^\perp)=\dim V+\dim V^\perp = k+n-k=n$, so $V\oplus V^\perp =F^n$ if $V\cap V^\perp=0$.
::: {.proof}
dimension formula.
:::

<1>7. $B|_{V\times V}=0$ forces $V\subset V^\perp$, so $k\le n-k$, i.e. $k\le n/2$.
::: {.proof}
$B(v,w)=0$ for all $v,w\in V$ means $V\subset V^\perp$.
:::

<1>8. Contradicting $k>n/2$.
::: {.proof}
<1>7.
:::

<1>9. Q.E.D.
::: {.proof}
<1>8.
:::
:::
