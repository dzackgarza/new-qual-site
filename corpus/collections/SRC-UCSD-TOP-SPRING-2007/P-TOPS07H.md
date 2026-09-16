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
<1>1. $\pi_1(X) = 1$.
::: {.proof}
the suspension of a path-connected space is simply connected (the two cones are contractible and their intersection is $M$, which is path-connected, so van Kampen gives the trivial group).
:::

<1>2. $H_0(X) = \ZZ$.
::: {.proof}
$X$ is path-connected.
:::

<1>3. $H_1(X) = 0$.
::: {.proof}
$H_1(X) \cong H_0(M)$ by the suspension isomorphism, and $H_0(M) = \ZZ$; more precisely $\widetilde H_{n+1}(\Sigma M) \cong \widetilde H_n(M)$, so $H_1(X) \cong \widetilde H_0(M) = 0$.
:::

<1>4. $H_2(X) = 0$.
::: {.proof}
$H_2(X) \cong \widetilde H_1(M) = 0$ (since $M$ is a homology sphere, $\widetilde H_1(M) = 0$).
:::

<1>5. $H_3(X) = 0$.
::: {.proof}
$H_3(X) \cong \widetilde H_2(M) = 0$ (homology sphere).
:::

<1>6. $H_4(X) = \ZZ$.
::: {.proof}
$H_4(X) \cong \widetilde H_3(M) = \ZZ$ (homology sphere).
:::

<1>7. Hence $X$ has the homology of $S^4$ and trivial fundamental group.
::: {.proof}
<1>1–<1>6.
:::

<1>8. $X$ is homotopy equivalent to $S^4$.
::: {.proof}
The suspension of the closed $3$-manifold $M$ has CW type, and <1>1 shows it is simply connected. The degree-$2$ Hurewicz theorem gives $\pi_2(X)\cong H_2(X)=0$. Thus $X$ is $2$-connected, so Hurewicz in degree $3$ gives $\pi_3(X)\cong H_3(X)=0$. Hence $X$ is $3$-connected, and Hurewicz now gives an isomorphism
$$
\pi_4(X)\xrightarrow{\cong}H_4(X)\cong\ZZ.
$$
Choose $f:S^4\to X$ representing a class mapping to a generator of $H_4(X)$. Then $f_*$ is an isomorphism on $H_4$; it is also an isomorphism on $H_0$, and all homology groups in degrees $1,2,3$ and above $4$ vanish on both spaces. Thus $f$ is a homology equivalence between simply connected CW complexes. The homological Whitehead theorem therefore implies that $f$ is a homotopy equivalence.
:::

<1>9. Q.E.D.
::: {.proof}
<1>7 and <1>8.
:::
:::
