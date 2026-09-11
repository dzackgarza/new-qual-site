---
schema: qual/card@1
id: P-BKF77-7
kind: problem
title: Evaluate $\int_{-\infty}^{\infty}(1+x^{2n})^{-1}dx$
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
  note: "Evaluated the positive-half integral on a sector of angle pi/n with one enclosed pole and doubled by evenness."
---

::: problem
Evaluate
\[
\int_{-\infty}^{\infty}\frac{dx}{1+x^{2n}},
\]
where $n$ is a positive integer.
:::

::: solution
Set
$$
I_n=\int_0^\infty\frac{dx}{1+x^{2n}}.
$$
Since the integrand is even, the required integral is $2I_n$.

<1>1. Integrate over a sector of angle $\pi/n$.
::: proof
Let
$$
F(z)=\frac1{1+z^{2n}},
$$
and consider the positively oriented boundary of the sector
$$
0\le \arg z\le \frac\pi n,
\qquad |z|\le R,
$$
with $R>1$.

The poles of $F$ are the $2n$ roots of $-1$. Exactly one lies in the interior
of this sector, namely
$$
\zeta=e^{i\pi/(2n)}.
$$
It is simple, and
$$
\operatorname{Res}(F;\zeta)
=\frac1{2n\zeta^{2n-1}}.
$$
Since $\zeta^{2n}=-1$,
$$
\zeta^{2n-1}=-\zeta^{-1},
$$
so
$$
\operatorname{Res}(F;\zeta)
=-\frac{\zeta}{2n}.
$$
:::

<1>2. Compute the two radial contributions and show the arc vanishes.
::: proof
The integral along the positive real radius is
$$
I_n(R)=\int_0^R\frac{dx}{1+x^{2n}}.
$$

On the upper radius write
$$
z=re^{i\pi/n}.
$$
Because
$$
z^{2n}=r^{2n}e^{2\pi i}=r^{2n},
$$
and this radius is traversed from $R$ back to $0$, its contribution is
$$
-e^{i\pi/n}I_n(R).
$$

On the circular arc $|z|=R$,
$$
|1+z^{2n}|\ge R^{2n}-1.
$$
The arc has length $\pi R/n$, hence its integral has absolute value at most
$$
\frac{\pi R/n}{R^{2n}-1},
$$
which tends to $0$ as $R\to\infty$.
:::

<1>3. Apply the residue theorem.
::: proof
Letting $R\to\infty$ in the sector integral gives
$$
\left(1-e^{i\pi/n}\right)I_n
=2\pi i\left(-\frac{\zeta}{2n}\right)
=-\frac{\pi i\zeta}{n}.
$$
Put
$$
\theta=\frac\pi{2n},
\qquad \zeta=e^{i\theta}.
$$
Then
$$
1-e^{i\pi/n}
=1-e^{2i\theta}
=-2i e^{i\theta}\sin\theta
=-2i\zeta\sin\theta.
$$
Therefore
$$
I_n
=\frac{-\pi i\zeta/n}{-2i\zeta\sin\theta}
=\frac{\pi}{2n}\csc\left(\frac\pi{2n}\right).
$$
Doubling gives
$$
\boxed{
\int_{-\infty}^{\infty}\frac{dx}{1+x^{2n}}
=\frac\pi n\csc\left(\frac\pi{2n}\right).}
$$
:::
:::
