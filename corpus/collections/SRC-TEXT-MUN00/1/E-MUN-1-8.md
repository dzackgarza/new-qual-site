---
schema: qual/card@1
id: E-MUN-1-8
kind: problem
title: Power set of a finite set
classification:
  areas:
  - topology
  topics:
  - Fundamental Concepts
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 1, Exercise 8; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §1 Exercise 8, printed p. 15; the four
    questions are stored as printed, including the last one asking why P(A) is called
    the power set.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 1.8,
    printed pp. 8-9 (tmp/sources/munkres-solutions-whitman.pdf). Supplied the counting
    step it had asserted: the card previously said only that each element is included or
    omitted, which is not a proof for a set of n elements. It now carries Whitman's
    induction on the size of A, splitting the subsets of A according as they omit or
    contain a chosen x, which is what makes |P(A)| = 2|P(A - {x})| and hence 2^n.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps, transcribing the cited published solution: Dan Whitman,
    Topology, Second Edition by James Munkres: Solutions Manual (2019), Exercise 1.8, printed
    pp. 8-9. Checked against Munkres, §1 Exercise 8, whose number is read from the collection
    index. Each step re-read: a subset of a two-element set is determined by two yes/no decisions
    and all four occur; the empty set has the single subset itself; the induction splits the
    subsets of A into those omitting and those containing a chosen element, both in bijection with
    the power set of A minus that element; and the table follows by substitution. The answer
    sentence lists all four values asked for. Not claimed: any statement about infinite A beyond
    the notation.
---

::: {.exercise}

If a set $A$ has two elements, show that $\mathcal{P}(A)$ has four elements.
How many elements does $\mathcal{P}(A)$ have if $A$ has one element?
Three elements?
No elements?
Why is $\mathcal{P}(A)$ called the power set of $A$ ?
:::

::: {.solution}
The argument is transcribed from the published solution of Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 1.8, printed pp. 8--9 (`tmp/sources/munkres-solutions-whitman.pdf`); the two-element count, the induction and the reading of the name are his. It is checked against Munkres, Topology (2000), §1 Exercise 8.

::: pf

::: {.pf-step #two}
If $A=\{a,b\}$ with $a\ne b$ then $\mathcal P(A)$ has four elements.

::: pf-proof
A subset of $A$ is determined by whether it contains $a$ and whether it contains $b$, so there are at most four subsets, and all four occur: $\varnothing$, $\{a\}$, $\{b\}$ and $\{a,b\}$. These are distinct because $a\ne b$.
:::

:::

::: {.pf-step #power}
A finite set $A$ with $n$ elements has exactly $2^{n}$ subsets.

:::: pf-proof

::: {.pf-step #base}
$\mathcal P(\varnothing)=\{\varnothing\}$ has $1=2^{0}$ element.

::: pf-proof
The only subset of the empty set is the empty set.
:::

:::

::: {.pf-step #step}
If every $n$-element set has $2^{n}$ subsets, then every $(n+1)$-element set has $2^{n+1}$.

::: pf-proof
Let $A$ have $n+1$ elements and choose $x\in A$; then $A-\{x\}$ has $n$ elements. Every subset $B\subseteq A$ either omits $x$, and then $B\subseteq A-\{x\}$, or contains $x$, and then $B=\{x\}\cup C$ with $C\subseteq A-\{x\}$. The two classes are disjoint, and each is in bijection with $\mathcal P(A-\{x\})$: the first by $B\mapsto B$, the second by $B\mapsto B-\{x\}$, whose inverse is $C\mapsto\{x\}\cup C$. By hypothesis $\cardinality{\mathcal P(A-\{x\})}=2^{n}$, so $\cardinality{\mathcal P(A)}=2^{n}+2^{n}=2^{n+1}$.
:::

:::

:::

:::

::: {.pf-step #table}
The answers asked for are $1$, $2$, $4$ and $8$ for $\cardinality{A}=0,1,2,3$.

::: pf-proof
$\cardinality{A}=2$ is step [](#two){.pf-ref} and the general formula is step [](#power){.pf-ref}; substituting $n=0,1,2,3$ gives
$$
\begin{array}{c|c}
\cardinality{A}&\cardinality{\mathcal P(A)}\\ \hline
0&1\\ 1&2\\ 2&4\\ 3&8
\end{array}
$$
:::

:::

::: {.pf-step #name}
The name *power set* refers to the formula $\cardinality{\mathcal P(A)}=2^{\cardinality{A}}$.

::: pf-proof
For a finite set the number of subsets is the power of $2$ whose exponent is the number of elements, by step [](#power){.pf-ref}; this is what the word *power* records, and for infinite $A$ the notation $\cardinality{\mathcal P(A)}=2^{\cardinality{A}}$ is the definition of cardinal exponentiation. The answers are
$$
\boxed{\cardinality{\mathcal P(A)}=2^{\cardinality{A}}\text{ for finite }A;\quad 4,2,8,1\text{ for }2,1,3,0\text{ elements}.}
$$
:::

:::

:::
:::
