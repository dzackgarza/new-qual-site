---
schema: qual/card@1
id: P-APAS20B
kind: problem
title: Singular values and Frobenius perturbation bound $\dim\ker(\phi+\psi)$
classification:
  areas:
  - applied-algebra
  topics:
  - Singular Values
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the two parts already on the card, whose numerical
    content is correct: for k = 2 the min--max bound is sigma_9^2 + sigma_10^2 = 4 + 1 = 5 > 1 =
    ||psi||_F^2. Added: the Cauchy-interlacing (min--max) derivation of the k-dimensional bound,
    which the card quoted without proof; the reason ||psi||_F^2 >= ||psi u||^2 for a unit
    vector; and in (b) the chain of equalities written out with the identification sigma_10^2 as
    the least eigenvalue of phi*phi, plus the observation that psi u != 0 is what makes the rank
    exactly 1 rather than at most 1. No statement was changed. Not claimed: a retained solution
    set; the collection's provenance is the examination paper only.
---

::: {.problem}
Suppose $\CC^{10}$ has its usual inner product and $\phi,\psi\colon\CC^{10}\to\CC^{10}$ are two linear maps.
Suppose that the singular values of $\phi$ are given by $\sigma_i(\phi)=11-i$ for $1\le i\le 10$; i.e.,
$$
\sigma_1(\phi)=10,\ \sigma_2(\phi)=9,\ \sigma_3(\phi)=8,\ \ldots,\ \sigma_{10}(\phi)=1;
$$
and that the Frobenius norm $\norm{\psi}_{\mathrm{Frob}}$ is exactly $1$.

(a) Show that $\dim\ker(\phi+\psi)\le 1$.

(b) Show that if $\dim\ker(\phi+\psi)=1$ then $\psi$ has rank $1$.
:::

::: {.solution}
Throughout $\phi, \psi\colon\CC^{10} \to \CC^{10}$ are linear, $\sigma_{1}(\phi) \ge \cdots \ge \sigma_{10}(\phi)$ are the singular values with $\sigma_{i}(\phi) = 11 - i$, so $\sigma_{9} = 2$ and $\sigma_{10} = 1$, $\norm{\psi}_{\mathrm{Frob}}^{2} = \sum_{j}\norm{\psi e_{j}}^{2}$ for any orthonormal basis, and $K \coloneqq \ker(\phi+\psi)$. The collection's `provenance` is the Spring 2020 preliminary examination, and no solutions sheet accompanies it, so the argument below is the card's own.

::: pf

::: {.pf-step #kydim}
For every $k$-dimensional subspace $S$ with orthonormal basis $u_{1},\ldots,u_{k}$, $\sum_{j=1}^{k}\norm{\phi u_{j}}^{2} \ge \sigma_{11-k}(\phi)^{2} + \cdots + \sigma_{10}(\phi)^{2}$.

::: pf-proof
Let $A \coloneqq \phi^{*}\phi$, whose eigenvalues are $\sigma_{1}^{2} \ge \cdots \ge \sigma_{10}^{2}$ in some orthonormal eigenbasis. For the compression $A_{S} \coloneqq P_{S}A\restriction_{S}$ one has $\sum_{j}\norm{\phi u_{j}}^{2} = \operatorname{tr}A_{S}$, and Cauchy interlacing for compressions gives that the $j$-th largest eigenvalue of $A_{S}$ is at least the $(j + 10 - k)$-th largest eigenvalue of $A$, that is $\sigma_{j+10-k}^{2}$. Summing over $j = 1,\ldots,k$ gives the displayed bound; this is the min--max principle in the form that a $k$-dimensional subspace captures at least the $k$ smallest singular values.

:::

:::

::: {.pf-step #a}
(a) $\dim K \le 1$.

::: pf-proof
Suppose $\dim K \ge 2$ and choose orthonormal $u_{1}, u_{2} \in K$. Since $\phi u_{j} = -\psi u_{j}$ for $u_{j} \in K$, one has $\norm{\psi u_{j}} = \norm{\phi u_{j}}$, so $\norm{\psi}_{\mathrm{Frob}}^{2} \ge \norm{\psi u_{1}}^{2} + \norm{\psi u_{2}}^{2} = \norm{\phi u_{1}}^{2} + \norm{\phi u_{2}}^{2}$. Applying step [](#kydim){.pf-ref} with $k = 2$ gives $\norm{\phi u_{1}}^{2} + \norm{\phi u_{2}}^{2} \ge \sigma_{9}^{2} + \sigma_{10}^{2} = 4 + 1 = 5$, so $\norm{\psi}_{\mathrm{Frob}}^{2} \ge 5 > 1$, contradicting $\norm{\psi}_{\mathrm{Frob}} = 1$.

:::

:::

::: {.pf-step #b-chain}
(b) If $\dim K = 1$ and $u$ is a unit vector in $K$ then $1 = \norm{\psi}_{\mathrm{Frob}}^{2} = \norm{\psi u}^{2} = \norm{\phi u}^{2} = \sigma_{10}(\phi)^{2}$.

::: pf-proof
The inequality $\norm{\psi}_{\mathrm{Frob}}^{2} \ge \norm{\psi u}^{2}$ holds because $u$ is a unit vector and the Frobenius norm is the sum of the squared norms of the images of the members of any orthonormal basis, so it dominates each term; $\norm{\psi u} = \norm{\phi u}$ as in step [](#a){.pf-ref}; and $\norm{\phi u}^{2} = \langle\phi^{*}\phi u, u\rangle \ge \sigma_{10}^{2} = 1$ because $\sigma_{10}^{2}$ is the least eigenvalue of $\phi^{*}\phi$. The chain begins and ends at $1$, so every term equals $1$.

:::

:::

::: {.pf-step #b}
(b) If $\dim K = 1$ then $\operatorname{rank}\psi = 1$.

::: pf-proof
Extend the unit $u$ of step [](#b-chain){.pf-ref} to an orthonormal basis $u, u_{2}, \ldots, u_{10}$. Then $1 = \norm{\psi}_{\mathrm{Frob}}^{2} = \norm{\psi u}^{2} + \sum_{j \ge 2}\norm{\psi u_{j}}^{2}$, and $\norm{\psi u}^{2} = 1$ by step [](#b-chain){.pf-ref}, so every $\psi u_{j} = 0$ with $j \ge 2$; hence $\psi$ vanishes on $u^{\perp}$ and $\operatorname{rank}\psi \le 1$. Moreover $\psi u = -\phi u \ne 0$, since $\norm{\phi u}^{2} = 1$; so the image of $\psi$ is one-dimensional and $\operatorname{rank}\psi = 1$.

:::

:::

:::
:::
