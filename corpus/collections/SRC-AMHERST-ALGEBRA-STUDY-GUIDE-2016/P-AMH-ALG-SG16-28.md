---
schema: qual/card@1
id: P-AMH-ALG-SG16-28
kind: problem
title: Cubic polynomials over a field are irreducible exactly when rootless
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
(January 1999) Let $k$ be a field. Show that a cubic polynomial $f(x)\in k[x]$ is irreducible in $k[x]$ if and only if $f(x)$ has no roots in $k$.
:::

::: {.solution}
Proof. We’ll prove f reducible iﬀ f has a root in k.
(=⇒): Since f is reducible, there exist g,h∈k[x] with f =gh and with degg, degh< 3. Since deg g
and degh are nonnegative integers summing to deg f = 3, one of g and h must have degree 1 and
the other must have degree 2. Without loss, deg g = 1. That is, g(x) =ax +b for some a,b∈k with
a⁄= 0. Then −b/a∈k, and
f
(
− b
a
)
=g
(
− b
a
)
h
(
− b
a
)
=
[
a
(
− b
a
)
+b
]
h
(
− b
a
)
= (−b +b)h
(
− b
a
)
= 0·
(
− b
a
)
= 0,
and hence−b/a is a root of of f in k.
(⇐=): Let c∈k be a root of f, and let g(x) = x−c∈k[x]. By the division algorithm for f and g,
there exist polynomials q,r ∈k[x] with f =qg +r and with either r = 0 or degr< degg = 1.
If r⁄= 0 but degr< 1, then degr = 0, which means that r =b is a nonzero constant. Hence,
0 =f(c) =q(c)g(c) +r(c) =q(c)· (c−c) +b = 0 +b =b⁄= 0,
a contradiction. Thus, we must in fact have r = 0, and hence f =qg. Since deg f = 3 and degg = 1,
we must have deg q = 3− 1 = 2, and hence we have factored f as a product of two lower-degree
polynomials g and q, proving that f is reducible. QED
:::
