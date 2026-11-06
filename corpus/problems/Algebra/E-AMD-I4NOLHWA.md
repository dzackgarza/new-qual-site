---
schema: qual/card@1
id: E-AMD-I4NOLHWA
kind: problem
title: Groups of order 10
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Groups
  - Sylow Theory
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-06
  note: >-
    Rewritten as a Lamport structured proof. What was checked: the statement (a
    classification, no repair needed), and the existing prose solution against a
    fresh re-derivation: n_5 divides 2 and is 1 mod 5, so n_5 = 1 and P is normal,
    P = C_5; P cap Q = 1 and |PQ| = 10 so G = P x| Q; Aut(C_5) = (Z/5)^x = C_4 and
    a homomorphism from Q = C_2 is determined by the image of its nontrivial
    element, an element of order dividing 2, so there are exactly two actions,
    trivial and inversion; the trivial one gives C_5 x C_2 = C_10, the inversion one
    gives the dihedral presentation with s r s = r^{-1}, i.e. D_5, and the two are
    distinguished by abelianness. Correct. The prose did not justify that there are
    exactly two homomorphisms, nor that C_5 x C_2 is C_10; both are now steps. No
    source solution is retained for this card, so no source comparison was made.
    What was not checked: any printed source.
---

::: {.exercise}
Classify all groups of order 10.
:::

::: {.solution}
Let $G$ be a group with $\abs{G}=10=2\cdot5$, and let $P$ be a Sylow $5$-subgroup and $Q$ a Sylow $2$-subgroup.

::: pf

::: {.pf-step #sylow}
$P\trianglelefteq G$ and $P\cong C_5$; also $Q\cong C_2$.

::: pf-proof
By the Sylow theorems the number $n_5$ of Sylow $5$-subgroups satisfies $n_5\mid\abs{G}$ and $n_5\equiv1\pmod 5$, so $n_5\mid 2$ with $n_5\in\{1,6,11,\ldots\}$, leaving $n_5=1$; a unique Sylow $p$-subgroup is normal, so $P\trianglelefteq G$. A group of prime order $5$ is cyclic, so $P\cong C_5$, and likewise $Q\cong C_2$.
:::

:::

::: {.pf-step #product}
$P\cap Q=1$ and $PQ=G$, so $G\cong P\rtimes Q$ with respect to the conjugation action of $Q$ on $P$.

::: pf-proof
$P\cap Q$ is a subgroup of both $P$ and $Q$, so its order divides $\gcd(5,2)=1$, giving $P\cap Q=1$. The product set $PQ$ has $\abs{P}\abs{Q}/\abs{P\cap Q}=5\cdot2=10$ elements, hence is all of $G$. Because $P$ is normal, $PQ$ is a subgroup, and a group that is the product of a normal subgroup and a complement is the semidirect product $P\rtimes Q$ with the action given by conjugation.
:::

:::

::: {.pf-step #actions}
$\Aut(P)\cong C_4$ and there are exactly two homomorphisms $Q\to\Aut(P)$: the trivial one and the one sending the nontrivial element of $Q$ to inversion.

::: pf-proof
Every automorphism of $C_5$ is determined by the image of a generator, which must be another generator, so $\Aut(C_5)\cong(\ZZ/5\ZZ)^\times$, a group of order $4$, cyclic. A homomorphism $Q\to\Aut(P)$ is determined by the image of the nontrivial element $t\in Q$, whose order is $2$; the image must have order dividing $2$, so it is the identity or the unique element of order $2$ in the cyclic group $C_4$, which acts on $C_5$ by inversion $x\mapsto x^{-1}$.
:::

:::

::: {.pf-step #two}
The two actions give $C_{10}$ and $D_5$, which are not isomorphic, so there are exactly two groups of order $10$.

::: pf-proof
With the trivial action, conjugation by $Q$ is trivial, so $G\cong P\times Q\cong C_5\times C_2$, and since $\gcd(5,2)=1$ this is cyclic of order $10$, that is $C_{10}$. With the nontrivial action, $G=\generators{P,t}$ where $t$ generates $Q$ and $t$ acts by inversion, so $G$ has the presentation $\generators{r,s\mid r^5=s^2=1,\ srs=r^{-1}}$ with $r$ a generator of $P$ and $s=t$: that is the dihedral group of order $10$, written $D_5$. These two are not isomorphic, since $C_{10}$ is abelian while $D_5$ is not ($srs^{-1}=r^{-1}\neq r$ for $r\neq1$). Every group of order $10$ falls into one of the two cases by steps [](#product){.pf-ref} and [](#actions){.pf-ref}, so the groups of order $10$ are exactly $C_{10}$ and $D_5$.
:::

:::

:::
:::
