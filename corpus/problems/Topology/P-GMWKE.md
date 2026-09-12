---
schema: qual/card@1
id: P-GMWKE
kind: problem
title: Cohomology of $S^2 \vee S^2 \vee S^4$
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Homology
  - Cell Complexes
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
Compute the cohomology groups and cohomology ring $H^*(S^2 \vee S^2 \vee S^4; \mathbb{Z})$ of the wedge sum $X = S^2 \vee S^2 \vee S^4$.
:::

::: solution
Let
$$
X=S^2_a\vee S^2_b\vee S^4.
$$

<1>1. The reduced cohomology of a finite wedge is the direct sum of the reduced cohomologies of the summands. Hence
$$
H^k(X;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&k=0,4,\\
\mathbb Z^2,&k=2,\\
0,&\text{otherwise}.
\end{cases}
$$

<1>2. Let $\alpha,\beta\in H^2(X;\mathbb Z)$ be the classes coming from the two $2$-sphere summands, and let $\gamma\in H^4(X;\mathbb Z)$ be the class coming from the $4$-sphere summand.

<1>3. Every product of two positive-degree classes is zero.
::: proof
For each wedge summand, the square of its positive-degree generator vanishes for dimensional reasons. Products of classes supported on distinct wedge summands vanish because the reduced diagonal of a wedge has no mixed component between distinct summands. Thus
$$
\alpha^2=\beta^2=\alpha\beta=0,
$$
and every product involving $\gamma$ also vanishes by degree.
:::

<1>4. Therefore, as a graded ring,
$$
H^*(X;\mathbb Z)
\cong
\mathbb Z[\alpha,\beta,\gamma]/
(\alpha^2,\beta^2,\alpha\beta,\alpha\gamma,\beta\gamma,\gamma^2),
$$
with $|\alpha|=|\beta|=2$ and $|\gamma|=4$.
:::
