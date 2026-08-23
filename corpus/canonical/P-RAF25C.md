---
schema: qual/card@1
id: P-RAF25C
kind: problem
title: "Pointwise and weak-star dual characterizations of the constraint u >= f"
classification:
  areas:
  - real-analysis
  topics:
  - L-infinity Spaces
  - Weak* Topology
  - Duality
relations: []
review: draft
solved: false
---

::: problem
Let $\Omega \subset \mathbb{R}^n$ be a Lebesgue measurable set, $f : \Omega \to \mathbb{R}$ measurable and define
$$
X := \{u \in L^\infty(\Omega) : u \geq f \text{ a.e. in } \Omega\}, \quad Y := \left\{u \in L^\infty(\Omega) : \int_\Omega u\varphi \, dx \geq \int_\Omega f\varphi \, dx \; \forall \varphi \in W\right\},
$$
where $W := \{\varphi \in L^1(\Omega) : \varphi f \in L^1(\Omega), \varphi \geq 0 \text{ a.e. in } \Omega\}$.

(1) Prove that if $f \in L^\infty(\Omega)$, then $X = Y$.

(2) Prove that (1) holds when $f$ is just measurable.

(3) Prove that $X$ is sequentially closed in the weak*-topology in $L^\infty(\Omega)$.
:::
