---
schema: qual/card@1
id: E-SMI-8000E-MT2
kind: exercise
title: PIDs have unique factorization
classification:
  areas:
  - algebra
  topics:
  - Principal Ideal Domains
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.exercise}
(a) Prove every principal ideal domain $R$ has "unique factorization".

(b) Give an example of a ring with unique factorization that is not a principal ideal domain.
(You do not have to prove it.)
:::

::: {.solution}
**(a).**

<1>1. Let $R$ be a PID. First, $R$ is Noetherian.
::: {.proof}
every ideal is principal, hence finitely generated.
:::

<1>2. Every nonzero nonunit $a \in R$ factors into a product of irreducibles.
::: {.proof}
if $a$ is not irreducible, write $a = bc$ with $b, c$ nonunits; iterating, the ascending chain of ideals $(a) \subsetneq (b) \subsetneq \cdots$ must terminate (Noetherian, <1>1), so the process stops at irreducibles.
:::

<1>3. Irreducibles in a PID are prime.
::: {.proof}
if $p$ is irreducible and $p \mid ab$, then $(p)$ is maximal (since $R$ is a PID and $p$ irreducible implies $(p)$ is maximal among proper principal ideals, hence maximal), so $R/(p)$ is a field, hence an integral domain, so $p$ is prime.
:::

<1>4. Uniqueness: if $a = p_1 \cdots p_m = q_1 \cdots q_n$ are two factorizations into irreducibles, then $p_1$ divides some $q_j$ (since $p_1$ is prime), and by induction the factorizations agree up to order and units.
::: {.proof}
<1>3 and the standard induction.
:::

<1>5. Hence $R$ has unique factorization.
::: {.proof}
<1>2 and <1>4.
:::

**(b).**

<1>1. $\mathbb{Z}[x]$ is a UFD but not a PID.
::: {.proof}
$\mathbb{Z}[x]$ is a UFD (Gauss's lemma), but the ideal $(2, x)$ is not principal.
:::

<1>2. Q.E.D.
::: {.proof}
<1>5 (a) and <1>1 (b).
:::
:::
