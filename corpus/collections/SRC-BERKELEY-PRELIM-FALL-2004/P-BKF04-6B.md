---
schema: qual/card@1
id: P-BKF04-6B
kind: problem
title: Averages of $f$ over the circle $\abs{z}=1/n$ for $f$ with a pole at $0$
classification:
  areas: [prelim]
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Structured the argument into numbered steps, and repaired a clause that understated the
    geometric-sum computation: the average for f = z^{-m} equals n^m when n divides m and 0
    otherwise, so the sequence is eventually zero because n > m makes n | m impossible; the card
    said only that the sum vanishes when n > m, without the value in the remaining case. Also
    supplied the two estimates used silently: the uniform O(1/n) bound for a function holomorphic at
    the origin, from the derivative on a compact disc, and the finiteness of the principal part,
    which is what makes the decomposition into a finite sum of powers plus an entire function
    legitimate. Every macro used is one the preamble defines. No source text is retained for this
    examination.
---

::: {.problem}
Suppose that $f(z)$ is holomorphic on all of $\CC$ except for a pole at $z=0$. Prove that

$$
\lim_{n\to\infty}\frac1n\sum_{k=1}^n f\left(\frac1ne^{2\pi ik/n}\right)
$$

exists.
:::

::: {.solution}

The argument is the card's own; the card is an examination problem and no published solution is retained for it.

Let $f$ be holomorphic on $\CC\setminus\{0\}$ with a pole at $0$, and for $n\geq1$ put
$$
A_{n}=\frac1n\sum_{k=1}^{n}f\Bigl(\frac1n e^{2\pi ik/n}\Bigr).
$$

::: pf

::: {.pf-step #rho}
The points $\frac1ne^{2\pi ik/n}$, $k=1,\dots,n$, are distinct and all lie on the circle $\abs{z}=1/n$.

::: pf-proof
$\abs{\frac1ne^{2\pi ik/n}}=1/n$, and the arguments $2\pi k/n$ for $k=1,\dots,n$ are distinct modulo $2\pi$, so the points are distinct.
:::

:::

::: {.pf-step #holo}
If $f$ is holomorphic at $0$ as well, then $A_{n}\to f(0)$.

::: pf-proof
$f$ is then holomorphic on a neighbourhood of the closed disc $\abs{z}\leq1$, so $\abs{f'}\leq K$ there for some $K$. For each $k$, the mean value theorem along the segment from $0$ to $z_{k}=\frac1ne^{2\pi ik/n}$ gives $\abs{f(z_{k})-f(0)}\leq K\abs{z_{k}}=K/n$. Averaging, $\abs{A_{n}-f(0)}\leq K/n\to0$.
:::

:::

::: {.pf-step #principal}
$f$ is a finite linear combination of the functions $z\mapsto z^{-m}$, $m\geq1$, plus a function entire on $\CC$.

::: pf-proof
Because $f$ has a pole at $0$, its Laurent expansion about $0$ has a finite principal part: there are $a_{-M},\dots,a_{-1}$ and an entire function $g$ with
$$
f(z)=\sum_{m=1}^{M}a_{-m}z^{-m}+g(z)
$$
for $0<\abs{z}$. This is the standard decomposition of a meromorphic function with a single pole, the principal part being a finite sum because the pole has finite order.
:::

:::

::: {.pf-step #power}
For $f(z)=z^{-m}$ with $m\geq1$, $A_{n}$ equals $n^{m}$ when $n\mid m$ and $0$ otherwise; in particular $A_{n}=0$ for all $n>m$.

::: pf-proof
$f\bigl(\frac1ne^{2\pi ik/n}\bigr)=n^{m}e^{-2\pi ikm/n}$, so $A_{n}=n^{m-1}\sum_{k=1}^{n}e^{-2\pi ikm/n}$. The sum is a full geometric sum with ratio $q=e^{-2\pi im/n}$, which equals $n$ if $q=1$ and $\frac{q(1-q^{n})}{1-q}=0$ if $q\neq1$, since $q^{n}=e^{-2\pi im}=1$. And $q=1$ exactly when $n\mid m$, which for $n>m\geq1$ is impossible.
:::

:::

::: {.pf-step #limit}
$A_{n}$ converges, to the constant coefficient of the Laurent expansion of $f$ at $0$.

::: pf-proof
Write $f=\sum_{m=1}^{M}a_{-m}z^{-m}+g$ as in step [](#principal){.pf-ref}. By linearity of the average, $A_{n}=\sum_{m}a_{-m}A_{n}^{(m)}+A_{n}^{(g)}$, where $A^{(m)}$ is the average of $z^{-m}$ and $A^{(g)}$ that of $g$. For $n>M$ every $A_{n}^{(m)}=0$ by step [](#power){.pf-ref}, and $A_{n}^{(g)}\to g(0)$ by step [](#holo){.pf-ref}. Hence $A_{n}\to g(0)$ for $n>M$, and the limit exists.
:::

:::

::: {.pf-step}
$\lim_{n\to\infty}\frac1n\sum_{k=1}^{n}f\bigl(\frac1ne^{2\pi ik/n}\bigr)$ exists, and equals the constant term of $f$ at $0$.

::: pf-proof
Step [](#limit){.pf-ref} gives existence and identifies the value: the constant coefficient $a_{0}=g(0)$ of the Laurent expansion, since the principal part contributes nothing in the limit.
:::

:::

:::
:::
