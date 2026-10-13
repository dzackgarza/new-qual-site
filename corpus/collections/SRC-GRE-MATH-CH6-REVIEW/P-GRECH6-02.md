---
schema: qual/card@1
id: P-GRECH6-02
kind: problem
title: Digit sum of an LCM
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
  note: "Re-transcribed from Chapter 6 review Question 2 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), compared with assets/attachments/extracted/chapter-6.md, replacing the earlier paraphrased transcription."
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
<1>1. The greatest common divisor of $1001$ and $10101$ is $91$.

::: {.proof}
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

<1>2. Their least common multiple is
$$
L=111111.
$$

::: {.proof}
For positive integers $m,n$,
$$
\operatorname{lcm}(m,n)\gcd(m,n)=mn.
$$
Using step <1>1,
$$
L
=\frac{1001\cdot10101}{91}
=11\cdot10101
=111111.
$$
:::

<1>3. The sum of the digits of $L$ is
$$
\boxed{6},
$$
so the answer is (A).

::: {.proof}
By step <1>2, $L$ has six digits, each equal to $1$. Their sum is therefore $1+1+1+1+1+1=6$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the requested digit sum.
:::
:::
