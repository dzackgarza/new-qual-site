---
schema: qual/card@1
id: P-GRECH6-18
kind: problem
title: Which ring has a different number of units
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
  note: "Re-transcribed from Chapter 6 review Question 18 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), compared with assets/attachments/extracted/chapter-6.md, replacing the earlier paraphrased transcription."
---

::: {.problem}
Which one of the following rings does NOT have the same number of units as the other four?

(A) $\ZZ \oplus \ZZ$
(B) $\ZZ \oplus \ZZ_3$
(C) $\ZZ \oplus \ZZ_5$
(D) $\ZZ \oplus \ZZ_6$
(E) $\ZZ_3 \oplus \ZZ_3$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

A pair $(r,s)$ is a unit in a direct-product ring $R\oplus S$ exactly when both $r$ and $s$ are units in their respective rings.


::: pf-proof

If $(r,s)(r',s')=(1,1)$, then $rr'=1$ and $ss'=1$, so both components are units. Conversely, if $r^{-1}$ and $s^{-1}$ exist, then $(r^{-1},s^{-1})$ is the inverse of $(r,s)$.

:::

:::

::: {.pf-step #s1-2}

The rings $\ZZ$, $\ZZ_3$, and $\ZZ_6$ each have two units, while $\ZZ_5$ has four units.


::: pf-proof

The units are
$$
\ZZ^\times=\{1,-1\},
\qquad
\ZZ_3^\times=\{\overline1,\overline2\},
$$
$$
\ZZ_6^\times=\{\overline1,\overline5\},
\qquad
\ZZ_5^\times=\{\overline1,\overline2,\overline3,\overline4\}.
$$
For $\ZZ_n$, these are exactly the residue classes relatively prime to $n$.

:::

:::

::: {.pf-step #s1-3}

Choices (A), (B), (D), and (E) each have four units, whereas choice (C) has eight.


::: pf-proof

By steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref}, the numbers of units are respectively
$$
2\cdot2=4,
\quad
2\cdot2=4,
\quad
2\cdot4=8,
\quad
2\cdot2=4,
\quad
2\cdot2=4.
$$

:::

:::

::: {.pf-step #s1-4}

Therefore the exceptional ring is
$$
\boxed{\ZZ\oplus\ZZ_5},
$$
so the answer is (C).


::: pf-proof

Step [](#s1-3){.pf-ref} shows that this ring has eight units while each of the other four has four.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the required ring.

:::

:::

:::
