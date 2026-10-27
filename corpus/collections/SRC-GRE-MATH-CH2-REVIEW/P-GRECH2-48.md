---
schema: qual/card@1
id: P-GRECH2-48
kind: problem
title: Coefficient $k_3$ of $x^4$ expanded in powers of $x+1$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 48 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
If $k_i$ ($i = 0, 1, 2, 3, 4$) are constants such that $x^4 = k_0 + k_1(x+1) + k_2(x+1)^2 + k_3(x+1)^3 + k_4(x+1)^4$ is an identity in $x$, what is the value of $k_3$?

(A) $-4$
(B) $-3$
(C) $-2$
(D) $3$
(E) $4$
:::

::: {.solution}

::: pf

::: pf-step

Set $y=x+1$, so $x=y-1$.


::: pf-proof

This is a change of variable in the polynomial identity, chosen so that powers of $x+1$ become ordinary powers of $y$.

:::

:::

::: {.pf-step #s1-2}

In powers of $y$,
$$
x^4=(y-1)^4
=y^4-4y^3+6y^2-4y+1.
$$


::: pf-proof

This is the binomial expansion of $(y-1)^4$.

:::

:::

::: {.pf-step #s1-3}

The coefficient of $(x+1)^3$ is
$$
\boxed{k_3=-4},
$$
so the answer is (A).


::: pf-proof

The given identity becomes
$$
(y-1)^4=k_0+k_1y+k_2y^2+k_3y^3+k_4y^4.
$$
Comparing the coefficient of $y^3$ with step [](#s1-2){.pf-ref} gives $k_3=-4$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested coefficient and corresponding choice.

:::

:::

:::
