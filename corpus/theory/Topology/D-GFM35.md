---
schema: qual/card@1
id: D-GFM35
kind: definition
title: Simply connected space
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Homotopy
  - Connectedness
relations: []
review: draft
---

::: {.definition}
A topological space $X$ is \dfn{simply connected} if $X$ is [[D-X73EB|path connected]] and the [[D-EBNUE|fundamental group]] $\pi_1(X, x_0)$ is trivial for every $x_0\in X$.
:::

::: {.proposition}
For a path connected space $X$, the following are equivalent:

(i) $X$ is simply connected;

(ii) every continuous map $\gamma\colon S^1\to X$ is [[D-Z7I7F|homotopic]] to a constant map;

(iii) every continuous map $\gamma\colon S^1\to X$ extends to a continuous map $\hat\gamma\colon D^2\to X$, that is, $\hat\gamma|_{S^1} = \gamma$;

(iv) any two [[D-J6XOC|paths]] $p_1, p_2\colon[0,1]\to X$ with $p_1(0) = p_2(0)$ and $p_1(1) = p_2(1)$ are homotopic rel endpoints.
:::

::: {.concept}
See [@Hat02, §1.1, Proposition 1.6 and Exercise 5].
:::
