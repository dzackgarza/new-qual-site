---
schema: qual/card@1
id: P-7ALW6
kind: problem
title: Galois group of $\QQ(\sqrt{2},\sqrt{3})/\QQ$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
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

::: {.problem}
What is the Galois group of $\QQ(\sqrt{2}, \sqrt{3}) / \QQ$?
:::

::: {.solution}
Let
$$
K=\QQ(\sqrt2,\sqrt3).
$$
Since $\sqrt3\notin\QQ(\sqrt2)$,
$$
[K:\QQ]=4.
$$
Moreover, $K$ is the splitting field of
$$
(x^2-2)(x^2-3),
$$
so $K/\QQ$ is Galois.

Every $\QQ$-automorphism independently chooses the signs of $\sqrt2$ and $\sqrt3$:
$$
\sqrt2\mapsto\pm\sqrt2,
\qquad
\sqrt3\mapsto\pm\sqrt3.
$$
All four sign choices occur, giving four automorphisms. The three nonidentity ones all have order $2$. Therefore
$$
\boxed{\Gal(K/\QQ)\cong C_2\times C_2.}
$$
:::
