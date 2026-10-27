---
schema: qual/card@1
id: P-GRECH1-24
kind: problem
title: Simplify a trigonometric inverse expression
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
  note: Re-transcribed from Chapter 1 review Question 24 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), replacing the earlier chapter-1.pdf transcription. The book extraction read arccos; the chapter-1.pdf extraction and the book's solution read arccot.
---

::: {.problem}
Simplify $\sqrt{\csc^2\left(\operatorname{arccot}\frac{\pi}{4}\right)-1}$.

(A) $-1$
(B) $1$
(C) $\frac{\pi^2}{16}$
(D) $\frac{\pi}{4}$
(E) $\frac{\sqrt{\pi}}{2}$
:::

::: {.solution}

Set $\theta=\operatorname{arccot}(\pi/4)$.

::: pf

::: {.pf-step #s1-1}

$\csc^2\theta-1=\cot^2\theta$.


::: pf-proof

The Pythagorean identity
$$
1+\cot^2\theta=\csc^2\theta
$$
rearranges to the claimed equality.

:::

:::

::: {.pf-step #s1-2}

The requested expression is
$$
\boxed{\frac{\pi}{4}},
$$
so the answer is (D).


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
\sqrt{\csc^2\theta-1}
=\sqrt{\cot^2\theta}
=|\cot\theta|.
$$
Since $\theta=\operatorname{arccot}(\pi/4)$,
$$
\cot\theta=\frac{\pi}{4}>0.
$$
Thus $|\cot\theta|=\pi/4$.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} gives the requested simplified value and corresponding choice.

:::

:::

:::
