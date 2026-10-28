---
schema: qual/card@1
id: P-GRECH7-05
kind: problem
title: Expected number of die rolls showing at least $3$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 5 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
A fair die is tossed twice. About how many times would you expect to roll 3 or greater?

(A) $2$
(B) $\frac{3}{2}$
(C) $1$
(D) $\frac{1}{2}$
(E) $0$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

On each toss, the probability of rolling $3$ or greater is
$$
\frac{4}{6}=\frac23.
$$


::: pf-proof

The favorable outcomes are $3,4,5,6$, four of the six equally likely faces.

:::

:::

::: pf-step

If $X$ is the number of the two tosses that are at least $3$, then
$$
E[X]=\frac43.
$$


::: pf-proof

Let $I_1,I_2$ be the indicator variables for the events that the first and second tosses, respectively, are at least $3$. Then $X=I_1+I_2$, and by step [](#s1-1){.pf-ref},
$$
E[I_1]=E[I_2]=\frac23.
$$
Linearity of expectation gives
$$
E[X]=E[I_1]+E[I_2]=\frac23+\frac23=\frac43.
$$

:::

:::

::: {.pf-step #s1-3}

Among the listed choices, the closest value to $4/3$ is
$$
\boxed{\frac32},
$$
so the answer is (B).


::: pf-proof

The distance from $4/3$ to $3/2$ is $1/6$, while its distance to $1$ is $1/3$, and all other listed choices are still farther away.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested approximate expected number.

:::

:::

:::
