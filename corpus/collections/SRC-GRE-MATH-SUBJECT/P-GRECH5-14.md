---
schema: qual/card@1
id: P-GRECH5-14
kind: problem
title: Image under a linear transformation of $\RR^2$
classification:
  areas:
  - applied-algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Re-transcribed from Chapter 5 review Question 14 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR) and checked against the source scans in assets/attachments/gre-math-ch5-review/, replacing the earlier chapter-5.pdf transcription.
---

::: {.problem}
The linear transformation $T\colon \RR^2 \to \RR^2$ that maps $(1, 2)$ to $(-1, 1)$ and $(0, -1)$ to $(2, -1)$ will map $(1, 1)$ to

(A) $(1, 2)$
(B) $(1, 0)$
(C) $(2, -1)$
(D) $(2, 1)$
(E) $(1, 1)$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The vector $(1,1)$ decomposes as
$$
(1,1)=(1,2)+(0,-1).
$$


::: pf-proof

Adding the two vectors on the right gives $(1+0,2-1)=(1,1)$.

:::

:::

::: {.pf-step #s1-2}

One has
$$
\boxed{T(1,1)=(1,0)},
$$
so the answer is (B).


::: pf-proof

By linearity and step [](#s1-1){.pf-ref},
$$
T(1,1)=T(1,2)+T(0,-1)=(-1,1)+(2,-1)=(1,0).
$$

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} gives the requested image.

:::

:::

:::
