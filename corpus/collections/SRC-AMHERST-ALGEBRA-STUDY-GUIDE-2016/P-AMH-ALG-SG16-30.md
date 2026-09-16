---
schema: qual/card@1
id: P-AMH-ALG-SG16-30
kind: problem
title: Reducibility of $X^4+X^2+1$ over $\mathbb F_2$ and irreducibility of $X^3+2X^2+2X+3$ over $\mathbb F_5$
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
(January 2009) (a) Prove that $f(X)=X^4+X^2+1$ is reducible in the polynomial ring $\mathbb{F}_2[X]$, where $\mathbb{F}_2=\{0,1\}$ is the field of two elements.
(b) Prove that $g(X)=X^3+2X^2+2X+3$ is irreducible in the polynomial ring $\mathbb{F}_5[X]$, where $\mathbb{F}_5=\{0,1,2,3,4\}$ is the field of five elements.
:::

::: {.solution}
Proof.
(a) To be reducible,f must either have a degree one factor (and hence have a root in F2), orf must be a product of two irreducible factors of degree two.
But f(0) =f(1) = 1 so f has no roots in F2. Hence f is the product of two irreducible quadratic factors.
The possible quadratic polynomials are X 2, X 2 + 1, X 2 +X and X 2 +X + 1. The ﬁrst and third are clearly reducible, and over F2, we have X 2 + 1 = (X + 1)2, so X 2 +X + 1 is the only quadratic irreducible polynomial.
Then an explicit calculation (made easier by using (a +b)2 =a2 +b2 since we are working over F2) shows that f(X) = (X 2 +X + 1)(X 2 +X + 1). QED (b) Since degg = 3, we know that g is reducible if and only if it has no roots.
Checking shows: g(0) = 03 + 2(02) + 2(0) + 3 = 0 + 0 + 0 + 3 = 3⁄= 0 g(1) = 13 + 2(12) + 2(1) + 3 = 1 + 2 + 2 + 3 = 3⁄= 0 g(2) = 23 + 2(22) + 2(2) + 3 = 3 + 3 + 4 + 3 = 3⁄= 0 g(3) = 33 + 2(32) + 2(3) + 3 = 2 + 3 + 1 + 3 = 4⁄= 0 g(4) = 43 + 2(42) + 2(4) + 3 = 4 + 2 + 3 + 3 = 2⁄= 0 Since g(a)⁄= 0 for all a∈ F5, it follows that g is irreducible.
QED
:::
