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
---

::: {.exercise}

(a) Let $\prec$ be a strict partial order on the set $A$. Define a relation on $A$ by letting $a \preceq b$ if either $a \prec b$ or $a = b$. Show that this relation has the partial order axioms:
(i) $a\preceq a$ for all $a\in A$; (ii) $a\preceq b$ and $b\preceq a$ imply $a=b$; (iii) $a\preceq b$ and $b\preceq c$ imply $a\preceq c$.

(b) Let $P$ be a relation on $A$ satisfying (i)-(iii). Define $S$ by $aSb$ if $aPb$ and $a\ne b$. Show that $S$ is a strict partial order on $A$.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 11.2, printed p. 119** (`tmp/sources/munkres-solutions-whitman.pdf`); both verifications are his.

(a) (i) $a\preceq a$ because $a=a$.

(ii) Suppose $a\preceq b$ and $b\preceq a$. If $a\ne b$ then $a\prec b$ and $b\prec a$, so $a\prec a$ by transitivity, contradicting nonreflexivity. Hence $a=b$.

(iii) Suppose $a\preceq b$ and $b\preceq c$, so each of the two holds either by the strict relation or by equality. If $a=b$ or $b=c$ the conclusion is immediate. Otherwise $a\prec b$ and $b\prec c$, so $a\prec c$ by transitivity and $a\preceq c$.

(b) *Nonreflexivity:* $aSa$ would require $a\ne a$.

*Transitivity:* if $aSb$ and $bSc$ then $aPb$, $bPc$ and $a\ne b$, $b\ne c$; by (iii) $aPc$. If also $a=c$ then $bPc=aPb$, that is $aPb$ and $bPa$, so $a=b$ by (ii), a contradiction. Hence $a\ne c$ and $aSc$.
:::
