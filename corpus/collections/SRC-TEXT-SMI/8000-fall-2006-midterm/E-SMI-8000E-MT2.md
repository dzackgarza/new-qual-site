---
schema: qual/card@1
id: E-SMI-8000E-MT2
kind: problem
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

::: pf

::: {.pf-step #s1}

Let $R$ be a PID. Then $R$ is Noetherian.

::: pf-proof

Every ideal of $R$ is principal, hence finitely generated.

:::

:::

::: {.pf-step #s2}

Every nonzero nonunit $a \in R$ is a product of irreducibles.

::: pf-proof

Let $\mathcal S$ be the set of principal ideals $(a)$ with $a$ a nonzero nonunit that is not a product of irreducibles, and suppose $\mathcal S$ is nonempty. By step [](#s1){.pf-ref}, $\mathcal S$ has a maximal element $(a)$. The element $a$ is not irreducible, so $a = bc$ with $b, c$ nonzero nonunits. Then $(a) \subsetneq (b)$ and $(a) \subsetneq (c)$, so by maximality $b$ and $c$ are products of irreducibles. Hence so is $a = bc$, a contradiction.

:::

:::

::: {.pf-step #s3}

Irreducibles in a PID are prime.

::: pf-proof

Let $p$ be irreducible. If $(p) \subseteq (d)$, then $p = dx$ for some $x \in R$, so $d$ or $x$ is a unit; that is, $(d) = R$ or $(d) = (p)$. Since every ideal of $R$ is principal and $p$ is a nonunit, $(p)$ is a maximal ideal. Hence $R/(p)$ is a field, in particular an integral domain, so $p$ is prime.

:::

:::

::: {.pf-step #s4}

If $p_1 \cdots p_m = q_1 \cdots q_n$ with all $p_i, q_j$ irreducible, then $m = n$ and, after reordering, $q_i = u_i p_i$ with each $u_i$ a unit.

::: pf-proof

Induct on $m$. If $m = 0$, then $q_1 \cdots q_n = 1$, so $n = 0$ because irreducibles are nonunits. If $m \ge 1$, then $p_1$ divides $q_1 \cdots q_n$ and is prime by step [](#s3){.pf-ref}, so $p_1 \mid q_j$ for some $j$; reorder so that $j = 1$. Since $q_1$ is irreducible and $p_1$ is a nonunit, $q_1 = u_1 p_1$ with $u_1$ a unit. Cancelling $p_1$ in the domain $R$ gives $p_2 \cdots p_m = (u_1 q_2) q_3 \cdots q_n$ with $u_1 q_2$ irreducible, and the induction hypothesis applies.

:::

:::

::: {.pf-step #s5}

$R$ is a unique factorization domain.

::: pf-proof

Steps [](#s2){.pf-ref} and [](#s4){.pf-ref}.

**(b).**

:::

:::

::: {.pf-step #s6}

$\mathbb{Z}[x]$ is a UFD but not a PID.

::: pf-proof

$\mathbb{Z}[x]$ is a UFD by Gauss's lemma, and the ideal $(2, x)$ is not principal.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} proves (a), and step [](#s6){.pf-ref} gives the example for (b).

:::

:::

:::
