---
schema: qual/card@1
id: P-GRECH6-05
kind: problem
title: Trailing zeros of $100!$
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Re-transcribed from Chapter 6 review Question 5 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), compared with assets/attachments/chapter-6_extracted.md, replacing the earlier paraphrased transcription."
---

::: {.problem}
When expressed in its usual decimal notation, the number $100!$ (that is, $100$ factorial) ends in how many consecutive zeros?

(A) $20$
(B) $24$
(C) $30$
(D) $32$
(E) $50$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The number of trailing zeros of $100!$ is the exponent of $5$ in its prime factorization.


::: pf-proof

Each trailing zero contributes a factor of $10=2\cdot5$. In $100!$, every factor of $5$ can be paired with a distinct factor of $2$, because multiples of $2$ occur more frequently than multiples of $5$. Hence the number of factors of $10$ is the exponent of $5$ in $100!$.

:::

:::

::: {.pf-step #s1-2}

The exponent of $5$ in $100!$ is
$$
\left\lfloor\frac{100}{5}\right\rfloor
+\left\lfloor\frac{100}{25}\right\rfloor
=20+4=24.
$$


::: pf-proof

Each multiple of $5$ among $1,\dots,100$ contributes at least one factor of $5$, giving $\lfloor100/5\rfloor=20$ factors. Each multiple of $25$ contributes one additional factor of $5$, giving $\lfloor100/25\rfloor=4$ more. Since $125>100$, no integer in the product contributes a third factor of $5$.

:::

:::

::: {.pf-step #s1-3}

Therefore $100!$ ends in
$$
\boxed{24}
$$
consecutive zeros, so the answer is (B).


::: pf-proof

Combine steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested number of trailing zeros.

:::

:::

:::
