---
schema: qual/card@1
id: E-0EZ4U
kind: problem
title: Seifert-van Kampen with trivial intersection homomorphism
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

Suppose that the homomorphism $i_*$ induced by inclusion $i: U \cap V \to X$ is trivial.

(a) Show that $j_1$ and $j_2$ induce an epimorphism

$$
h: (\pi_1(U, x_0)/N_1) * (\pi_1(V, x_0)/N_2) \to \pi_1(X, x_0),
$$

where $N_1$ is the least normal subgroup of $\pi_1(U, x_0)$ containing image $i_1$, and $N_2$ is the least normal subgroup of $\pi_1(V, x_0)$ containing image $i_2$.

(b) Show that $h$ is an isomorphism.
[Hint: Use Theorem 70.1 to define a left inverse for $h$.]
:::

::: solution
**Goal:** Prove that when the inclusion $i: U \cap V \to X$ induces the trivial homomorphism on $\pi_1$, $\pi_1(X, x_0)$ is naturally isomorphic to the free product of the quotients $(\pi_1(U, x_0)/N_1) \ast (\pi_1(V, x_0)/N_2)$.

<1>1. Part (a): Construction and surjectivity of the homomorphism $h$.
    *Proof:*
    <2>1. Let $i_1: U \cap V \hookrightarrow U$, $i_2: U \cap V \hookrightarrow V$, $j_1: U \hookrightarrow X$, $j_2: V \hookrightarrow X$, with $i = j_1 \circ i_1 = j_2 \circ i_2$.
    <2>2. For any $\gamma \in \pi_1(U \cap V, x_0)$, $(j_1)_*((i_1)_*(\gamma)) = i_*(\gamma) = 1$ in $\pi_1(X, x_0)$ by assumption that $i_*$ is trivial.
    <2>3. Thus $\operatorname{im}((i_1)_*) \subseteq \ker((j_1)_*)$. Since $\ker((j_1)_*)$ is a normal subgroup of $\pi_1(U, x_0)$, the normal closure $N_1$ satisfies $N_1 \subseteq \ker((j_1)_*)$.
    <2>4. By the universal property of quotient groups, $(j_1)_*$ factors uniquely through a homomorphism:
        $$\phi_1: \pi_1(U, x_0)/N_1 \to \pi_1(X, x_0), \quad \phi_1([u]) = (j_1)_*(u).$$
    <2>5. By the identical argument on $V$, $(j_2)_*$ factors uniquely through:
        $$\phi_2: \pi_1(V, x_0)/N_2 \to \pi_1(X, x_0), \quad \phi_2([v]) = (j_2)_*(v).$$
    <2>6. By the universal property of the free product of groups, $\phi_1$ and $\phi_2$ determine a unique homomorphism:
        $$h: (\pi_1(U, x_0)/N_1) \ast (\pi_1(V, x_0)/N_2) \to \pi_1(X, x_0).$$
    <2>7. By the Seifert-van Kampen theorem, the images of $(j_1)_*$ and $(j_2)_*$ generate $\pi_1(X, x_0)$. Since $\operatorname{im}(h)$ contains $\operatorname{im}(\phi_1) = \operatorname{im}((j_1)_*)$ and $\operatorname{im}(\phi_2) = \operatorname{im}((j_2)_*)$, $h$ is surjective (an epimorphism).

<1>2. Part (b): $h$ is an isomorphism (existence of an inverse via universal property).
    *Proof:*
    <2>1. Let $G = (\pi_1(U, x_0)/N_1) \ast (\pi_1(V, x_0)/N_2)$. Let $q_1: \pi_1(U, x_0) \to \pi_1(U, x_0)/N_1 \hookrightarrow G$ and $q_2: \pi_1(V, x_0) \to \pi_1(V, x_0)/N_2 \hookrightarrow G$ be the canonical quotient-inclusion maps.
    <2>2. For any $\gamma \in \pi_1(U \cap V, x_0)$:
        - $(i_1)_*(\gamma) \in N_1 \implies q_1((i_1)_*(\gamma)) = 1 \in G$,
        - $(i_2)_*(\gamma) \in N_2 \implies q_2((i_2)_*(\gamma)) = 1 \in G$.
    <2>3. Therefore $q_1((i_1)_*(\gamma)) = q_2((i_2)_*(\gamma)) = 1$ for all $\gamma \in \pi_1(U \cap V, x_0)$.
    <2>4. By the universal property of the Seifert-van Kampen pushout (Theorem 70.1), the homomorphisms $q_1$ and $q_2$ induce a unique homomorphism:
        $$g: \pi_1(X, x_0) \to G$$
        satisfying $g \circ (j_1)_* = q_1$ and $g \circ (j_2)_* = q_2$.
    <2>5. We verify that $g \circ h = \operatorname{id}_G$:
        - On generators $[u] \in \pi_1(U, x_0)/N_1$: $(g \circ h)([u]) = g(\phi_1([u])) = g((j_1)_*(u)) = q_1(u) = [u]$.
        - On generators $[v] \in \pi_1(V, x_0)/N_2$: $(g \circ h)([v]) = g(\phi_2([v])) = g((j_2)_*(v)) = q_2(v) = [v]$.
    <2>6. Since $g \circ h$ is the identity on a generating set of $G$, $g \circ h = \operatorname{id}_G$.
    <2>7. Thus $h$ has a left inverse $g$, so $h$ is injective.
    <2>8. Being both surjective (<1>1) and injective, $h$ is an isomorphism of groups. Q.E.D.
:::
