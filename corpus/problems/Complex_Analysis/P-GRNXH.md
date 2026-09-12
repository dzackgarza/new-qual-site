---
schema: qual/card@1
id: P-GRNXH
kind: problem
title: Holomorphic interpolation at sequences accumulating at zero
classification:
  areas:
  - complex-analysis
  topics:
  - Identity Theorem
  - Zeros
  - Holomorphic Functions
relations: []
review: draft
---

::: problem
Suppose $f$ is analytic on $\DD^\circ$.
Determine with proof which of the following are possible:

a. $f\qty{1\over n} = (-1)^n$ for each $n>1$.

b. $f\qty{1\over n} = e^{-n}$ for each even integer $n>1$ while $f\qty{1\over n} = 0$ for each odd integer $n>1$.

c. $f\qty{1\over n^2} = {1\over n}$ for each integer $n>1$.

d. $f\qty{1\over n} = {n-2 \over n-1}$ for each integer $n>1$.
:::

::: solution
The points $1/n$ and $1/n^2$ accumulate at $0\in\mathbb D$, so analyticity at
$0$ strongly constrains all four cases.

**(a) Impossible.** Continuity at $0$ would force the sequence
$f(1/n)$ to converge to $f(0)$, but $(-1)^n$ does not converge.

**(b) Impossible.** For every odd $n>1$, $f(1/n)=0$. These zeros accumulate at
$0\in\mathbb D$, so the identity theorem gives $f\equiv0$. This contradicts
$f(1/n)=e^{-n}\ne0$ for even $n$.

**(c) Impossible.** Since $f(1/n^2)=1/n\to0$, continuity gives $f(0)=0$.
If $f$ is not identically zero, let $m\ge1$ be the order of its zero at $0$.
Then
\[
f(z)=z^m g(z),
\qquad g(0)\ne0.
\]
At $z=1/n^2$ this gives
\[
\frac1n=\frac{1}{n^{2m}}g(1/n^2),
\]
so
\[
g(1/n^2)=n^{2m-1},
\]
which diverges, contradicting $g(1/n^2)\to g(0)$. The identically-zero case
is also impossible.

**(d) Possible.** Define
\[
f(z)=\frac{1-2z}{1-z}.
\]
Its only pole is at $z=1$, so it is holomorphic on the open unit disk. For
$n>1$,
\[
f(1/n)
=\frac{1-2/n}{1-1/n}
=\frac{n-2}{n-1}.
\]

Hence precisely **(d)** can occur.
:::
