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
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read in the retained book `assets/attachments/Cracking_the_GRE_Mathematics_Subject.pdf`: the statement is problem 1 of the practice test, printed
    on PDF p. 416, and its printed words are the card's. The test carries no printed number, so the
    locator names its opening page (p. 415) and the problem number rather than inventing a test
    number. Not checked in this pass: the argument, which the edit does not touch.
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
This is problem 1 of the practice test that begins on PDF p. 415 of *Cracking the GRE Mathematics Subject Test*, retained in this repository as `assets/attachments/Cracking_the_GRE_Mathematics_Subject.pdf` (the test is printed without a number, so its opening page and the problem number locate it); the item is on PDF p. 416, and the statement below is its wording.

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
