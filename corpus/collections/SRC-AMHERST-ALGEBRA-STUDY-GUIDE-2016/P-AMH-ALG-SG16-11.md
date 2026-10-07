---
schema: qual/card@1
id: P-AMH-ALG-SG16-11
kind: problem
title: The order of a homomorphic image of a subgroup divides $|G_1|$
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored Amherst College Study Guide for Algebra (September 2016).
---

::: {.problem}
(February 2013) Let $G_1$ and $G_2$ be groups, let $\varphi:G_1\to G_2$ be a homomorphism, and let $H_1\subseteq G_1$ be a subgroup.
Recall that the set
\[
H_2=\{\varphi(x)\mid x\in H_1\}
\]
is a subgroup of $G_2$, called the image of $H_1$ under $\varphi$, sometimes notated $\varphi(H_1)$.
If $G_1$ is finite, prove that $|H_2|\mid |G_1|$.
That is, prove that the order of $H_2$ divides the order of $G_1$.
:::

::: {.solution}
<1>1. The order of $\varphi(G_1)$ divides $|G_1|$.
::: {.proof}
Let
$$
K=\ker\varphi.
$$
By the first isomorphism theorem,
$$
\varphi(G_1)\cong G_1/K.
$$
Since $G_1$ is finite,
$$
|\varphi(G_1)|
=|G_1/K|
=\frac{|G_1|}{|K|}.
$$
Hence
$$
|\varphi(G_1)|\mid |G_1|.
$$
:::

<1>2. The order of $H_2$ divides $|\varphi(G_1)|$.
::: {.proof}
By definition,
$$
H_2=\varphi(H_1).
$$
Since $H_1\le G_1$,
$$
H_2\le \varphi(G_1).
$$
The group $\varphi(G_1)$ is finite, so Lagrange's theorem gives
$$
|H_2|\mid |\varphi(G_1)|.
$$
:::

<1>3. Therefore
$$
\boxed{|H_2|\mid |G_1|}.
$$
::: {.proof}
By step <1>2,
$$
|H_2|\mid |\varphi(G_1)|,
$$
and by step <1>1,
$$
|\varphi(G_1)|\mid |G_1|.
$$
Divisibility is transitive.
:::

<1>4. Q.E.D.
::: {.proof}
Step <1>3 is the required conclusion.
:::
:::
