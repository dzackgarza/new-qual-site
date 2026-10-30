---
schema: qual/card@1
id: P-UCLAB07S-09
kind: problem
title: Continuous functions are Riemann integrable
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 9 of the retained UCLA Basic Examination, Spring 2007.
---
::: {.problem}

(a) Define what it means for a function $f$ to be Riemann integrable on $[0,1]$.

(b) Prove that every continuous function on $[0,1]$ is Riemann integrable.

:::

::: {.solution}

::: pf

::: {.pf-step #p2-s1}

Let
$$
P:\quad 0=x_0<x_1<\cdots<x_m=1
$$
be a partition of $[0,1]$.
For each subinterval
$$
I_i=[x_{i-1},x_i],
$$
define
$$
M_i=\sup_{x\in I_i}f(x),
\qquad
m_i=\inf_{x\in I_i}f(x),
$$
and define
$$
U(f,P)
=
\sum_{i=1}^m
M_i(x_i-x_{i-1}),
$$
$$
L(f,P)
=
\sum_{i=1}^m
m_i(x_i-x_{i-1}).
$$

::: pf-proof

These are the upper and lower Darboux sums of $f$ with respect to the partition $P$.
They are well-defined when $f$ is bounded.

:::

:::

::: {.pf-step #p2-s2}

A bounded function
$$
f:[0,1]\to\RR
$$
is Riemann integrable if
$$
\inf_P U(f,P)
=
\sup_P L(f,P).
$$
Equivalently, $f$ is Riemann integrable if for every
$$
\varepsilon>0
$$
there exists a partition $P$ such that
$$
U(f,P)-L(f,P)<\varepsilon.
$$

::: pf-proof

The equality of the upper and lower Darboux integrals is the definition of Riemann integrability.

For the equivalent criterion, note that for every partition $P$,
$$
L(f,P)
\le
\sup_Q L(f,Q)
\le
\inf_Q U(f,Q)
\le
U(f,P).
$$
Hence arbitrarily small gaps
$$
U(f,P)-L(f,P)
$$
force equality of the upper and lower integrals.

Conversely, if those two integrals are equal, choose one partition whose upper sum is within $\varepsilon/2$ of the common value and another whose lower sum is within $\varepsilon/2$.
A common refinement decreases the upper sum and increases the lower sum, producing a partition with gap less than $\varepsilon$.

:::

:::

::: {.pf-step #p2-s3}

Let $f$ be continuous on $[0,1]$.
Then $f$ is uniformly continuous.

::: pf-proof

The interval
$$
[0,1]
$$
is compact.
The Heine--Cantor theorem states that every continuous function on a compact metric space is uniformly continuous.

:::

:::

::: {.pf-step #p2-s4}

Fix
$$
\varepsilon>0.
$$
There exists
$$
\delta>0
$$
such that
$$
\abs{x-y}<\delta
$$
implies
$$
\abs{f(x)-f(y)}<\varepsilon
$$
for all
$$
x,y\in[0,1].
$$

::: pf-proof

Apply uniform continuity from step [](#p2-s3){.pf-ref}.

:::

:::

::: {.pf-step #p2-s5}

Choose a partition
$$
P
$$
whose mesh satisfies
$$
\max_i(x_i-x_{i-1})<\delta.
$$
Then for every subinterval $I_i$,
$$
M_i-m_i\le\varepsilon.
$$

::: pf-proof

Any two points
$$
x,y\in I_i
$$
satisfy
$$
\abs{x-y}
\le
x_i-x_{i-1}
<
\delta.
$$
Hence
$$
\abs{f(x)-f(y)}<\varepsilon.
$$
Therefore the oscillation of $f$ on $I_i$ is at most $\varepsilon$:
$$
M_i-m_i\le\varepsilon.
$$

:::

:::

::: {.pf-step #p2-s6}

For the partition $P$ from step [](#p2-s5){.pf-ref},
$$
U(f,P)-L(f,P)\le\varepsilon.
$$

::: pf-proof

Using step [](#p2-s5){.pf-ref},
$$
\begin{aligned}
U(f,P)-L(f,P)
&=
\sum_{i=1}^m
(M_i-m_i)(x_i-x_{i-1})\\
&\le
\varepsilon
\sum_{i=1}^m
(x_i-x_{i-1})\\
&=
\varepsilon.
\end{aligned}
$$
If strict inequality is desired, begin step [](#p2-s4){.pf-ref} with $\varepsilon/2$ instead.

:::

:::

::: {.pf-step #p2-s7}

Therefore every continuous function on $[0,1]$ is Riemann integrable.

::: pf-proof

Step [](#p2-s6){.pf-ref} shows that for every positive tolerance there exists a partition with arbitrarily small upper-minus-lower sum.
By the criterion in step [](#p2-s2){.pf-ref},
$$
\boxed{f\text{ is Riemann integrable}.}
$$

:::

:::

::: pf-qed

Steps [](#p2-s1){.pf-ref} and [](#p2-s2){.pf-ref} answer part (a) of the problem, and steps [](#p2-s3){.pf-ref}, [](#p2-s4){.pf-ref}, [](#p2-s5){.pf-ref}, [](#p2-s6){.pf-ref} and [](#p2-s7){.pf-ref} prove part (b).

:::

:::

:::
