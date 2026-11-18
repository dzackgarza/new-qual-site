---
schema: qual/card@1
id: P-TOP-WORKSHOP-D9-06
kind: problem
title: Homology of a wedge sum by Mayer--Vietoris
classification:
  areas:
  - topology
  topics:
  - Mayer-Vietoris
  - Homology
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Use the Meyer-Vietoris sequence to calculate the homology of $X\vee Y$.
:::

::: {.solution}

The argument is the card's own: the reduced Mayer–Vietoris sequence for the cover by the two halves has contractible intersection, so the direct sum sits in the middle.

::: pf

::: {.pf-step #cover}

There are open $U,V\subset X\vee Y$ with $U\simeq X$, $V\simeq Y$ and $U\cap V$ contractible.

::: pf-proof

Assume, as the standard hypothesis for a wedge, that the wedge point $x_{0}$ has an open neighbourhood $N_{X}\subset X$ deformation retracting onto $x_{0}$ and an open neighbourhood $N_{Y}\subset Y$ deformation retracting onto $x_{0}$. Take $U=X\cup N_{Y}$ and $V=Y\cup N_{X}$: each is open, $U\cup V=X\vee Y$, $U$ deformation retracts onto $X$ and $V$ onto $Y$, and $U\cap V=N_{X}\cup N_{Y}$ deformation retracts onto $x_{0}$, hence is contractible. For CW complexes wedged at $0$-cells such neighbourhoods exist.

:::

:::

::: {.pf-step #mv}

The reduced Mayer–Vietoris sequence gives $\widetilde H_{n}(X\vee Y)\cong\widetilde H_{n}(U)\oplus\widetilde H_{n}(V)$ for every $n$.

::: pf-proof

The reduced sequence for the cover $U,V$ is
$$
\cdots\to\widetilde H_{n}(U\cap V)\to\widetilde H_{n}(U)\oplus\widetilde H_{n}(V)\to\widetilde H_{n}(X\vee Y)\to\widetilde H_{n-1}(U\cap V)\to\cdots
$$
By step [](#cover){.pf-ref} $U\cap V$ is contractible, so its reduced homology vanishes in every degree. The exact sequence therefore has zero at both ends of the displayed stretch, which says precisely that the middle map is an isomorphism for every $n$.

:::

:::

::: {.pf-step #homotopy}

$\widetilde H_{n}(U)\oplus\widetilde H_{n}(V)\cong\widetilde H_{n}(X)\oplus\widetilde H_{n}(Y)$.

::: pf-proof

A deformation retraction is a homotopy equivalence, and homotopic maps induce equal maps on homology; hence the inclusions $X\to U$ and $Y\to V$ induce isomorphisms $\widetilde H_{n}(X)\cong\widetilde H_{n}(U)$ and $\widetilde H_{n}(Y)\cong\widetilde H_{n}(V)$ for all $n$.

:::

:::

::: {.pf-step #conclusion}

$\widetilde H_{n}(X\vee Y)\cong\widetilde H_{n}(X)\oplus\widetilde H_{n}(Y)$ for all $n$.

::: pf-proof

Composing steps [](#mv){.pf-ref} and [](#homotopy){.pf-ref},
$$
\boxed{\widetilde H_{n}(X\vee Y)\cong\widetilde H_{n}(X)\oplus\widetilde H_{n}(Y)\quad\text{for all } n.}
$$
In particular, if $X$ and $Y$ are path connected then $H_{0}(X\vee Y)\cong\ZZ$ and $H_{n}(X\vee Y)\cong H_{n}(X)\oplus H_{n}(Y)$ for $n\ge1$.

:::

:::

:::

:::
