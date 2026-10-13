---
schema: qual/card@1
id: P-GRECH2-02
kind: problem
title: Limit of the recursion $x_n=\sqrt{5x_{n-1}+6}$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 2 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
Let $(x_n)$ be the sequence with $x_1 = 2$ and $x_n = \sqrt{5x_{n-1} + 6}$ for every integer $n \ge 2$. Given that this sequence converges, what is its limit?

(A) $4$
(B) $6$
(C) $8$
(D) $10$
(E) $16$
:::

::: {.solution}
Let $L=\lim_{n\to\infty}x_n$, which exists by hypothesis.

<1>1. $L$ satisfies
$$
L=\sqrt{5L+6}.
$$

::: {.proof}
Since $(x_n)$ converges to $L$, the shifted sequence $(x_{n-1})$ also converges to $L$. The function $t\mapsto\sqrt{5t+6}$ is continuous on the values attained by the recurrence, so taking limits in
$$
x_n=\sqrt{5x_{n-1}+6}
$$
gives the displayed equation.
:::

<1>2. $L\in\{-1,6\}$.

::: {.proof}
Squaring the equation in step <1>1 gives
$$
L^2=5L+6,
$$
so
$$
L^2-5L-6=(L+1)(L-6)=0.
$$
:::

<1>3. In fact,
$$
\boxed{L=6},
$$
so the answer is (B).

::: {.proof}
Every term $x_n$ is nonnegative because it is either $x_1=2$ or a square root. Therefore its limit satisfies $L\geq0$, excluding the value $-1$ from step <1>2. Thus $L=6$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the requested limit and corresponding choice.
:::
:::
