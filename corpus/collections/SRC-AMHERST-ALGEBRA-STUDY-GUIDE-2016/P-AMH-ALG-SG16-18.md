---
schema: qual/card@1
id: P-AMH-ALG-SG16-18
kind: problem
title: Amherst algebra study guide problem 18
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
(January 2012) Let R = {[a b 0 c ]⏐⏐⏐a,b,c ∈ R } . You may assume that R is a ring under the operations of matrix addition and matrix multiplication. Prove that the set I = {[ a b 0 0 ]⏐⏐⏐a,b∈ R } is an ideal of R.
:::

::: {.solution}
Proof. (I non-empty)
[
0 0
0 0
]
∈I, so I⁄= ∅.
(I closed under−) Given r =
[a b
0 0
]
and s =
[c d
0 0
]
, r−s =
[a−c b −d
0 0
]
∈I.
(Sticky) Given r =
[a b
0 c
]
∈ R and s =
[x y
0 0
]
, rs =
[ax ay
0 0
]
∈ I and sr =
[ax bx +cy
0 0
]
∈ I.
QED
Here is problem that uses a deﬁnition you are not expected to have seen before.
:::
