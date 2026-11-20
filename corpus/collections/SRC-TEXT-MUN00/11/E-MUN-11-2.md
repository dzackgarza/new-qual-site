---
schema: qual/card@1
id: E-MUN-11-2
kind: problem
title: Passing between strict partial orders and partial orders
classification:
  areas:
  - topology
  topics:
  - Maximum Principle
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §11 Exercise 2, printed p. 70; both parts and
    the three partial order axioms are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 11.2,
    printed p. 119 (tmp/sources/munkres-solutions-whitman.pdf). The antisymmetry step
    uses nonreflexivity of the strict order to rule out a simultaneous a < b and b < a;
    part (b) uses antisymmetry of P to rule out a = c in a transitivity check.
- event: source-corrected
  by: claude
  date: 2026-11-18
  note: >-
    The earlier source check recorded this exercise on printed p. 70; reading the book's text
    (tmp/sources/munkres-2000-topology.md, PDF pp. 85-86) puts the Exercises of §11 on
    printed p. 71, with Exercise 2 there and p. 70 holding the discussion of the maximum
    principle. The statement is unchanged and matches the printed text of Exercise 2; only
    the page was wrong, and this event records the reading rather than editing the earlier
    one.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: reflexivity, antisymmetry and transitivity
    of the relation built from a strict partial order, then nonreflexivity and transitivity
    of the relation built from a partial order. The retained solution's cited page was not
    re-read in this pass; its citation is the earlier event's.
---

::: {.exercise}

(a) Let $\prec$ be a strict partial order on the set $A$. Define a relation on $A$ by letting $a \preceq b$ if either $a \prec b$ or $a = b$. Show that this relation has the partial order axioms:
(i) $a\preceq a$ for all $a\in A$; (ii) $a\preceq b$ and $b\preceq a$ imply $a=b$; (iii) $a\preceq b$ and $b\preceq c$ imply $a\preceq c$.

(b) Let $P$ be a relation on $A$ satisfying (i)-(iii). Define $S$ by $aSb$ if $aPb$ and $a\ne b$. Show that $S$ is a strict partial order on $A$.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 11.2** (`tmp/sources/munkres-solutions-whitman.pdf`); both verifications are his.

A strict partial order on $A$ is a relation $\prec$ that is nonreflexive, so $a\prec a$ holds for no $a$, and transitive. The relation $\preceq$ of (a) is defined by: $a\preceq b$ when $a\prec b$ or $a=b$.

::: pf

::: {.pf-step #partial-order}
(a) The relation $\preceq$ satisfies (i), (ii) and (iii).

::: pf-proof
One property per step.

::: {.pf-step #reflexive}
(i) $a\preceq a$ for every $a\in A$.

::: pf-proof
$a=a$, so the second clause of the definition applies.
:::

:::

::: {.pf-step #antisymmetric}
(ii) $a\preceq b$ and $b\preceq a$ imply $a=b$.

::: pf-proof
Suppose $a\ne b$. Then neither of the two relations can hold through its equality clause, so $a\prec b$ and $b\prec a$; transitivity of $\prec$ gives $a\prec a$, contradicting nonreflexivity. Hence $a=b$.
:::

:::

::: {.pf-step #transitive}
(iii) $a\preceq b$ and $b\preceq c$ imply $a\preceq c$.

::: pf-proof
If $a=b$ or $b=c$ the conclusion is immediate. Otherwise $a\preceq b$ holds through $a\prec b$ and $b\preceq c$ through $b\prec c$, so $a\prec c$ by transitivity, and then $a\preceq c$ by the first clause.
:::

:::

:::

:::

::: {.pf-step #strict}
(b) If $P$ satisfies (i)--(iii) and $S$ is defined by $aSb$ exactly when $aPb$ and $a\ne b$, then $S$ is a strict partial order on $A$.

::: pf-proof
Nonreflexivity and transitivity, in that order.

::: {.pf-step #irreflexive}
$aSa$ holds for no $a\in A$.

::: pf-proof
$aSa$ would require $a\ne a$, which is impossible; so $S$ is nonreflexive.
:::

:::

::: {.pf-step #s-transitive}
$aSb$ and $bSc$ imply $aSc$.

::: pf-proof
The hypotheses give $aPb$, $bPc$, $a\ne b$ and $b\ne c$; by (iii) $aPc$. If also $a=c$, then $bPc$ reads $bPa$, so $aPb$ and $bPa$, and (ii) gives $a=b$, contradicting $a\ne b$. Hence $a\ne c$, and with $aPc$ this is $aSc$.
:::

:::

:::

:::

:::
:::
