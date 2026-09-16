---
schema: qual/card@1
id: P-AGH359NONPROJ
kind: problem
title: A nonprojective infinitesimal extension of the projective plane
classification:
  areas:
  - algebraic-geometry
  topics:
  - Projectivity
  - Infinitesimal Extensions
  - Picard Group
  - Counterexamples
relations: []
review: draft
---

::: problem
We show the result of (Ex.
5.8) is false in dimension 2. Let $k$ be an algebraically closed field of characteristic 0, and let $X=\PP_k^2$.
Let $\omega$ be the sheaf of differential 2-forms (II, §8). Define an infinitesimal extension $X'$ of $X$ by $\omega$ by giving the element $\xi \in H^1(X, \omega \tensor \mct)$ defined as follows (Ex.
4.10).

Let $x_0, x_1, x_2$ be the homogeneous coordinates of $X$, let $U_0, U_1, U_2$ be the standard open covering, and let $\xi_{ij}=(x_j/x_i)\, d(x_i/x_j)$.
This gives a Čech 1-cocycle with values in $\Omega_X^1$, and since $\dim X=2$, we have $\omega \tensor \mct \cong \Omega^1$ (II, Ex.
5.16b). Now use the exact sequence
\[
\cdots \to H^1(X, \omega) \to \Pic X' \to \Pic X \mapsvia{\delta} H^2(X, \omega) \to \cdots
\]
of (Ex.
4.6) and show $\delta$ is injective.
We have $\omega \cong \mco_X(-3)$ by (II, 8.20.1), so $H^2(X, \omega) \cong k$.
Since $\characteristic k=0$, you need only show that $\delta(\mco(1)) \neq 0$, which can be done by calculating in Čech cohomology.

Since $H^1(X, \omega)=0$, we see that $\Pic X'=0$.
In particular, $X'$ has no ample invertible sheaves, so it is not projective.
:::

::: {.remark}
This result generalizes: for any nonsingular projective surface $X$ over an algebraically closed field $k$ of characteristic $0$, there is an infinitesimal extension $X'$ of $X$ by $\omega$ such that $X'$ is not projective over $k$.
Let $D$ be an ample divisor on $X$. Then $D$ determines an element $c_1(D) \in H^1(X, \Omega^1)$, which defines $X'$ as above.
For any divisor $E$ on $X$ one can show that $\delta(\mcl(E))=(D.E)$, where $(D.E)$ is the intersection number (Chapter V), considered as an element of $k$.
Hence if $E$ is ample, $\delta(\mcl(E)) \neq 0$, so $X'$ has no ample divisors.
On the other hand, over a field of characteristic $p>0$, a proper scheme $X$ is projective if and only if $X_{\red}$ is.
:::
