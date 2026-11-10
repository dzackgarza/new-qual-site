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
---

::: {.exercise}

Verify the following version of the principle of recursive definition: let $A$ be a set, and let $\rho$ be a function assigning, to every function $f$ mapping a section $S_n$ of $\ZZ_+$ into $A$, an element $\rho(f)$ of $A$. Then there is a unique function $h:\ZZ_+\to A$ such that $h(n)=\rho(\restrictionof{h}{S_n})$ for each $n\in\ZZ_+$.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 8.8, printed pp. 99--100** (`tmp/sources/munkres-solutions-whitman.pdf`); the reduction below is his.

Here $S_1=\{k\in\ZZ_+:k<1\}=\varnothing$ and $S_n=\{1,\dots,n-1\}$ for $n>1$.

*Existence.* Put $a_0=\rho(\varnothing)$, the value of $\rho$ at the unique function $\varnothing\to A$. By Theorem 8.4 there is a unique $h:\ZZ_+\to A$ with
$$
h(1)=a_0,
\qquad
h(i)=\rho(h\restrict\{1,\dots,i-1\})\quad(i>1).
$$
For $n=1$ this gives $h(1)=a_0=\rho(\varnothing)=\rho(\restrictionof{h}{\varnothing})=\rho(\restrictionof{h}{S_1})$; for $n>1$ it gives $h(n)=\rho(h\restrict\{1,\dots,n-1\})=\rho(\restrictionof{h}{S_n})$ directly. So $h$ satisfies the displayed formula for every $n$.

*Uniqueness.* Let $f:\ZZ_+\to A$ satisfy $f(n)=\rho(\restrictionof{f}{S_n})$ for all $n$. Then $f(1)=\rho(\restrictionof{f}{S_1})=\rho(\varnothing)=a_0$, and for $i>1$,
$$
f(i)=\rho(\restrictionof{f}{S_i})=\rho(f\restrict\{1,\dots,i-1\}),
$$
so $f$ satisfies the recursion of Theorem 8.4; by the uniqueness in that theorem $f=h$.
:::
