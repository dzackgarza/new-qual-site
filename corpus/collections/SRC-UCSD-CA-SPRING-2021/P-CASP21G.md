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

::: {.problem}
Let $\{f_n\}$ be a sequence of automorphisms of the unit disc $\DD$, converging locally uniformly in $\DD$ to a nonconstant function $f$.
Show that $f$ is an automorphism of $\DD$.

Hint: Examine the family $\mathcal{F}$ consisting of the inverse automorphisms $f_n^{-1} : \DD \to \DD$.
:::

::: {.solution}
Set $g_n=f_n^{-1}$. Since the family of holomorphic self-maps of $\DD$
is normal, some subsequence $g_{n_k}$ converges locally uniformly to a
holomorphic map $g:\DD\to\overline{\DD}$.

Because $f$ is nonconstant and $f_{n_k}\to f$ locally uniformly, Hurwitz's
theorem implies that $f$ is injective. In particular $f(\DD)$ is open.
Fix $z\in\DD$. For $k$ large, $f_{n_k}(z)$ stays in a compact subset of
$\DD$ around $f(z)$. Hence local uniform convergence of $g_{n_k}$ gives
$$
g(f(z))
=\lim_{k\to\infty}g_{n_k}(f_{n_k}(z))
=z.
$$
Thus $g\circ f=\operatorname{id}_{\DD}$.

Similarly, for any $w\in\DD$ choose a compact disk containing $w$ and
use $f_{n_k}\circ g_{n_k}=\operatorname{id}$. The identity above already
shows that $g$ is nonconstant, hence $g(\DD)\subset\DD$ by the
maximum principle. Passing to the limit gives
$$
f(g(w))=w.
$$
Therefore $f$ and $g$ are inverse biholomorphisms of $\DD$, so $f$ is an
automorphism.
:::
