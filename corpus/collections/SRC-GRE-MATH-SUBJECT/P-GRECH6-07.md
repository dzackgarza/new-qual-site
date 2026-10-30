---
schema: qual/card@1
id: P-GRECH6-07
kind: problem
title: Which direct product is cyclic
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
  note: "Re-transcribed from Chapter 6 review Question 7 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), compared with assets/attachments/chapter-6_extracted.md, replacing the earlier paraphrased transcription."
---

::: {.problem}
Which one of the following groups is cyclic?

(A) $\ZZ_2 \times \ZZ_4$
(B) $\ZZ_2 \times \ZZ_6$
(C) $\ZZ_3 \times \ZZ_4$
(D) $\ZZ_3 \times \ZZ_6$
(E) $\ZZ_4 \times \ZZ_6$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The direct product $\ZZ_m\times\ZZ_n$ is cyclic exactly when $\gcd(m,n)=1$.


::: pf-proof

The order of an element $(\overline a,\overline b)$ is
$$
\operatorname{lcm}\bigl(\operatorname{ord}(\overline a),\operatorname{ord}(\overline b)\bigr),
$$
which divides $\operatorname{lcm}(m,n)$. If $\gcd(m,n)>1$, then $\operatorname{lcm}(m,n)<mn=\cardinality{\ZZ_m\times\ZZ_n}$, so no element can generate the product. If $\gcd(m,n)=1$, then $(\overline1,\overline1)$ has order $\operatorname{lcm}(m,n)=mn$, so it generates the product.

:::

:::

::: {.pf-step #s1-2}

Among the five pairs of moduli, only $3$ and $4$ are relatively prime.


::: pf-proof

The greatest common divisors for the choices are
$$
\gcd(2,4)=2,\quad
\gcd(2,6)=2,\quad
\gcd(3,4)=1,\quad
\gcd(3,6)=3,\quad
\gcd(4,6)=2.
$$

:::

:::

::: {.pf-step #s1-3}

Hence the cyclic group is
$$
\boxed{\ZZ_3\times\ZZ_4},
$$
so the answer is (C).


::: pf-proof

Combine steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} identifies the unique cyclic choice.

:::

:::

:::
