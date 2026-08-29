---
schema: qual/card@1
id: P-HXOC6
kind: problem
title: Witt's theorem on real quadratic forms
classification:
  areas:
  - algebra
  topics:
  - Quadratic Forms
  - Bilinear Forms
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
State and explain Witt's Cancellation Theorem and Witt's Extension Theorem for quadratic forms (over $\mathbb{R}$ and general fields).
:::

::: solution
**Goal:** State and prove Witt's Theorem on quadratic and symmetric bilinear forms.

<1>1. Setting and Definitions:
    *Proof:*
    <2>1. Let $k$ be a field with $\operatorname{char}(k) \ne 2$ (e.g. $k = \mathbb{R}$).
    <2>2. A quadratic space $(V, q)$ is a finite-dimensional $k$-vector space $V$ equipped with a non-degenerate symmetric bilinear form $B(u, v) = \frac{1}{2}(q(u+v) - q(u) - q(v))$.
    <2>3. An isometry between quadratic spaces is a vector space isomorphism $\sigma: V_1 \to V_2$ preserving the form: $q_2(\sigma(v)) = q_1(v)$ for all $v \in V_1$.
    <2>4. An orthogonal direct sum is denoted $V = U \perp W$.

<1>2. Statements of Witt's Theorems:
    *Proof:*
    <2>1. **Witt's Extension Theorem:** Let $(V, q)$ be a non-degenerate quadratic space over $k$.
        Let $U \subseteq V$ be any subspace, and let $f: U \to V$ be an isometric embedding (i.e. $q(f(u)) = q(u)$ for all $u \in U$).
        Then there exists an isometry $\widetilde{f}: V \to V$ of the entire space $V$ such that $\widetilde{f}|_U = f$.
    <2>2. **Witt's Cancellation Theorem:** If $U_1, U_2, W_1, W_2$ are quadratic spaces over $k$ such that:
        $$U_1 \perp W_1 \cong U_2 \perp W_2 \quad \text{and} \quad U_1 \cong U_2,$$
        then $W_1 \cong W_2$.

<1>3. Proof Outline of Witt's Extension Theorem (Induction via Reflections):
    *Proof:*
    <2>1. By induction on $\dim U$, it suffices to handle the base case where $\dim U = 1$, spanned by a vector $x \in V$, with $y = f(x)$ and $q(x) = q(y)$.
    <2>2. **Case 1: $x$ is non-isotropic ($q(x) \ne 0$).**
        - Because $q(x) = q(y) \ne 0$, we have $q(x+y) + q(x-y) = 2q(x) + 2q(y) = 4q(x) \ne 0$.
        - Thus at least one of $x+y$ or $x-y$ is non-isotropic (has non-zero $q$).
        - If $q(x-y) \ne 0$, consider the hyperplane reflection $\tau_{x-y}: V \to V$ defined by:
            $$\tau_v(z) = z - \frac{2 B(z, v)}{q(v)} v.$$
            Then $\tau_{x-y}(x) = y$.
        - If $q(x+y) \ne 0$, $-\tau_{x+y}(x) = y$.
        - In either case, the reflection is an isometry extending $f$.
    <2>3. **Case 2: $x$ is isotropic ($q(x) = 0$).**
        - Embed $x$ into a hyperbolic plane $H \subset V$ and reduce to the non-degenerate case.

<1>4. Consequence for Real Quadratic Forms (Sylvester's Law of Inertia):
    *Proof:*
    <2>1. Over $\mathbb{R}$, every quadratic form is isometric to $\sum_{i=1}^p x_i^2 - \sum_{j=1}^q x_{p+j}^2$.
    <2>2. By Witt's theorem, the signature $(p, q)$ is an invariant that completely classifies non-degenerate real quadratic forms up to isometry.

<1>5. Conclusion:
    Witt's Theorem states every isometry of a subspace extends to an ambient isometry, implying the cancellation of isometric summands. Q.E.D.
:::
