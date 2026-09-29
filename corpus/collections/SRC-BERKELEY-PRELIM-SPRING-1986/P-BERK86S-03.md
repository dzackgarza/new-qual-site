---
schema: qual/card@1
id: P-BERK86S-03
kind: problem
title: Two contour integrals around the integers $0,\dots,k$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Computed the residues of I_k at 0,...,k and summed them as an alternating
    binomial sum, which vanishes for k>=1. For J_k only z=0 is a pole, with
    residue (-1)^k k!.
---

::: {.problem}
Let $C$ be a positively oriented simple closed contour enclosing the points $0,1,\dots,k$. Evaluate, for $k=0,1,2,\dots$,
\[
I_k=\int_C\frac{dz}{z(z-1)\cdots(z-k)}
\]
and
\[
J_k=\int_C\frac{(z-1)\cdots(z-k)}{z}\,dz.
\]
:::

::: {.solution}
::: pf

::: {.pf-step #i0-value-boxed}
For $k=0$,
$$
\boxed{I_0=2\pi i}.
$$

::: pf-proof
When $k=0$,
$$
I_0=\int_C\frac{dz}{z}.
$$
The contour contains the simple pole at $0$ with residue $1$, so the
residue theorem gives $I_0=2\pi i$.
:::

:::

::: {.pf-step #residue-formula}
For $k\geq1$ and $0\leq j\leq k$, the residue of the integrand of
$I_k$ at $z=j$ is
$$
\operatorname{Res}_{z=j}
\frac{1}{z(z-1)\cdots(z-k)}
=
\frac{(-1)^{k-j}}{j!(k-j)!}.
$$

::: pf-proof
The pole at $j$ is simple, so its residue is
$$
\frac{1}{
\displaystyle\prod_{\substack{0\leq m\leq k\\m\neq j}}(j-m)
}.
$$
The factors with $m<j$ multiply to
$$
j!,
$$
while the factors with $m>j$ multiply to
$$
(-1)^{k-j}(k-j)!.
$$
Taking the reciprocal gives the claimed residue.
:::

:::

::: {.pf-step #ik-zero-boxed}
For every $k\geq1$,
$$
\boxed{I_k=0}.
$$

::: pf-proof
By the residue theorem and step [](#residue-formula){.pf-ref},
$$
\begin{aligned}
I_k
&=
2\pi i
\sum_{j=0}^k
\frac{(-1)^{k-j}}{j!(k-j)!}\\
&=
\frac{2\pi i}{k!}
\sum_{j=0}^k
\binom{k}{j}(-1)^{k-j}\\
&=
\frac{2\pi i}{k!}(1-1)^k\\
&=0.
\end{aligned}
$$
:::

:::

::: {.pf-step #jk-residue}
For every $k\geq0$, the only pole of the integrand of $J_k$ is
$z=0$, and its residue is
$$
(-1)^k k!.
$$

::: pf-proof
The numerator
$$
(z-1)\cdots(z-k)
$$
is a polynomial, so the factor $1/z$ supplies the only possible pole.
At $z=0$ the residue is the numerator evaluated at $0$:
$$
(-1)(-2)\cdots(-k)
=
(-1)^k k!.
$$
For $k=0$, the product is empty and equals $1=0!$, so the same formula
holds.
:::

:::

::: {.pf-step #jk-value-boxed}
Therefore, for every $k\geq0$,
$$
\boxed{J_k=2\pi i\,(-1)^k k!}.
$$

::: pf-proof
The contour encloses $0$ and the integrand of $J_k$ has no other poles.
Apply the residue theorem to the residue computed in step [](#jk-residue){.pf-ref}.
:::

:::

::: {.pf-step #combined-boxed}
Thus the two requested families are
$$
\boxed{
I_k=
\begin{cases}
2\pi i,&k=0,\\
0,&k\geq1,
\end{cases}
\qquad
J_k=2\pi i\,(-1)^k k!
}.
$$

::: pf-proof
Combine steps [](#i0-value-boxed){.pf-ref}, [](#ik-zero-boxed){.pf-ref}, and [](#jk-value-boxed){.pf-ref}.
:::

:::

::: pf-qed
Step [](#combined-boxed){.pf-ref} gives both evaluations.
:::

:::
:::
