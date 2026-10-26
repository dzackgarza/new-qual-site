---
schema: qual/card@1
id: P-GRECH7-23
kind: problem
title: Cardinality of power sets of products of finite sets
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 23 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
Given set $A = \{a, b\}$, set $B = \{c, d, e, f\}$, and set $C = \{g, h, i\}$. If set $D = P(C) \times B$, which of the following sets has the same cardinality as $P(D)$?

(A) $P[P(A) \times P(C)]$
(B) $P[A \times C]$
(C) $P(A) \times P(C)$
(D) $[P(B) \times P(C)]$
(E) $P[P(A) \times P(B)]$
:::

::: pf

::: pf-step

The set $D=P(C)\times B$ has cardinality
$$
|D|=32.
$$


::: pf-proof

Since $|C|=3$, its power set has
$$
|P(C)|=2^3=8
$$
elements. Since $|B|=4$,
$$
|D|=|P(C)|\,|B|=8\cdot4=32.
$$

:::

:::

::: pf-step

Therefore
$$
|P(D)|=2^{32}.
$$


::: pf-proof

The power set of a finite set with $n$ elements has $2^n$ elements. Apply this with $n=32$ from step <1>1.

:::

:::

::: pf-step

Choice (A) also has cardinality $2^{32}$.


::: pf-proof

Because $|A|=2$ and $|C|=3$,
$$
|P(A)|=4,
\qquad
|P(C)|=8.
$$
Hence
$$
|P(A)\times P(C)|=4\cdot8=32,
$$
and therefore
$$
\bigl|P[P(A)\times P(C)]\bigr|=2^{32}.
$$

:::

:::

::: pf-step

None of choices (B)--(E) has cardinality $2^{32}$.


::: pf-proof

Their cardinalities are respectively
$$
2^{|A\times C|}=2^6,
$$
$$
|P(A)\times P(C)|=32,
$$
$$
|P(B)\times P(C)|=16\cdot8=128,
$$
and
$$
2^{|P(A)\times P(B)|}=2^{4\cdot16}=2^{64}.
$$

:::

:::

::: pf-step

Hence the required set is
$$
\boxed{P[P(A)\times P(C)]},
$$
so the answer is (A).


::: pf-proof

Steps <1>2 and <1>3 show that choice (A) has the same cardinality as $P(D)$, while step <1>4 rules out the remaining choices.

:::

:::

::: pf-qed

Step <1>5 gives the required choice.

:::

:::
