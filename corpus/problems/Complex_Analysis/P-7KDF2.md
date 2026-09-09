---
schema: qual/card@1
id: P-7KDF2
kind: problem
title: The parallelogram identity for complex numbers and its geometric meaning
classification:
  areas:
  - complex-analysis
  topics:
  - Geometry
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Prove that $|z_1 + z_2|^2 + |z_1 - z_2|^2 = 2(|z_1|^2 + |z_2|^2)$ for any two complex numbers $z_1, z_2 \in \mathbb{C}$, and explain the geometric meaning of this identity.
:::

::: solution
Using $|w|^2=w\overline w$,
\[
|z_1+z_2|^2
=(z_1+z_2)(\overline z_1+\overline z_2)
=|z_1|^2+|z_2|^2+z_1\overline z_2+z_2\overline z_1,
\]
while
\[
|z_1-z_2|^2
=|z_1|^2+|z_2|^2-z_1\overline z_2-z_2\overline z_1.
\]
Adding gives
\[
|z_1+z_2|^2+|z_1-z_2|^2
=2(|z_1|^2+|z_2|^2).
\]

Geometrically, $0,z_1,z_1+z_2,z_2$ are the vertices of the parallelogram spanned by $z_1,z_2$. Its diagonal lengths are $|z_1+z_2|$ and $|z_1-z_2|$, while its four side lengths are $|z_1|,|z_2|,|z_1|,|z_2|$. Thus the identity says that the sum of the squares of the diagonal lengths equals the sum of the squares of the four side lengths.
:::
