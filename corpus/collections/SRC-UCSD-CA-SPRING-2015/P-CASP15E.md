---
schema: qual/card@1
id: P-CASP15E
kind: problem
title: "Partial fraction expansion of cos(pi z)/sin^2(pi z)"
classification:
  areas:
  - complex-analysis
  topics:
  - Partial Fractions
  - Meromorphic Functions
  - Periodic Functions
relations: []
review: draft
---

::: problem
Show that
$$
\pi^2\frac{\cos \pi z}{\sin^2 \pi z} = \sum_{n \in \mathbb{Z}} \frac{(-1)^n}{(z - n)^2}.
$$
(Hint: Compare singular parts and use periodicity.)
:::

::: remark
The local transcription previously placed $\pi^2$ in the denominator. The
official Spring 2015 UCSD exam has the factor $\pi^2$ multiplying
$\cos(\pi z)/\sin^2(\pi z)$, as written here.
:::

::: solution
The series
\[
S(z)=\sum_{n\in\mathbb Z}\frac{(-1)^n}{(z-n)^2}
\]
converges normally on compact subsets of $\mathbb C\setminus\mathbb Z$.
At $z=n$,
\[
\pi^2\frac{\cos\pi z}{\sin^2\pi z}
=\frac{(-1)^n}{(z-n)^2}+O(1),
\]
so
\[
H(z)=\pi^2\frac{\cos\pi z}{\sin^2\pi z}-S(z)
\]
has removable singularities at all integers and hence extends to an entire
function.

Both terms are anti-periodic with period $1$:
\[
H(z+1)=-H(z).
\]
It therefore suffices to bound $H$ on a vertical strip of width $1$. Away
from small disks around the integers, normal convergence bounds $S$ uniformly,
and the trigonometric term is bounded there; near the integers the singular
parts cancel. Thus $H$ is bounded on a fundamental strip and hence, by
anti-periodicity, on all of $\mathbb C$. Liouville's theorem gives that $H$ is
constant, and $H(z+1)=-H(z)$ forces that constant to be $0$. Therefore
\[
\boxed{\pi^2\frac{\cos\pi z}{\sin^2\pi z}
=\sum_{n\in\mathbb Z}\frac{(-1)^n}{(z-n)^2}.}
\]
:::
