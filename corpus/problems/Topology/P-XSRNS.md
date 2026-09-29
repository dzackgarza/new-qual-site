---
schema: qual/card@1
id: P-XSRNS
kind: problem
title: Homology of two $2$-spheres glued along their equators
classification:
  areas:
  - topology
  topics:
  - Homology
  - Mayer-Vietoris
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
- Show that if $X = S^2 \disjoint_{\id} S^2$ is a pushout along the equators, then $H_n(X) = [\ZZ, 0, \ZZ^3, 0, \cdots]$.
:::

::: {.solution}

::: pf

::: pf-step

$X$ is the union of two copies of $S^2$ glued along a common equator $S^1$.

::: pf-proof

the pushout of two $S^2$'s along their equators (identified by the identity map).

:::

:::

::: pf-step

Give the equator and both spheres compatible CW structures, so that the common equator $S^1$ is a subcomplex of each sphere. Let $A$ and $B$ denote the two sphere subcomplexes of $X$. Then $A\cap B=S^1$ and $A\cup B=X$.

::: pf-proof

Take the usual CW structure on $S^2$ obtained from an equatorial $S^1$ by attaching one $2$-cell along each side. After identifying the two equators, the images of the two spheres and their common equator are CW subcomplexes of the pushout.

:::

:::

::: pf-step

The cellular chain complexes fit into a short exact sequence
$$
0\longrightarrow C_*(S^1)\xrightarrow{(i_*,-j_*)}C_*(S^2)\oplus C_*(S^2)\longrightarrow C_*(X)\longrightarrow0,
$$
and hence give the Mayer–Vietoris long exact sequence
$$\cdots \to H_n(S^1) \to H_n(S^2) \oplus H_n(S^2) \to H_n(X) \to H_{n-1}(S^1) \to \cdots.$$

::: pf-proof

For CW subcomplexes $A,B$ with $X=A\cup B$, the cellular chain groups satisfy
$$0\to C_*(A\cap B)\to C_*(A)\oplus C_*(B)\to C_*(X)\to0,$$
because each cell of $X$ lies in $A$ or $B$, and a cell occurring in both lies in $A\cap B$. The associated long exact sequence in homology is the cellular Mayer–Vietoris sequence displayed above.

:::

:::

::: {.pf-step #s4}

$H_0(X) = \ZZ$.

::: pf-proof

$X$ is connected.

:::

:::

::: {.pf-step #s5}

$H_1(X) = 0$.

::: pf-proof

::: pf-step

The relevant part is $H_1(S^1) \to H_1(S^2) \oplus H_1(S^2) \to H_1(X) \to H_0(S^1) \to H_0(S^2) \oplus H_0(S^2)$.

::: pf-proof

Mayer–Vietoris in low degrees.

:::

:::

::: pf-step

$H_1(S^2) = 0$, and the map $H_0(S^1) \to H_0(S^2) \oplus H_0(S^2)$ is injective (both inclusions induce the identity on $H_0$).

::: pf-proof

$H_0(S^1) = \ZZ$ and $H_0(S^2) = \ZZ$, with the map $\ZZ \to \ZZ \oplus \ZZ$ given by $1 \mapsto (1,1)$, which is injective.

:::

:::

::: pf-step

Hence $H_1(X) = 0$.

::: pf-proof

exactness: $H_1(X) \to H_0(S^1)$ is injective (kernel is image of $H_1(S^2) \oplus H_1(S^2) = 0$), and its image is the kernel of $H_0(S^1) \to H_0(S^2) \oplus H_0(S^2)$, which is $0$ (since that map is injective); so $H_1(X) = 0$.

:::

:::

:::

:::

::: {.pf-step #s6}

$H_2(X) = \ZZ^3$.

::: pf-proof

::: pf-step

The relevant part is $H_2(S^1) \to H_2(S^2) \oplus H_2(S^2) \to H_2(X) \to H_1(S^1) \to H_1(S^2) \oplus H_1(S^2)$.

::: pf-proof

Mayer–Vietoris.

:::

:::

::: pf-step

$H_2(S^1) = 0$ and $H_1(S^2) = 0$.

::: pf-proof

standard.

:::

:::

::: pf-step

Hence $0 \to \ZZ \oplus \ZZ \to H_2(X) \to \ZZ \to 0$ is exact.

::: pf-proof

$H_2(S^2) \oplus H_2(S^2) = \ZZ \oplus \ZZ$ and $H_1(S^1) = \ZZ$.

:::

:::

::: pf-step

Therefore $H_2(X) \cong \ZZ^3$.

::: pf-proof

the short exact sequence $0 \to \ZZ^2 \to H_2(X) \to \ZZ \to 0$ splits (the last term is free), so $H_2(X) \cong \ZZ^2 \oplus \ZZ = \ZZ^3$.

:::

:::

:::

:::

::: {.pf-step #s7}

$H_n(X) = 0$ for $n \ge 3$.

::: pf-proof

$H_n(S^1) = H_n(S^2) = 0$ for $n \ge 3$, so the Mayer–Vietoris sequence gives $H_n(X) = 0$.

:::

:::

::: pf-qed

$H_0 = \ZZ$, $H_1 = 0$, $H_2 = \ZZ^3$, $H_n = 0$ for $n \ge 3$ (steps [](#s4){.pf-ref}, [](#s5){.pf-ref}, [](#s6){.pf-ref} and [](#s7){.pf-ref}).

:::

:::

:::
