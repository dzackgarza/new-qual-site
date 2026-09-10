---
schema: qual/card@1
id: P-CASP04D
kind: problem
title: "Basin of attraction of a fixed point with contraction coefficient"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Let $G$ be an open connected and bounded subset of $\mathbb{C}$, and $f: G \to \mathbb{C}$ an analytic function with $f(G) \subset G$.
Let $f^n$ denote the $n$th iterate of $f$.
Suppose that $a \in G$ is a fixed point of $f$ (i.e.\ $f(a) = a$) and $|f'(a)| < 1$.
Define the basin of attraction of $z = a$ to be the set $$\Omega := \{z \in G : \lim_{n \to \infty} f^n(z) = a\}.$$

(a) Show that there is a $\delta > 0$ such that $\{z : |z - a| < \delta\} \subset \Omega$.

(b) Show, using part (a), that in fact $\Omega = G$.
:::

::: solution
(a) Choose $q$ with $|f'(a)|<q<1$. By continuity of
\[
\frac{f(z)-f(a)}{z-a}
\]
at $a$, there is $\delta>0$ such that
\[
|f(z)-a|\le q|z-a|
\]
whenever $|z-a|<\delta$, with the disk contained in $G$. Therefore
\[
|f^n(z)-a|\le q^n|z-a|\to0
\]
for every point of that disk. Hence $B(a,\delta)\subset\Omega$.

(b) Since $G$ is bounded, the family of iterates $\{f^n\}$ is locally
bounded and hence normal by Montel's theorem. Let $(f^{n_j})$ be any
subsequence. It has a further subsequence converging locally uniformly to a
holomorphic function $F:G\to\overline G$. On the disk from part (a), however,
the whole sequence $f^n$ converges to $a$, so $F\equiv a$ there. The identity
theorem gives $F\equiv a$ on all of $G$.

Thus every convergent subsequence of the normal family has the same limit
$a$. Consequently the entire sequence $f^n$ converges locally uniformly to
$a$ on $G$. In particular $f^n(z)\to a$ for every $z\in G$, so
\[
\boxed{\Omega=G}.
\]
:::
