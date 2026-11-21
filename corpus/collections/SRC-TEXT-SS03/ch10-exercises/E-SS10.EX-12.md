---
schema: qual/card@1
id: E-SS10.EX-12
kind: problem
title: A Lambert-series formula for $\theta^4$ equivalent to the four-squares theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Theta Functions
  - Number Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Repaired a statement or hint transcription defect before solving.
---

::: {.exercise}
Here we give another identity involving $\theta^4$, which is equivalent to the four-squares theorem.

(a) Show that for $\abs{q} < 1$
$$
\sum_{n=1}^{\infty} \frac{n q^n}{1 - q^n} = \sum_{n=1}^{\infty} \frac{q^n}{(1 - q^n)^2}.
$$
[Hint: The left-hand side is $\sum \sigma_1(n) q^n$. Use $x/(1-x)^2 = \sum_{n=1}^{\infty} n x^n$.]

(b) Show as a result that
$$
\sum_{n=1}^{\infty} \frac{n q^n}{1 - q^n} - \sum_{n=1}^{\infty} \frac{4n q^{4n}}{1 - q^{4n}} = \sum_{n=1}^{\infty} \frac{q^n}{(1 - q^n)^2} - 4 \sum_{n=1}^{\infty} \frac{q^{4n}}{(1 - q^{4n})^2} = \sum \sigma_1^*(n) q^n
$$
where $\sigma_1^*(n)$ is the sum of the divisors of $n$ that are not divisible by $4$.

(c) Show that the four-squares theorem is equivalent to the identity
$$
\theta(\tau)^4 = 1 + 8 \sum_{n=1}^{\infty} \frac{q^n}{(1 + (-1)^n q^n)^2}, \quad q = e^{\pi i \tau}.
$$
:::

::: {.solution}

The argument is the card's own: a double series reindexed gives (a), the divisor sums are split by divisibility by $4$ for (b), and the split into odd and even terms identifies the series of (c) with the divisor sum, so that Jacobi's theorem becomes the stated identity. Throughout $\abs{q}<1$, so every series below converges absolutely.

::: pf

::: {.pf-step #parta}

(a) $\displaystyle\sum_{n=1}^{\infty}\frac{nq^{n}}{1-q^{n}}=\sum_{n=1}^{\infty}\frac{q^{n}}{(1-q^{n})^{2}}$.

::: pf-proof

For $\abs{x}<1$ the geometric series gives $\frac{1}{1-x}=\sum_{k\ge0}x^{k}$, and differentiating term by term — legitimate inside the disc of convergence — gives $\frac{x}{(1-x)^{2}}=\sum_{k\ge1}kx^{k}$. Taking $x=q^{n}$ and summing over $n$,
$$
\sum_{n\ge1}\frac{q^{n}}{(1-q^{n})^{2}}=\sum_{n\ge1}\sum_{k\ge1}kq^{nk}.
$$
The double series converges absolutely (the terms are $\abs{k q^{nk}}$ with $\sum_{n,k}k\abs{q}^{nk}<\infty$), so the order of summation may be exchanged; writing $N=nk$ and summing first over the factorisations of $N$ gives
$$
\sum_{n,k\ge1}kq^{nk}=\sum_{N\ge1}\Bigl(\sum_{n\mid N}\frac{N}{n}\Bigr)q^{N}=\sum_{N\ge1}\Bigl(\sum_{k\mid N}k\Bigr)q^{N}=\sum_{N\ge1}\sigma_{1}(N)q^{N}.
$$
Reindexing the same double sum the other way, summing over $k$ first, gives $\sum_{n\ge1}n\sum_{k\ge1}q^{nk}=\sum_{n\ge1}\frac{nq^{n}}{1-q^{n}}$, which is the left side.

:::

:::

::: {.pf-step #divisors}

(b) $A(q)-4A(q^{4})=\sum_{N\ge1}\sigma_{1}^{*}(N)q^{N}$, where $A(q)=\sum_{n\ge1}\frac{nq^{n}}{1-q^{n}}$ and $\sigma_{1}^{*}(N)$ is the sum of the divisors of $N$ not divisible by $4$.

::: pf-proof

By step [](#parta){.pf-ref}, $A(q)=\sum_{N\ge1}\sigma_{1}(N)q^{N}$, since $\sum_{k\mid N}k=\sigma_{1}(N)$. Hence $A(q^{4})=\sum_{N\ge1}\sigma_{1}(N)q^{4N}=\sum_{M\ge1}\sigma_{1}(M/4)q^{M}$, with the convention that $\sigma_{1}(M/4)=0$ unless $4\mid M$. Therefore the coefficient of $q^{N}$ in $A(q)-4A(q^{4})$ is $\sigma_{1}(N)-4\sigma_{1}(N/4)$. A divisor $d$ of $N$ is divisible by $4$ exactly when $d=4e$ with $e\mid N/4$, so the divisors divisible by $4$ contribute $4\sigma_{1}(N/4)$ to $\sigma_{1}(N)$ and the remainder is the sum of the divisors of $N$ not divisible by $4$, that is $\sigma_{1}^{*}(N)$.

:::

:::

::: {.pf-step #partb}

(b) $\displaystyle\sum_{n=1}^{\infty}\Bigl(\frac{nq^{n}}{1-q^{n}}-\frac{4nq^{4n}}{1-q^{4n}}\Bigr)=\sum_{n=1}^{\infty}\Bigl(\frac{q^{n}}{(1-q^{n})^{2}}-\frac{4q^{4n}}{(1-q^{4n})^{2}}\Bigr)=\sum_{N\ge1}\sigma_{1}^{*}(N)q^{N}$.

::: pf-proof

The first series is $A(q)-4A(q^{4})$ and, by step [](#parta){.pf-ref} applied at $q$ and separately at $q^{4}$, so is the second; step [](#divisors){.pf-ref} identifies their common value with the series of $\sigma_{1}^{*}$.

:::

:::

::: {.pf-step #spliteven}

$\displaystyle\sum_{n=1}^{\infty}\frac{q^{n}}{(1+(-1)^{n}q^{n})^{2}}=\sum_{n=1}^{\infty}\frac{q^{n}}{(1-q^{n})^{2}}-4\sum_{n=1}^{\infty}\frac{q^{4n}}{(1-q^{4n})^{2}}$.

::: pf-proof

For odd $n$ we have $(-1)^{n}=-1$, so the summand is $\frac{q^{n}}{(1-q^{n})^{2}}$. For even $n=2m$ put $x=q^{2m}$; then the summand is $\frac{x}{(1+x)^{2}}$, and the identity $\frac{x}{(1-x)^{2}}-\frac{4x^{2}}{(1-x^{2})^{2}}=\frac{x}{(1+x)^{2}}$ holds because $\frac{4x^{2}}{(1-x^{2})^{2}}=\frac{4x^{2}}{(1-x)^{2}(1+x)^{2}}$ and
$$
\frac{x}{(1-x)^{2}}-\frac{4x^{2}}{(1-x)^{2}(1+x)^{2}}=\frac{x\bigl((1+x)^{2}-4x\bigr)}{(1-x)^{2}(1+x)^{2}}=\frac{x(1-x)^{2}}{(1-x)^{2}(1+x)^{2}}=\frac{x}{(1+x)^{2}}.
$$
Summing the even-$n$ summands over $m\ge1$ therefore gives $\sum_{m\ge1}\frac{q^{2m}}{(1-q^{2m})^{2}}-4\sum_{m\ge1}\frac{q^{4m}}{(1-q^{4m})^{2}}$, and adding the odd-$n$ summands, which extend the first sum to all $n\ge1$, yields the displayed identity.

:::

:::

::: {.pf-step #partc}

(c) Jacobi's four-squares theorem is equivalent to $\theta(\tau)^{4}=1+8\sum_{n\ge1}\frac{q^{n}}{(1+(-1)^{n}q^{n})^{2}}$.

::: pf-proof

By definition $\theta(\tau)=\sum_{n\in\ZZ}q^{n^{2}}$, so $\theta(\tau)^{4}=\sum_{N\ge0}r_{4}(N)q^{N}$, where $r_{4}(N)$ counts the representations of $N$ as a sum of four squares; the constant term is $r_{4}(0)=1$, the unique representation $0=0^{2}+0^{2}+0^{2}+0^{2}$. Steps [](#partb){.pf-ref} and [](#spliteven){.pf-ref} identify the series on the right of (c) with $\sum_{N\ge1}\sigma_{1}^{*}(N)q^{N}$, so the identity of (c) says
$$
1+\sum_{N\ge1}r_{4}(N)q^{N}=1+8\sum_{N\ge1}\sigma_{1}^{*}(N)q^{N}.
$$
Two power series with the same coefficients are equal, so (c) holds exactly when $r_{4}(N)=8\sigma_{1}^{*}(N)$ for every $N\ge1$, which is Jacobi's theorem:
$$
\boxed{\theta(\tau)^{4}=1+8\sum_{n=1}^{\infty}\frac{q^{n}}{(1+(-1)^{n}q^{n})^{2}}\iff r_{4}(N)=8\sigma_{1}^{*}(N)\ \ (N\ge1).}
$$

:::

:::

:::

:::
