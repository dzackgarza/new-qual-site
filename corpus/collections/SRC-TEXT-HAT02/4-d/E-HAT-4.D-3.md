---
schema: qual/card@1
id: E-HAT-4.D-3
kind: problem
title: Cohomology of Stiefel manifolds via Leray--Hirsch
classification:
  areas:
  - topology
  topics:
  - Fiber Bundles
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
Use the Leray–Hirsch theorem as in Corollary 4D.3 to compute $H^*(V_n(\CC^k); \ZZ) \approx \Lambda_\ZZ[x_{2k-2n+1}, x_{2k-2n+3}, \ldots, x_{2k-1}]$ and similarly in the quaternionic case.
:::

::: {.solution}
The projection $V_n(\CC^k)\to V_{n-1}(\CC^k)$ forgets the last frame vector. Its fiber is the unit sphere of the complex orthogonal-complement bundle $E$ of rank $k-n+1$, hence is $S^{2k-2n+1}$. The first $n-1$ frame vectors trivialize the complementary summand of $E$, so
$$
E\oplus\underline{\CC}^{,n-1}\cong\underline{\CC}^{,k}.
$$
Thus all Chern classes of $E$ vanish, including its Euler class $c_{k-n+1}(E)$. In the Gysin sequence of its oriented sphere bundle, vanishing of the Euler class says that a class
$$
x_{2k-2n+1}\in H^{2k-2n+1}(V_n(\CC^k);\ZZ)
$$
restricts to the generator on every fiber. Leray--Hirsch then makes $H^*(V_n(\CC^k);\ZZ)$ a free module over $H^*(V_{n-1}(\CC^k);\ZZ)$ with basis $1,x_{2k-2n+1}$.

Start with $V_1(\CC^k)=S^{2k-1}$ and repeat. The resulting cohomology is torsionfree, and each new generator has odd degree. Graded commutativity makes twice its square zero, so its square is zero. Leray--Hirsch gives the products of distinct generators as an additive basis. Therefore
$$
H^*(V_n(\CC^k);\ZZ)\cong
\Lambda_\ZZ[x_{2k-2n+1},x_{2k-2n+3},\ldots,x_{2k-1}].
$$

For quaternionic frames the complement is a quaternionic bundle of rank $k-n+1$, stably trivial by the same frame decomposition. Its integral Euler class is its top Chern class and vanishes. The sphere fiber has dimension $4k-4n+3$. The same Gysin and Leray--Hirsch argument yields
$$
H^*(V_n(\quaternions^k);\ZZ)\cong
\Lambda_\ZZ[x_{4k-4n+3},x_{4k-4n+7},\ldots,x_{4k-1}].
$$
:::
