---
schema: qual/card@1
id: P-GRECH1-06
kind: problem
title: Recover a function from a composition identity
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
  note: Re-transcribed from Chapter 1 review Question 6 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), replacing the earlier chapter-1.pdf transcription.
---

::: {.problem}
Let $f, g$, and $h$ be real-valued functions defined for all positive $x$ such that:

$$
(f \circ g)(x) = (g \circ h)(x)
$$

If $f(x) = x + 1$ and $g(x) = \sqrt{x}$, what is $h(x)$?

(A) $x^2 - 1$
(B) $\sqrt{x - 1}$
(C) $\sqrt{x} + 2$
(D) $x\sqrt{x} + 1$
(E) $1 + (\sqrt{x} + 2)\sqrt{x}$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

$(f\circ g)(x)=\sqrt{x}+1$.


::: pf-proof

Using the given formulas,
$$
(f\circ g)(x)=f(\sqrt{x})=\sqrt{x}+1.
$$

:::

:::

::: {.pf-step #s1-2}

The composition identity implies
$$
\sqrt{h(x)}=\sqrt{x}+1.
$$


::: pf-proof

Since $g(t)=\sqrt{t}$,
$$
(g\circ h)(x)=\sqrt{h(x)}.
$$
Equating this with step [](#s1-1){.pf-ref} gives the displayed equality.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
h(x)=\boxed{1+(\sqrt{x}+2)\sqrt{x}},
$$
so the answer is (E).


::: pf-proof

Squaring the equality in step [](#s1-2){.pf-ref} gives
$$
h(x)=(\sqrt{x}+1)^2=x+2\sqrt{x}+1
=1+(\sqrt{x}+2)\sqrt{x}.
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested function and corresponding choice.

:::

:::

:::
