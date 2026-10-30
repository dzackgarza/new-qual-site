---
schema: qual/card@1
id: P-ALGS07B
kind: problem
title: 'The colon ideal $\{r : rJ \subseteq I\}$ and its generator in a PID'
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Compared both parts with Problem 2 on pages 3-4 of the official Spring 2007 UCSD algebra
    qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the ideal axioms and the PID intersection formula, including the zero-ideal
    cases via the divisibility characterization of a least common multiple.
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-31
  note: 'Part (a) defined K as the intersection of I and J; the exam (page 3, read from the
    page image) defines K = {r : rJ contained in I}. Restored the statement and rewrote the
    solution for the colon ideal.'
---

::: {.problem}
Let $I$, $J$ be two ideals in a commutative ring $R$ (with unit).

(a) Define $K = \{r : rJ \subseteq I\}$.
Show that $K$ is an ideal.

(b) If $R$ is a principal ideal domain, so $I = (i)$, $J = (j)$, give a formula for a generator $k$ of $K$.
:::

::: {.solution}

::: pf

::: pf-step

The set $K=\{r\in R : rJ\subseteq I\}$ is an ideal of $R$.

::: pf-proof

Since $0\cdot J=\{0\}\subseteq I$, one has $0\in K$.
Let $a,b\in K$ and $x\in J$.
Then $ax\in I$ and $bx\in I$, so
$$
(a-b)x=ax-bx\in I.
$$
Hence $a-b\in K$, and $K$ is an additive subgroup of $R$.

Let $r\in R$, $a\in K$ and $x\in J$.
Then $ax\in I$, and since $I$ is an ideal,
$$
(ra)x=r(ax)\in I.
$$
Hence $ra\in K$.
Thus $K$ is an ideal.

:::

:::

::: pf-step

Let $R$ be a PID with $I=(i)$ and $J=(j)$.
If $j=0$, then $K=R=(1)$.
If $j\neq0$, let $d=\gcd(i,j)$; then
$$
K=\left(\frac{i}{d}\right).
$$

::: pf-proof

If $j=0$, then $J=(0)$ and $rJ=\{0\}\subseteq I$ for every $r\in R$, so $K=R$.

Assume $j\neq0$.
Then $d\neq0$, because $d\mid j$.
Write $i=di'$ and $j=dj'$.
Since $d=\gcd(i,j)$, the elements $i'$ and $j'$ are coprime, so there are $a,b\in R$ with $ai'+bj'=1$.

Because $J=(j)$ and $I$ is an ideal, $rJ\subseteq I$ holds if and only if $rj\in I$.
Hence for $r\in R$,
$$
r\in K
\iff i\mid rj
\iff di'\mid rdj'
\iff i'\mid rj',
$$
where the last equivalence cancels the nonzero element $d$ in the domain $R$.

If $i'\mid r$, then $i'\mid rj'$.
Conversely, if $i'\mid rj'$, then
$$
r=r(ai'+bj')=(ra)i'+b(rj')
$$
is divisible by $i'$.
Therefore $r\in K$ if and only if $i'\mid r$, that is, $K=(i')=(i/d)$.

When $i=0$, one has $d=j$ up to a unit and $i'=0$, so the formula gives $K=(0)$.
This agrees with the definition: $rj=0$ forces $r=0$ in a domain when $j\neq0$.

:::

:::

:::

:::
