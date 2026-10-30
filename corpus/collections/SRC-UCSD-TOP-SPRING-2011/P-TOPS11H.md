---
schema: qual/card@1
id: P-TOPS11H
kind: problem
title: 'No odd-degree map $S^2\times S^2\to\CP^2$'
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Cup Product
  - Degree
  - Manifolds
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: source-checked
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
(1) What are the integer cohomology rings of $S^2 \times S^2$ and $\CP^2$?
(2) Show that there is no continuous map $f: S^2 \times S^2 \to \CP^2$ having **odd degree**.
:::

::: {.solution}

::: pf

::: pf-step
Let $u,v\in H^2(S^2\times S^2;\ZZ)$ be the pullbacks of the positive generator of $H^2(S^2;\ZZ)$ under the two projections. Then
$$
H^*(S^2\times S^2;\ZZ)
\cong \ZZ[u,v]/(u^2,v^2),
\qquad \gradeddegree{u}=\gradeddegree{v}=2,
$$
and $uv$ generates $H^4(S^2\times S^2;\ZZ)$ after choosing the product orientation.

:::

::: pf-step
If $x\in H^2(\CP^2;\ZZ)$ is the standard generator, then
$$
H^*(\CP^2;\ZZ)
\cong \ZZ[x]/(x^3),
\qquad \gradeddegree{x}=2,
$$
with $x^2$ generating $H^4(\CP^2;\ZZ)$ after choosing the usual orientation.

:::

::: pf-step
Let $f:S^2\times S^2\to\CP^2$ be continuous.

::: pf-proof

::: pf-step
Since $H^2(S^2\times S^2;\ZZ)=\ZZ u\oplus\ZZ v$, write
$$
f^*(x)=au+bv
$$
for integers $a,b$.
:::

::: pf-step
Naturality of cup products gives
$$
f^*(x^2)=(au+bv)^2
=a^2u^2+2ab\,uv+b^2v^2
=2ab\,uv.
$$
:::

::: pf-step
By the definition of degree,
$$
f^*(x^2)=\deg(f)\,uv.
$$
Thus $\deg(f)=2ab$, which is even.
:::

:::

:::

::: pf-step
Therefore no map $S^2\times S^2\to\CP^2$ has odd degree.

:::

:::

:::
