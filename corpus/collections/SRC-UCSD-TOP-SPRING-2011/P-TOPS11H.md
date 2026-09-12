---
schema: qual/card@1
id: P-TOPS11H
kind: problem
title: "No odd-degree map from S^2 x S^2 to CP^2"
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

::: problem
(1) What are the integer cohomology rings of $S^2 \times S^2$ and $\mathbb{CP}^2$?
(2) Show that there is no continuous map $f: S^2 \times S^2 \to \mathbb{CP}^2$ having **odd degree**.
:::

::: solution
<1>1. Let $u,v\in H^2(S^2\times S^2;\mathbb Z)$ be the pullbacks of the positive generator of $H^2(S^2;\mathbb Z)$ under the two projections. Then
$$
H^*(S^2\times S^2;\mathbb Z)
\cong \mathbb Z[u,v]/(u^2,v^2),
\qquad |u|=|v|=2,
$$
and $uv$ generates $H^4(S^2\times S^2;\mathbb Z)$ after choosing the product orientation.

<1>2. If $x\in H^2(\mathbb{CP}^2;\mathbb Z)$ is the standard generator, then
$$
H^*(\mathbb{CP}^2;\mathbb Z)
\cong \mathbb Z[x]/(x^3),
\qquad |x|=2,
$$
with $x^2$ generating $H^4(\mathbb{CP}^2;\mathbb Z)$ after choosing the usual orientation.

<1>3. Let $f:S^2\times S^2\to\mathbb{CP}^2$ be continuous.
<2>1. Since $H^2(S^2\times S^2;\mathbb Z)=\mathbb Zu\oplus\mathbb Zv$, write
$$
f^*(x)=au+bv
$$
for integers $a,b$.
<2>2. Naturality of cup products gives
$$
f^*(x^2)=(au+bv)^2
=a^2u^2+2ab\,uv+b^2v^2
=2ab\,uv.
$$
<2>3. By the definition of degree,
$$
f^*(x^2)=\deg(f)\,uv.
$$
Thus $\deg(f)=2ab$, which is even.

<1>4. Therefore no map $S^2\times S^2\to\mathbb{CP}^2$ has odd degree.
:::
