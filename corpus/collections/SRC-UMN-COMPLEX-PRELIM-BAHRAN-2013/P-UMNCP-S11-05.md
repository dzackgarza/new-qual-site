---
schema: qual/card@1
id: P-UMNCP-S11-05
kind: problem
title: A nonconstant entire function has dense image
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
  note: Checked against Spring 2011, 5 as reproduced in Cihan Bahran's vendored 2013 University of Minnesota complex-prelim solution compilation.
---

::: {.problem}
Prove that a nonconstant entire function maps \(\mathbb C\) onto a dense subset of \(\mathbb C\).
:::

::: {.solution}
Let
$$
f:\CC\to\CC
$$
be a nonconstant entire function.

<1>1. Suppose, toward a contradiction, that
$$
f(\CC)
$$
is not dense in $\CC$.

::: {.proof}
This is the negation of the desired conclusion.
:::

<1>2. There exist
$$
a\in\CC
$$
and
$$
r>0
$$
such that
$$
D(a,r)\cap f(\CC)=\varnothing.
$$

::: {.proof}
If
$$
f(\CC)
$$
is not dense, then its closure is a proper closed subset of $\CC$. Choose
$$
a\notin\overline{f(\CC)}.
$$
Since the complement of the closure is open, some disk
$$
D(a,r)
$$
lies entirely in that complement.
:::

<1>3. The function
$$
g(z)
\coloneqq
\frac1{f(z)-a}
$$
is entire and bounded.

::: {.proof}
By step <1>2,
$$
f(z)\ne a
$$
for every $z$, so $g$ is entire. Moreover,
$$
|f(z)-a|
\ge
r
$$
for every $z$, because the open disk of radius $r$ about $a$ is disjoint from the image. Hence
$$
|g(z)|
\le
\frac1r.
$$
:::

<1>4. The function $g$ is constant.

::: {.proof}
Step <1>3 gives a bounded entire function. Liouville's theorem implies that it is constant.
:::

<1>5. The function $f$ is constant.

::: {.proof}
If
$$
g(z)\equiv c,
$$
then
$$
\frac1{f(z)-a}
=
c.
$$
Since $g$ never vanishes,
$$
c\ne0,
$$
and therefore
$$
f(z)
=
a+\frac1c
$$
for every $z$.
:::

<1>6. This contradicts the hypothesis that $f$ is nonconstant.

::: {.proof}
Step <1>5 contradicts the standing assumption on $f$.
:::

<1>7. Therefore
$$
\boxed{
\overline{f(\CC)}
=
\CC}.
$$

::: {.proof}
The assumption in step <1>1 led to a contradiction, so the image must be dense.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is exactly the required conclusion.
:::
:::
