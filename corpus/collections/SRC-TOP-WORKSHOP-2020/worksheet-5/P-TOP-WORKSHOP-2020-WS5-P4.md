---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS5-P4
kind: problem
title: Local connectedness is equivalent to open components, and is preserved by quotient maps
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Quotient Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
(May 2013) A space is locally connected if for each point $x\in X$ and every neighborhood $U$ of $x$, there is a connected neighborhood $V$ of $x$ contained in $U$.

(a) Prove that $X$ is locally connected if and only if for every open set $U$ of $X$, each connected component of $U$ is open in $X$.

(b) Prove that if $p\colon X\to Y$ is a quotient map and $X$ is locally connected, then $Y$ is locally connected.
:::

::: {.solution}
**(a).**

<1>1. ($\Rightarrow$) Suppose $X$ is locally connected, and let $U$ be open with a component $C$ of $U$.
Proof: setup.

<1>2. For $x \in C$, local connectedness gives a connected neighborhood $V$ of $x$ with $V \subseteq U$.
Proof: definition of local connectedness.

<1>3. Since $C$ is the component of $U$ containing $x$, $V \subseteq C$.
Proof: <1>2 (a connected subset of $U$ containing $x$ lies in the component $C$).

<1>4. Hence $C$ is a neighborhood of each of its points, so $C$ is open.
Proof: <1>3.

<1>5. ($\Leftarrow$) Suppose every component of every open set is open, and let $x \in X$ with a neighborhood $U$ of $x$.
Proof: setup.

<1>6. Let $C$ be the component of $U$ containing $x$; then $C$ is open (by hypothesis) and connected, and $C \subseteq U$.
Proof: <1>5 and the hypothesis.

<1>7. Hence $X$ is locally connected.
Proof: <1>6.

**(b).**

<1>1. Let $V \subseteq Y$ be open, and let $C$ be a component of $V$.
Proof: setup.

<1>2. $p^{-1}(V)$ is open in $X$, and its components are open (by (a), since $X$ is locally connected).
Proof: <1>1 and (a).

<1>3. $p^{-1}(C)$ is a union of components of $p^{-1}(V)$.
Proof: $p^{-1}(C)$ is a union of connected components of $p^{-1}(V)$ (each component of $p^{-1}(V)$ maps into a single component of $V$).

<1>4. Hence $p^{-1}(C)$ is open in $X$.
Proof: <1>2 and <1>3.

<1>5. Since $p$ is a quotient map, $C$ is open in $Y$ (a set is open in $Y$ iff its preimage is open in $X$).
Proof: <1>4 and the definition of quotient map.

<1>6. Hence every component of every open set in $Y$ is open, so $Y$ is locally connected (by (a)).
Proof: <1>5 and (a).

<1>7. Q.E.D.
Proof: <1>4, <1>7 (a) and <1>6 (b).
:::
