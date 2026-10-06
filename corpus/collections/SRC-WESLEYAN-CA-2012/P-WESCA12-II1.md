---
schema: qual/card@1
id: P-WESCA12-II1
kind: problem
title: 'Coefficientwise products of power series and strictness'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problems, problem 1 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Let $A$ and $B$ be the radii of convergence of $\sum a_kz^k$ and $\sum b_kz^k$.

(a) Prove that the radius of convergence of $\sum a_kb_kz^k$ is at least $AB$.

(b) Give an example for which the inequality is strict.
:::

::: {.solution}
Let
\[
R
\]
denote the radius of convergence of
\[
\sum_{k=0}^{\infty}
a_kb_k z^k.
\]

<1>1. Fix real numbers
\[
0<r<A,
\qquad
0<s<B.
\]
Then
\[
\sum_{k=0}^{\infty}
|a_k|r^k
\]
and
\[
\sum_{k=0}^{\infty}
|b_k|s^k
\]
converge.

::: {.proof}
Power series converge absolutely at every point strictly inside their disks
of convergence.
:::

<1>2. The sequence
\[
|b_k|s^k
\]
is bounded.

::: {.proof}
Every convergent series has terms tending to zero. Therefore
\[
|b_k|s^k\to0.
\]
In particular, the sequence is bounded: there exists
\[
M<\infty
\]
such that
\[
|b_k|s^k\le M
\qquad
(k\ge0).
\]
:::

<1>3. The series
\[
\sum_{k=0}^{\infty}
|a_kb_k|(rs)^k
\]
converges.

::: {.proof}
Using step <1>2,
\[
\begin{aligned}
|a_kb_k|(rs)^k
&=
\bigl(|a_k|r^k\bigr)
\bigl(|b_k|s^k\bigr)\\
&\le
M|a_k|r^k.
\end{aligned}
\]
The comparison series
\[
\sum M|a_k|r^k
\]
converges by step <1>1.
:::

<1>4. Hence
\[
R\ge rs.
\]

::: {.proof}
Step <1>3 says the coefficientwise-product power series converges absolutely
at every
\[
z
\]
with
\[
|z|=rs.
\]
Therefore its radius of convergence is at least $rs$.
:::

<1>5. Therefore
\[
\boxed{
R\ge AB.
}
\]

::: {.proof}
If
\[
A=0
\quad\text{or}\quad
B=0,
\]
the inequality is trivial.

Assume
\[
A,B>0.
\]
Step <1>4 holds for every
\[
r<A,
\qquad
s<B.
\]
Let
\[
r\uparrow A,
\qquad
s\uparrow B.
\]
Then
\[
rs\uparrow AB,
\]
so
\[
R\ge AB.
\]

If one of $A,B$ is infinite, choose arbitrarily large finite $r$ or $s$;
the same argument gives
\[
R=\infty
\]
whenever
\[
AB=\infty.
\]
:::

<1>6. The inequality can be strict.

::: {.proof}
Define
\[
a_k
=
\begin{cases}
1,&k\text{ even},\\
0,&k\text{ odd},
\end{cases}
\]
and
\[
b_k
=
\begin{cases}
0,&k\text{ even},\\
1,&k\text{ odd}.
\end{cases}
\]

Then
\[
\sum a_k z^k
=
1+z^2+z^4+\cdots
=
\frac1{1-z^2}
\]
for
\[
|z|<1,
\]
so its radius is
\[
A=1.
\]

Likewise,
\[
\sum b_k z^k
=
z+z^3+z^5+\cdots
=
\frac{z}{1-z^2},
\]
so
\[
B=1.
\]

But
\[
a_kb_k=0
\qquad
\text{for every }k.
\]
Hence
\[
\sum a_kb_kz^k
\equiv
0
\]
has infinite radius of convergence:
\[
R=\infty.
\]
Thus
\[
R>AB=1.
\]
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>5 proves part (a), and step <1>6 gives the strict example required
in part (b).
:::
:::
