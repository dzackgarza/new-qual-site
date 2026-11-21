---
schema: qual/card@1
id: P-CASP17C
kind: problem
title: 'An entire function bounded by $1+(\log(1+\abs z))^n$ is constant'
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Liouville's Theorem
  - Growth Estimates
relations: []
review: draft
audit:
  - event: solution-reviewed
    by: claude
    date: 2026-11-18
    note: >-
      Restructured into Lamport steps, and the audit list this card lacked is created here. The
      source is a course examination, so there is no retained solution set behind the card and the
      problem statement is the source. Each step re-read: Cauchy's estimate bounds the k-th
      derivative at 0 by k!/R^k times the supremum on the circle; the hypothesis bounds that
      supremum; a power of a logarithm divided by R^k tends to 0, so every positive-order Taylor
      coefficient at 0 vanishes; and an entire function equals its Taylor series. The case n = 0 is
      covered by the same estimate and is also the direct Liouville case. Not claimed: any
      statement with a bound growing like a power of R, where nonconstant examples exist.
---

::: {.problem}
Let $n \geq 0$ be an integer.
Assume $f : \CC \to \CC$ is an entire function such that
$$
\abs{f(z)} \leq 1 + (\log(1 + \abs{z}))^n.
$$
Prove that $f$ is constant.
:::

::: {.solution}
The argument is the card's own; the collection is a course examination, so there is no printed solution set behind the card and the problem statement is the source.

::: pf

::: {.pf-step #cauchy}
For every $R>0$ and $k\ge1$, $\abs{f^{(k)}(0)}\le\dfrac{k!}{R^{k}}\max_{\abs{z}=R}\abs{f(z)}$.

::: pf-proof
This is Cauchy's estimate for the derivatives of a function holomorphic on the disc of radius $R$: the $k$-th Taylor coefficient at $0$ is $\frac{1}{2\pi i}\oint_{\abs{z}=R}\frac{f(\zeta)}{\zeta^{k+1}}d\zeta$, whose modulus is at most $\frac{1}{2\pi}\cdot2\pi R\cdot\frac{\max\abs{f}}{R^{k+1}}$.
:::

:::

::: {.pf-step #growth}
$\max_{\abs{z}=R}\abs{f(z)}\le1+\bigl(\log(1+R)\bigr)^{n}$.

::: pf-proof
This is the hypothesis, evaluated on the circle $\abs{z}=R$, where $\abs{z}=R$ throughout.
:::

:::

::: {.pf-step #vanish}
For each fixed $k\ge1$, $\abs{f^{(k)}(0)}\le\frac{k!}{R^{k}}\bigl(1+(\log(1+R))^{n}\bigr)\to0$ as $R\to\infty$.

::: pf-proof
The right-hand side is $k!\,\frac{1+(\log(1+R))^{n}}{R^{k}}$; the numerator is bounded by a constant times $(\log(1+R))^{n}$ for large $R$, and $\frac{(\log(1+R))^{n}}{R^{k}}\to0$ because a power of a logarithm grows more slowly than any positive power of $R$. Hence the bound tends to $0$ and, being independent of anything but $R$, it forces the left side to be $0$.
:::

:::

::: {.pf-step #constant}
$f^{(k)}(0)=0$ for every $k\ge1$, so $f$ is constant.

::: pf-proof
Step [](#vanish){.pf-ref} gives $f^{(k)}(0)\le0$ in absolute value, so the Taylor series of $f$ at $0$ is the constant $f(0)$. An entire function equals the sum of its Taylor series at every point, so $f(z)=f(0)$ for all $z$.
:::

:::

::: {.pf-step}
$f$ is constant.

::: pf-proof
Steps [](#cauchy){.pf-ref}, [](#growth){.pf-ref}, [](#vanish){.pf-ref} and [](#constant){.pf-ref} give
$$
\boxed{\abs{f(z)}\le1+(\log(1+\abs{z}))^{n}\text{ for entire }f\implies f\text{ is constant}.}
$$
For $n=0$ the hypothesis reads $\abs{f}\le2$ and Liouville's theorem gives the conclusion directly; the argument above covers that case as well, since then $1+(\log(1+R))^{0}=2$ and the estimate still tends to $0$.
:::

:::

:::
:::
