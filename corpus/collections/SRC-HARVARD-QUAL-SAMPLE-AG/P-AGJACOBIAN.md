---
schema: qual/card@1
id: P-AGJACOBIAN
kind: problem
title: The Jacobian, the Abel--Jacobi map, and the case of genus $1$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Jacobians
  - Abel-Jacobi Map
  - Elliptic Curves
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the Harvard sample qualifying-exam algebraic-geometry PDF; this is Wodzicki's follow-up on the significance of the Jacobian, the Abel--Jacobi map, and genus one.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
What is the significance of the Jacobian?

What kind of map is the Abel--Jacobi map?

What is it in the case of genus $1$?
:::

::: {.solution}
Let $X$ be a smooth projective connected complex curve of genus $g$.  Its Jacobian is
\[
\operatorname{Jac}(X)
=H^0(X,\Omega_X^1)^\vee/H_1(X,\mathbb Z),
\]
where $H_1(X,\mathbb Z)$ is embedded as the period lattice by integration.

::: pf

::: pf-step
The Jacobian is a complex torus of dimension $g$, and in fact an abelian variety.

::: pf-proof
The vector space
\[
H^0(X,\Omega_X^1)
\]
has complex dimension $g$, so its dual does as well.  Integration of holomorphic differentials over integral $1$-cycles gives a lattice of real rank $2g$ in that dual.  The quotient is therefore a compact complex torus of complex dimension $g$.

The classical theta-divisor construction supplies a polarization, hence makes this complex torus projective; therefore it is an abelian variety.
:::

:::

::: pf-step
The Abel--Jacobi map on degree-zero divisors is the homomorphism
\[
\operatorname{AJ}:\operatorname{Div}^0(X)
\longrightarrow
\operatorname{Jac}(X)
\]
defined by
\[
\operatorname{AJ}\!\left(\sum_i n_ip_i\right)
=\left[
\omega\longmapsto
\sum_i n_i\int_{p_0}^{p_i}\omega
\right].
\]

::: pf-proof
Because
\[
\sum_i n_i=0,
\]
the class does not depend on the chosen common base point $p_0$.  Changing any integration path changes the functional by a period, so the class modulo the period lattice is well-defined.  Additivity of integration makes the construction a group homomorphism.
:::

:::

::: {.pf-step #pic0-jac-iso}
Abel's theorem and Jacobi inversion identify
\[
\boxed{
\operatorname{Pic}^0(X)\cong\operatorname{Jac}(X).
}
\]
Thus the degree-zero divisor classes, equivalently the degree-zero line bundles, form a projective variety that is an algebraic group.

::: pf-proof
Abel's theorem says
\[
\ker(\operatorname{AJ})
=\operatorname{Prin}(X).
\]
Thus Abel--Jacobi descends to an injective homomorphism
\[
\operatorname{Pic}^0(X)
=\operatorname{Div}^0(X)/\operatorname{Prin}(X)
\hookrightarrow
\operatorname{Jac}(X).
\]
Jacobi inversion says this map is surjective.  Hence it is an isomorphism.
:::

:::

::: {.pf-step #pointwise-aj-injective}
After fixing $p_0\in X$, the pointwise Abel--Jacobi map is
\[
j_{p_0}:X\longrightarrow\operatorname{Jac}(X),
\qquad
p\longmapsto\operatorname{AJ}(p-p_0).
\]
If $g\ge1$, this map is injective.

::: pf-proof
Suppose
\[
j_{p_0}(p)=j_{p_0}(q).
\]
Then
\[
\operatorname{AJ}(p-q)=0.
\]
By Abel's theorem, $p-q$ is principal.  If $p\ne q$, there would be a nonconstant meromorphic function $f$ with
\[
\operatorname{div}(f)=p-q.
\]
Such an $f:X\to\mathbb P^1$ has exactly one simple pole, hence degree $1$.  A degree-one morphism between smooth projective curves is an isomorphism, so $X\cong\mathbb P^1$, contradicting $g\ge1$.  Therefore $p=q$.
:::

:::

::: {.pf-step #aj-immersion-embedding}
For $g\ge1$, the map $j_{p_0}$ is an immersion and hence a closed embedding.

::: pf-proof
The cotangent space of $\operatorname{Jac}(X)$ at the origin is naturally
\[
H^0(X,\Omega_X^1).
\]
The dual of the tangent map of $j_{p_0}$ at $p$ is the evaluation map
\[
H^0(X,\Omega_X^1)
\longrightarrow
\Omega_{X,p}^1\otimes\kappa(p),
\qquad
\omega\longmapsto\omega(p).
\]
Thus $j_{p_0}$ is immersive at $p$ exactly when some holomorphic differential does not vanish at $p$.

If $g=1$, the canonical bundle has degree $0$ and a nonzero global section, hence is trivial; its nonzero differential vanishes nowhere.

If $g\ge2$, then a degree-one divisor $p$ satisfies
\[
\ell(p)=1,
\]
for otherwise it would give a degree-one map $X\to\mathbb P^1$.  Riemann--Roch gives
\[
\ell(K-p)
=\ell(p)+\deg(K-p)+1-g
=1+(2g-3)+1-g
=g-1.
\]
Since
\[
\ell(K)=g,
\]
not every holomorphic differential vanishes at $p$.  Hence the tangent map is injective everywhere.

The curve $X$ is proper, so its image in the separated variety $\operatorname{Jac}(X)$ is closed.  An injective proper immersion of a smooth curve is a closed embedding.  Thus $j_{p_0}$ embeds $X$ in its Jacobian for every $g\ge1$.
:::

:::

::: {.pf-step #genus-one-aj-isomorphism}
If $g=1$, the Abel--Jacobi map is an isomorphism
\[
\boxed{
X\xrightarrow{\sim}\operatorname{Jac}(X).
}
\]

::: pf-proof
By step [](#aj-immersion-embedding){.pf-ref}, $j_{p_0}$ is a closed embedding.  Both source and target are irreducible smooth projective curves of dimension $1$.  The image of a nonconstant morphism from a curve is one-dimensional, so the closed image must be all of the irreducible one-dimensional target.  Hence the embedding is surjective and therefore an isomorphism.
:::

:::

::: {.pf-step #elliptic-curve-group-iso}
If $X=E$ is an elliptic curve and $p_0=0$ is its origin, then
\[
j_0:E\xrightarrow{\sim}\operatorname{Jac}(E),
\qquad
p\longmapsto\mathcal O_E(p-0),
\]
is an isomorphism of algebraic groups.

::: pf-proof
Under the identification
\[
\operatorname{Jac}(E)\cong\operatorname{Pic}^0(E),
\]
the group law is tensor product of degree-zero line bundles.  Thus
\[
j_0(p)+j_0(q)
=\mathcal O_E(p+q-2\cdot0).
\]
There is a unique point $r\in E$ such that
\[
p+q-r-0
\]
is principal; this is precisely the elliptic-curve group law $r=p+q$.  Therefore
\[
j_0(p+q)=j_0(p)+j_0(q).
\]
Together with step [](#genus-one-aj-isomorphism){.pf-ref}, this makes $j_0$ an isomorphism of algebraic groups.
:::

:::

::: pf-qed
Step [](#pic0-jac-iso){.pf-ref} gives the significance of the Jacobian, steps [](#pointwise-aj-injective){.pf-ref} and [](#aj-immersion-embedding){.pf-ref} describe the Abel--Jacobi map, and steps [](#genus-one-aj-isomorphism){.pf-ref} and [](#elliptic-curve-group-iso){.pf-ref} give the genus-one case.
:::

:::
:::
