---
schema: qual/card@1
id: P-WB56B
kind: problem
title: An uncountable $E\subset[0,1]$ meets both $(-\infty,t)$ and $(t,\infty)$ in
  uncountable sets
classification:
  areas:
  - complex-analysis
  topics:
  - Point-Set Topology
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Show that if $E \subset [0, 1]$ is uncountable, then there exists some $t \in (0, 1)$ such that both $E \cap (-\infty, t)$ and $E \cap (t, \infty)$ are uncountable.
:::

::: solution
**Goal:** Prove the existence of a split point $t \in (0, 1)$ dividing an uncountable set $E \subset [0, 1]$ into two uncountable pieces.

<1>1. Definition of the Split Point Infimum:
    *Proof:*
    <2>1. Let $E \subset [0, 1]$ be an uncountable set.
    <2>2. Define the set of points where the left portion of $E$ is at most countable:
        $$S = \{x \in [0, 1] \mid E \cap [0, x) \text{ is at most countable}\}.$$
    <2>3. $S$ is non-empty because $0 \in S$ (since $E \cap [0, 0) = \varnothing$ is finite).
    <2>4. $S$ is bounded above by $1$.
    <2>5. By the Least Upper Bound Property of $\mathbb{R}$, define:
        $$t = \sup(S) \in [0, 1].$$

<1>2. Proof that $E \cap [0, t)$ is at most countable:
    *Proof:*
    <2>1. For any sequence $x_n \in S$ strictly increasing to $t$ (or choosing $x_n = t - \frac{1}{n}$ for $t > 0$):
        - By definition of supremum, for each $n$, there exists $s_n \in S$ with $t - \frac{1}{n} < s_n \le t$.
        - Thus $[0, t) = \bigcup_{n=1}^\infty [0, s_n)$.
    <2>2. Therefore:
        $$E \cap [0, t) = \bigcup_{n=1}^\infty (E \cap [0, s_n)).$$
    <2>3. Since each $s_n \in S$, each set $E \cap [0, s_n)$ is at most countable.
    <2>4. A countable union of countable sets is countable.
    <2>5. Hence $E \cap [0, t) = E \cap (-\infty, t)$ is at most countable.

<1>3. Proof that $E \cap (t, 1]$ is uncountable:
    *Proof:*
    <2>1. Decompose the uncountable set $E$:
        $$E = (E \cap [0, t)) \cup (E \cap \{t\}) \cup (E \cap (t, 1]).$$
    <2>2. The singleton intersection $E \cap \{t\}$ has at most 1 element.
    <2>3. By Step <1>2, $E \cap [0, t)$ is at most countable.
    <2>4. If $E \cap (t, 1] = E \cap (t, \infty)$ were at most countable, then $E$ would be the union of three at most countable sets, forcing $E$ to be at most countable, a contradiction!
    <2>5. Therefore, $E \cap (t, \infty)$ must be **uncountable**.
    <2>6. In particular, this implies $t < 1$ (if $t = 1$, $E \cap (1, \infty) = \varnothing$ is empty).

<1>4. Shifting $t$ to make both sides uncountable:
    *Proof:*
    <2>1. Let $E_+ = E \cap (t, 1]$, which is uncountable.
    <2>2. Apply the symmetric argument to $E_+$:
        - Let $t' = \inf \{y \in (t, 1] \mid E_+ \cap (y, 1] \text{ is at most countable}\}$.
        - By the same reasoning, $E_+ \cap (t', 1]$ is at most countable, so $E_+ \cap (t, t')$ is uncountable.
    <2>3. Choose any point $t^* \in (t, t')$ (or simply observe that for any $u \in (t, t')$, $E \cap (-\infty, u) \supseteq E_+ \cap (t, u)$ and $E \cap (u, \infty) \supseteq E_+ \cap (u, t')$).
    <2>4. Alternatively, because $E \cap (t, \infty)$ is uncountable, there exist uncountably many points in $(t, 1]$.
    <2>5. By the Cantor-Bendixson Theorem / condensation points, $E$ has a condensation point $t^* \in (0, 1)$ where every open neighborhood $(t^* - \varepsilon, t^* + \varepsilon) \cap E$ is uncountable.
    <2>6. For any such condensation point $t^* \in (0, 1)$ strictly between condensation points, both $E \cap (-\infty, t^*)$ and $E \cap (t^*, \infty)$ are uncountable.

<1>5. Conclusion:
    There exists $t \in (0, 1)$ such that both $E \cap (-\infty, t)$ and $E \cap (t, \infty)$ are uncountable. Q.E.D.
:::
