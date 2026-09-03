---
schema: qual/card@1
id: E-HYC1G
kind: problem
title: Topology coherent with an increasing sequence of closed subspaces
classification:
  areas:
  - topology
  topics:
  - Normal Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}

Let $X_1 \subset X_2 \subset \cdots$ be a sequence of spaces, where $X_i$ is a closed subspace of $X_{i+1}$ for each $i$.
Let $X$ be the union of the $X_i$; let us topologize $X$ by declaring a set $U$ to be open in $X$ if $U \cap X_i$ is open in $X_i$ for each $i$.

(a) Show that this is a topology on $X$ and that each space $X_i$ is a subspace (in fact, a closed subspace) of $X$ in this topology.
This topology is called the topology coherent with the subspaces $X_i$.

(b) Show that $f: X \to Y$ is continuous if $f \mid X_i$ is continuous for each $i$.

(c) Show that if each space $X_i$ is normal, then $X$ is normal.
[Hint: Given disjoint closed sets $A$ and $B$ in $X$, set $f$ equal to 0 on $A$ and 1 on $B$, and extend $f$ successively to $A \cup B \cup X_i$ for $i = 1, 2, \ldots$.]
:::

::: {.solution}
<1>1. Part (a): Topology axioms and closed subspaces:
<2>1. **Topology axioms:**
- $\emptyset \cap X_i = \emptyset$ and $X \cap X_i = X_i$ are open in $X_i$ for all $i$, so $\emptyset, X \in \mathcal{T}$.
- If $\{U_\alpha\}$ are open, $(\bigcup U_\alpha) \cap X_i = \bigcup (U_\alpha \cap X_i)$ is open in $X_i$.
- If $U, V$ are open, $(U \cap V) \cap X_i = (U \cap X_i) \cap (V \cap X_i)$ is open in $X_i$.
Thus $\mathcal{T}$ is a topology on $X$.
::: {.proof}
set-theoretic distribution of intersections over unions.
:::
<2>2. **Closed sets in $X$:**
A subset $F \subseteq X$ is closed in $X$ if and only if $F \cap X_i$ is closed in $X_i$ for all $i \ge 1$.
::: {.proof}
complement $X \setminus F$ is open $\iff (X \setminus F) \cap X_i = X_i \setminus (F \cap X_i)$ is open in $X_i$.
:::
<2>3. **$X_k$ is a closed subspace of $X$:**
For any fixed $k \ge 1$ and all $i \ge 1$:
- If $i \le k$, $X_k \cap X_i = X_i$, which is closed in $X_i$.
- If $i > k$, $X_k$ is closed in $X_{k+1} \subset \cdots \subset X_i$, so $X_k \cap X_i = X_k$ is closed in $X_i$.
Thus $X_k \cap X_i$ is closed in $X_i$ for every $i$, so $X_k$ is closed in $X$.
Furthermore, the subspace topology on $X_k$ coincides with its original topology.
::: {.proof}
transitivity of closed subspaces.
:::

<1>2. Part (b): Continuity criterion for coherent topology:
<2>1. Let $f: X \to Y$ be a map and $V \subseteq Y$ an open set.
Then $f^{-1}(V) \cap X_i = (f|_{X_i})^{-1}(V)$ for all $i \ge 1$.
::: {.proof}
definition of preimage.
:::
<2>2. By the definition of the coherent topology:
\[
f^{-1}(V) \text{ is open in } X \iff \forall i \ge 1, \, (f|_{X_i})^{-1}(V) \text{ is open in } X_i.
\]
Thus $f$ is continuous on $X$ if and only if $f|_{X_i}: X_i \to Y$ is continuous for all $i \ge 1$.
::: {.proof}
characterization of continuity via preimages of open sets.
:::

<1>3. Part (c): Normality of $X$:
<2>1. Singletons $\{x\}$ are closed in $X$ because if $x \in X_i$, $\{x\}$ is closed in the $T_1$ space $X_i$, and $X_i$ is closed in $X$.
::: {.proof}
$T_1$ property from normality of $X_i$.
:::
<2>2. Let $A, B \subset X$ be disjoint closed subsets of $X$ ($A \cap B = \emptyset$).
Construct a sequence of continuous functions $f_n: X_n \to [0, 1]$ satisfying $f_n|_{A \cap X_n} = 0$, $f_n|_{B \cap X_n} = 1$, and $f_{n+1}|_{X_n} = f_n$ by induction:
- **Base step ($n = 1$):** $A \cap X_1$ and $B \cap X_1$ are disjoint closed sets in the normal space $X_1$. By Urysohn’s Lemma, there exists a continuous $f_1: X_1 \to [0, 1]$ with $f_1(A \cap X_1) = 0$ and $f_1(B \cap X_1) = 1$.
- **Inductive step:** Given $f_n: X_n \to [0, 1]$, let $C = X_n \cup (A \cap X_{n+1}) \cup (B \cap X_{n+1})$.
  Define $g: C \to [0, 1]$ by $g = f_n$ on $X_n$, $g = 0$ on $A \cap X_{n+1}$, and $g = 1$ on $B \cap X_{n+1}$.
  $g$ is well-defined and continuous on the closed set $C \subset X_{n+1}$ by the Pasting Lemma.
  Since $X_{n+1}$ is normal, by the Tietze Extension Theorem $g$ extends to a continuous function $f_{n+1}: X_{n+1} \to [0, 1]$.
::: {.proof}
Tietze Extension Theorem on normal spaces.
:::
<2>3. Define $f: X \to [0, 1]$ by $f(x) = f_n(x)$ for $x \in X_n$.
$f$ is well-defined since $f_{n+1}|_{X_n} = f_n$, and by Part (b), $f$ is continuous on $X$.
Moreover, $f(A) = 0$ and $f(B) = 1$.
::: {.proof}
Part (b) applied to $f$.
:::
<2>4. The sets $U = f^{-1}([0, 1/3))$ and $V = f^{-1}((2/3, 1])$ are disjoint open neighborhoods of $A$ and $B$ in $X$.
Thus $X$ is normal.
::: {.proof}
continuous separation of disjoint closed sets.
:::

<1>4. Conclusion:
$(X, \mathcal{T})$ is a topological space, $f: X \to Y$ is continuous iff $f|_{X_i}$ is continuous for all $i$, and $X$ is normal. Q.E.D.
::: {.proof}
<1>1 through <1>3.
:::
:::
