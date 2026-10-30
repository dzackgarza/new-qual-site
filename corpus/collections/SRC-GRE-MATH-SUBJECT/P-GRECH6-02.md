---
schema: qual/card@1
id: P-GRECH6-02
kind: problem
title: Digit sum of an LCM
classification:
  areas:
  - algebra
  topics:
  - Least Common Multiple
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Re-transcribed from Chapter 6 review Question 2 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), compared with assets/attachments/chapter-6_extracted.md, replacing the earlier paraphrased transcription."
---

::: {.problem}
Let $L$ be the least common multiple of $1001$ and $10101$. What's the sum of the digits of $L$? (All numbers are written in their usual decimal representation.)

(A) $6$
(B) $11$
(C) $17$
(D) $22$
(E) $33$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The greatest common divisor of $1001$ and $10101$ is $91$.


::: pf-proof

The Euclidean algorithm gives
$$
10101=10\cdot1001+91,
\qquad
1001=11\cdot91.
$$
Hence the last nonzero remainder is $91$, so
$$
\gcd(1001,10101)=91.
$$

:::

:::

::: {.pf-step #s1-2}

Their least common multiple is
$$
L=111111.
$$


::: pf-proof

For positive integers $m,n$,
$$
\operatorname{lcm}(m,n)\gcd(m,n)=mn.
$$
Using step [](#s1-1){.pf-ref},
$$
L
=\frac{1001\cdot10101}{91}
=11\cdot10101
=111111.
$$

:::

:::

::: {.pf-step #s1-3}

The sum of the digits of $L$ is
$$
\boxed{6},
$$
so the answer is (A).


::: pf-proof

By step [](#s1-2){.pf-ref}, $L$ has six digits, each equal to $1$. Their sum is therefore $1+1+1+1+1+1=6$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested digit sum.

:::

:::

:::
