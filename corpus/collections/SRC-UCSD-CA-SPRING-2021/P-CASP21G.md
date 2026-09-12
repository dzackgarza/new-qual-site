---
schema: qual/card@1
id: P-CASP21G
kind: problem
title: "Locally uniform limit of disc automorphisms is an automorphism"
classification:
  areas:
  - complex-analysis
  topics:
  - Automorphisms
  - Normal Families
  - Holomorphic Functions
relations: []
review: draft
---

::: problem
Let $\{f_n\}$ be a sequence of automorphisms of the unit disc $\Delta$, converging locally uniformly in $\Delta$ to a nonconstant function $f$.
Show that $f$ is an automorphism of $\Delta$.

Hint: Examine the family $\mathcal{F}$ consisting of the inverse automorphisms $f_n^{-1} : \Delta \to \Delta$.
:::

::: solution
Set $g_n=f_n^{-1}$. Since the family of holomorphic self-maps of $\mathbb D$
is normal, some subsequence $g_{n_k}$ converges locally uniformly to a
holomorphic map $g:\mathbb D\to\overline{\mathbb D}$.

Because $f$ is nonconstant and $f_{n_k}\to f$ locally uniformly, Hurwitz's
theorem implies that $f$ is injective. In particular $f(\mathbb D)$ is open.
Fix $z\in\mathbb D$. For $k$ large, $f_{n_k}(z)$ stays in a compact subset of
$\mathbb D$ around $f(z)$. Hence local uniform convergence of $g_{n_k}$ gives
\[
g(f(z))
=\lim_{k\to\infty}g_{n_k}(f_{n_k}(z))
=z.
\]
Thus $g\circ f=\operatorname{id}_{\mathbb D}$.

Similarly, for any $w\in\mathbb D$ choose a compact disk containing $w$ and
use $f_{n_k}\circ g_{n_k}=\operatorname{id}$. The identity above already
shows that $g$ is nonconstant, hence $g(\mathbb D)\subset\mathbb D$ by the
maximum principle. Passing to the limit gives
\[
f(g(w))=w.
\]
Therefore $f$ and $g$ are inverse biholomorphisms of $\mathbb D$, so $f$ is an
automorphism.
:::
