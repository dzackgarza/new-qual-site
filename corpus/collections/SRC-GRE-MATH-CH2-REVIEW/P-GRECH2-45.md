---
schema: qual/card@1
id: P-GRECH2-45
kind: problem
title: Sum of $\sum_{n\ge1} nx^{2n}$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 45 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
If $-1 < x < 1$, then $\sum_{n=1}^{\infty} n x^{2n} =$

(A) $\frac{x^3}{(1-x)^2}$
(B) $\frac{x^2}{(1-x^2)^2}$
(C) $\frac{x}{(1+x^2)^2}$
(D) $\frac{x^3}{(1+x)^2}$
(E) $\frac{x^2}{(1+x^2)^2}$
:::

::: pf

::: pf-step

For $\abs{t}<1$,
$$
\sum_{n=1}^\infty n t^n=\frac{t}{(1-t)^2}.
$$


::: pf-proof

The geometric series satisfies
$$
\sum_{n=0}^\infty t^n=\frac1{1-t}
$$
for $\abs{t}<1$. Termwise differentiation inside its radius of convergence gives
$$
\sum_{n=1}^\infty n t^{n-1}=\frac1{(1-t)^2}.
$$
Multiplying by $t$ yields the stated identity.

:::

:::

::: pf-step

For $-1<x<1$,
$$
\sum_{n=1}^\infty n x^{2n}
=\frac{x^2}{(1-x^2)^2}.
$$


::: pf-proof

Since $\abs{x}<1$, one has $\abs{x^2}<1$. Substitute $t=x^2$ into the identity from step <1>1.

:::

:::

::: pf-step

Therefore the answer is
$$
\boxed{\text{(B) }\frac{x^2}{(1-x^2)^2}}.
$$


::: pf-proof

Step <1>2 is exactly the series in the problem.

:::

:::

::: pf-qed

Step <1>3 gives the requested expression and corresponding choice.

:::

:::
