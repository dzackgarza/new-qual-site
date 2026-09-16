---
schema: qual/card@1
id: PR-DIVZEROPOLE
kind: proposition
title: Zeros and poles of a rational function
classification:
  areas:
  - algebraic-geometry
  topics:
  - Divisors
  - Discrete Valuation Rings
  - Normal Schemes
relations:
- kind: uses
  target: D-5PQ5W
- kind: uses
  target: D-QJ5M9
review: draft
prompts:
- Why does a rational function on an integral Noetherian scheme have only finitely many zeros and poles?
- Why is a rational function with no poles on a normal Noetherian scheme regular?
---

Let $X$ be an integral Noetherian scheme with function field $K$.
For a prime divisor $Y \subseteq X$ with generic point $\eta_Y$ such that $\OO_{X, \eta_Y}$ is a discrete valuation ring with valuation $v_Y$, a function $t \in K^\times$ has a \dfn{zero} along $Y$ if $v_Y(t) > 0$ and a \dfn{pole} along $Y$ if $v_Y(t) < 0$.

::: {.proposition}
1. A Noetherian topological space has finitely many irreducible components.

2. For $t \in K^\times$, there are only finitely many codimension-one points $y \in X$ with $t \notin \OO_{X,y}^\times$.

3. If $X$ is regular in codimension one, then $\div t = \sum_Y v_Y(t)\, Y$ is a finite sum, hence a Weil divisor.

4. If $X$ is normal, then $t \in K$ has no poles if and only if $t \in \OO_X(X)$.
:::

<1>1. A Noetherian topological space $T$ is a finite union of irreducible closed subsets, hence has finitely many irreducible components.

::: {.proof}
Suppose not, and let $\mathcal{S}$ be the set of closed subsets of $T$ that are not finite unions of irreducible closed subsets.
By the descending chain condition $\mathcal{S}$ has a minimal element $Z$.
$Z$ is not irreducible, so $Z = Z_1 \cup Z_2$ with $Z_1, Z_2 \subsetneq Z$ closed; by minimality both are finite unions of irreducible closed subsets, and so is $Z$, a contradiction.
If $T = T_1 \cup \cdots \cup T_r$ with $T_i$ irreducible and closed, every irreducible component of $T$ is contained in, hence equal to, some $T_i$.
:::

<1>2. For $t \in K^\times$, only finitely many codimension-one points $y$ have $t \notin \OO_{X,y}^\times$.

::: {.proof}
Cover $X$ by finitely many affine opens $\Spec A$ with $A$ a Noetherian domain and write $t = f/g$ with $f, g \in A \setminus \{0\}$.
If $t \notin \OO_{X,\mathfrak{p}}^\times$ at a height-one prime $\mathfrak{p}$ of $A$, then $f \in \mathfrak{p}$ or $g \in \mathfrak{p}$.
A height-one prime containing $f \neq 0$ is minimal over $(f)$, since $(0) \subsetneq \mathfrak{q} \subseteq \mathfrak{p}$ forces $\mathfrak{q} = \mathfrak{p}$, so it is the generic point of an irreducible component of $V(f) = \Spec A/(f)$.
By step <1>1 applied to the Noetherian space $\Spec A/(f)$, there are finitely many, and likewise for $g$.
:::

<1>3. If $X$ is regular in codimension one, $\div t$ is a Weil divisor.

::: {.proof}
Each local ring at a codimension-one point is a regular local ring of dimension one, hence a discrete valuation ring, so $v_Y(t)$ is defined, and $v_Y(t) \neq 0$ exactly when $t$ is not a unit of $\OO_{X, \eta_Y}$; by step <1>2 this happens for finitely many $Y$.
:::

<1>4. If $X$ is normal and $t$ has no poles, then $t \in \OO_X(X)$.

::: {.proof}
A normal Noetherian local ring of dimension one is a discrete valuation ring, so $v_Y$ is defined for every prime divisor $Y$.
On an affine open $\Spec A$, $A$ is a Noetherian integrally closed domain, and $A = \bigcap_{\operatorname{ht} \mathfrak{p} = 1} A_{\mathfrak{p}}$ inside $K$.
If $t$ has no poles, then $t \in A_{\mathfrak{p}}$ for every height-one prime, so $t \in A$.
These elements agree on overlaps as elements of $K$, so they glue to a section of $\OO_X$ over $X$.
Conversely a regular function has $v_Y(t) \geq 0$ for every $Y$.
:::
