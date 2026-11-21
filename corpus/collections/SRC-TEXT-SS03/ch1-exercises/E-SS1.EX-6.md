---
schema: qual/card@1
id: E-SS1.EX-6
kind: problem
title: "Connected components as equivalence classes"
classification:
  areas:
    - complex-analysis
  topics: [Connectedness, Connected Components]
relations: []
review: draft
audit:
  - event: solution-written
    by: gpt-5.6-sol
    date: 2026-09-10
---

::: {.exercise}
Let $\Omega$ be an open set in $\CC$ and $z \in \Omega$. The connected component (or simply the component) of $\Omega$ containing $z$ is the set $\mathcal{C}_z$ of all points $w$ in $\Omega$ that can be joined to $z$ by a curve entirely contained in $\Omega$.

(a) Check first that $\mathcal{C}_z$ is open and connected. Then, show that $w \in \mathcal{C}_z$ defines an equivalence relation, that is: (i) $z \in \mathcal{C}_z$, (ii) $w \in \mathcal{C}_z$ implies $z \in \mathcal{C}_w$, and (iii) if $w \in \mathcal{C}_z$ and $z \in \mathcal{C}_\zeta$, then $w \in \mathcal{C}_\zeta$.

Thus $\Omega$ is the union of all its connected components, and two components are either disjoint or coincide.

(b) Show that $\Omega$ can have only countably many distinct connected components.

(c) Prove that if $\Omega$ is the complement of a compact set, then $\Omega$ has only one unbounded component.

[Hint: For (b), one would otherwise obtain an uncountable number of disjoint open balls. Now, each ball contains a point with rational coordinates. For (c), note that the complement of a large disc containing the compact set is connected.]
:::

::: {.solution}

The argument is the card's own: components are the equivalence classes of "joinable by a curve", they are open because $\Omega$ is, and countability comes from rational points.

::: pf

::: {.pf-step #open}

For $z\in\Omega$ the set $\mathcal{C}_{z}$ of points joinable to $z$ by a curve in $\Omega$ is open and connected.

::: pf-proof

Take $w\in\mathcal{C}_{z}$. Since $\Omega$ is open, some disc $D(w,r)\subset\Omega$; each $u\in D(w,r)$ is joined to $w$ by the line segment in that disc, and concatenating it with a curve from $z$ to $w$ joins $z$ to $u$, so $u\in\mathcal{C}_{z}$ and $D(w,r)\subset\mathcal{C}_{z}$. Hence $\mathcal{C}_{z}$ is open. It is path connected, because any two of its points are joined by way of $z$, with one curve reversed; a path connected set is connected.

:::

:::

::: {.pf-step #equivalence}

$w\in\mathcal{C}_{z}$ is an equivalence relation, with $\mathcal{C}_{z}$ as the class of $z$.

::: pf-proof

Reflexivity: the constant curve joins $z$ to $z$. Symmetry: reversing a curve from $z$ to $w$ gives one from $w$ to $z$, so $w\in\mathcal{C}_{z}$ implies $z\in\mathcal{C}_{w}$. Transitivity: concatenating a curve from $z$ to $w$ with one from $w$ to $\zeta$ gives a curve from $z$ to $\zeta$, so $w\in\mathcal{C}_{z}$ and $\zeta\in\mathcal{C}_{w}$ give $\zeta\in\mathcal{C}_{z}$, which by symmetry is the assertion $w\in\mathcal{C}_{z}$ and $z\in\mathcal{C}_{\zeta}$ imply $w\in\mathcal{C}_{\zeta}$. Hence the classes are the sets $\mathcal{C}_{z}$, they are pairwise disjoint or equal, and their union is $\Omega$ since $z\in\mathcal{C}_{z}$.

:::

:::

::: {.pf-step #countable}

(b) $\Omega$ has at most countably many components.

::: pf-proof

Each component $\mathcal{C}_{z}$ is nonempty and open by step [](#open){.pf-ref}, and $\Omega\subset\CC\cong\RR^{2}$ is second countable with $\QQ^{2}$ dense, so $\mathcal{C}_{z}$ contains a point of $\QQ^{2}$. Distinct components are disjoint by step [](#equivalence){.pf-ref}, so choosing one rational point in each gives an injection from the set of components into the countable set $\QQ^{2}$; a set injecting into a countable set is countable.

:::

:::

::: {.pf-step #unbounded}

(c) If $\Omega$ is the complement of a compact set then $\Omega$ has exactly one unbounded component.

::: pf-proof

Write $\Omega=\CC-K$ with $K$ compact. Choose $R>0$ with $K\subset D(0,R)$; then the exterior $E=\{z:\abs{z}>R\}$ lies in $\Omega$ and is connected, being homeomorphic to $(R,\infty)\times S^{1}$, so $E$ is contained in the single component $U$ of $\Omega$ that contains it. Any unbounded component $V$ contains a point with $\abs{z}>R$, hence meets $E\subset U$; two components that meet are equal, so $V=U$:
$$
\boxed{\Omega=\CC-K\ \text{with } K \text{ compact has exactly one unbounded component, and } \mathcal{C}_{z} \text{ is countably many open connected pieces.}}
$$

:::

:::

:::

:::
