---
schema: qual/card@1
id: P-CAF11C
kind: problem
title: "Schwarz-Pick type inequality for analytic functions mapping into the left half-plane"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Let $f \in H(\mathbb{D})$ be nonconstant such that $f(\mathbb{D}) \subset \{z \in \mathbb{C} : \operatorname{Re} z < 0\}$ and $f(0) = -1$.
Prove that for any $z \in \mathbb{D}$, $$\frac{1 - |z|}{1 + |z|} \leq |f(z)| \leq \frac{1 + |z|}{1 - |z|}.$$
:::

::: solution
The Möbius map
\[
\Phi(w)=\frac{w+1}{w-1}
\]
maps the left half-plane conformally onto $\mathbb D$ and sends $-1$ to $0$.
Thus
\[
g=\Phi\circ f:\mathbb D\to\mathbb D
\]
is holomorphic and satisfies $g(0)=0$. Schwarz's lemma gives
\[
|g(z)|\le |z|.
\]
Solving for $f$ yields
\[
f(z)=\frac{g(z)+1}{g(z)-1}.
\]
Therefore, writing $r=|z|$,
\[
|f(z)|=\frac{|1+g(z)|}{|1-g(z)|}
\le \frac{1+|g(z)|}{1-|g(z)|}
\le \frac{1+r}{1-r}.
\]
Likewise,
\[
|f(z)|
\ge \frac{1-|g(z)|}{1+|g(z)|}
\ge \frac{1-r}{1+r}.
\]
This is the required pair of inequalities.
:::
