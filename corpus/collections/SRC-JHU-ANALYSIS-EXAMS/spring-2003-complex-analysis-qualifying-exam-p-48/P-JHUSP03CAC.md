---
schema: qual/card@1
id: P-JHUSP03CAC
kind: problem
title: Recovering zeros from logarithmic-derivative moments
classification:
  areas:
  - complex-analysis
  topics:
  - Argument Principle
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the right half-disk contour, both weighted logarithmic-derivative integrals and the explicit-zero request with Spring 2003 problem 3."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Converted the two integrals into first and second power sums with multiplicity, used Re(z)>1 in the region to force exactly two zeros, and solved their quadratic from the two moments."
---

::: {.problem}
Let $C$ be the closed curve defined by two pieces: the first piece is given by the set of all $z$ satisfying $|z - 1| = 3$ and $\operatorname{Re}(z - 1) \geq 0$.
The second piece is the straight line segment from $1 + 3i$ to $1 - 3i$.
Orient $C$ in the counterclockwise direction, and let $\Omega$ be the region enclosed by $C$.
Suppose $f$ is holomorphic in a neighborhood of $\overline{\Omega}$ with no zeros on $C$.
Suppose also that:

$$\frac{1}{2\pi i} \int_C \frac{zf'(z)}{f(z)} \, dz = 3 \qquad \text{and} \qquad \frac{1}{2\pi i} \int_C \frac{z^2 f'(z)}{f(z)} \, dz = \frac{5}{2}.$$

Determine all the zeros of $f$ in $\Omega$ explicitly.
:::

::: solution
The zeros in $\Omega$, counted with multiplicity, are
$$
\boxed{\frac32+i\quad\text{and}\quad\frac32-i}.
$$

<1>1. The two contour integrals are the first two power sums of the zeros.
::: proof
Let the zeros of $f$ in $\Omega$, repeated according to multiplicity, be
$\zeta_1,\dots,\zeta_N$. There are finitely many because $f$ is holomorphic on
a neighborhood of $\overline\Omega$, has no zero on $C$, and is not identically
zero.

If $\zeta$ is a zero of multiplicity $m$, then locally
$f(z)=(z-\zeta)^m h(z)$ with $h(\zeta)\ne0$, so
$$
\frac{f'(z)}{f(z)}=\frac{m}{z-\zeta}+\frac{h'(z)}{h(z)}.
$$
Hence the residues of $z f'/f$ and $z^2f'/f$ at $\zeta$ are respectively
$m\zeta$ and $m\zeta^2$. The residue theorem therefore gives
$$
\sum_{j=1}^N\zeta_j=3,
\qquad
\sum_{j=1}^N\zeta_j^2=\frac52.
$$
:::

<1>2. The geometry of $\Omega$ forces $N=2$.
::: proof
The contour consists of the right semicircle centered at $1$ of radius $3$
and the vertical segment from $1+3i$ to $1-3i$. Thus every point of the
interior $\Omega$ satisfies
$$
\operatorname{Re}z>1.
$$
Taking real parts in the first power-sum identity gives
$$
3=\sum_{j=1}^N\operatorname{Re}\zeta_j>N.
$$
Hence $N\le2$. If $N=1$, the first identity would give $\zeta_1=3$, but then
the second would give $\zeta_1^2=9$, contradicting $5/2$. Thus $N=2$.
:::

<1>3. The two power sums determine the two zeros uniquely.
::: proof
Let the two zeros be $\zeta_1,\zeta_2$. Then
$$
\zeta_1+\zeta_2=3,
\qquad
\zeta_1^2+\zeta_2^2=\frac52.
$$
Using
$(\zeta_1+\zeta_2)^2=\zeta_1^2+\zeta_2^2+2\zeta_1\zeta_2$
gives
$$
\zeta_1\zeta_2=\frac{9-5/2}{2}=\frac{13}{4}.
$$
Therefore $\zeta_1,\zeta_2$ are the roots of
$$
t^2-3t+\frac{13}{4}=0,
$$
namely
$$
\frac{3\pm\sqrt{-4}}2=\frac32\pm i.
$$
Both lie in $\Omega$ because their real part is $3/2>1$ and
$$
\left|\left(\frac32\pm i\right)-1\right|^2
=\frac14+1=\frac54<9.
$$
Thus these are exactly all the zeros requested.
:::
:::
