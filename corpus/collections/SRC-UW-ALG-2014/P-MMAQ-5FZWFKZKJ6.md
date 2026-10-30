---
schema: qual/card@1
id: P-MMAQ-5FZWFKZKJ6
kind: problem
title: Class sums form a $\ZZ$-basis of the center of $\ZZ[G]$, and $\cardinality{C}\chi_\pi(C)/\dim V$ is an algebraic integer
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: {.problem}
Let $G$ be a finite group and $\ZZ[G]$ its integral group ring.
Let $\mathcal{Z} = Z(\ZZ[G])$ be the center of $\ZZ[G]$.
For each conjugacy class $C \subseteq G$, let $P_C = \sum_{g \in C} g$ be the class sum.

(1) Show that the class sums $\{P_C\}$ form a $\ZZ$-basis for $\mathcal{Z}$. Hence $\mathcal{Z} \cong \ZZ^d$ as an abelian group, where $d$ is the number of conjugacy classes in $G$.
(2) Show that if a ring $R$ is isomorphic to $\ZZ^d$ as an abelian group, then every element in $R$ satisfies a monic integral polynomial (i.e. is integral over $\ZZ$).
(3) Let $\pi: G \to \operatorname{GL}(V)$ be an irreducible complex representation of $G$. Show that $\pi(P_C)$ acts on $V$ as multiplication by the scalar:
$$\omega_\pi(C) = \frac{\cardinality{C} \chi_\pi(C)}{\dim V}$$
where $\chi_\pi(C)$ is the value of the character $\chi_\pi$ on any element of $C$.
(4) Conclude that $\frac{\cardinality{C} \chi_\pi(C)}{\dim V}$ is an **algebraic integer**.
:::

::: {.solution}
**Goal:** Prove that class sums form a $\ZZ$-basis of $Z(\ZZ[G])$, that finite free $\ZZ$-algebras are integral, that $\pi(P_C)$ acts by scalar $\omega_\pi(C)$ via Schur's Lemma, and that $\omega_\pi(C)$ is an algebraic integer.

::: pf

::: pf-step
Part 1: Class Sums Form a $\ZZ$-Basis for $\mathcal{Z} = Z(\ZZ[G])$:

::: pf-proof

::: pf-step
Let $x = \sum_{g \in G} a_g g \in \ZZ[G]$ with $a_g \in \ZZ$.

:::

::: pf-step
The element $x$ lies in the center $\mathcal{Z}$ if and only if $h x h^{-1} = x$ for all $h \in G$:
$$h x h^{-1} = \sum_{g \in G} a_g (h g h^{-1}) = \sum_{y \in G} a_{h^{-1} y h} y = \sum_{y \in G} a_y y.$$

:::

::: pf-step
Equating coefficients of basis elements $y \in G$:
$$a_{h^{-1} y h} = a_y \quad \text{for all } h, y \in G.$$

:::

::: pf-step
This means the coefficient function $g \mapsto a_g$ is constant on each conjugacy class $C$ of $G$.

:::

::: pf-step
Let $C_1, C_2, \dots, C_d$ be the distinct conjugacy classes of $G$.

:::

::: pf-step
Then $x$ can be written uniquely as:
$$x = \sum_{i=1}^d c_i \left( \sum_{g \in C_i} g \right) = \sum_{i=1}^d c_i P_{C_i} \quad (c_i \in \ZZ).$$

:::

::: pf-step
Since the conjugacy classes $C_i$ partition $G$, the elements $P_{C_1}, \dots, P_{C_d}$ are support-disjoint in $G$, hence linearly independent over $\ZZ$.

:::

::: pf-step
Thus $\{P_C\}$ forms a $\ZZ$-basis of $\mathcal{Z}$, and $\mathcal{Z} \cong \ZZ^d$ as an abelian group.

:::

:::

:::

::: pf-step
Part 2: Rings with $R \cong \ZZ^d$ are Integral over $\ZZ$:

::: pf-proof

::: pf-step
Let $R$ be a ring whose additive group is free abelian of finite rank $d$, with $\ZZ$-basis $\{v_1, v_2, \dots, v_d\}$.

:::

::: pf-step
For any fixed element $r \in R$, multiplication by $r$ defines an additive group endomorphism $L_r: R \to R$ ($L_r(x) = r x$).

:::

::: pf-step
Expressing $L_r(v_i)$ in the basis:
$$r v_i = \sum_{j=1}^d a_{ij} v_j \quad \text{where } A = (a_{ij}) \in M_d(\ZZ).$$

:::

::: pf-step
In matrix-vector notation: $(r I_d - A) \mathbf{v} = \mathbf{0}$, where $\mathbf{v} = [v_1, \dots, v_d]^T$.

:::

::: pf-step
Multiplying by the adjugate matrix $\operatorname{adj}(r I_d - A)$:
$$\det(r I_d - A) \cdot \mathbf{v} = \mathbf{0} \implies \det(r I_d - A) v_i = 0 \quad \text{for all } i = 1, \dots, d.$$

:::

::: pf-step
Since $\{v_1, \dots, v_d\}$ is a $\ZZ$-basis of $R$, the identity element $1 = \sum c_i v_i \in R$ satisfies $\det(r I_d - A) \cdot 1 = 0$, so:
$$\det(r I_d - A) = 0 \in R.$$

:::

::: pf-step
The characteristic polynomial $p_A(t) = \det(t I_d - A) \in \ZZ[t]$ is a **monic polynomial with integer coefficients** of degree $d$.

:::

::: pf-step
Since $p_A(r) = 0$, every element $r \in R$ is an **algebraic integer** (integral over $\ZZ$).

:::

:::

:::

::: pf-step
Part 3: Action of $\pi(P_C)$ via Schur's Lemma:

::: pf-proof

::: pf-step
Let $(\pi, V)$ be an irreducible complex representation of $G$, and let $n = \dim_\CC(V)$.

:::

::: pf-step
Since $P_C \in \mathcal{Z}$, for every $h \in G$, $\pi(h) \pi(P_C) = \pi(h P_C) = \pi(P_C h) = \pi(P_C) \pi(h)$.

:::

::: pf-step
By **Schur's Lemma**, any $G$-equivariant endomorphism of an irreducible complex representation is a scalar multiple of the identity:
$$\pi(P_C) = \lambda_C \operatorname{id}_V \quad \text{for some scalar } \lambda_C \in \CC.$$

:::

::: pf-step
We compute the trace of both sides:
$$\operatorname{Tr}(\pi(P_C)) = \operatorname{Tr}(\lambda_C \operatorname{id}_V) = \lambda_C \dim(V) = n \lambda_C.$$

:::

::: pf-step
On the other hand, by linearity of trace and definition of character $\chi_\pi$:
$$\operatorname{Tr}(\pi(P_C)) = \sum_{g \in C} \operatorname{Tr}(\pi(g)) = \sum_{g \in C} \chi_\pi(g) = \cardinality{C} \chi_\pi(C)$$
since $\chi_\pi$ is constant on the conjugacy class $C$.

:::

::: pf-step
Equating the two trace computations:
$$n \lambda_C = \cardinality{C} \chi_\pi(C) \implies \lambda_C = \frac{\cardinality{C} \chi_\pi(C)}{\dim V}.$$

:::

:::

:::

::: pf-step
Part 4: $\frac{\cardinality{C}\chi_\pi(C)}{\dim V}$ is an Algebraic Integer:

::: pf-proof

::: pf-step
The algebra homomorphism $\pi: \ZZ[G] \to \operatorname{End}_\CC(V)$ restricts on the center to a ring homomorphism:
$$\pi\restrict_\mathcal{Z}: \mathcal{Z} \longrightarrow \CC \cdot \operatorname{id}_V \cong \CC, \qquad P_C \longmapsto \lambda_C = \frac{\cardinality{C}\chi_\pi(C)}{\dim V}.$$

:::

::: pf-step
By Part 1, $\mathcal{Z} \cong \ZZ^d$ as an abelian group.

:::

::: pf-step
By Part 2, the class sum $P_C \in \mathcal{Z}$ satisfies a monic polynomial $p(t) \in \ZZ[t]$ with $p(P_C) = 0$.

:::

::: pf-step
Applying the ring homomorphism $\pi$:
$$p(\lambda_C) = p\left(\frac{\cardinality{C}\chi_\pi(C)}{\dim V}\right) = 0.$$

:::

::: pf-step
Since $\lambda_C$ is a root of a monic polynomial with integer coefficients, $\frac{\cardinality{C}\chi_\pi(C)}{\dim V}$ is an **algebraic integer**.

:::

:::

:::

::: pf-step
Conclusion:
Class sums form a $\ZZ$-basis of $\mathcal{Z} \cong \ZZ^d$, whose elements are integral over $\ZZ$; by Schur's Lemma $\pi(P_C) = \omega_\pi(C) \operatorname{id}_V$, so $\omega_\pi(C) = \frac{\cardinality{C}\chi_\pi(C)}{\dim V}$ is an algebraic integer.
:::

:::

:::
