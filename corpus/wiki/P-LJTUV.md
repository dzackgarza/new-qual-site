---
schema: qual/card@1
id: P-LJTUV
kind: problem
title: "Since $T^n = \\prod_nS^1$, we have $\\pi_1(T^n) = \\prod_n \\pi_1(S^1) = \\ZZ^n$."
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
---

5. Since $T^n = \prod_nS^1$, we have $\pi_1(T^n) = \prod_n \pi_1(S^1) = \ZZ^n$.
   We can also construct a cover $p:\RR^n \into T^n$ by just taking $\RR \surjects S^1$ the usual cover in each coordinate, yielding the covering space $\tilde X = \RR^n$ over $X = T^n$.

By Hatcher (prop 4.1), the induced maps $p_*^i: \pi_i(\tilde X) \into \pi_i(X)$ is an isomorphism for $i \geq 2$.
But $\pi_i(\RR^n) = 0$ for $i \neq 0$, so by this isomorphism $\pi_i(T^n) = i \geq 2$.
