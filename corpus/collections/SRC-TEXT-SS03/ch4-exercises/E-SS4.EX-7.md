---
schema: qual/card@1
id: E-SS4.EX-7
kind: problem
title: "The Poisson summation formula applied to specific examples often provides intere"
classification:
  areas:
  - complex-analysis
  topics: ['Fourier Transform', 'Poisson Summation']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: exercise
7. The Poisson summation formula applied to specific examples often provides interesting identities.

(a) Let $\tau$ be fixed with $\operatorname { I m } ( \tau ) > 0$ . Apply the Poisson summation formula to

$$
f (z) = (\tau + z) ^ {- k},
$$

where k is an integer $\geq 2 .$ , to obtain

$$
\sum_ {n = - \infty} ^ {\infty} \frac {1}{(\tau + n) ^ {k}} = \frac {(- 2 \pi i) ^ {k}}{(k - 1) !} \sum_ {m = 1} ^ {\infty} m ^ {k - 1} e ^ {2 \pi i m \tau}.
$$

(b) Set $k = 2$ in the above formula to show that if $\operatorname { I m } ( \tau ) > 0$ , then

$$
\sum_ {n = - \infty} ^ {\infty} \frac {1}{(\tau + n) ^ {2}} = \frac {\pi^ {2}}{\sin^ {2} (\pi \tau)}.
$$

(c) Can one conclude that the above formula holds true whenever $\tau$ is any complex number that is not an integer?

[Hint: For (a), use residues to prove that $\hat { f } ( \xi ) = 0 , \mathrm { i f } \ \xi < 0$ , and

$$
\hat {f} (\xi) = \frac {(- 2 \pi i) ^ {k}}{(k - 1) !} \xi^ {k - 1} e ^ {2 \pi i \xi \tau}, \quad \text { when } \xi > 0. ]
$$
:::

::: solution
Let
\[
f(x)=(\tau+x)^{-k},\qquad \Im\tau>0,\quad k\ge2.
\]
The only pole of $f(z)$ is at $z=-\tau$, which lies in the lower half-plane.

For $\xi<0$, close the contour in the upper half-plane. The exponential $e^{-2\pi iz\xi}$ decays there and there are no poles, so
\[
\widehat f(\xi)=0.
\]
For $\xi>0$, close in the lower half-plane. The contour is clockwise, and the pole at $-\tau$ has order $k$. Its residue is
\[
\frac1{(k-1)!}
\left.\frac{d^{k-1}}{dz^{k-1}}e^{-2\pi iz\xi}\right|_{z=-\tau}
=\frac{(-2\pi i\xi)^{k-1}}{(k-1)!}e^{2\pi i\tau\xi}.
\]
Thus
\[
\widehat f(\xi)
=-2\pi i\,\operatorname{Res}_{z=-\tau}
\frac{e^{-2\pi iz\xi}}{(z+\tau)^k}
=\frac{(-2\pi i)^k}{(k-1)!}\xi^{k-1}e^{2\pi i\tau\xi}.
\]
At $\xi=0$, closing in the upper half-plane gives $\widehat f(0)=0$.

Poisson summation now yields
\[
\sum_{n\in\mathbb Z}\frac1{(\tau+n)^k}
=\sum_{m\in\mathbb Z}\widehat f(m)
=\frac{(-2\pi i)^k}{(k-1)!}
\sum_{m=1}^{\infty}m^{k-1}e^{2\pi im\tau}.
\]
This proves (a).

For $k=2$, let $q=e^{2\pi i\tau}$; since $\Im\tau>0$, $|q|<1$. Then
\[
\sum_{m=1}^{\infty}m q^m=\frac{q}{(1-q)^2},
\]
so
\[
\sum_{n\in\mathbb Z}\frac1{(\tau+n)^2}
=-4\pi^2\frac{q}{(1-q)^2}.
\]
But
\[
\sin^2(\pi\tau)=-\frac{(1-q)^2}{4q},
\]
hence
\[
\sum_{n\in\mathbb Z}\frac1{(\tau+n)^2}
=\frac{\pi^2}{\sin^2(\pi\tau)}.
\]

The identity remains valid for every $\tau\in\mathbb C\setminus\mathbb Z$. Indeed, the series on the left converges normally on compact subsets of $\mathbb C\setminus\mathbb Z$, so it defines a holomorphic function there; the right side is also holomorphic there. They agree on the upper half-plane, and $\mathbb C\setminus\mathbb Z$ is connected, so the identity theorem extends the equality to all nonintegral $\tau$.
:::
