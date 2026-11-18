---
schema: qual/card@1
id: E-MUN-8-2
kind: problem
title: Defining the $n$-fold product of a sequence by recursive definition
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
    Read against Munkres, Topology (2000), §8 Exercise 2, printed p. 56; the stored
    statement matches.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 8.2,
    printed p. 94 (tmp/sources/munkres-solutions-whitman.pdf). His choice is
    rho(f) = f(m) * b_{m+1} with a_0 = b_1.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: the data of Theorem 8.4, the recursion
    it yields, the two printed equations, and the uniqueness that makes the definition
    unambiguous. Read Theorem 8.4 at tmp/sources/munkres-2000-topology.md, printed p. 54 (PDF p. 69),
    and the exercise's two equations on the card; the choice of rho is the retained
    solution's, Whitman Exercise 8.2 printed p. 94. The printed page of the exercise
    itself was not re-read here; its source check on the card is the earlier event.
---

::: {.exercise}

Let $(b_1, b_2, \ldots)$ be an infinite sequence of real numbers. We define the product $\prod_{k=1}^n b_k$ by the equations
$$
\prod_{k=1}^{1} b_k = b_1,
\qquad
\prod_{k=1}^{n} b_k = \left(\prod_{k=1}^{n-1} b_k\right)\cdot b_n \quad \text{for } n > 1.
$$
Use Theorem 8.4 to define this product rigorously.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 8.2, printed p. 94** (`tmp/sources/munkres-solutions-whitman.pdf`); the choice of $\rho$ below is his.

Theorem 8.4 (printed p. 54) reads: given a set $A$, an element $a_{0}\in A$, and a function $\rho$ assigning to each function from a nonempty section of $\ZZ_{+}$ into $A$ an element of $A$, there is a unique $h:\ZZ_{+}\to A$ with $h(1)=a_{0}$ and $h(i)=\rho\bigl(\restrictionof{h}{\{1,\dots,i-1\}}\bigr)$ for $i>1$. The application is with $A=\RR$.

::: pf

::: {.pf-step #data}
With $A=\RR$, $a_{0}=b_{1}$ and $\rho(f)=f(m)\,b_{m+1}$, where $\{1,\dots,m\}$ is the domain of $f$, the map $\rho$ is a function assigning to each function from a nonempty section of $\ZZ_{+}$ into $\RR$ an element of $\RR$.

::: pf-proof
A nonempty section of $\ZZ_{+}$ is $\{1,\dots,m\}$ for a unique $m\ge1$, so the number $m$ in the formula is determined by $f$; then $f(m)\in\RR$ because $f$ maps into $A=\RR$, and $b_{m+1}\in\RR$ because $(b_{1},b_{2},\dots)$ is a sequence of reals. So the product $f(m)\,b_{m+1}$ is a well-defined real number depending only on $f$, which is what Theorem 8.4 requires of $\rho$.
:::

:::

::: {.pf-step #recursion}
There is a unique $p:\ZZ_{+}\to\RR$ with $p(1)=b_{1}$ and $p(n)=\rho\bigl(\restrictionof{p}{\{1,\dots,n-1\}}\bigr)$ for $n>1$.

::: pf-proof
Apply Theorem 8.4 to the data of step [](#data){.pf-ref}: it supplies exactly one such function, with $a_{0}=b_{1}$.
:::

:::

::: {.pf-step #equations}
For that $p$ one has $p(1)=b_{1}$ and $p(n)=p(n-1)\,b_{n}$ for $n>1$.

::: pf-proof
The first equation is the recursion formula's initial condition. For $n>1$ the domain of $\restrictionof{p}{\{1,\dots,n-1\}}$ is $\{1,\dots,n-1\}$, so its largest element is $m=n-1$ and $\rho\bigl(\restrictionof{p}{\{1,\dots,n-1\}}\bigr)=p(n-1)\,b_{n}$ by the definition of $\rho$ in step [](#data){.pf-ref}; hence $p(n)=p(n-1)\,b_{n}$.
:::

:::

::: {.pf-step #unique}
Setting $\prod_{k=1}^{n}b_{k}=p(n)$ gives a rigorous definition: the two printed recursion equations hold, and no other function satisfies them.

::: pf-proof
By step [](#equations){.pf-ref}, $p(1)=b_{1}=\prod_{k=1}^{1}b_{k}$ and, for $n>1$, $p(n)=p(n-1)\,b_{n}=\bigl(\prod_{k=1}^{n-1}b_{k}\bigr)b_{n}$, which are the two equations the exercise displays. If $q:\ZZ_{+}\to\RR$ satisfied them, then $q(1)=b_{1}$ and $q(n)=q(n-1)b_{n}=\rho\bigl(\restrictionof{q}{\{1,\dots,n-1\}}\bigr)$ for $n>1$, so $q$ obeys the recursion formula of Theorem 8.4 and $q=p$ by the uniqueness in step [](#recursion){.pf-ref}. Hence the product is defined at every $n$, takes the value demanded by the printed equations, and is the only such assignment.
:::

:::

:::
:::
