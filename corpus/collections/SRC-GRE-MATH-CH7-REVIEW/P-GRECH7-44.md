---
schema: qual/card@1
id: P-GRECH7-44
kind: problem
title: Probability of between $40$ and $50$ heads
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 44 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
A fair coin is flipped $10$ times. What's the probability of getting between $40$ and $50$ "heads"?

(A) $10\%$
(B) $38\%$
(C) $41\%$
(D) $47\%$
(E) $53\%$
:::

::: {.remark}
As printed, ten flips cannot produce forty heads; the book's solution treats one hundred flips.
:::

::: pf

::: {.pf-step #s1-1}

As printed with $10$ flips, the requested probability is $0$.


::: pf-proof

Ten coin flips can produce at most ten heads. Hence the event of obtaining between $40$ and $50$ heads is empty, so its probability is $0$. None of the listed choices equals $0$.

:::

:::

::: {.pf-step #s1-2}

If the intended number of flips is $100$, then for $X\sim\operatorname{Binomial}(100,1/2)$ the exact probability is
$$
\mathbb P(40\le X\le50)
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

::: {.pf-step #s1-3}

The probability in step [](#s1-2){.pf-ref} is approximately
$$
0.5221945186=52.21945186\%.
$$


::: pf-proof

Dividing the numerator by the denominator in step [](#s1-2){.pf-ref} gives the displayed decimal. In particular, its distance from $53\%$ is less than $0.8$ percentage points, whereas its distance from $47\%$ exceeds $5$ percentage points; the other listed percentages are farther away still.

:::

:::

::: {.pf-step #s1-4}

The normal approximation with continuity correction also gives approximately $52.2\%$, not $47\%$.


::: pf-proof

For $X\sim\operatorname{Binomial}(100,1/2)$, the mean is $50$ and the standard deviation is $5$. Continuity correction replaces $40\le X\le50$ by
$$
39.5<Y<50.5,
$$
so the standardized interval is
$$
-2.1<Z<0.1.
$$
Thus
$$
\mathbb P(40\le X\le50)
\approx \Phi(0.1)-\Phi(-2.1)
\approx0.5398-0.0179
=0.5219.
$$

:::

:::

::: {.pf-step #s1-5}

Therefore the printed question has no listed answer; after the evident correction from $10$ to $100$ flips, the closest listed answer is
$$
\boxed{53\%},
$$
which is choice (E), not the source's supplied choice (D).


::: pf-proof

Step [](#s1-1){.pf-ref} settles the literal question. Steps [](#s1-2){.pf-ref} through [](#s1-4){.pf-ref} independently show that the corrected $100$-flip problem has probability about $52.2\%$, making choice (E) the nearest listed percentage.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} records both the literal result and the corrected multiple-choice result.

:::

:::
