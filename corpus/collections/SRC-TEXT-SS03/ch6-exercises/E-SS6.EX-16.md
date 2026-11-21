---
schema: qual/card@1
id: E-SS6.EX-16
kind: problem
title: Analytic continuation of $\zeta$ from its Gamma-integral representation
classification:
  areas:
  - complex-analysis
  topics:
  - Zeta Function
  - Gamma Function
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
    Restructured into numbered steps for issue #2: the split of $\Gamma\zeta$, the entire second integral, the
    Taylor split of $x/(e^{x}-1)$ at order $N$, the finite principal part plus a holomorphic remainder, and the
    cancellation at the nonpositive integers with the surviving simple pole. No retained solution set covers
    this exercise (the collection retains the textbook, not a solutions manual), so the argument is the
    card's own; it was re-read for this pass.
---

::: {.exercise}
Use the previous exercise to give another proof that $\zeta(s)$ is continuable in the complex plane with only singularity a simple pole at $s = 1$.

[Hint: Write
$$
\zeta(s) = \frac{1}{\Gamma(s)} \int_0^1 \frac{x^{s-1}}{e^x - 1}\, dx + \frac{1}{\Gamma(s)} \int_1^{\infty} \frac{x^{s-1}}{e^x - 1}\, dx.
$$
The second integral defines an entire function, while
$$
\int_0^1 \frac{x^{s-1}}{e^x - 1}\, dx = \sum_{m=0}^{\infty} \frac{B_m}{m!\,(s + m - 1)},
$$
where $B_m$ denotes the $m^{\text{th}}$ Bernoulli number defined by
$$
\frac{x}{e^x - 1} = \sum_{m=0}^{\infty} \frac{B_m}{m!} x^m.
$$
Then $B_0 = 1$, and since $z/(e^z - 1)$ is holomorphic for $\abs{z} < 2\pi$, we must have $\limsup_{m \to \infty} \abs{B_m/m!}^{1/m} = 1/2\pi$.]
:::

::: {.solution}
No retained solution set covers this exercise; the collection retains the textbook (`assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`) and no solutions manual, so the argument is the card's own. Use is made of $\Gamma(s)\zeta(s)=\int_{0}^{\infty}\frac{x^{s-1}}{e^{x}-1}dx$ for $\Re s>1$, of the Bernoulli expansion $\frac{x}{e^{x}-1}=\sum_{m\ge0}\frac{B_{m}}{m!}x^{m}$ for $\abs{x}<2\pi$ with $B_{0}=1$, and of $1/\Gamma$ being entire with simple zeros at $0,-1,-2,\dots$.

::: pf

::: {.pf-step #split}
For $\Re s>1$, $\Gamma(s)\zeta(s)=\int_{0}^{1}\frac{x^{s-1}}{e^{x}-1}dx+\int_{1}^{\infty}\frac{x^{s-1}}{e^{x}-1}dx$.

::: pf-proof
Split the defining integral at $x=1$; both pieces converge absolutely for $\Re s>1$, near $0$ because $e^{x}-1\sim x$ and near $\infty$ because $e^{-x}$ decays faster than any power.
:::

:::

::: {.pf-step #entire}
The second integral defines an entire function of $s$.

::: pf-proof
On a compact set of $s$-values $\abs{s}\le M$ and $1\le x<\infty$, the integrand is bounded by $x^{M-1}/(e^{x}-1)\le C x^{M}e^{-x}$ for a suitable $C$, which is integrable on $[1,\infty)$; the bound is independent of $s$ and locally integrable, so dominated convergence gives continuity in $s$, and the same argument after differentiating under the integral sign under $\partial/\partial s$ gives holomorphy on all of $\CC$.
:::

:::

::: {.pf-step #taylor}
For each $N\ge0$ there is $r_{N}$ holomorphic near $[0,1]$ with $\dfrac{x}{e^{x}-1}=\sum_{m=0}^{N}\frac{B_{m}}{m!}x^{m}+x^{N+1}r_{N}(x)$ on a neighbourhood of $[0,1]$.

::: pf-proof
$h(x)=x/(e^{x}-1)$ extends holomorphically to $\abs{x}<2\pi$, the origin being removable with value $1=B_{0}$; its Taylor series there is $\sum\frac{B_{m}}{m!}x^{m}$ by the definition of the $B_{m}$. Subtracting the partial sum through degree $N$ leaves a holomorphic function vanishing to order at least $N+1$ at $0$, which is $x^{N+1}r_{N}(x)$ with $r_{N}$ holomorphic; the disc of radius $2\pi$ contains $[0,1]$.
:::

:::

::: {.pf-step #principal}
$\displaystyle\int_{0}^{1}\frac{x^{s-1}}{e^{x}-1}dx=\sum_{m=0}^{N}\frac{B_{m}}{m!\,(s+m-1)}+H_{N}(s)$ with $H_{N}$ holomorphic on $\Re s>-N$.

::: pf-proof
Write the integrand as $x^{s-2}h(x)$ and insert the expansion of step [](#taylor){.pf-ref}:
$$
\int_{0}^{1}\frac{x^{s-1}}{e^{x}-1}dx=\sum_{m=0}^{N}\frac{B_{m}}{m!}\int_{0}^{1}x^{s+m-2}dx+\int_{0}^{1}x^{s+N-1}r_{N}(x)\,dx,
$$
and $\int_{0}^{1}x^{s+m-2}dx=\frac{1}{s+m-1}$. The remainder is $\int_{0}^{1}x^{s+N-1}r_{N}(x)dx$: on $\Re s>-N$ the factor $x^{s+N-1}$ is integrable at $0$ and $r_{N}$ is bounded on $[0,1]$, and differentiating under the integral sign as in step [](#entire){.pf-ref} shows it is holomorphic there. That is $H_{N}$.
:::

:::

::: {.pf-step #continuation}
$\zeta$ continues meromorphically to $\CC$ with poles contained in $\{1,0,-1,-2,\dots\}$.

::: pf-proof
By steps [](#split){.pf-ref}, [](#entire){.pf-ref} and [](#principal){.pf-ref}, $\Gamma(s)\zeta(s)$ agrees on $\Re s>1$ with a function meromorphic on $\Re s>-N$ whose poles lie among $s=1-m$ for $0\le m\le N$; the identity theorem extends the agreement, and $N$ is arbitrary, so $\Gamma\zeta$ is meromorphic on $\CC$ with poles contained in $\{1-m:m\ge0\}$. Multiplying by the entire function $1/\Gamma(s)$ gives a meromorphic continuation of $\zeta$ with poles contained in the same set.
:::

:::

::: {.pf-step}
The only singularity is a simple pole at $s=1$, so $\zeta$ is meromorphic on $\CC$ with just that pole.

::: pf-proof
At $s=1-m$ with $m\ge1$ the singular point is a nonpositive integer; $1/\Gamma$ has a simple zero there, and by step [](#continuation){.pf-ref} the factor $\Gamma\zeta$ has at worst a simple pole at each $1-m$, so the product is holomorphic at $s=1-m$ for every $m\ge1$: the singularity is removable. At $s=1$ the term with $m=0$ is $\frac{B_{0}}{s-1}=\frac{1}{s-1}$ by $B_{0}=1$, the remainder $H_{N}$ is holomorphic near $1$, and $\frac{1}{\Gamma(1)}=1$, so $\zeta$ has a simple pole at $s=1$ with residue $1$. Hence $\zeta$ is continuable to the whole plane with only singularity a simple pole at $s=1$, which is the assertion.
:::

:::

:::
:::
