---
schema: qual/card@1
id: P-CASP18F
kind: problem
title: "Pointwise convergence with bounded derivatives implies uniform convergence on compact subsets"
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

::: problem
Let $\{f_n\}$ be a sequence in $H(G)$ such that $f_n(z)$ converges for every $z \in G$ to a complex value $f(z)$, i.e. $\lim_{n \to \infty} f_n(z) = f(z) \in \mathbb{C}$.
Assume that $|f_n'(z)| \leq h(z)$ for some continuous real-valued function $h$ in $G$.
Show that $f(z)$ is analytic in $G$ and $f_n \to f$ in $H(G)$.
:::

::: solution
Fix a compact set $K\Subset G$. Choose finitely many closed disks
$\overline{D_j}\Subset G$ whose interiors cover $K$. Since $h$ is continuous,
it is bounded on each $\overline{D_j}$, say by $M_j$. Therefore, for
$z,w\in D_j$ with the segment $[z,w]\subset D_j$,
\[
|f_n(z)-f_n(w)|
\le M_j|z-w|.
\]
Thus $(f_n)$ is equicontinuous on each $D_j$, hence on $K$ after shrinking
the cover slightly. Pointwise convergence to $f$ then implies that $f$ is
continuous.

Suppose convergence were not uniform on $K$. Then some subsequence
$f_{n_k}$ and points $z_k\in K$ would satisfy
\[
|f_{n_k}(z_k)-f(z_k)|\ge\varepsilon>0.
\]
After passing to a subsequence, $z_k\to z\in K$. Equicontinuity of the
$f_n$ and continuity of $f$ give
\[
|f_{n_k}(z_k)-f(z_k)|
\le |f_{n_k}(z_k)-f_{n_k}(z)|
+|f_{n_k}(z)-f(z)|+|f(z)-f(z_k)|\to0,
\]
a contradiction. Hence $f_n\to f$ uniformly on every compact subset of $G$.

By the Weierstrass theorem on locally uniform limits of holomorphic functions,
$f$ is holomorphic. Therefore
\[
f_n\to f\quad\text{in }H(G).
\]
:::
