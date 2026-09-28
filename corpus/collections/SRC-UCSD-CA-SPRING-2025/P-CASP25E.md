---
schema: qual/card@1
id: P-CASP25E
kind: problem
title: "Bounded holomorphic sequence converging on a convergent sequence converges uniformly on compact subsets"
classification:
  areas:
  - complex-analysis
  topics:
  - Normal Families
  - Uniform Convergence
  - Holomorphic Functions
relations: []
review: draft
---

::: {.problem}
Let $f_n : \mathbb{D} \to \mathbb{C}$ be a bounded sequence of holomorphic functions, and let $\{z_m\}_{m \geq 1}$ be a sequence in $\mathbb{D}$ that converges in $\mathbb{D}$.
Assume that $\lim_{n \to \infty} f_n(z_m)$ exists for all $m \geq 1$.
Show that the sequence $\{f_n\}$ converges uniformly on compact subsets of $\mathbb{D}$.
:::

::: {.solution}
The statement is false as printed because the sequence $(z_m)$ need not contain
distinct points. Take $z_m=0$ for every $m$ and
\[
f_n(z)=(-1)^n z.
\]
Then the family is uniformly bounded on $\DD$ and $f_n(z_m)=0$ for every
$m,n$, but $(f_n)$ does not converge locally uniformly.

The standard corrected form assumes that the set $\{z_m:m\ge1\}$ has an
accumulation point in $\DD$; in particular it suffices that the $z_m$ are
distinct and converge in $\DD$. Under that hypothesis the conclusion follows
from Montel's theorem and the identity theorem.

Indeed, uniform boundedness makes $(f_n)$ a normal family. Any subsequence has
a further subsequence converging locally uniformly to some holomorphic $g$.
For every fixed $m$, the scalar sequence $f_n(z_m)$ has a unique limit, hence
every such subsequential limit satisfies
\[
g(z_m)=\lim_{n\to\infty}f_n(z_m).
\]
Therefore any two subsequential limits agree on the set $\{z_m\}$, which has
an interior accumulation point, and so agree identically by the identity
theorem. Thus the normal family has a unique cluster point. If the original
sequence failed to converge locally uniformly to it, some subsequence would
stay a fixed positive distance away on a compact set, but Montel would give a
further subsequence converging to that same cluster point, a contradiction.
:::
