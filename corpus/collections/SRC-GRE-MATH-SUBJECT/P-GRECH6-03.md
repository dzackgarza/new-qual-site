---
schema: qual/card@1
id: P-GRECH6-03
kind: problem
title: Two smallest solutions of a congruence
classification:
  areas:
  - algebra
  topics:
  - Congruences
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Re-transcribed from Chapter 6 review Question 3 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), compared with assets/attachments/chapter-6_extracted.md, replacing the earlier paraphrased transcription."
---

::: {.problem}
Let $x_1$ and $x_2$ be the two smallest positive integers for which the following statement is true: "$85x - 12$ is a multiple of $19$." Then $x_1 + x_2 =$

(A) $19$
(B) $27$
(C) $31$
(D) $38$
(E) $47$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The divisibility condition is equivalent to
$$
9x\equiv 12\pmod{19}.
$$


::: pf-proof

The statement that $85x-12$ is a multiple of $19$ means
$$
85x\equiv12\pmod{19}.
$$
Since $85\equiv9\pmod{19}$, this is equivalent to the displayed congruence.

:::

:::

::: {.pf-step #s1-2}

The solutions are precisely
$$
x\equiv14\pmod{19}.
$$


::: pf-proof

Because
$$
9\cdot17=153\equiv1\pmod{19},
$$
the inverse of $9$ modulo $19$ is $17$. Multiplying the congruence in step [](#s1-1){.pf-ref} by $17$ gives
$$
x\equiv17\cdot12=204\equiv14\pmod{19}.
$$

:::

:::

::: {.pf-step #s1-3}

The two smallest positive solutions are $x_1=14$ and $x_2=33$, and therefore
$$
\boxed{x_1+x_2=47},
$$
so the answer is (E).


::: pf-proof

By step [](#s1-2){.pf-ref}, every solution has the form $14+19t$ with $t\in\ZZ$. The two smallest positive values occur for $t=0$ and $t=1$, namely $14$ and $33$, whose sum is $47$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested sum.

:::

:::

:::
