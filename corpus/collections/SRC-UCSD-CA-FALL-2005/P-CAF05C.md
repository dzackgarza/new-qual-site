---
schema: qual/card@1
id: P-CAF05C
kind: problem
title: "Minimum modulus principle for analytic functions on bounded domains"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Prove that if $f$ is a non-constant analytic function on a bounded region $G \subset \mathbb{C}$ and is continuous on $\overline{G}$, then either $f$ has a zero in $G$ or $|f(z)|$ reaches its minimum value on $\partial G$.
:::

::: remark
The Fall 2005 source says only that $G$ is a bounded open set. Connectedness is
necessary: on a disconnected open set, a zero-free holomorphic function may be
constant with smaller modulus on one component and nonconstant on another. The
statement above makes the intended region hypothesis explicit.
:::

::: solution
Assume that $f$ has no zeros in $G$. Then
\[
g=\frac1f
\]
is holomorphic on $G$ and continuous on $\overline G$.

Because $G$ is bounded, $\overline G$ is compact, so $|f|$ attains a minimum
at some point of $\overline G$. Suppose a minimum is attained at an interior
point $a\in G$. Since $f$ is zero-free, this means that $|g|=1/|f|$ attains a
maximum at $a$. By the maximum modulus principle, $g$ is constant on the
connected region $G$, hence so is $f$, contradicting the hypothesis.

Therefore no minimum of $|f|$ can occur only in the interior. Since a minimum
exists on $\overline G$, at least one minimizing point lies on $\partial G$.
Thus either $f$ has a zero in $G$, or $|f|$ reaches its minimum value on
$\partial G$.
:::
