---
schema: qual/card@1
id: T-NOETHD
kind: theorem
title: Noether's bound on the degrees of generators of an invariant ring
slogan: 'invariants of degree at most $\size G$ generate when $\size G$ is invertible in $k$'
classification:
  areas:
  - algebra
  topics:
  - Invariant Theory
  - Degree Bounds
relations: []
review: draft
---

::: {.theorem}
Let $G$ be a finite group acting linearly on a finite-dimensional vector space $V$ over a field $k$ whose characteristic does not divide $\size G$.
Then the invariant ring $k[V]^G$ is generated as a $k$-algebra by its elements of degree at most $\size G$.

This is Noether's bound in the non-modular case, due to Fleischmann, *The Noether bound in invariant theory of finite groups*, Advances in Mathematics 156 (2000), 23--32, and Fogarty, *On Noether's bound for polynomial invariants of a finite group*, Electronic Research Announcements of the American Mathematical Society 7 (2001), 5--7.
The numbered statement used here is Knop, *On Noether's and Weyl's bound in positive characteristic* (arXiv:math/0207194), Corollary 3.4: if $A$ is an $\NN$-graded algebra with $\beta(A)\leq1$ and $\size G$ is invertible in $A$, then $\beta(A^G)\leq\size G$, where $\beta(A)$ is the least $n$ such that $A$ is generated as a ring by its elements of degree at most $n$; Knop records there that the trivial subgroup gives the theorem of Fleischmann and Fogarty.

Cox--Little--O'Shea, *Ideals, Varieties, and Algorithms*, Chapter 7, §3, Theorem 5 proves the characteristic-zero case, and its printed proof does not extend to prime characteristic: the last step divides by $b_\alpha=\size G\,a_\alpha$, where $a_\alpha$ is the multinomial coefficient in $(x_1+\cdots+x_n)^k=\sum_{\abs\alpha=k}a_\alpha x^\alpha$ (Exercise 4 of that section). With $\size G=2$, $\operatorname{char}k=3$ and $\alpha=(2,1)$ one has $a_\alpha=3=0$ in $k$, hence $b_\alpha=0$ although $\size G=2$ is invertible, and the argument gives no expression for $R_G(x^2y)$. So the invertibility of $\size G!$ alone is not what that proof uses.
:::
