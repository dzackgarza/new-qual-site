---
schema: qual/card@1
id: P-CAF06G
kind: problem
title: "Interpolation by entire functions at prescribed points"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Suppose that the $a_n$ are pairwise distinct, $a_n \to \infty$, and $A_n$ are arbitrary complex numbers.
Show that there exists an entire function $f(z)$ which satisfies $f(a_n) = A_n$.
:::

::: remark
The Fall 2006 source does not state that the interpolation nodes are distinct.
That hypothesis is necessary for arbitrary prescribed values: repeated nodes
with different $A_n$ would make the interpolation conditions inconsistent.
:::

::: solution
Because the distinct sequence $\{a_n\}$ has no finite accumulation point,
the Weierstrass product theorem gives an entire function $g$ whose zeros are
exactly the $a_n$, all simple. Thus $g'(a_n)\ne0$ for every $n$.

By the Mittag--Leffler theorem, there is a meromorphic function $H$ whose
principal part at $a_n$ is
\[
\frac{A_n}{g'(a_n)(z-a_n)}
\]
and which has no other poles. Define
\[
f(z)=g(z)H(z).
\]
Away from the $a_n$, this is holomorphic. Near $a_n$ write
\[
g(z)=(z-a_n)g'(a_n)+O((z-a_n)^2)
\]
and
\[
H(z)=\frac{A_n}{g'(a_n)(z-a_n)}+O(1).
\]
Their product therefore has a removable singularity at $a_n$, with
\[
f(a_n)=A_n.
\]
After filling in these removable singularities, $f$ is entire and interpolates
all prescribed values.
:::
