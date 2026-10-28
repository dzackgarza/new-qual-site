---
schema: qual/card@1
id: P-GRECH6-09
kind: problem
title: Number of subgroups of $\ZZ_3\oplus\ZZ_{16}$
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
  note: "Re-transcribed from Chapter 6 review Question 9 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), compared with assets/attachments/extracted/chapter-6.md, replacing the earlier paraphrased transcription."
---

::: {.problem}
How many subgroups does the group $\ZZ_3 \oplus \ZZ_{16}$ have?

(A) $6$
(B) $10$
(C) $12$
(D) $20$
(E) $24$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The group $\ZZ_3\oplus\ZZ_{16}$ is cyclic of order $48$.


::: pf-proof

The element $(\overline1,\overline1)$ has order
$$
\operatorname{lcm}(3,16)=48
$$
because $\gcd(3,16)=1$. The direct sum also has $3\cdot16=48$ elements, so this element generates the whole group. Hence
$$
\ZZ_3\oplus\ZZ_{16}\cong\ZZ_{48}.
$$

:::

:::

::: {.pf-step #s1-2}

A cyclic group of order $48$ has exactly one subgroup for each positive divisor of $48$.


::: pf-proof

If $G=\langle g\rangle$ has order $48$ and $d\mid48$, then $\langle g^{48/d}\rangle$ is the unique subgroup of order $d$. Conversely, the order of every subgroup divides $48$ by Lagrange's theorem.

:::

:::

::: {.pf-step #s1-3}

The integer $48=2^4\cdot3$ has
$$
(4+1)(1+1)=10
$$
positive divisors.


::: pf-proof

Every positive divisor has the unique form $2^a3^b$ with $0\le a\le4$ and $0\le b\le1$, giving $5\cdot2=10$ choices.

:::

:::

::: {.pf-step #s1-4}

Therefore $\ZZ_3\oplus\ZZ_{16}$ has
$$
\boxed{10}
$$
subgroups, so the answer is (B).


::: pf-proof

By step [](#s1-1){.pf-ref} the group is cyclic of order $48$; steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref} show that such a group has exactly ten subgroups.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the requested number of subgroups.

:::

:::

:::
