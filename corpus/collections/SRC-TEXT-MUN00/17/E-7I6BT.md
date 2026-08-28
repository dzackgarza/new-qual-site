---
schema: qual/card@1
id: E-7I6BT
kind: exercise
title: Closures of intervals in finer topologies on the line
classification:
  areas:
  - topology
  topics:
  - Closure
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Consider the lower limit topology on $\mathbb{R}$ and the topology given by the basis $\mathcal{C}$ of Exercise 8 of §13. Determine the closures of the intervals $A = (0, \sqrt{2})$ and $B = (\sqrt{2}, 3)$ in these two topologies.
:::

::: solution
**Goal:** Determine the closures of $A = (0, \sqrt{2})$ and $B = (\sqrt{2}, 3)$ in the lower limit topology $\mathbb{R}_\ell$ (basis $\{[x, y) \mid x < y \in \mathbb{R}\}$) and the topology $\mathcal{T}_{\mathcal{C}}$ (basis $\mathcal{C} = \{[a, b) \mid a < b \in \mathbb{Q}\}$).

<1>1. Preliminary topology containment:
    Both $\mathbb{R}_\ell$ and $\mathcal{T}_{\mathcal{C}}$ are finer than the standard topology on $\mathbb{R}$.
    Therefore, the closures in both topologies are contained within the standard Euclidean closures:
    $$\overline{A} \subseteq [0, \sqrt{2}] \quad \text{and} \quad \overline{B} \subseteq [\sqrt{2}, 3].$$

<1>2. Closures in the lower limit topology $\mathbb{R}_\ell$:
    $\overline{A} = [0, \sqrt{2})$ and $\overline{B} = [\sqrt{2}, 3)$.
    *Proof:*
    <2>1. **For $A = (0, \sqrt{2})$:**
        - At $x = 0$: Every basic neighborhood $[0, \epsilon)$ intersects $(0, \sqrt{2})$ in $(0, \min(\epsilon, \sqrt{2})) \neq \varnothing$, so $0 \in \overline{A}$.
        - At $x = \sqrt{2}$: The basic open set $[\sqrt{2}, 2)$ contains $\sqrt{2}$ and is disjoint from $(0, \sqrt{2})$, so $\sqrt{2} \notin \overline{A}$.
        - Hence $\overline{A}_{\mathbb{R}_\ell} = [0, \sqrt{2})$.
    <2>2. **For $B = (\sqrt{2}, 3)$:**
        - At $x = \sqrt{2}$: Every basic neighborhood $[\sqrt{2}, \sqrt{2}+\epsilon)$ intersects $(\sqrt{2}, 3)$ in $(\sqrt{2}, \min(\sqrt{2}+\epsilon, 3)) \neq \varnothing$, so $\sqrt{2} \in \overline{B}$.
        - At $x = 3$: The basic open set $[3, 4)$ contains $3$ and is disjoint from $(\sqrt{2}, 3)$, so $3 \notin \overline{B}$.
        - Hence $\overline{B}_{\mathbb{R}_\ell} = [\sqrt{2}, 3)$.

<1>3. Closures in the rational-endpoint topology $\mathcal{T}_{\mathcal{C}}$:
    $\overline{A} = [0, \sqrt{2}]$ and $\overline{B} = [\sqrt{2}, 3)$.
    *Proof:*
    <2>1. **Neighborhood behavior at rational vs irrational points:**
        - For a rational $q \in \mathbb{Q}$, $[q, q')$ with $q' \in \mathbb{Q}$ is an open neighborhood.
        - For an irrational $z \notin \mathbb{Q}$, any basic set $[a, b) \in \mathcal{C}$ containing $z$ must satisfy $a < z < b$ (since $a \in \mathbb{Q} \implies a \neq z$). Thus every basic neighborhood of $z$ contains an open interval $(a, b)$ around $z$.
    <2>2. **For $A = (0, \sqrt{2})$:**
        - At $x = 0 \in \mathbb{Q}$: For any rational $q > 0$, $[0, q) \cap (0, \sqrt{2}) \neq \varnothing$, so $0 \in \overline{A}$.
        - At $x = \sqrt{2} \notin \mathbb{Q}$: Any $[a, b) \in \mathcal{C}$ containing $\sqrt{2}$ satisfies $a < \sqrt{2} < b$, so $[a, b) \cap (0, \sqrt{2}) \supseteq (\max(0, a), \sqrt{2}) \neq \varnothing$. Thus $\sqrt{2} \in \overline{A}$.
        - Hence $\overline{A}_{\mathcal{T}_{\mathcal{C}}} = [0, \sqrt{2}]$.
    <2>3. **For $B = (\sqrt{2}, 3)$:**
        - At $x = \sqrt{2} \notin \mathbb{Q}$: Any $[a, b) \in \mathcal{C}$ containing $\sqrt{2}$ satisfies $a < \sqrt{2} < b$, so $[a, b) \cap (\sqrt{2}, 3) \supseteq (\sqrt{2}, \min(b, 3)) \neq \varnothing$. Thus $\sqrt{2} \in \overline{B}$.
        - At $x = 3 \in \mathbb{Q}$: The basic set $[3, 4) \in \mathcal{C}$ contains $3$ and is disjoint from $(\sqrt{2}, 3)$, so $3 \notin \overline{B}$.
        - Hence $\overline{B}_{\mathcal{T}_{\mathcal{C}}} = [\sqrt{2}, 3)$.

<1>4. Conclusion:
    - In $\mathbb{R}_\ell$: $\overline{A} = [0, \sqrt{2})$ and $\overline{B} = [\sqrt{2}, 3)$.
    - In $\mathcal{T}_{\mathcal{C}}$: $\overline{A} = [0, \sqrt{2}]$ and $\overline{B} = [\sqrt{2}, 3)$. Q.E.D.
:::
