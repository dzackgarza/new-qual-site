---
schema: qual/card@1
id: P-AGWEILCARTIER
kind: problem
title: Weil and Cartier divisors on a curve, and the divisor of $f \in K^*$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Divisors
  - Cartier Divisors
  - Function Fields
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the Harvard sample qualifying-exam algebraic-geometry PDF; this is Ogus's pair of questions on Weil/Cartier divisors on curves and the divisor attached to $f\in K^*$.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Describe Weil divisors and Cartier divisors on curves.

How do you get a Weil divisor from an element $f \in K^*$, in the canonical isomorphism?
:::

::: {.solution}
Let $C$ be a smooth integral curve with function field
\[
K=K(C).
\]

::: pf

::: {.pf-step #weil-divisor-definition}
A Weil divisor on $C$ is a finite formal sum
\[
\boxed{
D=\sum_{p\in C^{(1)}}n_p[p],
\qquad n_p\in\mathbb Z,
}
\]
where $C^{(1)}$ is the set of codimension-one points.

::: pf-proof
A prime Weil divisor is by definition an integral closed subscheme of codimension one.  Since $C$ has dimension one, its codimension-one points are precisely its closed points, and the corresponding prime divisors are the points $[p]$.  A Weil divisor is a finite integer combination of these prime divisors.
:::

:::

::: {.pf-step #cartier-divisor-definition}
A Cartier divisor on $C$ is represented by an open cover $\{U_i\}$ and rational functions
\[
f_i\in K^*
\]
such that
\[
\frac{f_i}{f_j}\in\mathcal O_C^*(U_i\cap U_j)
\]
on every overlap.

::: pf-proof
Equivalently, a Cartier divisor is a global section of the quotient sheaf
\[
\mathcal K_C^*/\mathcal O_C^*,
\]
where $\mathcal K_C$ is the sheaf of rational functions.  Choosing representatives of such a section on an open cover gives exactly the displayed local rational equations, and changing a representative by a unit gives the same Cartier divisor.
:::

:::

::: {.pf-step #dvr-valuation}
Because $C$ is smooth, every local ring
\[
\mathcal O_{C,p}
\]
at a closed point is a discrete valuation ring.  Denote its valuation by
\[
\operatorname{ord}_p:K^*\longrightarrow\mathbb Z.
\]

::: pf-proof
Smoothness makes $\mathcal O_{C,p}$ a regular local ring of dimension one.  A one-dimensional Noetherian regular local domain is a DVR, whose normalized valuation is the order of vanishing at $p$.
:::

:::

::: {.pf-step #cartier-to-weil-map}
The canonical map from Cartier divisors to Weil divisors is
\[
\boxed{
\{(U_i,f_i)\}
\longmapsto
\sum_{p\in C}\operatorname{ord}_p(f_i)[p],
}
\]
where $i$ is any index with $p\in U_i$.

::: pf-proof
If $p\in U_i\cap U_j$, then
\[
f_i/f_j
\]
is a unit in $\mathcal O_{C,p}$.  Units have valuation zero, so
\[
\operatorname{ord}_p(f_i)
=\operatorname{ord}_p(f_j).
\]
Thus the coefficient is independent of the chosen local equation.

Only finitely many coefficients are nonzero.  The generic point is not in the support of a Cartier divisor, so its support is a proper closed subset of the one-dimensional Noetherian integral scheme $C$.  Every such closed subset is a finite union of closed points.
:::

:::

::: {.pf-step #cartier-weil-isomorphism}
On a smooth curve, the map in step [](#cartier-to-weil-map){.pf-ref} is an isomorphism
\[
\boxed{\operatorname{CaDiv}(C)\cong\operatorname{Div}(C).}
\]

::: pf-proof
To prove injectivity, suppose a Cartier divisor has valuation zero at every closed point.  Every local equation $f_i$ then has zero valuation in every DVR on $U_i$, so it is a unit at every point of $U_i$.  Hence the Cartier divisor is zero.

For surjectivity, let
\[
D=\sum_{j=1}^r n_j[p_j]
\]
be a Weil divisor.  For each $p_j$, choose a neighborhood $U_j$ containing no other point of the support and choose a uniformizer $t_j$ at $p_j$, shrinking $U_j$ so that $t_j$ is represented by a regular function whose only zero on $U_j$ is $p_j$.  Use the local equation
\[
t_j^{n_j}
\]
on $U_j$, and use the equation $1$ on
\[
C\setminus\{p_1,\ldots,p_r\}.
\]
On every overlap the ratio of two chosen equations has no zero or pole and is therefore a unit.  These local equations define a Cartier divisor whose valuation at $p_j$ is $n_j$ and whose valuation elsewhere is zero.  It maps to $D$.
:::

:::

::: {.pf-step #principal-divisor-formula}
For a single rational function
\[
f\in K^*,
\]
the corresponding principal Cartier divisor maps to the principal Weil divisor
\[
\boxed{
\operatorname{div}(f)
=\sum_{p\in C}\operatorname{ord}_p(f)[p].
}
\]

::: pf-proof
The principal Cartier divisor is represented on the one-set cover $\{C\}$ by the rational function $f$.  Applying the map in step [](#cartier-to-weil-map){.pf-ref} gives precisely the displayed sum.  Positive coefficients record zeros and negative coefficients record poles, with their orders.
:::

:::

::: pf-step
Consequently, on a smooth curve the divisor class group and the Cartier divisor class group agree:
\[
\operatorname{Cl}(C)\cong\operatorname{Pic}(C).
\]

::: pf-proof
Step [](#cartier-weil-isomorphism){.pf-ref} identifies Weil and Cartier divisors, and step [](#principal-divisor-formula){.pf-ref} identifies their principal subgroups.  Passing to the quotients gives the stated isomorphism.
:::

:::

::: pf-qed
Steps [](#weil-divisor-definition){.pf-ref}, [](#cartier-divisor-definition){.pf-ref}, [](#dvr-valuation){.pf-ref}, [](#cartier-to-weil-map){.pf-ref} and [](#cartier-weil-isomorphism){.pf-ref} describe the two divisor notions and their canonical identification; step [](#principal-divisor-formula){.pf-ref} answers explicitly how $f\in K^*$ produces its Weil divisor.
:::

:::
:::
