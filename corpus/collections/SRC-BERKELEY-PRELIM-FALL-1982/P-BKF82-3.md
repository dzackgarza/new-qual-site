---
schema: qual/card@1
id: P-BKF82-3
kind: problem
title: Negative Laurent coefficients of $\cot(\pi z)$ on $1<|z|<2$
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
  date: 2026-09-11
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Computed negative Laurent coefficients by integrating on a circle 1<rho<2 and summing residues at -1,0,1."
---

::: {.problem}
Let
\[
\cot(\pi z)=\sum_{n=-\infty}^{\infty}a_nz^n
\]
be the Laurent expansion on $1<|z|<2$. Compute $a_n$ for $n<0$.
:::

::: {.solution}
Write $n=-m$ with $m\ge1$, and choose any radius $\rho$ with
$$
1<\rho<2.
$$

<1>1. Express $a_{-m}$ as a contour integral.
::: {.proof}
The Laurent coefficient formula gives
$$
a_{-m}
=\frac{1}{2\pi i}\int_{|z|=\rho}
\cot(\pi z)z^{m-1}\,dz.
$$
Inside this circle, $\cot(\pi z)$ has simple poles precisely at
$z=-1,0,1$. At every integer $k$,
$$
\operatorname{Res}_{z=k}\cot(\pi z)=\frac1\pi,
$$
because $\sin(\pi z)$ has derivative $\pi\cos(\pi k)=\pi(-1)^k$ and
$\cos(\pi k)=(-1)^k$.
:::

<1>2. Compute the coefficient $a_{-1}$.
::: {.proof}
For $m=1$, the integrand is simply $\cot(\pi z)$. Therefore
$$
a_{-1}
=\frac1\pi+\frac1\pi+\frac1\pi
=\boxed{\frac3\pi}.
$$
:::

<1>3. Compute the coefficients $a_{-m}$ for $m>1$.
::: {.proof}
When $m>1$, multiplication by $z^{m-1}$ removes the pole at $0$, so only
$z=\pm1$ contribute. Hence
$$
\begin{aligned}
a_{-m}
&=\frac{(-1)^{m-1}}\pi+\frac1\pi\\
&=\frac{1+(-1)^{m-1}}\pi.
\end{aligned}
$$
Thus this coefficient is $2/\pi$ when $m$ is odd and $0$ when $m$ is even.
:::

<1>4. State all negative coefficients.
::: {.proof}
Combining steps <1>2 and <1>3,
$$
\boxed{
a_n=
\begin{cases}
3/\pi,&n=-1,\\[2mm]
2/\pi,&n=-3,-5,-7,\ldots,\\[2mm]
0,&n=-2,-4,-6,\ldots.
\end{cases}}
$$
:::
:::
