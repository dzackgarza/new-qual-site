---
schema: qual/card@1
id: P-GRECH1-11
kind: problem
title: Determine a hyperbola parameter from a focus
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
  note: Re-transcribed from Chapter 1 review Question 11 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), replacing the earlier chapter-1.pdf transcription.
---

::: {.problem}
One of the foci of the hyperbola $y^2 = \left(\frac{x}{a}\right)^2 + 1$ is the point $(0, \sqrt{2})$. Find $a$.

(A) $\frac{1}{2\sqrt{2}}$
(B) $\frac{1}{\sqrt{2}}$
(C) $\frac{1}{2}$
(D) $1$
(E) $\sqrt{3}$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The hyperbola can be written as
$$
\frac{y^2}{1}-\frac{x^2}{a^2}=1.
$$


::: pf-proof

Rearranging the given equation gives
$$
y^2-\frac{x^2}{a^2}=1,
$$
which is the displayed standard form.

:::

:::

::: {.pf-step #s1-2}

The focus condition implies $a^2=1$.


::: pf-proof

For a hyperbola
$$
\frac{y^2}{b^2}-\frac{x^2}{A^2}=1,
$$
the foci are $(0,\pm c)$ with $c^2=A^2+b^2$. In step [](#s1-1){.pf-ref}, $b^2=1$ and $A^2=a^2$. Since the stated focus has $c=\sqrt2$,
$$
2=c^2=a^2+1,
$$
so $a^2=1$.

:::

:::

::: {.pf-step #s1-3}

Thus $|a|=1$, and the listed value is
$$
\boxed{a=1},
$$
so the answer is (D).


::: pf-proof

Step [](#s1-2){.pf-ref} gives $a=\pm1$. The equation of the hyperbola depends only on $a^2$, while among the listed choices only $a=1$ occurs.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} identifies the unique listed choice satisfying the focus condition.

:::

:::

:::
