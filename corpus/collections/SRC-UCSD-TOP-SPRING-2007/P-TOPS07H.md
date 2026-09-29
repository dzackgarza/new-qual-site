---
schema: qual/card@1
id: P-TOPS07H
kind: problem
title: "Suspension of a homology 3-sphere is homotopy equivalent to S^4"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Suspensions
  - Homotopy Type
  - Manifolds
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
Let $M^3$ be a homology sphere — a closed $3$-manifold having the same homology groups as $S^3$ — and let $X = \Sigma M$ be its suspension.
What are the fundamental group and homology groups of $X$?
Show that $X$ is homotopy equivalent to $S^4$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

$\pi_1(X) = 1$.

::: pf-proof

the suspension of a path-connected space is simply connected (the two cones are contractible and their intersection is $M$, which is path-connected, so van Kampen gives the trivial group).

:::

:::

::: {.pf-step #s2}

$H_0(X) = \ZZ$.

::: pf-proof

$X$ is path-connected.

:::

:::

::: {.pf-step #s3}

$H_1(X) = 0$.

::: pf-proof

$H_1(X) \cong H_0(M)$ by the suspension isomorphism, and $H_0(M) = \ZZ$; more precisely $\widetilde H_{n+1}(\Sigma M) \cong \widetilde H_n(M)$, so $H_1(X) \cong \widetilde H_0(M) = 0$.

:::

:::

::: {.pf-step #s4}

$H_2(X) = 0$.

::: pf-proof

$H_2(X) \cong \widetilde H_1(M) = 0$ (since $M$ is a homology sphere, $\widetilde H_1(M) = 0$).

:::

:::

::: {.pf-step #s5}

$H_3(X) = 0$.

::: pf-proof

$H_3(X) \cong \widetilde H_2(M) = 0$ (homology sphere).

:::

:::

::: {.pf-step #s6}

$H_4(X) = \ZZ$.

::: pf-proof

$H_4(X) \cong \widetilde H_3(M) = \ZZ$ (homology sphere).

:::

:::

::: {.pf-step #s7}

Hence $X$ has the homology of $S^4$ and trivial fundamental group.

::: pf-proof

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref}, [](#s5){.pf-ref} and [](#s6){.pf-ref}.

:::

:::

::: {.pf-step #s8}

$X$ is homotopy equivalent to $S^4$.

::: pf-proof

The suspension of the closed $3$-manifold $M$ has CW type, and step [](#s1){.pf-ref} shows it is simply connected. The degree-$2$ Hurewicz theorem gives $\pi_2(X)\cong H_2(X)=0$. Thus $X$ is $2$-connected, so Hurewicz in degree $3$ gives $\pi_3(X)\cong H_3(X)=0$. Hence $X$ is $3$-connected, and Hurewicz now gives an isomorphism
$$
\pi_4(X)\xrightarrow{\cong}H_4(X)\cong\ZZ.
$$
Choose $f:S^4\to X$ representing a class mapping to a generator of $H_4(X)$. Then $f_*$ is an isomorphism on $H_4$; it is also an isomorphism on $H_0$, and all homology groups in degrees $1,2,3$ and above $4$ vanish on both spaces. Thus $f$ is a homology equivalence between simply connected CW complexes. The homological Whitehead theorem therefore implies that $f$ is a homotopy equivalence.

:::

:::

::: pf-qed

Steps [](#s7){.pf-ref} and [](#s8){.pf-ref}.

:::

:::

:::
