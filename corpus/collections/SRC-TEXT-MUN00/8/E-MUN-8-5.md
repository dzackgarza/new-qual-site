---
schema: qual/card@1
id: E-MUN-8-5
kind: problem
title: Existence and uniqueness for a square-root recursion
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
    Read against Munkres, Topology (2000), §8 Exercise 5, printed p. 56; the stored
    statement matches, with R_+ the set of positive reals.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 8.5,
    printed p. 96 (tmp/sources/munkres-solutions-whitman.pdf). Existence is his rho(f) =
    [f(m) + 1]^{1/2}, well defined because f(m) > 0; uniqueness is his induction.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps from the retained Whitman solution (Exercise 8.5, printed p. 96); statement unchanged. Existence is split into the two obligations Theorem 8.4 imposes -- that rho be a well-defined function into R+ on every nonempty section, which the prose asserted in one clause, and that the recursion formula then holds at i = 1 and at i > 1 -- and uniqueness is a single induction on the set where the two candidates agree. Pages checked against the retained PDF: Theorem 8.4 (principle of recursive definition) begins on printed p. 54 and its examples run to p. 55; the exercise is on printed p. 56.

---

::: {.exercise}

Show that there is a unique function $h: \ZZ_+ \to \RR_+$ satisfying the formula
$$
h(1) = 3,
\qquad
h(i) = [h(i-1) + 1]^{1/2} \quad \text{for } i > 1.
$$

:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 8.5** (`tmp/sources/munkres-solutions-whitman.pdf`); the choice of $\rho$ and the uniqueness induction are his.

Throughout, $\RR_+$ is the set of positive reals, and the principle of recursive definition is Theorem 8.4 : if $A$ is a set, $a_0\in A$, and $\rho$ assigns to each function on a nonempty section $\{1,\dots,m\}$ of $\ZZ_+$ into $A$ an element of $A$, then there is a unique $h:\ZZ_+\to A$ with $h(1)=a_0$ and $h(i)=\rho(h\restriction\{1,\dots,i-1\})$ for $i>1$. The exercise is on printed p. 56.

::: pf

::: {.pf-step #existence}
There is a function $h:\ZZ_+\to\RR_+$ with $h(1)=3$ and $h(i)=[h(i-1)+1]^{1/2}$ for $i>1$.

::: pf-proof

::: {.pf-step #rho}
The rule $\rho(f)=[f(m)+1]^{1/2}$, for $f:\{1,\dots,m\}\to\RR_+$, is a function assigning to each such $f$ an element of $\RR_+$.

::: pf-proof
A function on the section $\{1,\dots,m\}$ has a value $f(m)$, and $f(m)>0$ because the values of $f$ lie in $\RR_+$; hence $f(m)+1>0$, which has a unique positive square root, and $[f(m)+1]^{1/2}\in\RR_+$. The rule is therefore defined on every admissible $f$ and single-valued.

:::

:::

::: {.pf-step #recursion}
Theorem 8.4 gives $h$.

::: pf-proof
Take $A=\RR_+$, $a_0=3$ and $\rho$ as in step [](#rho){.pf-ref}. Then $h$ with $h(1)=a_0$ and $h(i)=\rho(h\restriction\{1,\dots,i-1\})=[h(i-1)+1]^{1/2}$ for $i>1$ exists, since $h\restriction\{1,\dots,i-1\}$ is a function on the nonempty section $\{1,\dots,i-1\}$ into $\RR_+$.

:::

:::

:::

:::

::: {.pf-step #uniqueness}
Any two functions satisfying the formula coincide.

::: pf-proof
Let $g$ and $h$ both satisfy it, and let $S=\{i\in\ZZ_+: g(i)=h(i)\}$. Then $1\in S$ because $g(1)=3=h(1)$. If $i\in S$ then
$$
g(i+1)=[g(i)+1]^{1/2}=[h(i)+1]^{1/2}=h(i+1),
$$
the middle equality holding because $g(i)=h(i)$ and the positive square root is a function of its argument; so $i+1\in S$. Hence $S$ is inductive, so $S=\ZZ_+$ by the principle of induction, that is $g=h$.

:::

:::

:::

:::
