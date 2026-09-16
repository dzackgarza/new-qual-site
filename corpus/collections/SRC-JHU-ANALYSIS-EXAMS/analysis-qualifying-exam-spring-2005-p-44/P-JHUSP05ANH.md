---
schema: qual/card@1
id: P-JHUSP05ANH
kind: problem
title: "Zeros equal poles for a meromorphic function with positive real boundary values"
classification:
  areas:
  - complex-analysis
  topics:
  - Argument Principle
  - Meromorphic Functions
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the neighborhood of the closed disk, positive real boundary values and multiplicity convention with Spring 2005 problem 8 in the retained JHU extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Used the single-valued real logarithm along the positive boundary image and checked the argument principle without assuming a logarithm throughout the disk."
---

::: {.problem}
Let $U$ be an open set in $\mathbb{C}$ containing the closed unit disk $\overline{D}$.
Suppose $f$ is a meromorphic function on $U$ such that $f(\partial D) \subset \mathbb{R}^{+}$.
(In particular, $f$ has no zeros or poles on $\partial D$.)
Show that $f$ has the same number of zeros as poles in $D$, counting multiplicities.
:::

::: {.solution}
<1>1. The logarithmic derivative has integral zero around the unit circle.
::: {.proof}
Since $f$ has no pole on $\partial D$, it is holomorphic
on a neighborhood of that circle. Put $c(t)=f(e^{it})$
for $0\leq t\leq2\pi$. This is a continuously differentiable
function with values in the positive real numbers, and
$c(0)=c(2\pi)$. The ordinary real logarithm is therefore
defined along its entire image and has derivative $c'/c$.
By the chain rule,
$$
\int_{|z|=1}\frac{f'(z)}{f(z)}\,dz
=\int_0^{2\pi}\frac{c'(t)}{c(t)}\,dt
=\log c(2\pi)-\log c(0)=0.
$$
The circle is oriented counterclockwise. This uses only
a logarithm along the boundary image, not a holomorphic
logarithm at any interior zero or pole.
:::

<1>2. The argument principle equates the zero and pole counts.
::: {.proof}
The function is meromorphic on a neighborhood of the
closed disk and has neither zeros nor poles on its
boundary. It is not identically zero on the component
containing the disk, since its boundary values are positive.
Its zeros and poles in the closed disk consequently form
a finite set, with finite orders, by their local
meromorphic factorizations and compactness [@SS03].
The argument principle gives
$$
N-P=\frac1{2\pi i}\int_{|z|=1}\frac{f'}f\,dz=0,
$$
where $N$ is the sum of the zero orders and $P$ the sum
of the pole orders in $D$ [@SS03]. Thus $N=P$, exactly
the requested equality with multiplicities.
:::
:::
