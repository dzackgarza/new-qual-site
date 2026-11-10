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
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 8.5, printed p. 96** (`tmp/sources/munkres-solutions-whitman.pdf`); the choice of $\rho$ and the uniqueness induction are his.

*Existence.* Put $A=\RR_+$, $a_0=3$, and for $f:\{1,\dots,m\}\to\RR_+$ set
$$
\rho(f)=[f(m)+1]^{1/2}.
$$
Since $f(m)>0$ we have $f(m)+1>0$, so $\rho(f)$ is a defined positive real number and $\rho$ satisfies the hypothesis of Theorem 8.4. Hence there is $h:\ZZ_+\to\RR_+$ with $h(1)=3$ and
$$
h(i)=\rho(h\restrict\{1,\dots,i-1\})=[h(i-1)+1]^{1/2}\quad(i>1).
$$

*Uniqueness.* Let $g$ and $h$ both satisfy the formula. Then $g(1)=3=h(1)$, and if $g(i)=h(i)$ then
$$
g(i+1)=[g(i)+1]^{1/2}=[h(i)+1]^{1/2}=h(i+1),
$$
the positive square root being the same for equal arguments. By induction $g=h$.
:::
