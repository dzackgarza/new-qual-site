---
schema: qual/card@1
id: E-SS4.PR-1
kind: exercise
title: "Suppose  as  , for some"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
solved: false
---

::: exercise
1. Suppose ${ \hat { f } } ( \xi ) = O ( e ^ { - a | \xi | ^ { p } } )$ as $| \xi | \to \infty$ , for some $p > 1$ . Then f is holomorphic for all z and satisfies the growth condition

$$

| f (z) | \leq A e ^ {a | z | ^ {q}}
$$

where $1 / p + 1 / q = 1$

Note that on the one hand, when $p \longrightarrow \infty$ then $q \to 1$ , and this limiting case can be interpreted as part of Theorem 3.3. On the other hand, when $p \to 1$ then $q \to \infty$ , and this limiting case in a sense brings us back to Theorem 2.1.

[Hint: To prove the result, use the inequality $- \xi ^ { p } + \xi u \le u ^ { q }$ , which is valid when ξ and u are non-negative. To establish this inequality, examine separately the cases $\xi ^ { p } \ge \xi u$ and $\xi ^ { p } < \xi u ;$ note also that the functions $\xi = u ^ { q - 1 }$ and $u = \xi ^ { p - 1 }$ are inverses of each other because $( p - 1 ) ( q - 1 ) = 1 . ]$
:::
