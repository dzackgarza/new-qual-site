---
schema: qual/card@1
id: P-BKS05-2B
kind: problem
title: Zeros of $\sin z+1/(z+i)$ near the real axis
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against fresh deterministic MinerU Flash extractions of the UC Berkeley Spring 2005 exam and its companion solution packet; unambiguous duplicated-statement extraction defects were normalized.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Independently checked the retained Rouche argument and chose a radius
    rho strictly smaller than both epsilon and pi, so the comparison disks
    are disjoint, lie inside the strip, and contain exactly one zero of sin.
---

::: {.problem}
Prove that, for any $\varepsilon > 0$ , the function $\begin{array} { r } { f ( z ) = \sin { z } + \frac { 1 } { z + i } } \end{array}$ has infinitely many zeros in the strip $| \operatorname { I m } z | < \varepsilon$
:::

::: {.solution}
Fix $\varepsilon>0$, and choose
$$
0<\rho<\min\{\varepsilon,\pi\}.
$$
For each positive integer $n$, let
$$
C_n\coloneqq\{z\in\CC:|z-2\pi n|=\rho\},
\qquad
D_n\coloneqq\{z\in\CC:|z-2\pi n|<\rho\}.
$$

<1>1. There is a constant $m_\rho>0$ such that
$$
|\sin z|\geq m_\rho
$$
for every $z\in C_n$ and every $n$.

::: {.proof}
The circle $|w|=\rho$ contains no zero of $\sin w$, because the zeros
of sine are the integer multiples of $\pi$ and $0<\rho<\pi$.
Hence compactness gives
$$
m_\rho
\coloneqq
\min_{|w|=\rho}|\sin w|
>0.
$$
Since sine has period $2\pi$,
$$
|\sin z|
=
|\sin(z-2\pi n)|
\geq m_\rho
$$
on $C_n$.
:::

<1>2. For all sufficiently large $n$,
$$
\left|\frac1{z+i}\right|<m_\rho
$$
for every $z\in C_n$, and the closed disk bounded by $C_n$ does not
contain the pole $-i$.

::: {.proof}
For $z\in C_n$,
$$
|z+i|
\geq
2\pi n-\rho-1.
$$
The right-hand side tends to infinity with $n$. Thus for all
sufficiently large $n$ it exceeds $1/m_\rho$, which gives the
required inequality. Also
$$
|2\pi n-(-i)|
=
|2\pi n+i|
>2\pi n
>\rho,
$$
so the pole $-i$ lies outside $\overline{D_n}$.
:::

<1>3. For every sufficiently large $n$, the function
$$
f(z)=\sin z+\frac1{z+i}
$$
has exactly one zero in $D_n$, counted with multiplicity.

::: {.proof}
For such $n$, both $\sin z$ and $1/(z+i)$ are holomorphic on a
neighborhood of $\overline{D_n}$. Steps <1>1 and <1>2 give
$$
\left|\frac1{z+i}\right|
<
|\sin z|
$$
on $C_n$. By Rouché's theorem, $f$ and $\sin z$ have the same number
of zeros in $D_n$.

Since $\rho<\pi$, the only zero of sine in $D_n$ is the simple zero
$2\pi n$. Hence $f$ has exactly one zero there.
:::

<1>4. These zeros give infinitely many distinct zeros of $f$ in the
strip
$$
|\operatorname{Im}z|<\varepsilon.
$$

::: {.proof}
If $z\in D_n$, then
$$
|\operatorname{Im}z|
\leq|z-2\pi n|
<\rho
<\varepsilon,
$$
so every zero from step <1>3 lies in the required strip. Moreover,
the disks $D_n$ are pairwise disjoint because their centers are
$2\pi$ apart and $\rho<\pi$. Thus the zeros obtained for distinct
large $n$ are distinct. There are infinitely many such $n$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 proves the required assertion.
:::
:::
