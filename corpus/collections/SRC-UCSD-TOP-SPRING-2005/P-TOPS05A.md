---
schema: qual/card@1
id: P-TOPS05A
kind: problem
title: "Free Z/2 action on S^{2n} is the antipodal map; covering spaces of S^{2n}"
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Group Actions
  - Spheres
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
(a) Let $G$ be a group of homeomorphisms of $S^{2n}$ such that for all $g \in G$, $gx = x$ if and only if $g = 1$.
Prove if $G$ has $2$ elements, then one of them is the antipodal map.

(b) If $S^{2n} \to X$ is a covering space, prove $X$ is homeomorphic to $S^{2n}$ or $\mathbb{RP}^{2n}$.
:::

::: {.solution}
<1>1. Part (a): Degree of a fixed-point-free involution on $S^{2n}$:
<2>1. Let $G = \{1, \tau\}$ be a group of homeomorphisms of $S^{2n}$ acting freely, so $\tau(x) \neq x$ for all $x \in S^{2n}$ and $\tau^2 = \operatorname{id}$.
::: {.proof}
hypothesis.
:::
<2>2. The homology groups of $S^{2n}$ are $H_0(S^{2n}; \mathbb{Q}) \cong \mathbb{Q}$, $H_{2n}(S^{2n}; \mathbb{Q}) \cong \mathbb{Q}$, and $H_k(S^{2n}; \mathbb{Q}) = 0$ for $0 < k < 2n$.
::: {.proof}
homology of spheres.
:::
<2>3. The Lefschetz number of $\tau$ is:
\[
\Lambda(\tau) = \sum_{k=0}^{2n} (-1)^k \operatorname{Tr}\big(\tau_* |_{H_k(S^{2n})}\big) = \operatorname{Tr}\big(\tau_* |_{H_0}\big) + (-1)^{2n} \operatorname{Tr}\big(\tau_* |_{H_{2n}}\big) = 1 + \deg(\tau).
\]
::: {.proof}
Lefschetz trace formula.
:::
<2>4. By the Lefschetz Fixed Point Theorem, since $\tau$ has no fixed points on $S^{2n}$, $\Lambda(\tau) = 0$.
Therefore:
\[
1 + \deg(\tau) = 0 \implies \deg(\tau) = -1.
\]
This matches the degree of the standard antipodal map $a(x) = -x$, which has degree $(-1)^{2n+1} = -1$.
::: {.proof}
Lefschetz Fixed Point Theorem.
:::

<1>2. Part (b): Classification of covering spaces of $S^{2n}$:
<2>1. Let $p: S^{2n} \to X$ be a covering map.
For $n \ge 1$, $S^{2n}$ is simply connected ($\pi_1(S^{2n}) = 0$), so $S^{2n}$ is the universal covering space of $X$.
::: {.proof}
$\pi_1(S^k) = 0$ for $k \ge 2$.
:::
<2>2. The deck transformation group $G = \operatorname{Deck}(S^{2n}/X) \cong \pi_1(X)$ acts freely on $S^{2n}$, and $X \cong S^{2n}/G$.
::: {.proof}
classification of covering spaces by deck groups.
:::
<2>3. By Part (a), every non-identity element $g \in G \setminus \{1\}$ acts without fixed points, so $\deg(g) = -1$.
::: {.proof}
Lefschetz Fixed Point Theorem applied to $g$.
:::
<2>4. The degree map $\deg: G \to \{\pm 1\}$ is a group homomorphism.
If $|G| \ge 3$, there exist two distinct non-identity elements $g_1 \neq g_2 \in G \setminus \{1\}$.
Then $g_1 g_2^{-1} \neq 1$, so $\deg(g_1 g_2^{-1}) = -1$.
However, by the homomorphism property:
\[
\deg(g_1 g_2^{-1}) = \deg(g_1) \deg(g_2)^{-1} = (-1)(-1) = 1,
\]
which is a contradiction.
Thus $|G| \le 2$.
::: {.proof}
degree homomorphism properties.
:::
<2>5. We have two cases for the order of $G$:
- If $|G| = 1$, then $G = \{1\}$, so $X \cong S^{2n}/\{1\} \cong S^{2n}$.
- If $|G| = 2$, then $G = \{1, \tau\}$ is a free $\mathbb{Z}_2$-action, so $X = S^{2n}/\{1, \tau\} \cong \mathbb{RP}^{2n}$.
::: {.proof}
quotient of $S^{2n}$ by a free involution.
:::

<1>3. Conclusion:
Any covering space of $S^{2n}$ is homeomorphic to $S^{2n}$ or $\mathbb{RP}^{2n}$. Q.E.D.
::: {.proof}
<1>1 and <1>2.
:::
:::
