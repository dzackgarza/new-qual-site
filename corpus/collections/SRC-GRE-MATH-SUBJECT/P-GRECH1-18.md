---
schema: qual/card@1
id: P-GRECH1-18
kind: problem
title: Solve a quadratic equation in log x
classification:
  areas:
  - algebra
  topics:
  - Exponential and Logarithmic Functions
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Re-transcribed from Chapter 1 review Question 18 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), replacing the earlier chapter-1.pdf transcription. The book extraction read e^{2i} in choice (C); the chapter-1.pdf extraction and the book's solution give e^2.
---

::: {.problem}
What are the roots of the following equation?

$$
(\log x)^2 = 2 \log x
$$

(A) $1, e^{-2}$
(B) $1, \sqrt{e}$
(C) $1, e^{2}$
(D) all $x > 0$
(E) all real $x$
:::

::: {.solution}

Set $y=\log x$.

::: pf

::: {.pf-step #s1-1}

$y=0$ or $y=2$.


::: pf-proof

The given equation becomes
$$
y^2=2y,
$$
so
$$
y(y-2)=0.
$$
Thus $y=0$ or $y=2$.

:::

:::

::: {.pf-step #s1-2}

The roots are
$$
\boxed{x=1\ \text{or}\ x=e^2},
$$
so the answer is (C).


::: pf-proof

Since the logarithm is defined only for $x>0$, exponentiating the alternatives from step [](#s1-1){.pf-ref} gives
$$
x=e^0=1
\quad\text{or}\quad
x=e^2.
$$
Both values are positive and therefore lie in the domain of the original equation.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} gives all solutions of the transformed equation within the logarithm's domain.

:::

:::

:::
