---
schema: qual/card@1
id: E-1DM8W
kind: problem
title: Seifert-van Kampen when one inclusion is surjective
classification:
  areas:
  - topology
  topics:
  - Seifert-van Kampen Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Suppose that $i_2$ is surjective.

(a) Show that $j_1$ induces an epimorphism

$$
h: \pi_1(U, x_0)/M \to \pi_1(X, x_0),
$$

where $M$ is the least normal subgroup of $\pi_1(U, x_0)$ containing $i_1(\ker i_2)$.
[Hint: Show $j_1$ is surjective.]

(b) Show that $h$ is an isomorphism.
[Hint: Let $H = \pi_1(U, x_0)/M$. Let $\phi_1: \pi_1(U, x_0) \to H$ be the projection. Use the fact that $\pi_1(U \cap V, x_0)/\ker i_2$ is isomorphic to $\pi_1(V, x_0)$ to define a homomorphism $\phi_2: \pi_1(V, x_0) \to H$. Use Theorem 70.1 to define a left inverse for $h$.]
:::

::: solution
**Goal:** Prove that when the inclusion homomorphism $i_2: \pi_1(U \cap V, x_0) \to \pi_1(V, x_0)$ is surjective, $\pi_1(X, x_0) \cong \pi_1(U, x_0)/M$, where $M$ is the normal closure of $i_1(\ker i_2)$.

<1>1. Part (a): Surjectivity of $j_1$ and existence of the epimorphism $h$.
    *Proof:*
    <2>1. By the Seifert-van Kampen theorem, the images of $(j_1)_*$ and $(j_2)_*$ generate $\pi_1(X, x_0)$, and $(j_1)_* \circ (i_1)_* = (j_2)_* \circ (i_2)_*$.
    <2>2. For any $v \in \pi_1(V, x_0)$, surjectivity of $(i_2)_*$ guarantees the existence of $w \in \pi_1(U \cap V, x_0)$ such that $(i_2)_*(w) = v$.
    <2>3. Then $(j_2)_*(v) = (j_2)_*((i_2)_*(w)) = (j_1)_*((i_1)_*(w)) \in \operatorname{im}((j_1)_*)$.
    <2>4. Thus $\operatorname{im}((j_2)_*) \subseteq \operatorname{im}((j_1)_*)$, which implies $\operatorname{im}((j_1)_*) = \pi_1(X, x_0)$, so $(j_1)_*$ is surjective.
    <2>5. For any $w \in \ker((i_2)_*)$, $(j_1)_*((i_1)_*(w)) = (j_2)_*((i_2)_*(w)) = (j_2)_*(1) = 1$.
    <2>6. Thus $(i_1)_*(\ker(i_2)_*) \subseteq \ker((j_1)_*)$. Since $\ker((j_1)_*)$ is normal, the normal closure $M \subseteq \ker((j_1)_*)$.
    <2>7. By the First Isomorphism Theorem, $(j_1)_*$ factors through the quotient to define an epimorphism:
        $$h: \pi_1(U, x_0)/M \to \pi_1(X, x_0), \quad h([u]) = (j_1)_*(u).$$

<1>2. Part (b): $h$ is an isomorphism (construction of a left inverse via pushout).
    *Proof:*
    <2>1. Let $H = \pi_1(U, x_0)/M$, and let $\phi_1: \pi_1(U, x_0) \to H$ be the canonical projection homomorphism.
    <2>2. Consider the homomorphism $\phi_1 \circ (i_1)_*: \pi_1(U \cap V, x_0) \to H$. For any $w \in \ker((i_2)_*)$, $(i_1)_*(w) \in M = \ker(\phi_1)$, so $\ker((i_2)_*) \subseteq \ker(\phi_1 \circ (i_1)_*)$.
    <2>3. Since $(i_2)_*: \pi_1(U \cap V, x_0) \to \pi_1(V, x_0)$ is surjective, $\pi_1(U \cap V, x_0)/\ker((i_2)_*) \cong \pi_1(V, x_0)$.
    <2>4. Therefore $\phi_1 \circ (i_1)_*$ factors through $(i_2)_*$ to yield a unique homomorphism $\phi_2: \pi_1(V, x_0) \to H$ satisfying:
        $$\phi_2 \circ (i_2)_* = \phi_1 \circ (i_1)_*.$$
    <2>5. By the universal property of the Seifert-van Kampen theorem (Theorem 70.1), there exists a unique homomorphism $g: \pi_1(X, x_0) \to H$ such that $g \circ (j_1)_* = \phi_1$ and $g \circ (j_2)_* = \phi_2$.
    <2>6. For any $[u] \in H$:
        $$(g \circ h)([u]) = g((j_1)_*(u)) = \phi_1(u) = [u].$$
    <2>7. Thus $g \circ h = \operatorname{id}_H$, so $h$ has a left inverse $g$ and is therefore injective.
    <2>8. Being both surjective and injective, $h$ is an isomorphism of groups. Q.E.D.
:::
