---
schema: qual/card@1
id: P-PRACT20-W3-10
kind: problem
title: Error of the quadratic Taylor approximation to $\sqrt{1.01}$
classification:
  areas:
  - prelim
  topics:
  - Taylor Series
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against page 3-4 of the retained solutions booklet GRE Prep: Calculus
    II & III Practice Problem Solutions by Christian Parkinson
    (assets/attachments/Week3_solns.pdf), which prints this problem and a worked
    solution. The practice sheet itself is not retained and the collection's
    provenance list is empty, so the printed statement in that booklet is the
    source used for the statement. the printed problem lists the same five choices and asks which best approximates the error in approximating sqrt 1.01 by the same quadratic, and the printed solution selects (A)
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    The booklet's route is transcribed: the binomial expansion to third order with epsilon = x - 1, the subtraction of the quadratic, and the evaluation at epsilon = 0.01 giving (1/16) x 10^-6, with the elimination of the other choices recorded.
---

::: {.problem}
The polynomial $p(x) = 1 + \frac{1}{2}(x - 1) - \frac{1}{8}(x - 1)^{2}$ is used to approximate $\sqrt{1.01}$. Which of the following best approximates the error $\sqrt{1.01} - p(1.01)$?

(A) $\frac{1}{16} \times 10^{-6}$

(B) $\frac{1}{48} \times 10^{-8}$

(C) $\frac{3}{8} \times 10^{-10}$

(D) $-\frac{3}{8} \times 10^{-10}$

(E) $-\frac{1}{16} \times 10^{-6}$
:::

::: {.solution}

Put $\varepsilon=x-1$ and compare $\sqrt{1+\varepsilon}$ with
$p(1+\varepsilon)=1+\frac\varepsilon2-\frac{\varepsilon^2}{8}$, so that the
error is $\sqrt{1+\varepsilon}-(1+\frac\varepsilon2-\frac\varepsilon^2{8})$.

::: pf

::: {.pf-step #binomial}

$\sqrt{1+\varepsilon}=1+\frac\varepsilon2-\frac{\varepsilon^2}{8}+\frac{\varepsilon^3}{16}+O(\varepsilon^4)$
as $\varepsilon\to0$.

::: pf-proof

This is the binomial series of $(1+\varepsilon)^{1/2}$ from problem 4 of the
same sheet, with $\alpha=\frac12$: the coefficients are
$\frac{\alpha(\alpha-1)\cdots(\alpha-k+1)}{k!}$, which give $\alpha=\frac12$
for $k=1$, $\frac{\frac12\cdot(-\frac12)}{2}=-\frac18$ for $k=2$ and
$\frac{\frac12\cdot(-\frac12)\cdot(-\frac32)}{6}=\frac1{16}$ for $k=3$. The
series converges for $\abs\varepsilon<1$, so the remainder after the cubic
term is $O(\varepsilon^4)$.

:::

:::

::: {.pf-step #error}

The error is
$\sqrt{1+\varepsilon}-p(1+\varepsilon)=\frac{\varepsilon^3}{16}+O(\varepsilon^4)$.

::: pf-proof

Subtracting the polynomial, which consists of the terms of degree at most two,
from the expansion of step [](#binomial){.pf-ref} leaves
$\frac{\varepsilon^3}{16}+O(\varepsilon^4)$.

:::

:::

::: {.pf-step #answer}

With $\varepsilon=10^{-2}$ the error is about $\frac1{16}\times10^{-6}>0$, so
the answer is (A).

::: pf-proof

$\varepsilon^3=10^{-6}$, so the leading term is $\frac{1}{16}\times10^{-6}$,
positive, and the remainder is of order $10^{-8}$ at most for this
$\varepsilon$, far smaller. Hence the error is $\frac1{16}\times10^{-6}$ to
the precision of the choices: it is not of order $10^{-8}$ or $10^{-10}$,
which rules out (B), (C) and (D), and it is positive, which rules out (E). So
(A) is the answer.

:::

:::

:::


:::
