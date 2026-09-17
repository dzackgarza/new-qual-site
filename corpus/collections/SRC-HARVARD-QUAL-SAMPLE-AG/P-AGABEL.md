---
schema: qual/card@1
id: P-AGABEL
kind: problem
title: Abel's theorem
classification:
  areas:
  - algebraic-geometry
  topics:
  - Abel-Jacobi Map
  - Divisors
  - Jacobians
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the Harvard sample qualifying-exam algebraic-geometry PDF; the source asks Wodzicki's question "State Abel's theorem."
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
State Abel's theorem.
:::

::: {.solution}
Let $X$ be a smooth projective connected curve over $\mathbb C$.  Its Jacobian is
\[
\operatorname{Jac}(X)
=H^0(X,\Omega_X^1)^\vee/H_1(X,\mathbb Z),
\]
where the homology group is embedded as the period lattice.

<1>1. For a degree-zero divisor
\[
D=\sum_i n_i p_i,
\qquad
\sum_i n_i=0,
\]
the Abel--Jacobi class is
\[
\operatorname{AJ}(D)
=\left[
\omega\longmapsto\sum_i n_i\int_{p_0}^{p_i}\omega
\right]
\in\operatorname{Jac}(X),
\]
where $p_0\in X$ is any base point.
::: {.proof}
Changing the integration paths changes the displayed functional by periods, so its class in the quotient is well-defined.  Because $\deg D=0$, changing the common base point contributes
\[
\left(\sum_i n_i\right)\int_{p_0'}^{p_0}\omega=0,
\]
so the class is independent of the choice of $p_0$ as well.
:::

<1>2. Abel's theorem states
\[
\boxed{
D\text{ is principal}
\quad\Longleftrightarrow\quad
\operatorname{AJ}(D)=0\text{ in }\operatorname{Jac}(X).
}
\]
::: {.proof}
Equivalently, the kernel of the Abel--Jacobi homomorphism
\[
\operatorname{Div}^0(X)\longrightarrow\operatorname{Jac}(X)
\]
is exactly the subgroup $\operatorname{Prin}(X)$ of principal divisors.  This is the standard form of Abel's theorem for a compact Riemann surface.
:::

<1>3. Equivalently, if $p_1,\ldots,p_m,q_1,\ldots,q_m\in X$ are counted with multiplicity, then there exists a nonzero meromorphic function $f$ with
\[
\operatorname{div}(f)
=\sum_{i=1}^m p_i-
\sum_{i=1}^m q_i
\]
if and only if
\[
\boxed{
\sum_{i=1}^m\operatorname{AJ}(p_i-p_0)
=
\sum_{i=1}^m\operatorname{AJ}(q_i-p_0)
\quad\text{in }\operatorname{Jac}(X).
}
\]
::: {.proof}
Apply <1>2 to the degree-zero divisor
\[
D=\sum_i p_i-\sum_i q_i.
\]
The divisor is principal exactly when it is the divisor of a meromorphic function, while additivity of the Abel--Jacobi map gives the displayed equality.
:::

<1>4. Thus Abel's theorem makes the Abel--Jacobi map descend to an injective homomorphism
\[
\operatorname{Pic}^0(X)
=\operatorname{Div}^0(X)/\operatorname{Prin}(X)
\hookrightarrow
\operatorname{Jac}(X).
\]
Jacobi inversion is the separate surjectivity statement; together the two theorems give
\[
\operatorname{Pic}^0(X)\cong\operatorname{Jac}(X).
\]
::: {.proof}
By <1>2, two degree-zero divisors have the same Abel--Jacobi image exactly when their difference is principal.  Hence the induced map on $\operatorname{Pic}^0(X)$ is injective.  Surjectivity is not part of this kernel statement; it is supplied by Jacobi inversion.
:::

<1>5. Q.E.D.
::: {.proof}
Step <1>2 is Abel's theorem, and step <1>3 is its equivalent zero-and-pole formulation.
:::
:::
