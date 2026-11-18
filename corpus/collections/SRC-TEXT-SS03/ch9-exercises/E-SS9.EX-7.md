---
schema: qual/card@1
id: E-SS9.EX-7
kind: problem
title: $\zeta(2)$ and $\zeta(4)$ from $\sum_m(m+\tau)^{-2}=\pi^2/\sin^2\pi\tau$
classification:
  areas:
  - complex-analysis
  topics:
  - Zeta Function
  - Series of Numbers
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
Setting $\tau = 1/2$ in the expression
$$
\sum_{m=-\infty}^{\infty} \frac{1}{(m + \tau)^2} = \frac{\pi^2}{\sin^2(\pi\tau)},
$$
deduce that
$$
\sum_{m \geq 1,\ m \text{ odd}} \frac{1}{m^2} = \frac{\pi^2}{8} \quad \text{and} \quad \sum_{m \geq 1} \frac{1}{m^2} = \frac{\pi^2}{6} = \zeta(2).
$$
Similarly, using $\sum 1/(m + \tau)^4$ deduce that
$$
\sum_{m \geq 1,\ m \text{ odd}} \frac{1}{m^4} = \frac{\pi^4}{96} \quad \text{and} \quad \sum_{m \geq 1} \frac{1}{m^4} = \frac{\pi^4}{90} = \zeta(4).
$$
These results were already obtained using Fourier series in the exercises at the end of Chapters 2 and 3 in Book I.
:::

::: {.solution}

The argument is the card's own: no copy of Stein and Shakarchi and no published solution set for this book is retained in `tmp/sources`, so nothing below is transcribed. The statement is the exercise the collection index records as Stein and Shakarchi, *Complex Analysis* (2003), Ch. 9, Exercise 7. Here the identity used is $\sum_{m\in\ZZ}(m+\tau)^{-2}=\pi^{2}/\sin^{2}(\pi\tau)$ for $\Im\tau>0$, and $\zeta(s)=\sum_{r\geq1}r^{-s}$.

::: pf

::: {.pf-step #tauhalf}

At $\tau=1/2$, $\sum_{m\in\ZZ}(m+\tfrac12)^{-2}=\pi^{2}$.

::: pf-proof

Substitute $\tau=1/2$ in the identity: $\sin^{2}(\pi/2)=1$.

:::

:::

::: {.pf-step #odd2}

$\sum_{r\geq1,\ r\ \text{odd}}r^{-2}=\pi^{2}/8$.

::: pf-proof

For each $m\in\ZZ$, $(m+\tfrac12)^{-2}=4(2m+1)^{-2}$, and $2m+1$ ranges over the odd integers as $m$ does; the odd integers pair as $r$ and $-r$, both contributing $r^{-2}$, so the sum equals $8\sum_{r\ \text{odd}\geq1}r^{-2}$. With step [](#tauhalf){.pf-ref}, $\pi^{2}=8\sum_{r\ \text{odd}\geq1}r^{-2}$.

:::

:::

::: {.pf-step #zeta2}

$\zeta(2)=\pi^{2}/6$.

::: pf-proof

Every positive integer is odd or twice an integer: $\zeta(2)=\sum_{r\ \text{odd}}r^{-2}+\sum_{r\geq1}(2r)^{-2}=\frac{\pi^{2}}{8}+\frac{1}{4}\zeta(2)$ by step [](#odd2){.pf-ref}, whence $\frac34\zeta(2)=\frac{\pi^{2}}{8}$.

:::

:::

::: {.pf-step #fourth}

$\sum_{m\in\ZZ}(m+\tfrac12)^{-4}=\pi^{4}/3$.

::: pf-proof

Differentiate the identity twice in $\tau$: the left side has second derivative $6\sum_{m}(m+\tau)^{-4}$, and the right side is $\pi^{2}\csc^{2}u$ with $u=\pi\tau$, whose second derivative is $\pi^{4}(4\csc^{2}u\cot^{2}u+2\csc^{4}u)$, equal to $2\pi^{4}$ at $u=\pi/2$. So $6\sum_{m}(m+\tfrac12)^{-4}=2\pi^{4}$.

:::

:::

::: {.pf-step #odd4}

$\sum_{r\ \text{odd}\geq1}r^{-4}=\pi^{4}/96$.

::: pf-proof

As in step [](#odd2){.pf-ref}, $(m+\tfrac12)^{-4}=16(2m+1)^{-4}$ and the odd integers pair, so the sum of step [](#fourth){.pf-ref} equals $32\sum_{r\ \text{odd}\geq1}r^{-4}$; hence that sum is $\frac{\pi^{4}}{3\cdot32}=\frac{\pi^{4}}{96}$.

:::

:::

::: {.pf-step #zeta4}

$\zeta(4)=\pi^{4}/90$.

::: pf-proof

$\zeta(4)=\sum_{r\ \text{odd}}r^{-4}+\frac{1}{16}\zeta(4)=\frac{\pi^{4}}{96}+\frac{1}{16}\zeta(4)$ by step [](#odd4){.pf-ref}, whence $\frac{15}{16}\zeta(4)=\frac{\pi^{4}}{96}$.

:::

:::

:::

:::
