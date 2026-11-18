---
schema: qual/card@1
id: E-BTI7W
kind: problem
title: Pointwise but not uniform convergence to the zero function
classification:
  areas:
  - topology
  topics:
  - Uniform Convergence
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §21 Exercise 9, printed p. 134, with Figure 21.1
    and Theorem 21.6; both parts are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 21.9, PDF pp. 25-26. The pointwise limit is 0 — at
    the origin because the denominator is n+1, and elsewhere because n^2(nx^2 - 2x)
    dominates — while at x_n = 1/n each f_n equals 1, so the convergence is not uniform;
    with continuous f_n that also follows from Exercise 21.8. (tmp/sources/munkres-
    solutions-positron-ch2.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked (a) at the two points 0 and x nonzero (the
    denominator expansion n^3(x-1/n)^2+1 = n^3x^2-2n^2x+n+1 bounded below by n eventually)
    and (b) through sup_x f_n = f_n(1/n) = 1. positron0802, Exercise 21.9, PDF pp. 25-26;
    the card proves (b) directly rather than through Exercise 21.8 and says so. The printed
    statement needed no repair.
---

::: {.exercise}

Let $f_n: \RR \to \RR$ be the function

$$
f_n(x) = \frac{1}{n^3[x - (1/n)]^2 + 1}.
$$

Let $f: \RR \to \RR$ be the zero function.

(a) Show that $f_n(x) \to f(x)$ for each $x \in \RR$.

(b) Show that $f_n$ does not converge uniformly to $f$.
(This shows that the converse of Theorem 21.6 does not hold; the limit function $f$ may be continuous even though the convergence is not uniform.)
:::

::: {.solution}
The published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 21.9, PDF pp. 25--26** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); both parts are theirs. The proof of (b) below uses the sup norm directly instead of their appeal to continuity of the $f_{n}$.

Let $f_{n}(x)=1/\big(n^{3}[x-(1/n)]^{2}+1\big)$ and let $f$ be the zero function.

::: pf

::: {.pf-step #pointwise}
(a) $f_{n}(x)\to f(x)$ for each $x\in\RR$.

:::: pf-proof

::: {.pf-step #at-zero}
$f_{n}(0)=1/(n+1)\to0$.

::: pf-proof
At $x=0$ the denominator is $n^{3}\cdot(1/n)^{2}+1=n+1$, so $f_{n}(0)=1/(n+1)$, which tends to $0$.
:::

:::

::: {.pf-step #at-nonzero}
For $x\ne0$, $f_{n}(x)\to0$.

::: pf-proof
Expanding,
$$
n^{3}\Big(x-\frac1n\Big)^{2}+1=n^{3}x^{2}-2n^{2}x+n+1 .
$$
Since $x\ne0$, choose $N$ with $n\abs{x}\ge4$ for all $n\ge N$; then $n^{3}x^{2}-2n^{2}x\ge n^{3}x^{2}-2n^{2}\abs{x}=n^{2}\abs{x}\big(n\abs{x}-2\big)\ge\tfrac12 n^{2}\abs{x}\cdot n\abs{x}=\tfrac12 n^{3}x^{2}$. Hence for $n\ge N$ the denominator is at least $n$, so $0\le f_{n}(x)\le1/n$, and $1/n\to0$.
:::

:::

::: {.pf-step}
(a) holds.

::: pf-proof
Steps [](#at-zero){.pf-ref} and [](#at-nonzero){.pf-ref} cover every $x\in\RR$, and $f$ is the zero function.
:::

:::

:::

:::

::: {.pf-step #not-uniform}
(b) $f_{n}$ does not converge uniformly to $f$.

::: pf-proof
At $x_{n}=1/n$ the denominator is $n^{3}\cdot0+1=1$, so $f_{n}(x_{n})=1$ for every $n$. Also $0<f_{n}(x)\le1$ for every $x$, since the denominator is at least $1$. Hence
$$
\sup_{x\in\RR}\abs{f_{n}(x)-f(x)}=\sup_{x\in\RR}f_{n}(x)=1
$$
for every $n$, which does not tend to $0$. Uniform convergence to the zero function would require this supremum to tend to $0$, so the convergence is not uniform.
:::

:::

:::
:::
