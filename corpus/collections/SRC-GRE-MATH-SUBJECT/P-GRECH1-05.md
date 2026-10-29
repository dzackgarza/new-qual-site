---
schema: qual/card@1
id: P-GRECH1-05
kind: problem
title: Evaluate a composition using an inverse function
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
  note: Re-transcribed from Chapter 1 review Question 5 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), replacing the earlier chapter-1.pdf transcription.
---

::: {.problem}
Let $f$ be a real-valued function whose inverse is given by the equation:

$$
f^{-1}(x) = x(1 + x^2) + (1 - x^2)
$$

What's the value of $f(f^{-1}(f(2)))$?

(A) $-2$
(B) $-1$
(C) $1$
(D) $2$
(E) $7$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

$f^{-1}(1)=2$.


::: pf-proof

Substituting $x=1$ into the given formula gives
$$
f^{-1}(1)=1(1+1^2)+(1-1^2)=2.
$$

:::

:::

::: {.pf-step #s1-2}

$f(2)=1$.


::: pf-proof

Apply $f$ to the equality in step [](#s1-1){.pf-ref}. Since $f\circ f^{-1}$ is the identity on the domain of $f^{-1}$,
$$
f(2)=f\bigl(f^{-1}(1)\bigr)=1.
$$

:::

:::

::: {.pf-step #s1-3}

The requested value is
$$
f\bigl(f^{-1}(f(2))\bigr)=\boxed{1},
$$
so the answer is (C).


::: pf-proof

The inverse identity gives
$$
f\bigl(f^{-1}(f(2))\bigr)=f(2),
$$
and step [](#s1-2){.pf-ref} evaluates the right-hand side.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested value and choice.

:::

:::

:::
