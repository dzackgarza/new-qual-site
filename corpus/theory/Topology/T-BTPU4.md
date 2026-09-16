---
schema: qual/card@1
id: T-BTPU4
kind: theorem
title: Seifert--van Kampen theorem
classification:
  areas:
  - topology
  topics:
  - van Kampen
  - Fundamental Group
relations: []
review: draft
---

::: {.theorem}
Let $X = U_{1} \union U_{2}$, where $U_1$, $U_2$ and $U_1\intersect U_2$ are open, path-connected and nonempty, and let $x_0 \in U_1\intersect U_2$.
Let $\iota_k\colon \pi_1(U_1\intersect U_2, x_0)\to\pi_1(U_k, x_0)$, $k = 1, 2$, be induced by the inclusions.
Then the inclusions $U_1, U_2\injects X$ induce an isomorphism
$$
\pi_{1}(U_1, x_0) \ast_{\pi_{1}(U_1 \intersect U_2, x_0)} \pi_{1}(U_2, x_0) \xrightarrow{\ \sim\ } \pi_{1}(X, x_0)
$$
onto $\pi_1(X, x_0)$ from the [[D-WSFYS|free product with amalgamation]], which is the [[D-5S7PK|pushout]] of $\pi_1(U_1, x_0)\xleftarrow{\iota_1}\pi_1(U_1\intersect U_2, x_0)\xrightarrow{\iota_2}\pi_1(U_2, x_0)$ in the category of groups [@Hat02].
:::

::: {.proposition}
In the situation of the theorem, suppose
$$
\pi_{1}(U_1, x_0) = \left\langle u_{1}, \ldots, u_{k} \suchthat \alpha_{1}, \ldots, \alpha_{l}\right\rangle, \qquad
\pi_{1}(U_2, x_0) = \left\langle v_{1}, \ldots, v_{m} \suchthat \beta_{1}, \ldots, \beta_{n}\right\rangle,
$$
and that $w_1, \ldots, w_p$ generate $\pi_1(U_1\intersect U_2, x_0)$.
Then
$$
\pi_{1}(X, x_0) \cong \left\langle u_{1}, \ldots, u_{k}, v_{1}, \ldots, v_{m} \suchthat \alpha_{1}, \ldots, \alpha_{l},\ \beta_{1}, \ldots, \beta_{n},\ \iota_1(w_{1}) \iota_2(w_{1})^{-1}, \ldots, \iota_1(w_{p}) \iota_2(w_{p})^{-1} \right\rangle
$$
[@Hat02].
:::

::: {.remark}
The hypothesis that $U_1 \intersect U_2$ is path-connected is necessary: for $S^1$ covered by two open arcs, the intersection has two components, both arcs are simply connected, and $\pi_1(S^1)\cong\ZZ$.
:::

![Example of a pushout of spaces](../../assets/Topology/figures/image_2020-06-01-00-07-39.png)
