---
schema: qual/card@1
id: P-BKS05-2B
kind: problem
title: Zeros of $\sin z+1/(z+i)$ near the real axis
classification:
  areas:
  - prelim
  topics:
  - Complex Analysis
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
Prove that, for any $\varepsilon > 0$, the function $f(z) = \sin z + \frac{1}{z + i}$ has infinitely many zeros in the strip $\abs{\Im z} < \varepsilon$.
:::

::: {.solution}
Fix $\varepsilon>0$, and choose
$$
0<\rho<\min\{\varepsilon,\pi\}.
$$
For each positive integer $n$, let
$$
C_n\coloneqq\{z\in\CC:\abs{z-2\pi n}=\rho\},
\qquad
D_n\coloneqq\{z\in\CC:\abs{z-2\pi n}<\rho\}.
$$

::: pf

::: {.pf-step #s1}

There is a constant $m_\rho>0$ such that
$$
\abs{\sin z}\geq m_\rho
$$
for every $z\in C_n$ and every $n$.

::: pf-proof

The circle $\abs{w}=\rho$ contains no zero of $\sin w$, because the zeros
of sine are the integer multiples of $\pi$ and $0<\rho<\pi$.
Hence compactness gives
$$
m_\rho
\coloneqq
\min_{\abs{w}=\rho}\abs{\sin w}
>0.
$$
Since sine has period $2\pi$,
$$
\abs{\sin z}
=
\abs{\sin(z-2\pi n)}
\geq m_\rho
$$
on $C_n$.

:::

:::

::: {.pf-step #s2}

For all sufficiently large $n$,
$$
\abs{\frac1{z+i}}<m_\rho
$$
for every $z\in C_n$, and the closed disk bounded by $C_n$ does not
contain the pole $-i$.

::: pf-proof

For $z\in C_n$,
$$
\abs{z+i}
\geq
2\pi n-\rho-1.
$$
The right-hand side tends to infinity with $n$. Thus for all
sufficiently large $n$ it exceeds $1/m_\rho$, which gives the
required inequality. Also
$$
\abs{2\pi n-(-i)}
=
\abs{2\pi n+i}
>2\pi n
>\rho,
$$
so the pole $-i$ lies outside $\overline{D_n}$.

:::

:::

::: {.pf-step #s3}

For every sufficiently large $n$, the function
$$
f(z)=\sin z+\frac1{z+i}
$$
has exactly one zero in $D_n$, counted with multiplicity.

::: pf-proof

For such $n$, both $\sin z$ and $1/(z+i)$ are holomorphic on a
neighborhood of $\overline{D_n}$. Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} give
$$
\abs{\frac1{z+i}}
<
\abs{\sin z}
$$
on $C_n$. By Rouché's theorem, $f$ and $\sin z$ have the same number
of zeros in $D_n$.

Since $\rho<\pi$, the only zero of sine in $D_n$ is the simple zero
$2\pi n$. Hence $f$ has exactly one zero there.

:::

:::

::: {.pf-step #s4}

These zeros give infinitely many distinct zeros of $f$ in the
strip
$$
\abs{\operatorname{Im}z}<\varepsilon.
$$

::: pf-proof

If $z\in D_n$, then
$$
\abs{\operatorname{Im}z}
\leq\abs{z-2\pi n}
<\rho
<\varepsilon,
$$
so every zero from step [](#s3){.pf-ref} lies in the required strip. Moreover,
the disks $D_n$ are pairwise disjoint because their centers are
$2\pi$ apart and $\rho<\pi$. Thus the zeros obtained for distinct
large $n$ are distinct. There are infinitely many such $n$.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} proves the required assertion.

:::

:::

:::
