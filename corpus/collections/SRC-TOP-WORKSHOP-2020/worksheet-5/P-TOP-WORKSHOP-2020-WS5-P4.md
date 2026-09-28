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

<1>1. If $X$ is locally connected, every component $C$ of an open set $U$ is open.
::: {.proof}
Let $x \in C$. Since $U$ is a neighborhood of $x$, local connectedness gives a connected neighborhood $V$ of $x$ with $V \subseteq U$. As $V$ is a connected subset of $U$ containing $x$, it lies in the component $C$ of $x$. So $C$ is a neighborhood of each of its points, hence open.
:::

<1>2. If every component of every open set is open, $X$ is locally connected.
::: {.proof}
Let $x \in X$ and let $U$ be a neighborhood of $x$; replacing $U$ by its interior, assume $U$ is open. The component $C$ of $U$ containing $x$ is open by hypothesis and connected, and $C \subseteq U$, so $C$ is a connected neighborhood of $x$ inside $U$.
:::

**(b).**

<1>3. For an open set $V \subseteq Y$ and a component $C$ of $V$, the set $p^{-1}(C)$ is a union of components of $p^{-1}(V)$.
::: {.proof}
If $K$ is a component of $p^{-1}(V)$, then $p(K)$ is a connected subset of $V$, so it lies in a single component of $V$. Hence $K \subseteq p^{-1}(C)$ whenever $K$ meets $p^{-1}(C)$, and $p^{-1}(C)$ is the union of the components $K$ that meet it.
:::

<1>4. Every component $C$ of an open set $V \subseteq Y$ is open in $Y$.
::: {.proof}
$p^{-1}(V)$ is open because $p$ is continuous, so its components are open by step <1>1 applied to the locally connected space $X$. By step <1>3, $p^{-1}(C)$ is a union of open sets, hence open. Since $p$ is a quotient map, $C$ is open in $Y$.
:::

<1>5. Q.E.D.
::: {.proof}
Steps <1>1 and <1>2 prove (a). Step <1>4 and step <1>2 applied to $Y$ prove (b).
:::
:::
