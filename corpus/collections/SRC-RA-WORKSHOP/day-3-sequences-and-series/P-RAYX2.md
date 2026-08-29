---
schema: qual/card@1
id: P-RAYX2
kind: problem
title: Produce sequences $\{a_n\},\,\{b_n\}$ of
classification:
  areas:
  - real-analysis
  topics:
  - Sequences of Numbers
  - Limits
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: problem
Produce sequences $\{a_n\},\,\{b_n\}$ of positive real numbers such that $$\liminf_{n\to\infty}(a_nb_n)>\left(\liminf_{n\to\infty} a_n\right) \left(\liminf_{n\to\infty} b_n\right).$$

If $\{a_n\},\,\{b_n\}$ are sequences of positive real numbers and $\{a_n\}$ converges, prove that $$\liminf_{n\to\infty}(a_nb_n)=\left(\lim_{n\to\infty}a_n\right)\left(\liminf_{n\to\infty}b_n\right).$$
:::
::: {.solution}
<1>1. (Part 1) Take $a_n = 2 + (-1)^n$ and $b_n = 2 - (-1)^n$.
Proof: $a_n = 3, 1, 3, 1, \ldots$ and $b_n = 1, 3, 1, 3, \ldots$, both positive.
Then $\liminf a_n = 1$ and $\liminf b_n = 1$, so the right-hand side is $1$.
But $a_n b_n = (2+(-1)^n)(2-(-1)^n) = 4 - 1 = 3$ for all $n$, so $\liminf(a_n b_n) = 3 > 1$.
<1>2. (Part 2) Let $a_n \to a$ with $a_n, b_n > 0$.
Then $\liminf(a_n b_n) = a \liminf b_n$.
Proof: $a > 0$ since $a_n > 0$ for all $n$ (the limit of positive numbers is $\ge 0$; if $a = 0$ the claim is immediate: $0 \le \liminf a_n b_n$ and for any subsequence, $a_n b_n$ along it tends to $0$, so $\liminf a_n b_n = 0$). For $a > 0$: since $a_n \to a$, for any $\eps$ with $0 < \eps < a/2$ there is $N$ with $a - \eps \le a_n \le a + \eps$ for $n \ge N$.
Hence for $n \ge N$, $(a-\eps)b_n \le a_n b_n \le (a+\eps)b_n$.
Taking liminf (which ignores the finite initial segment), \[ (a-\eps)\liminf b_n \le \liminf(a_n b_n) \le (a+\eps)\liminf b_n . \] Letting $\eps \to 0$ gives the claim.
(Finite $\liminf$: if $\liminf b_n = \infty$ the inequality is read in the extended sense and both sides are $\infty$.)
<1>3. Q.E.D.
:::
