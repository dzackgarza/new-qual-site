---
schema: qual/card@1
id: E-MUN-8-1
kind: problem
title: Defining the $n$-fold sum of a sequence by recursive definition
classification:
  areas:
  - topology
  topics:
  - Recursive Definition
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §8 Exercise 1, printed pp. 55-56; the stored
    statement matches, and Theorem 8.4 is stated in §8 immediately before the exercises.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 8.1,
    printed p. 94 (tmp/sources/munkres-solutions-whitman.pdf). His choice is
    rho(f) = f(m) + b_{m+1} for f : {1,...,m} -> R with a_0 = b_1.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into Lamport steps. The statement was checked against Munkres, *Topology* (2000), §8 Exercise 1, printed pp. 55--56, and the choice of $\rho$ is transcribed from the retained set: Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 8.1, printed p. 94. Checked: $\rho$ takes values in $A=\RR$ and is defined on every nonempty section, so Theorem 8.4 applies; the resulting $h$ satisfies both recursion clauses; and uniqueness is Theorem 8.4's.
---

::: {.exercise}

Let $(b_1, b_2, \ldots)$ be an infinite sequence of real numbers. The sum $\sum_{k=1}^n b_k$ is defined by induction as follows:
$$
\sum_{k=1}^{n} b_k = b_1 \ \text{ for } n = 1,
\qquad
\sum_{k=1}^{n} b_k = \left(\sum_{k=1}^{n-1} b_k\right) + b_n \ \text{ for } n > 1.
$$
Let $A$ be the set of real numbers; choose $\rho$ so that Theorem 8.4 applies to define this sum rigorously.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 8.1** (`tmp/sources/munkres-solutions-whitman.pdf`); the choice of $\rho$ below is his. The statement is Munkres, *Topology* (2000), §8 Exercise 1.

::: pf

::: {.pf-step #rho}
With $A=\RR$ and $a_0\coloneqq b_1$, the formula $\rho(f)\coloneqq f(m)+b_{m+1}$, for a function $f$ on the section $\{1,\dots,m\}$, defines a function $\rho$ to which Theorem 8.4 applies.

::: pf-proof
The domain of $\rho$ is the set of all functions from nonempty sections of $\ZZ_+$ into $\RR$, and $\rho(f)=f(m)+b_{m+1}$ is a sum of two real numbers, hence an element of $A=\RR$. So $\rho$ assigns an element of $A$ to every such function, which is the hypothesis of the principle of recursive definition (Theorem 8.4).
:::
:::

::: {.pf-step #exists}
There is a function $h:\ZZ_+\to\RR$ with $h(1)=b_1$ and $h(n)=h(n-1)+b_n$ for $n>1$.

::: pf-proof
Theorem 8.4 applied to $a_0$ and $\rho$ of step [](#rho){.pf-ref} gives $h$ with $h(1)=a_0=b_1$ and $h(n)=\rho(h\restrictionof{\{1,\dots,n-1\}})=h(n-1)+b_n$.
:::
:::

::: {.pf-step #unique}
The function $h$ is the unique one with those values.

::: pf-proof
This is the uniqueness clause of Theorem 8.4, whose hypothesis was verified in step [](#rho){.pf-ref}.
:::
:::

::: {.pf-step}
Defining $\sum_{k=1}^n b_k\coloneqq h(n)$ gives a rigorous definition satisfying the two recursion clauses, and it is the only one.

::: pf-proof
Step [](#exists){.pf-ref} produces $h$ satisfying exactly the two clauses of the induction and step [](#unique){.pf-ref} shows no other function does, so the sum is defined rigorously and uniquely.
:::
:::

:::
:::
