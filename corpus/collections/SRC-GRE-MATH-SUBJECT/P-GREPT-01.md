---
schema: qual/card@1
id: P-GREPT-01
kind: problem
title: "Express $x^4+x$ given $x^2+x=3$"
classification:
  areas: [prelim]
  topics:
  - Polynomials
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 1 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
If $x^2 + x = 3$, then $x^4 + x =$

(A) $x^2 + 3$
(B) $4(3 - x)$
(C) $3(x - 1)$
(D) $6(2 - x)$
(E) $3x$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The given equation implies
$$
x^2=3-x.
$$


::: pf-proof

Subtracting $x$ from both sides of $x^2+x=3$ gives the stated identity.

:::

:::

::: {.pf-step #s1-2}

One has
$$
x^4=12-7x.
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
x^4=(x^2)^2=(3-x)^2=9-6x+x^2.
$$
Substituting $x^2=3-x$ again gives $x^4=9-6x+3-x=12-7x$.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
x^4+x=\boxed{6(2-x)},
$$
so the answer is (D).


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
x^4+x=(12-7x)+x=12-6x=6(2-x).
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the required expression.

:::

:::

:::
