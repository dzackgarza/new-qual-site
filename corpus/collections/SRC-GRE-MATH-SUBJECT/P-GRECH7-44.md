---
schema: qual/card@1
id: P-GRECH7-44
kind: problem
title: Probability of between $40$ and $50$ heads
classification:
  areas: [prelim]
  topics:
  - Probability
  - Binomial Distribution
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 44 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source prints 10 flips, for which 40 to 50 heads is impossible, and supplies answer (D); the book solution uses 100 flips. The statement now has 100 flips and asks for the approximate probability; the closest choice is (E).
---

::: {.problem}
A fair coin is flipped $100$ times. Approximately what is the probability of getting between $40$ and $50$ "heads"?

(A) $10\%$
(B) $38\%$
(C) $41\%$
(D) $47\%$
(E) $53\%$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-2}

For $X\sim\operatorname{Binomial}(100,1/2)$ the exact probability is
$$
\Prob(40\le X\le50)
=2^{-100}\sum_{k=40}^{50}\binom{100}{k}
=\frac{661960194919833116818686458436}{1267650600228229401496703205376}.
$$


::: pf-proof

For a fair coin, the probability of exactly $k$ heads in $100$ independent flips is
$$
\binom{100}{k}\left(\frac12\right)^{100}.
$$
The events for distinct $k$ are disjoint, so summing from $40$ through $50$ gives the displayed expression. Direct integer summation of those eleven binomial coefficients gives the stated numerator.

:::

:::

::: pf-step

The probability is approximately $52.2\%$, so the closest choice is
$$
\boxed{53\%},
$$
which is choice (E).


::: pf-proof

Dividing the numerator by the denominator in step [](#s1-2){.pf-ref} gives
$$
0.5221945186\ldots
$$
Its distance from $53\%$ is less than $0.8$ percentage points, whereas its distance from $47\%$ exceeds $5$ percentage points; the other listed percentages are farther away still. As a check, the normal approximation with mean $50$, standard deviation $5$ and continuity correction gives $\Phi(0.1)-\Phi(-2.1)\approx0.5398-0.0179=0.5219$.

:::

:::

:::

:::
