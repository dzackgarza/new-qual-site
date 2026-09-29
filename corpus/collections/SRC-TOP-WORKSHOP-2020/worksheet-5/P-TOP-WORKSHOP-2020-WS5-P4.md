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

::: pf

::: {.pf-step #s1}

If $X$ is locally connected, every component $C$ of an open set $U$ is open.

::: pf-proof

Let $x \in C$. Since $U$ is a neighborhood of $x$, local connectedness gives a connected neighborhood $V$ of $x$ with $V \subseteq U$. As $V$ is a connected subset of $U$ containing $x$, it lies in the component $C$ of $x$. So $C$ is a neighborhood of each of its points, hence open.

:::

:::

::: {.pf-step #s2}

If every component of every open set is open, $X$ is locally connected.

::: pf-proof

Let $x \in X$ and let $U$ be a neighborhood of $x$; replacing $U$ by its interior, assume $U$ is open. The component $C$ of $U$ containing $x$ is open by hypothesis and connected, and $C \subseteq U$, so $C$ is a connected neighborhood of $x$ inside $U$.

**(b).**

:::

:::

::: {.pf-step #s3}

For an open set $V \subseteq Y$ and a component $C$ of $V$, the set $p^{-1}(C)$ is a union of components of $p^{-1}(V)$.

::: pf-proof

If $K$ is a component of $p^{-1}(V)$, then $p(K)$ is a connected subset of $V$, so it lies in a single component of $V$. Hence $K \subseteq p^{-1}(C)$ whenever $K$ meets $p^{-1}(C)$, and $p^{-1}(C)$ is the union of the components $K$ that meet it.

:::

:::

::: {.pf-step #s4}

Every component $C$ of an open set $V \subseteq Y$ is open in $Y$.

::: pf-proof

$p^{-1}(V)$ is open because $p$ is continuous, so its components are open by step [](#s1){.pf-ref} applied to the locally connected space $X$. By step [](#s3){.pf-ref}, $p^{-1}(C)$ is a union of open sets, hence open. Since $p$ is a quotient map, $C$ is open in $Y$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} prove (a). Step [](#s4){.pf-ref} and step [](#s2){.pf-ref} applied to $Y$ prove (b).

:::

:::

:::
