---
schema: qual/card@1
id: E-IIK8L
kind: exercise
title: Closures in the ordered square
classification:
  areas:
  - topology
  topics:
  - Closure
  - Order Topology
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: {.exercise}
Determine the **closures** of the following subsets of the **ordered square** $I_o^2 = [0, 1] \times [0, 1]$ equipped with the dictionary order topology:

$$
A = \left\{ \frac{1}{n} \times 0 \;\middle|\; n \in \mathbb{Z}_+ \right\},
$$

$$
B = \left\{ \left(1 - \frac{1}{n}\right) \times \frac{1}{2} \;\middle|\; n \in \mathbb{Z}_+ \right\},
$$

$$
C = \{ x \times 0 \mid 0 < x < 1 \},
$$

$$
D = \left\{ x \times \frac{1}{2} \;\middle|\; 0 < x < 1 \right\},
$$

$$
E = \left\{ \frac{1}{2} \times y \;\middle|\; 0 < y < 1 \right\}.
$$
:::

::: solution
**Goal:** Determine the closure $\overline{S}$ for each subset in the dictionary order topology on $I_o^2 = [0, 1] \times [0, 1]$.

<1>1. Basis for the Dictionary Order Topology on $I_o^2$:
    *Proof:*
    <2>1. The dictionary order on $I \times I$ is defined by $(x_1, y_1) < (x_2, y_2) \iff x_1 < x_2 \text{ or } (x_1 = x_2 \text{ and } y_1 < y_2)$.
    <2>2. Open intervals $((a, b), (c, d))$ form a basis:
        - If $a = c$, the interval is a vertical open segment in the single fiber: $\{a\} \times (b, d)$.
        - If $a < c$, the interval consists of $\{a\} \times (b, 1] \cup (a, c) \times [0, 1] \cup \{c\} \times [0, d)$.
    <2>3. In particular, for any point $(x, y)$, a basic neighborhood either lies within the vertical fiber $\{x\} \times (y - \epsilon, y + \epsilon)$ (if $0 < y < 1$), or if $y = 0$, reaches down to the top of the preceding fibers: $(x - \epsilon, x) \times (1 - \delta, 1] \cup \{x\} \times [0, \epsilon)$.

<1>2. Closure of $A = \{ (1/n) \times 0 \mid n \in \mathbb{Z}_+ \}$:
    *Proof:*
    <2>1. The sequence $x_n = 1/n$ decreases to $0$: $1/n > 0$.
    <2>2. As $n \to \infty$, $(1/n, 0)$ approaches $(0, 1)$ from the right!
    <2>3. Specifically, any open interval containing $(0, 1)$, such as $[(0, 0), (0, 1)] \cup ((0, 1), (c, d)) = [0 \times 0, c \times d)$ with $c > 0$, contains all points $(1/n, 0)$ for all $n > 1/c$.
    <2>4. On the other hand, $(0, 0)$ has neighborhood $[0 \times 0, 0 \times \epsilon)$ which contains no points of $A$.
    <2>5. Thus $(0, 1)$ is the only limit point of $A$.
    <2>6. Therefore:
        $$\overline{A} = A \cup \{ (0, 1) \} = \left\{ \frac{1}{n} \times 0 \;\middle|\; n \in \mathbb{Z}_+ \right\} \cup \{ (0, 1) \}.$$

<1>3. Closure of $B = \{ (1 - 1/n) \times \frac{1}{2} \mid n \in \mathbb{Z}_+ \}$:
    *Proof:*
    <2>1. The sequence $x_n = 1 - 1/n$ increases to $1$ from the left: $x_n < 1$.
    <2>2. As $n \to \infty$, any neighborhood of $(1, 0)$ contains an interval $((1 - \epsilon, 1), (1, \delta)) = (1 - \epsilon, 1) \times (0, 1] \cup \{1\} \times [0, \delta)$.
    <2>3. For large $n$, $1 - 1/n > 1 - \epsilon$, so $(1 - 1/n, 1/2) \in (1 - \epsilon, 1) \times (0, 1]$.
    <2>4. Thus $(1, 0)$ is the unique limit point of $B$.
    <2>5. Therefore:
        $$\overline{B} = B \cup \{ (1, 0) \} = \left\{ \left(1 - \frac{1}{n}\right) \times \frac{1}{2} \;\middle|\; n \in \mathbb{Z}_+ \right\} \cup \{ (1, 0) \}.$$

<1>4. Closure of $C = \{ x \times 0 \mid 0 < x < 1 \}$:
    *Proof:*
    <2>1. For any fixed $x_0 \in (0, 1]$, the point $(x_0, 0)$ is approached by $x \to x_0$ from the right, while the point $(x_0, 1)$ is approached by points $(x, 0)$ with $x < x_0$ (since $(x, 0) < (x_0, 1)$).
    <2>2. But the points $(x, y)$ with $0 < y < 1$ are isolated from $C$: $\{x\} \times (0, 1)$ is open and disjoint from $C$ except at $y = 0$.
    <2>3. The limit points of $C$ are $x \times 0$ for $x \in [0, 1]$ and $x \times 1$ for $x \in [0, 1)$.
    <2>4. Thus:
        $$\overline{C} = C \cup \{ 0 \times 0, 1 \times 0 \} \cup \{ x \times 1 \mid 0 \le x < 1 \} = ([0, 1] \times \{0\}) \cup ([0, 1) \times \{1\}).$$

<1>5. Closure of $D = \{ x \times \frac{1}{2} \mid 0 < x < 1 \}$:
    *Proof:*
    <2>1. In the interior of each fiber $0 < x < 1$, $\{x\} \times (0, 1)$ is open and contains only the single point $(x, 1/2)$ of $D$.
    <2>2. The only limit points arise at the boundaries of the fibers:
        - As $x \to x_0^-$ (from the left), $(x, 1/2) \to (x_0, 0)$ for all $x_0 \in (0, 1]$.
        - As $x \to x_0^+$ (from the right), $(x, 1/2) \to (x_0, 1)$ for all $x_0 \in [0, 1)$.
    <2>3. Thus:
        $$\overline{D} = D \cup ((0, 1] \times \{0\}) \cup ([0, 1) \times \{1\}).$$

<1>6. Closure of $E = \{ \frac{1}{2} \times y \mid 0 < y < 1 \}$:
    *Proof:*
    <2>1. The set $E$ is the open vertical line segment within the single fiber $x = 1/2$.
    <2>2. In the subspace topology on the fiber $\{1/2\} \times [0, 1]$, the topology is simply the standard Euclidean interval topology.
    <2>3. The limit points within this fiber are the endpoints $(1/2, 0)$ and $(1/2, 1)$.
    <2>4. No points in other fibers $x \ne 1/2$ are limit points of $E$.
    <2>5. Thus:
        $$\overline{E} = \left\{ \frac{1}{2} \right\} \times [0, 1].$$

<1>7. Conclusion:
    - $\overline{A} = A \cup \{ (0, 1) \}$
    - $\overline{B} = B \cup \{ (1, 0) \}$
    - $\overline{C} = ([0, 1] \times \{0\}) \cup ([0, 1) \times \{1\})$
    - $\overline{D} = D \cup ((0, 1] \times \{0\}) \cup ([0, 1) \times \{1\})$
    - $\overline{E} = \{1/2\} \times [0, 1]$. Q.E.D.
:::
