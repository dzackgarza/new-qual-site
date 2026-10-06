---
schema: qual/card@1
id: P-UMNCP-S11-06
kind: problem
title: A sectorial growth restriction forces an entire function to be constant
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Spring 2011, 6 as reproduced in Cihan Bahran's vendored 2013 University of Minnesota complex-prelim solution compilation.
---

::: {.problem}
Suppose \(f\) is entire and there is \(M>0\) such that
\[
|\operatorname{Re}f(z)|\ge |\operatorname{Im}f(z)|
\]
whenever \(|z|\ge M\). Prove that \(f\) is constant.
:::

::: {.solution}
Write
$$
f(z)
=
u(z)+iv(z),
$$
where
$$
u=\operatorname{Re}f,
\qquad
v=\operatorname{Im}f.
$$

<1>1. For every
$$
|z|\ge M,
$$
one has
$$
\boxed{
\operatorname{Re}(f(z)^2)\ge0}.
$$

::: {.proof}
Compute
$$
f(z)^2
=
(u^2-v^2)+2iuv.
$$
Hence
$$
\operatorname{Re}(f(z)^2)
=
u(z)^2-v(z)^2.
$$
The hypothesis
$$
|u(z)|\ge|v(z)|
$$
implies
$$
u(z)^2-v(z)^2\ge0.
$$
:::

<1>2. The entire function
$$
g(z)
\coloneqq
e^{-f(z)^2}
$$
satisfies
$$
|g(z)|\le1
$$
whenever
$$
|z|\ge M.
$$

::: {.proof}
The function $g$ is entire because $f$ and the exponential are entire. Moreover,
$$
|g(z)|
=
e^{-\operatorname{Re}(f(z)^2)}.
$$
By step <1>1, the exponent is nonpositive when
$$
|z|\ge M,
$$
so
$$
|g(z)|\le1.
$$
:::

<1>3. The function $g$ is bounded on all of $\CC$.

::: {.proof}
Step <1>2 gives a bound outside the closed disk
$$
|z|\le M.
$$
Inside that disk, $g$ is continuous on a compact set, so
$$
\max_{|z|\le M}|g(z)|
$$
is finite. Combining the two bounds gives a global bound.
:::

<1>4. The function $g$ is constant.

::: {.proof}
Step <1>3 gives a bounded entire function. Liouville's theorem implies that it is constant.
:::

<1>5. The function
$$
f^2
$$
is constant.

::: {.proof}
Since
$$
g(z)=e^{-f(z)^2}
$$
is constant, differentiating gives
$$
0
=
g'(z)
=
-2f(z)f'(z)e^{-f(z)^2}.
$$
The exponential factor never vanishes, so
$$
f(z)f'(z)=0
$$
for every $z$. Therefore
$$
(f^2)'(z)
=
2f(z)f'(z)
=0
$$
identically. Hence $f^2$ is constant.
:::

<1>6. The function $f$ is constant.

::: {.proof}
Suppose
$$
f(z)^2\equiv c.
$$
If
$$
c=0,
$$
then $f\equiv0$.

If
$$
c\ne0,
$$
then $f$ takes values only in the two-point set
$$
\{\sqrt c,-\sqrt c\}.
$$
Since $f$ is continuous and $\CC$ is connected, its image is connected. A connected subset of a two-point set consists of one point. Thus $f$ is constant.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required conclusion.
:::
:::
