---
schema: qual/card@1
id: P-AGH426PUSHFORWARDDIVISORS
kind: problem
title: The pushforward $f_*$ on divisors and the determinant of $f_* \mcl(D)$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Riemann-Hurwitz
  - Canonical Divisor
  - Jacobians
relations: []
review: draft
---

::: {.problem}
Let $f: X \to Y$ be a finite morphism of curves of degree $n$.
We define a homomorphism $f_*: \Div X \to \Div Y$ by $f_*(\sum n_i P_i)=\sum n_i f(P_i)$ for any divisor $D=\sum n_i P_i$ on $X$.

a. For any locally free sheaf $\mce$ on $Y$, of rank $r$, we define $\det \mce=\wedge^r \mce \in \Pic Y$ (II, Ex.
6.11). In particular, for any invertible sheaf $\mcm$ on $X$, $f_* \mcm$ is locally free of rank $n$ on $Y$, so we can consider $\det f_* \mcm \in \Pic Y$.
Show that for any divisor $D$ on $X$,
$$
\det\left(f_* \mcl(D)\right) \cong \det f_*(\OO_X) \tensor \mcl(f_* D).
$$
Note in particular that $\det(f_* \mcl(D)) \neq \mcl(f_* D)$ in general!
Hint: First consider an effective divisor $D$, apply $f_*$ to the exact sequence $0 \to \mcl(-D) \to \OO_X \to \OO_D \to 0$, and use (II, Ex.
6.11).

b. Conclude that $f_* D$ depends only on the linear equivalence class of $D$, so there is an induced homomorphism $f_*: \Pic X \to \Pic Y$.
Show that $f_* f^*: \Pic Y \to \Pic Y$ is just multiplication by $n$.

c. Use duality for a finite flat morphism (III, Ex.
6.10) and (III, Ex.
7.2) to show that $$\det f_* \Omega_X \cong \qty{ \det f_* \OO_X}^{-1} \tensor \Omega_Y^{\tensor n}.$$

d. Now assume that $f$ is separable, so we have the ramification divisor $R$.
We define the **branch divisor** $B$ to be the divisor $f_* R$ on $Y$.
Show that $$\left(\det f_* \OO_X\right)^2 \cong \mcl(-B).$$
:::
