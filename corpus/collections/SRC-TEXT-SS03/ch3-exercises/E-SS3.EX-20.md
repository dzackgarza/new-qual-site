---
schema: qual/card@1
id: E-SS3.EX-20
kind: problem
title: "This exercise shows how the mean square convergence dominates the uniform conver"
classification:
  areas:
  - complex-analysis
  topics: ['Meromorphic Functions', 'Residue Theorem', 'Argument Principle']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: exercise
20. This exercise shows how the mean square convergence dominates the uniform convergence of analytic functions.
    If U is an open subset of C we use the notation

$$
\| f \| _ {L ^ {2} (U)} = \left(\int_ {U} | f (z) | ^ {2} d x d y\right) ^ {1 / 2}
$$

for the mean square norm, and

$$
\| f \| _ {L ^ {\infty} (U)} = \sup _ {z \in U} | f (z) |
$$

for the sup norm.

(a) If f is holomorphic in a neighborhood of the disc $D _ { r } ( z _ { 0 } )$ , show that for any $0 < s < r$ there exists a constant $C > 0$ (which depends on s and $r )$ such that

$$
\| f \| _ {L ^ {\infty} (D _ {s} (z _ {0}))} \leq C \| f \| _ {L ^ {2} (D _ {r} (z _ {0}))}.
$$

(b) Prove that if $\left\{ f _ { n } \right\}$ is a Cauchy sequence of holomorphic functions in the mean square norm $\| \cdot \| _ { L ^ { 2 } ( U ) }$ , then the sequence $\left\{ f _ { n } \right\}$ converges uniformly on every compact subset of $\dot { U }$ to a holomorphic function.

[Hint: Use the mean-value property.]
:::

::: solution
(a) Fix $0<s<r$ and put
\[
\rho=\frac{r-s}{2}>0.
\]
For every $z\in D_s(z_0)$, the closed disc $\overline{D_\rho(z)}$ lies in $D_r(z_0)$. Since $|f|^2$ is subharmonic (equivalently, by the mean-value inequality for holomorphic functions),
\[
|f(z)|^2\le \frac1{\pi\rho^2}\int_{D_\rho(z)}|f(w)|^2\,dA(w)
\le \frac1{\pi\rho^2}\|f\|_{L^2(D_r(z_0))}^2.
\]
Thus
\[
\|f\|_{L^\infty(D_s(z_0))}
\le \frac1{\sqrt\pi\rho}\|f\|_{L^2(D_r(z_0))}.
\]
So one may take $C=(\sqrt\pi\rho)^{-1}$.

(b) Let $K\Subset U$. Choose finitely many discs
\[
K\subset\bigcup_{j=1}^N D_{s_j}(z_j),
\qquad
\overline{D_{r_j}(z_j)}\subset U,
\qquad
0<s_j<r_j.
\]
Applying part (a) to $f_n-f_m$ on each disc gives
\[
\|f_n-f_m\|_{L^\infty(K)}
\le C_K\|f_n-f_m\|_{L^2(U)}
\]
for a constant $C_K$ independent of $m,n$. Since $(f_n)$ is Cauchy in $L^2(U)$, it is uniformly Cauchy on $K$. Hence it converges uniformly on every compact subset of $U$ to a function $f$. By the Weierstrass theorem on locally uniform limits of holomorphic functions, $f$ is holomorphic on $U$.
:::
