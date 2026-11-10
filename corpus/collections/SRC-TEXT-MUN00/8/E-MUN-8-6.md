---
schema: qual/card@1
id: E-MUN-8-6
kind: problem
title: A recursion with no solution, and one repaired by a case distinction
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
    Read against Munkres, Topology (2000), §8 Exercise 6, printed p. 56; both parts are
    stored as printed, R_+ being the positive reals.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 8.6,
    printed pp. 96-97 (tmp/sources/munkres-solutions-whitman.pdf). Part (a) is his
    computation h(1) = 3, h(2) = sqrt2, then h(3) = sqrt(sqrt2 - 1) in (0,1) so that
    h(3) - 1 < 0 and [h(4)]^2 < 0; the reason the principle is not violated - rho is not
    defined at every f - is his. Part (b) is his piecewise rho and its verification.
---

::: {.exercise}

(a) Show that there is no function $h: \ZZ_+ \to \RR_+$ satisfying the formula
$$
h(1) = 3,
\qquad
h(i) = [h(i-1) - 1]^{1/2} \quad \text{for } i > 1,
$$
and explain why this example does not violate the principle of recursive definition.

(b) Consider the recursion formula
$$
h(1) = 3,
\qquad
h(i) = \begin{cases}[h(i-1)-1]^{1/2} & \text{if } h(i-1) > 1,\\ 5 & \text{if } h(i-1)\le1,\end{cases} \quad \text{for } i > 1.
$$
Show that there exists a unique function $h:\ZZ_+\to\RR_+$ satisfying this formula.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 8.6, printed pp. 96--97** (`tmp/sources/munkres-solutions-whitman.pdf`); both parts are his.

(a) Suppose $h$ exists. Then $h(1)=3$ and
$$
h(2)=[h(1)-1]^{1/2}=\sqrt2 .
$$
Since $1<\sqrt2<2$ we have $0<\sqrt2-1<1$, so
$$
h(3)=[h(2)-1]^{1/2}=\sqrt{\sqrt2-1}\in(0,1).
$$
Then $h(3)-1<0$, and the formula at $i=4$ would give
$$
[h(4)]^2=h(3)-1<0,
$$
which is impossible for a real $h(4)$. Hence no such $h$ exists.

This does not contradict the principle of recursive definition, because that principle requires a function $\rho$ defined on **every** function from a nonempty section into $A$. Here the natural candidate is $\rho(f)=[f(m)-1]^{1/2}$, which is undefined as soon as $f(m)\le1$, so no such $\rho:\{$functions into $\RR_+\}\to\RR_+$ exists and the theorem's hypothesis fails.

(b) Now set $A=\RR_+$, $a_0=3$, and
$$
\rho(f)=\begin{cases}[f(m)-1]^{1/2}& f(m)>1,\\ 5 & f(m)\le1.\end{cases}
$$
If $f(m)>1$ then $f(m)-1>0$ and $\rho(f)$ is a defined positive real; if $f(m)\le1$ then $\rho(f)=5>0$. So $\rho$ is defined on every function from a nonempty section into $\RR_+$ with values in $\RR_+$, and Theorem 8.4 gives a unique $h$ with $h(1)=3$ and $h(n)=\rho(h\restrict\{1,\dots,n-1\})$ for $n>1$, which is exactly the displayed formula. Uniqueness is that of Theorem 8.4.
:::
