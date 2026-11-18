---
schema: qual/card@1
id: E-HAT-3.3-34
kind: problem
title: Poincaré duality diagram for manifolds with boundary
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 34; the stored statement matches the current online text and diagram where applicable.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 34; it matches the printed text. The card writes $[M,\partial M]\frown-$ where the print abbreviates the same relative fundamental class as $[M]\frown-$; the diagram is otherwise transcribed as printed.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the diagram square by square: the middle square is naturality of the cap product, and the
    outer ones follow from the chain-level identity
    $\partial(c\frown\varphi)=(\partial c)\frown\varphi\pm c\frown\delta\varphi$ together with
    $\partial[M,\partial M]=[\partial M]$, the sign being left to the conventions as the exercise
    allows.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    The card left the signs to "the chosen cap and connecting-map conventions", which is exactly the
    part of the exercise that has content. The two outer squares are now computed from Hatcher's
    chain identity p.240 in the form $\partial(c\frown\varphi)=(-1)^\ell(\partial c\frown\varphi
    -c\frown\delta\varphi)$: the third square commutes up to $(-1)^k$, and the first exactly, once a
    cochain on the boundary is extended through the collar. The middle square is now justified by
    both sides being the same chain-level product rather than by the word "naturality". Not verified:
    the sign of the relative cap product forms, which is taken from p.240 and not recomputed.
- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    The cochain extension in the first square formerly claimed to come from a retraction of M onto
    its boundary. No such retraction exists by Exercise 32 for compact M with nonempty boundary.
    It is replaced by the algebraic extension singular cohomology always provides: C_*(boundary M)
    is free on a subset of the singular-simplex basis of C_*(M), so define Psi by psi on that subset
    and zero on the remaining simplices. Then Psi restricts to psi and its coboundary is relative
    because psi is a cocycle. The sign computations are unchanged.

- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps. No retained solution set covers this exercise, so the
    argument is the card's own and the card says so. Checked against Hatcher, Section 3.3
    Exercise 34, printed p. 264, and against the cap product formula of p. 240, which the retained
    text prints with the sign $(-1)^\ell$ exactly as used here. Each step re-read: the two rows are
    the long exact sequences of the pair $(M,\partial M)$; the middle square commutes with no sign
    because both composites are the class of the same chain $c\frown\Psi$; the third square
    commutes up to $(-1)^k$, the only sign in the diagram; the first square commutes because a
    cocycle on $\partial M$ extends to a cochain on $M$ vanishing off $\partial M$, so the
    connecting map is carried to $i_*$ up to the boundary term. Not claimed: that the diagram
    commutes with no sign at all, which the exercise does not ask and which the $(-1)^k$ of the
    third square contradicts; nor any statement for coefficients other than a commutative ring.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Page correction to the note above, which cited the exercise one page off (or, for the Section 4
    cards, carried over the Section 4.1 page). The exercise is printed on p. 260 of Hatcher,
    Algebraic Topology (2002), checked against the retained PDF text at PDF p. 269, whose running
    folio reads 260. The solution section now states the corrected page; the mathematics is
    unchanged.
---

::: {.problem}
For a compact manifold $M$ verify that the following diagram relating Poincaré duality for $M$ and $\partial M$ is commutative, up to sign at least:

$$
\begin{array}{ccccccc}
H^{k-1}(\partial M;R)&\longrightarrow&H^k(M,\partial M;R)&\longrightarrow&H^k(M;R)&\longrightarrow&H^k(\partial M;R)\\
\downarrow{[\partial M]\frown-}&&\downarrow{[M,\partial M]\frown-}&&\downarrow{[M,\partial M]\frown-}&&\downarrow{[\partial M]\frown-}\\
H_{n-k}(\partial M;R)&\longrightarrow&H_{n-k}(M;R)&\longrightarrow&H_{n-k}(M,\partial M;R)&\longrightarrow&H_{n-k-1}(\partial M;R)
\end{array}
$$
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on the card, and none of the retained Hatcher sets solves this exercise. It is checked against Hatcher, Algebraic Topology, Section 3.3 Exercise 34, printed p. 260, and against the cap product formulas of pp. 239--240, in particular
$$
\partial(\sigma\frown\varphi)=(-1)^{\ell}\bigl(\partial\sigma\frown\varphi-\sigma\frown\delta\varphi\bigr)
$$
for $\sigma$ of degree $k$ and $\varphi$ of degree $\ell$. The exercise asks for commutativity "up to sign at least", which is what is proved.

::: pf

::: {.pf-step #rows}
The top row is the cohomology long exact sequence of the pair $(M,\partial M)$ and the bottom row is its homology long exact sequence, shifted by the dimension.

::: pf-proof
For the pair $(M,\partial M)$ the cohomology sequence reads
$$
\cdots\to H^{k-1}(\partial M;R)\xrightarrow{\delta}H^{k}(M,\partial M;R)\xrightarrow{j^{*}}H^{k}(M;R)\xrightarrow{i^{*}}H^{k}(\partial M;R)\to\cdots ,
$$
where $j^{*}$ and $i^{*}$ are induced by the inclusions and $\delta$ is the connecting homomorphism. The homology sequence reads
$$
\cdots\to H_{n-k}(\partial M;R)\xrightarrow{i_{*}}H_{n-k}(M;R)\xrightarrow{q}H_{n-k}(M,\partial M;R)\xrightarrow{\partial_{*}}H_{n-k-1}(\partial M;R)\to\cdots ,
$$
with $q$ the map induced by the quotient $C_{*}(M)\to C_{*}(M,\partial M)$. These are the two rows displayed.
:::

:::

::: {.pf-step #middle}
The middle square commutes exactly: for $\psi\in H^{k}(M,\partial M;R)$ one has $q\bigl([M,\partial M]\frown\psi\bigr)=[M,\partial M]\frown j^{*}\psi$.

::: pf-proof
Let $c\in C_{n}(M;R)$ be a relative cycle representing $[M,\partial M]$, so $\partial c$ lies in $C_{n-1}(\partial M;R)$ and represents $[\partial M]$. Take $\psi$ represented by a relative cocycle $\Psi$ vanishing on chains in $\partial M$. The relative cap product $H_{n}(M,\partial M)\times H^{k}(M,\partial M)\to H_{n-k}(M)$ of p. 240 gives the class of $c\frown\Psi$ in $H_{n-k}(M)$; applying $q$ computes the same chain class modulo $C_{n-k}(\partial M)$, that is, the class of $c\frown\Psi$ in $H_{n-k}(M,\partial M)$. On the other hand $j^{*}\psi$ is represented by the same cochain $\Psi$, now regarded as an absolute cocycle on $M$ (it is a cocycle because $\delta\Psi$ vanishes on $M$), and $[M,\partial M]\frown j^{*}\psi$ is again the class of $c\frown\Psi$. Both composites therefore give one and the same class, so the square commutes with no sign.
:::

:::

::: {.pf-step #outer}
The two outer squares commute up to sign.

:::: pf-proof

::: {.pf-step #third}
The third square commutes up to the sign $(-1)^{k}$: for $\varphi\in H^{k}(M;R)$, $[\partial M]\frown i^{*}\varphi=(-1)^{k}\partial_{*}\bigl([M,\partial M]\frown\varphi\bigr)$.

::: pf-proof
Represent $\varphi$ by a cocycle, again written $\varphi$, and $[M,\partial M]$ by the relative cycle $c$. The identity above with $\ell=k$ gives
$$
\partial(c\frown\varphi)=(-1)^{k}\bigl(\partial c\frown\varphi-c\frown\delta\varphi\bigr)=(-1)^{k}\,\partial c\frown\varphi ,
$$
because $\delta\varphi=0$. The chain $\partial c$ lies in $C_{n-1}(\partial M;R)$ and represents $[\partial M]$, and the values of $\varphi$ on its faces are the values of $i^{*}\varphi$, so $\partial c\frown\varphi$ represents $[\partial M]\frown i^{*}\varphi$. The left-hand side is, by definition of the connecting map $\partial_{*}$, the class $\partial_{*}$ applied to the class of $c\frown\varphi$, which is $[M,\partial M]\frown\varphi$. Hence the two sides agree up to $(-1)^{k}$.
:::

:::

::: {.pf-step #first}
The first square commutes: for $\psi\in H^{k-1}(\partial M;R)$, $[M,\partial M]\frown\delta\psi=i_{*}\bigl([\partial M]\frown\psi\bigr)$, with the sign absorbed in the connecting homomorphism.

::: pf-proof
Represent $\psi$ by a cocycle on $\partial M$ and extend it to a cochain $\Psi$ on $M$ by $\Psi(\sigma)=\psi(\sigma)$ for singular simplices whose image lies in $\partial M$ and $\Psi(\sigma)=0$ otherwise; this is a cochain because those simplices form part of a basis of $C_{*}(M;R)$, so no retraction $M\to\partial M$ is needed. Then $\Psi$ restricts to $\psi$, and $\delta\Psi$ vanishes on chains in $\partial M$ because $\psi$ is a cocycle, so $\delta\Psi$ is a relative cocycle representing $\delta\psi$. The identity with $\ell=k-1$ gives
$$
\partial(c\frown\Psi)=(-1)^{k-1}\bigl(\partial c\frown\Psi-c\frown\delta\Psi\bigr),
\qquad\text{that is}\qquad
c\frown\delta\Psi=\partial c\frown\Psi-(-1)^{k-1}\partial(c\frown\Psi).
$$
In $H_{n-k}(M;R)$ the second term is a boundary, and $\partial c\frown\Psi=\partial c\frown\psi$ because $\Psi$ extends $\psi$; so the class of $c\frown\delta\Psi$ is $i_{*}\bigl([\partial M]\frown\psi\bigr)$, which is the assertion.
:::

:::

:::

:::

::: {.pf-step}
The displayed diagram commutes up to sign, which is the exercise's assertion.

::: pf-proof
The rows are the exact sequences of step [](#rows){.pf-ref}; the middle square commutes exactly by step [](#middle){.pf-ref}; and the outer squares commute up to sign by step [](#outer){.pf-ref}, the only sign being $(-1)^{k}$ in the third square. Hence the diagram commutes up to sign, as required.
:::

:::

:::
:::
