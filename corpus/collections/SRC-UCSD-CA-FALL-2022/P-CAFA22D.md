---
schema: qual/card@1
id: P-CAFA22D
kind: problem
title: "Mean value inequality and completeness of A^1(G)"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Let $G \subset \mathbb{C}$ be a bounded region.

(i) Show that if $f \in H(G)$ and $B = B(a,r) \subset G$, then
$$
|f(a)| \leq \frac{1}{|B|} \int_B |f(z)|\,dx\,dy,
$$
where $|B|$ denotes the area of $B$.

(ii) Show that the space
$$
A^1(G) = \{f \in H(G) : \|f\|_1 := \int_G |f(z)|\,dx\,dy < \infty\}
$$
endowed with the metric $d(f,g) = \|f - g\|_1$ is complete.

Note: You may use the result in part (i) even if you did not prove this.
:::

::: solution
For (i), the subharmonic mean-value inequality for $|f|$ gives
\[
|f(a)|\le \frac1{2\pi}\int_0^{2\pi}|f(a+\rho e^{it})|\,dt
\]
for every $0<\rho<r$. Multiply by $2\rho$ and integrate from $0$ to $r$.
Polar coordinates give
\[
r^2|f(a)|\le \frac1\pi\int_{B(a,r)}|f(z)|\,dA(z),
\]
which is the stated inequality because $|B|=\pi r^2$.

For (ii), let $(f_n)$ be Cauchy in $L^1(G)$. Then it converges in
$L^1(G)$ to some $f\in L^1(G)$. Fix a compact $K\Subset G$ and choose
$r>0$ such that $B(z,r)\subset G$ for every $z\in K$. Applying (i) to
$f_n-f_m$ gives
\[
\sup_K|f_n-f_m|\le \frac1{\pi r^2}\|f_n-f_m\|_1.
\]
Thus $(f_n)$ is uniformly Cauchy on every compact subset of $G$, so it
converges locally uniformly to a holomorphic function $g$. A subsequence of
the $L^1$-convergent sequence converges to $f$ almost everywhere, while the
same subsequence converges pointwise to $g$; hence $f=g$ almost everywhere.
Therefore $g\in A^1(G)$ and $\|f_n-g\|_1\to0$. So $A^1(G)$ is complete.
:::
