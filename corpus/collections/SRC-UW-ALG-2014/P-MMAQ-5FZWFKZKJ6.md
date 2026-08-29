---
schema: qual/card@1
id: P-MMAQ-5FZWFKZKJ6
kind: problem
title: Class sums form a $\mathbb{Z}$-basis of the center of $\mathbb{Z}[G]$, and
  $|C|\chi_\pi(C)/\dim V$ is an algebraic integer
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

::: problem
Let $G$ be a finite group and $\mathbb{Z}[G]$ its integral group ring.
Let $\mathcal{Z} = Z(\mathbb{Z}[G])$ be the center of $\mathbb{Z}[G]$.
For each conjugacy class $C \subseteq G$, let $P_C = \sum_{g \in C} g$ be the class sum.

(1) Show that the class sums $\{P_C\}$ form a $\mathbb{Z}$-basis for $\mathcal{Z}$. Hence $\mathcal{Z} \cong \mathbb{Z}^d$ as an abelian group, where $d$ is the number of conjugacy classes in $G$.
(2) Show that if a ring $R$ is isomorphic to $\mathbb{Z}^d$ as an abelian group, then every element in $R$ satisfies a monic integral polynomial (i.e. is integral over $\mathbb{Z}$).
(3) Let $\pi: G \to \operatorname{GL}(V)$ be an irreducible complex representation of $G$. Show that $\pi(P_C)$ acts on $V$ as multiplication by the scalar:
$$\omega_\pi(C) = \frac{|C| \chi_\pi(C)}{\dim V}$$
where $\chi_\pi(C)$ is the value of the character $\chi_\pi$ on any element of $C$.
(4) Conclude that $\frac{|C| \chi_\pi(C)}{\dim V}$ is an **algebraic integer**.
:::

::: solution
**Goal:** Prove that class sums form a $\mathbb{Z}$-basis of $Z(\mathbb{Z}[G])$, that finite free $\mathbb{Z}$-algebras are integral, that $\pi(P_C)$ acts by scalar $\omega_\pi(C)$ via Schur's Lemma, and that $\omega_\pi(C)$ is an algebraic integer.

<1>1. Part 1: Class Sums Form a $\mathbb{Z}$-Basis for $\mathcal{Z} = Z(\mathbb{Z}[G])$:
    *Proof:*
    <2>1. Let $x = \sum_{g \in G} a_g g \in \mathbb{Z}[G]$ with $a_g \in \mathbb{Z}$.
    <2>2. The element $x$ lies in the center $\mathcal{Z}$ if and only if $h x h^{-1} = x$ for all $h \in G$:
        $$h x h^{-1} = \sum_{g \in G} a_g (h g h^{-1}) = \sum_{y \in G} a_{h^{-1} y h} y = \sum_{y \in G} a_y y.$$
    <2>3. Equating coefficients of basis elements $y \in G$:
        $$a_{h^{-1} y h} = a_y \quad \text{for all } h, y \in G.$$
    <2>4. This means the coefficient function $g \mapsto a_g$ is constant on each conjugacy class $C$ of $G$.
    <2>5. Let $C_1, C_2, \dots, C_d$ be the distinct conjugacy classes of $G$.
    <2>6. Then $x$ can be written uniquely as:
        $$x = \sum_{i=1}^d c_i \left( \sum_{g \in C_i} g \right) = \sum_{i=1}^d c_i P_{C_i} \quad (c_i \in \mathbb{Z}).$$
    <2>7. Since the conjugacy classes $C_i$ partition $G$, the elements $P_{C_1}, \dots, P_{C_d}$ are support-disjoint in $G$, hence linearly independent over $\mathbb{Z}$.
    <2>8. Thus $\{P_C\}$ forms a $\mathbb{Z}$-basis of $\mathcal{Z}$, and $\mathcal{Z} \cong \mathbb{Z}^d$ as an abelian group.

<1>2. Part 2: Rings with $R \cong \mathbb{Z}^d$ are Integral over $\mathbb{Z}$:
    *Proof:*
    <2>1. Let $R$ be a ring whose additive group is free abelian of finite rank $d$, with $\mathbb{Z}$-basis $\{v_1, v_2, \dots, v_d\}$.
    <2>2. For any fixed element $r \in R$, multiplication by $r$ defines an additive group endomorphism $L_r: R \to R$ ($L_r(x) = r x$).
    <2>3. Expressing $L_r(v_i)$ in the basis:
        $$r v_i = \sum_{j=1}^d a_{ij} v_j \quad \text{where } A = (a_{ij}) \in M_d(\mathbb{Z}).$$
    <2>4. In matrix-vector notation: $(r I_d - A) \mathbf{v} = \mathbf{0}$, where $\mathbf{v} = [v_1, \dots, v_d]^T$.
    <2>5. Multiplying by the adjugate matrix $\operatorname{adj}(r I_d - A)$:
        $$\det(r I_d - A) \cdot \mathbf{v} = \mathbf{0} \implies \det(r I_d - A) v_i = 0 \quad \text{for all } i = 1, \dots, d.$$
    <2>6. Since $\{v_1, \dots, v_d\}$ is a $\mathbb{Z}$-basis of $R$, the identity element $1 = \sum c_i v_i \in R$ satisfies $\det(r I_d - A) \cdot 1 = 0$, so:
        $$\det(r I_d - A) = 0 \in R.$$
    <2>7. The characteristic polynomial $p_A(t) = \det(t I_d - A) \in \mathbb{Z}[t]$ is a **monic polynomial with integer coefficients** of degree $d$.
    <2>8. Since $p_A(r) = 0$, every element $r \in R$ is an **algebraic integer** (integral over $\mathbb{Z}$).

<1>3. Part 3: Action of $\pi(P_C)$ via Schur's Lemma:
    *Proof:*
    <2>1. Let $(\pi, V)$ be an irreducible complex representation of $G$, and let $n = \dim_\mathbb{C}(V)$.
    <2>2. Since $P_C \in \mathcal{Z}$, for every $h \in G$, $\pi(h) \pi(P_C) = \pi(h P_C) = \pi(P_C h) = \pi(P_C) \pi(h)$.
    <2>3. By **Schur's Lemma**, any $G$-equivariant endomorphism of an irreducible complex representation is a scalar multiple of the identity:
        $$\pi(P_C) = \lambda_C \operatorname{id}_V \quad \text{for some scalar } \lambda_C \in \mathbb{C}.$$
    <2>4. We compute the trace of both sides:
        $$\operatorname{Tr}(\pi(P_C)) = \operatorname{Tr}(\lambda_C \operatorname{id}_V) = \lambda_C \dim(V) = n \lambda_C.$$
    <2>5. On the other hand, by linearity of trace and definition of character $\chi_\pi$:
        $$\operatorname{Tr}(\pi(P_C)) = \sum_{g \in C} \operatorname{Tr}(\pi(g)) = \sum_{g \in C} \chi_\pi(g) = |C| \chi_\pi(C)$$
        since $\chi_\pi$ is constant on the conjugacy class $C$.
    <2>6. Equating the two trace computations:
        $$n \lambda_C = |C| \chi_\pi(C) \implies \lambda_C = \frac{|C| \chi_\pi(C)}{\dim V}.$$

<1>4. Part 4: $\frac{|C|\chi_\pi(C)}{\dim V}$ is an Algebraic Integer:
    *Proof:*
    <2>1. The algebra homomorphism $\pi: \mathbb{Z}[G] \to \operatorname{End}_\mathbb{C}(V)$ restricts on the center to a ring homomorphism:
        $$\pi|_\mathcal{Z}: \mathcal{Z} \longrightarrow \mathbb{C} \cdot \operatorname{id}_V \cong \mathbb{C}, \qquad P_C \longmapsto \lambda_C = \frac{|C|\chi_\pi(C)}{\dim V}.$$
    <2>2. By Part 1, $\mathcal{Z} \cong \mathbb{Z}^d$ as an abelian group.
    <2>3. By Part 2, the class sum $P_C \in \mathcal{Z}$ satisfies a monic polynomial $p(t) \in \mathbb{Z}[t]$ with $p(P_C) = 0$.
    <2>4. Applying the ring homomorphism $\pi$:
        $$p(\lambda_C) = p\left(\frac{|C|\chi_\pi(C)}{\dim V}\right) = 0.$$
    <2>5. Since $\lambda_C$ is a root of a monic polynomial with integer coefficients, $\frac{|C|\chi_\pi(C)}{\dim V}$ is an **algebraic integer**.

<1>5. Conclusion:
    Class sums form a $\mathbb{Z}$-basis of $\mathcal{Z} \cong \mathbb{Z}^d$, whose elements are integral over $\mathbb{Z}$; by Schur's Lemma $\pi(P_C) = \omega_\pi(C) \operatorname{id}_V$, so $\omega_\pi(C) = \frac{|C|\chi_\pi(C)}{\dim V}$ is an algebraic integer. Q.E.D.
:::
