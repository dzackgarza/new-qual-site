---
schema: qual/card@1
id: P-4KPQM
kind: problem
title: The fundamental theorem of algebra via the maximum modulus principle
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Modulus Principle
  - Polynomials
  - Zeros
relations: []
review: draft
---

::: {.problem}
Prove the fundamental theorem of Algebra using the maximum modulus principle.
:::

::: {.solution}
Let $p$ be a nonconstant complex polynomial. Suppose, for contradiction, that
$p$ has no zero. Then
\[
g(z)=\frac1{p(z)}
\]
is entire. Since $|p(z)|\to\infty$ as $|z|\to\infty$, we have
$g(z)\to0$ as $|z|\to\infty$.

Choose $R>0$ so large that
\[
|g(z)|<|g(0)|
\qquad (|z|\ge R).
\]
On the compact disk $\overline{D(0,R)}$, the continuous function $|g|$
attains a maximum, say at $z_0$. Because outside the disk $|g|<|g(0)|$, this
maximum is also the global maximum of $|g|$ on $\mathbb C$. Hence the entire
function $g$ attains its maximum modulus at an interior point. By the maximum
modulus principle, $g$ is constant, so $p$ is constant, a contradiction.

Therefore every nonconstant complex polynomial has a zero. This is the
fundamental theorem of algebra.
:::
