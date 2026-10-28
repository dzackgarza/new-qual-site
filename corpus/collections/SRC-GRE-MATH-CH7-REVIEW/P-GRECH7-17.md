---
schema: qual/card@1
id: P-GRECH7-17
kind: problem
title: Solution set of $x+6/x>5$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 17 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
Which of the following is the solution set of the inequality $x + \frac{6}{x} > 5$?

(A) $(0, 2) \cup (3, \infty)$
(B) $(0, 1) \cup (2, \infty)$
(C) $(-\infty, 2) \cup (3, \infty)$
(D) $(0, 2) \cap (3, \infty)$
(E) $(-\infty, 0)$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For $x\ne0$, the inequality is equivalent to
$$
\frac{(x-2)(x-3)}{x}>0.
$$


::: pf-proof

One has
$$
x+\frac6x-5
=\frac{x^2-5x+6}{x}
=\frac{(x-2)(x-3)}{x}.
$$
The original expression is undefined at $x=0$, so $x=0$ is excluded from the domain.

:::

:::

::: {.pf-step #s1-2}

The expression in step [](#s1-1){.pf-ref} is positive exactly on
$$
(0,2)\cup(3,\infty).
$$


::: pf-proof

The only sign-change points are $0$, $2$, and $3$. On the four resulting intervals:
$$
\begin{array}{c|c}
\text{interval}&\operatorname{sgn}\dfrac{(x-2)(x-3)}x\\ \hline
(-\infty,0)&-\\
(0,2)&+\\
(2,3)&-\\
(3,\infty)&+
\end{array}
$$
The inequality is strict, so the zeros $2$ and $3$ are excluded, as is the undefined point $0$.

:::

:::

::: {.pf-step #s1-3}

Therefore the solution set is
$$
\boxed{(0,2)\cup(3,\infty)},
$$
so the answer is (A).


::: pf-proof

This is exactly the positive-sign set found in step [](#s1-2){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested solution set.

:::

:::

:::
