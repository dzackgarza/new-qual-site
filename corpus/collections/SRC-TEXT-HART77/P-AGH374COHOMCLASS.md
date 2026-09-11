---
schema: qual/card@1
id: P-AGH374COHOMCLASS
kind: problem
title: The cohomology class of a subvariety
classification:
  areas:
  - algebraic-geometry
  topics:
  - Serre Duality
  - Sheaves of Differentials
  - Intersection Theory
  - Picard Group
relations: []
review: draft
---

::: problem
Let $X$ be a nonsingular projective variety of dimension $n$ over an algebraically closed field $k$. Let $Y$ be a nonsingular subvariety of codimension $p$, hence of dimension $n-p$. From the natural map $\Omega_X \tensor \mco_Y \to \Omega_Y$ of (II, 8.12) we deduce a map $\Omega_X^{n-p} \to \Omega_Y^{n-p}$. This induces a map on cohomology
\[
H^{n-p}(X, \Omega_X^{n-p}) \to H^{n-p}(Y, \Omega_Y^{n-p})
.\]
Now $\Omega_Y^{n-p} = \omega_Y$ is a dualizing sheaf for $Y$, so we have the trace map
\[
t_Y: H^{n-p}(Y, \Omega_Y^{n-p}) \to k
.\]
Composing, we obtain a linear map $H^{n-p}(X, \Omega_X^{n-p}) \to k$. By (7.13) this corresponds to an element $\eta(Y) \in H^p(X, \Omega_X^p)$, which we call the **cohomology class of $Y$**.

a. If $P \in X$ is a closed point, show that $t_X(\eta(P)) = 1$, where $\eta(P) \in H^n(X, \Omega^n)$ and $t_X$ is the trace map.

b. If $X = \PP^n$, identify $H^p(X, \Omega^p)$ with $k$ by (Ex. 7.3), and show that $\eta(Y) = (\deg Y) \cdot 1$, where $\deg Y$ is the degree of $Y$ as a projective variety (I, §7).

   Hint: cut with a hyperplane $H \subseteq X$, and use Bertini's theorem (II, 8.18) to reduce to the case where $Y$ is a finite set of points.

c. For any scheme $X$ of finite type over $k$, we define a homomorphism of sheaves of abelian groups $d\log: \mco_X^* \to \Omega_X$ by $d\log(f) = f^{-1} \, df$. Here $\mco_X^*$ is a group under multiplication, and $\Omega_X$ is a group under addition. This induces a map on cohomology
\[
\Pic X = H^1(X, \mco_X^*) \to H^1(X, \Omega_X)
,\]
which we denote by $c$. See (Ex. 4.5).

d. Returning to the hypotheses above, suppose $p = 1$. Show that $\eta(Y) = c(\mcl(Y))$, where $\mcl(Y)$ is the invertible sheaf corresponding to the divisor $Y$.
:::
