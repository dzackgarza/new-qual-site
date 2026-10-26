---
schema: qual/card@1
id: P-GRECH6-06
kind: problem
title: Number of generators of $\ZZ_{24}$
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
  note: "Re-transcribed from Chapter 6 review Question 6 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), compared with assets/attachments/extracted/chapter-6.md, replacing the earlier paraphrased transcription."
---

::: {.problem}
How many generators does the group $(\ZZ_{24}, +)$ have?

(A) $2$
(B) $6$
(C) $8$
(D) $10$
(E) $12$
:::

::: pf

::: pf-step

An element $\overline{k}\in\ZZ_{24}$ generates $(\ZZ_{24},+)$ exactly when $\gcd(k,24)=1$.


::: pf-proof

The order of $\overline{k}$ in the additive group $\ZZ_{24}$ is
$$
\frac{24}{\gcd(k,24)}.
$$
Thus $\overline{k}$ has order $24$, and hence generates the group, exactly when $\gcd(k,24)=1$.

:::

:::

::: pf-step

The residue classes relatively prime to $24$ are represented by
$$
1,5,7,11,13,17,19,23.
$$


::: pf-proof

Since $24=2^3\cdot3$, an integer is relatively prime to $24$ exactly when it is divisible by neither $2$ nor $3$. Inspecting the integers from $1$ through $23$ gives precisely the eight listed representatives.

:::

:::

::: pf-step

Therefore $(\ZZ_{24},+)$ has
$$
\boxed{8}
$$
generators, so the answer is (C).


::: pf-proof

By step <1>1, the generators are exactly the residue classes described in step <1>2, of which there are eight.

:::

:::

::: pf-qed

Step <1>3 gives the requested number of generators.

:::

:::
