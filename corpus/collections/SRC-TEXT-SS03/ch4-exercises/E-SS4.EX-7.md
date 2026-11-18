---
schema: qual/card@1
id: E-SS4.EX-7
kind: problem
title: $\sum_n(\tau+n)^{-k}$ and $\sum_n(\tau+n)^{-2}=\pi^2/\sin^2\pi\tau$ by Poisson summation
classification:
  areas:
  - complex-analysis
  topics:
  - Poisson Summation
  - Residues
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the card's prose argument into numbered steps without changing the mathematics, and
    re-checked each step against the definitions and theorems it invokes. What was not checked: no
    copy of Stein and Shakarchi and no solution set for it is retained in tmp/sources (the
    collection provenance is the Google Books ISBN link), so the printed statement and page were
    not re-read; the exercise number is the one the collection index records. No published
    solution is transcribed; the argument remains the card's own, as its solution section says.
---

::: {.exercise}
The Poisson summation formula applied to specific examples often provides interesting identities.

(a) Let $\tau$ be fixed with $\Im(\tau) > 0$. Apply the Poisson summation formula to
$$
f(z) = (\tau + z)^{-k},
$$
where $k$ is an integer $\geq 2$, to obtain
$$
\sum_{n=-\infty}^{\infty} \frac{1}{(\tau + n)^k} = \frac{(-2\pi i)^k}{(k - 1)!} \sum_{m=1}^{\infty} m^{k-1} e^{2\pi i m\tau}.
$$

(b) Set $k = 2$ in the above formula to show that if $\Im(\tau) > 0$, then
$$
\sum_{n=-\infty}^{\infty} \frac{1}{(\tau + n)^2} = \frac{\pi^2}{\sin^2(\pi\tau)}.
$$

(c) Can one conclude that the above formula holds true whenever $\tau$ is any complex number that is not an integer?

[Hint: For (a), use residues to prove that $\hat{f}(\xi) = 0$, if $\xi < 0$, and
$$
\hat{f}(\xi) = \frac{(-2\pi i)^k}{(k - 1)!} \xi^{k-1} e^{2\pi i\xi\tau}, \quad \text{when } \xi > 0.
$$
]
:::

::: {.solution}

The argument is the card's own: no copy of Stein and Shakarchi and no published solution set for this book is retained in `tmp/sources`, so nothing below is transcribed. The statement is the exercise the collection index records as Stein and Shakarchi, *Complex Analysis* (2003), Ch. 4, Exercise 7. Here $\Im\tau>0$, $k\geq2$ is an integer, $f(x)=(\tau+x)^{-k}$, and $\widehat f(\xi)=\int_{-\infty}^{\infty}f(x)e^{-2\pi ix\xi}\,dx$ is the Fourier transform in the normalization for which Poisson summation reads $\sum_{n\in\ZZ}f(n)=\sum_{m\in\ZZ}\widehat f(m)$.

::: pf

::: {.pf-step #pole}

$f$ has exactly one pole, a pole of order $k$ at $z=-\tau$, and it lies in the lower half-plane.

::: pf-proof

$(\tau+z)^{-k}$ is holomorphic away from $z=-\tau$, where it has a pole of order $k$; $\Im(-\tau)=-\Im\tau<0$.

:::

:::

::: {.pf-step #neg}

$\widehat f(\xi)=0$ for $\xi<0$.

::: pf-proof

For $\xi<0$ the factor $e^{-2\pi iz\xi}$ decays in the upper half-plane, where $f$ is holomorphic; closing the rectangular contour there and letting its top go to infinity gives a vanishing integral.

:::

:::

::: {.pf-step #pos}

$\widehat f(\xi)=\frac{(-2\pi i)^{k}}{(k-1)!}\xi^{k-1}e^{2\pi i\xi\tau}$ for $\xi>0$.

::: pf-proof

Close in the lower half-plane, which is clockwise, so the integral is $-2\pi i$ times the residue at $-\tau$. With $g(z)=e^{-2\pi iz\xi}$ and $h(z)=(z+\tau)^{k}$, the residue is $\frac{1}{(k-1)!}\frac{d^{k-1}}{dz^{k-1}}e^{-2\pi iz\xi}$ at $z=-\tau$, that is $\frac{(-2\pi i\xi)^{k-1}}{(k-1)!}e^{2\pi i\tau\xi}$; multiplying and simplifying $(-2\pi i)\cdot(-2\pi i\xi)^{k-1}=(-2\pi i)^{k}\xi^{k-1}$ gives the formula.

:::

:::

::: {.pf-step #zero}

$\widehat f(0)=0$.

::: pf-proof

At $\xi=0$ the integral is $\int(\tau+x)^{-k}\,dx$, taken by closing in the upper half-plane where there are no poles and the integrand decays like $\abs{z}^{-k}$ with $k\geq2$.

:::

:::

::: {.pf-step #a}

(a) $\sum_{n\in\ZZ}(\tau+n)^{-k}=\frac{(-2\pi i)^{k}}{(k-1)!}\sum_{m\geq1}m^{k-1}e^{2\pi im\tau}$.

::: pf-proof

Poisson summation applies to $f$, which is smooth and decays like $\abs{x}^{-k}$ with $k\geq2$: $\sum_{n}f(n)=\sum_{m}\widehat f(m)$. By steps [](#neg){.pf-ref}, [](#zero){.pf-ref} and [](#pos){.pf-ref} the only nonzero terms are $m\geq1$, and their sum is the right-hand side.

:::

:::

::: {.pf-step #b}

(b) $\sum_{n\in\ZZ}(\tau+n)^{-2}=\pi^{2}/\sin^{2}(\pi\tau)$.

::: pf-proof

With $k=2$, step [](#a){.pf-ref} gives $-4\pi^{2}\sum_{m\geq1}me^{2\pi im\tau}$. Put $q=e^{2\pi i\tau}$, so $\abs{q}<1$; then $\sum_{m\geq1}mq^{m}=\frac{q}{(1-q)^{2}}$ by differentiating the geometric series. Also $\sin(\pi\tau)=\frac{e^{i\pi\tau}-e^{-i\pi\tau}}{2i}=q^{1/2}\frac{1-q}{2i}$, so $\sin^{2}(\pi\tau)=-\frac{(1-q)^{2}}{4q}$; hence $-4\pi^{2}\frac{q}{(1-q)^{2}}=\frac{\pi^{2}}{\sin^{2}(\pi\tau)}$.

:::

:::

::: {.pf-step #c}

(c) The identity of (b) holds for every $\tau\in\CC\setminus\ZZ$.

::: pf-proof

Both sides are holomorphic on $\CC\setminus\ZZ$: the left is a series converging normally on compact subsets there, since $\abs{\tau+n}\geq c>0$ for all but finitely many $n$ on such a set and $\sum\abs{n}^{-2}$ converges, and the right is a quotient of holomorphic functions whose denominator does not vanish off $\ZZ$. They agree on the upper half-plane by step [](#b){.pf-ref}, and $\CC\setminus\ZZ$ is connected, so the identity theorem extends the equality.

:::

:::

:::

:::
