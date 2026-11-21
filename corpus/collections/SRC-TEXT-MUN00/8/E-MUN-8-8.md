---
schema: qual/card@1
id: E-MUN-8-8
kind: problem
title: The principle of recursive definition stated with sections
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
    Read against Munkres, Topology (2000), §8 Exercise 8, printed p. 56; the stored
    statement matches, and S_n is the section {k in Z_+ : k < n} of §8, so S_1 = empty
    set.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 8.8,
    printed pp. 99-100 (tmp/sources/munkres-solutions-whitman.pdf). The reduction takes
    a_0 = rho(empty) and applies Theorem 8.4. His last paragraph prints h where it means
    the second function f in the uniqueness step; the card writes f and its argument is
    his.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps, transcribing the cited published solution: Dan Whitman,
    Topology, Second Edition by James Munkres: Solutions Manual (2019), Exercise 8.8, printed
    pp. 99-100. Checked against Munkres §8 Exercise 8, whose number is read from the collection
    index. Each step re-read: the sections are the empty set and the initial segments; the
    existence statement is Theorem 8.4 applied to a_0 = rho(empty) and the obvious rule; the two
    cases n = 1 and n > 1 verify the displayed formula; and uniqueness follows because any
    solution obeys the recursion of Theorem 8.4. Not claimed: any statement about recursion over a
    general well-ordered set, which is a stronger principle.
---

::: {.exercise}

Verify the following version of the principle of recursive definition: let $A$ be a set, and let $\rho$ be a function assigning, to every function $f$ mapping a section $S_n$ of $\ZZ_+$ into $A$, an element $\rho(f)$ of $A$. Then there is a unique function $h:\ZZ_+\to A$ such that $h(n)=\rho(\restrictionof{h}{S_n})$ for each $n\in\ZZ_+$.
:::

::: {.solution}
The argument is transcribed from the published solution of Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 8.8, printed pp. 99--100 (`tmp/sources/munkres-solutions-whitman.pdf`); the reduction to the version of the principle in Theorem 8.4 is his. It is checked against Munkres, Topology (2000), §8 Exercise 8.

::: pf

::: {.pf-step #sections}
$S_{1}=\varnothing$ and $S_{n}=\{1,\dots,n-1\}$ for $n>1$.

::: pf-proof
By definition $S_{n}=\{k\in\ZZ_{+}:k<n\}$, which is empty for $n=1$ and is $\{1,\dots,n-1\}$ otherwise.
:::

:::

::: {.pf-step #existence}
There is $h:\ZZ_{+}\to A$ with $h(n)=\rho(\restrictionof{h}{S_{n}})$ for every $n$.

:::: pf-proof

::: {.pf-step #define}
Put $a_{0}=\rho(\varnothing)$, the value of $\rho$ at the unique function from the empty set.

::: pf-proof
$\varnothing\to A$ is a function from a section of $\ZZ_{+}$, so $\rho$ is defined on it.
:::

:::

::: {.pf-step #theorem}
There is $h:\ZZ_{+}\to A$ with $h(1)=a_{0}$ and $h(i)=\rho(h\restrict\{1,\dots,i-1\})$ for $i>1$.

::: pf-proof
This is Theorem 8.4 of the book, the principle of recursive definition, applied to the set $A$, the element $a_{0}$ and the rule assigning $\rho(h\restrict\{1,\dots,i-1\})$ to $h$ at stage $i$.
:::

:::

::: {.pf-step #formula}
This $h$ satisfies the required formula at every $n$.

::: pf-proof
At $n=1$: $h(1)=a_{0}=\rho(\varnothing)=\rho(\restrictionof{h}{S_{1}})$ because $S_{1}=\varnothing$. At $n>1$: $h(n)=\rho(h\restrict\{1,\dots,n-1\})=\rho(\restrictionof{h}{S_{n}})$ by step [](#sections){.pf-ref}.
:::

:::

:::

:::

::: {.pf-step #uniqueness}
Any $f$ satisfying the formula equals $h$.

::: pf-proof
Such an $f$ has $f(1)=\rho(\restrictionof{f}{S_{1}})=\rho(\varnothing)=a_{0}$ and, for $i>1$, $f(i)=\rho(\restrictionof{f}{S_{i}})=\rho(f\restrict\{1,\dots,i-1\})$; so $f$ obeys the recursion of Theorem 8.4, whose solution is unique, and hence $f=h$.
:::

:::

::: {.pf-step}
The stated form of the principle of recursive definition holds.

::: pf-proof
Steps [](#existence){.pf-ref} and [](#uniqueness){.pf-ref} give existence and uniqueness:
$$
\boxed{\exists!\,h:\ZZ_{+}\to A\text{ with }h(n)=\rho(\restrictionof{h}{S_{n}})\text{ for all }n.}
$$
The section version and the version of Theorem 8.4 are the same statement, related by the identification of step [](#sections){.pf-ref}.
:::

:::

:::
:::
