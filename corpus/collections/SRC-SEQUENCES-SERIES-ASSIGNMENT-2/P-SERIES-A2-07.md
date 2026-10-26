---
schema: qual/card@1
id: P-SERIES-A2-07
kind: problem
title: Convergence of ratios of consecutive Fibonacci numbers
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
The Fibonacci numbers $\{f_n\}$ are defined by
\[
f_0=f_1=1,\qquad f_{n+1}=f_n+f_{n-1}\quad(n\ge1),
\]
and for $n\ge1$ define $r_n=f_{n+1}/f_n$.

(a) Find a formula for $r_{n+1}$ in terms of $r_n$.

(b) Show that $f_n\ge n$ for all $n\ge2$.

(c) Show that
\[
f_{n+1}f_{n-1}-f_n^2=(-1)^{n+1}.
\]

(d) Hence show that, for $n\ge2$,
\[
|r_{n+1}-r_n|\le \frac1{(n-1)^2}.
\]

(e) Hence show that $\{r_n\}$ converges and compute its limit.
:::

## Part (a)

::: pf

::: pf-step

For \(n\ge1\),
\[
r_{n+1}
=
\frac{f_{n+2}}{f_{n+1}}.
\]


::: pf-proof

This is the definition of \(r_{n+1}\).

:::

:::

::: pf-step

Using the Fibonacci recurrence,
\[
f_{n+2}=f_{n+1}+f_n.
\]


::: pf-proof

Apply
\[
f_{m+1}=f_m+f_{m-1}
\]
with \(m=n+1\).

:::

:::

::: pf-step

Therefore
\[
\boxed{
r_{n+1}
=
1+\frac1{r_n}}.
\]


::: pf-proof

By steps <1>1--<1>2,
\[
\begin{aligned}
r_{n+1}
&=
\frac{f_{n+1}+f_n}{f_{n+1}}\\
&=
1+\frac{f_n}{f_{n+1}}\\
&=
1+\frac1{r_n}.
\end{aligned}
\]

:::

:::

::: pf-step

One has
\[
\boxed{f_2=2}.
\]


::: pf-proof

\[
f_2=f_1+f_0=1+1=2.
\]

:::

:::

::: pf-step

Also,
\[
\boxed{f_3=3}.
\]


::: pf-proof

\[
f_3=f_2+f_1=2+1=3.
\]

:::

:::

::: pf-step

Suppose for some \(n\ge3\) that
\[
f_n\ge n
\]
and
\[
f_{n-1}\ge n-1.
\]
Then
\[
f_{n+1}\ge n+1.
\]


::: pf-proof

Using the recurrence,
\[
\begin{aligned}
f_{n+1}
&=
f_n+f_{n-1}\\
&\ge
n+(n-1)\\
&=
2n-1\\
&\ge
n+1,
\end{aligned}
\]
because \(n\ge2\).

:::

:::

::: pf-step

Hence
\[
\boxed{
f_n\ge n
\qquad(n\ge2)}.
\]


::: pf-proof

Steps <1>4--<1>5 give the initial cases, and step <1>6 gives the induction
step.

:::

:::

::: pf-step

The initial value is
\[
\boxed{C_1=1}.
\]


::: pf-proof

\[
C_1
=
f_2f_0-f_1^2
=
2\cdot1-1
=
1.
\]

:::

:::

::: pf-step

The sequence \((C_n)\) satisfies
\[
\boxed{
C_{n+1}=-C_n}.
\]


::: pf-proof

\[
\begin{aligned}
C_{n+1}
&=
f_{n+2}f_n-f_{n+1}^2\\
&=
(f_{n+1}+f_n)f_n-f_{n+1}^2\\
&=
f_n^2-f_{n+1}(f_{n+1}-f_n)\\
&=
f_n^2-f_{n+1}f_{n-1}\\
&=
-C_n.
\end{aligned}
\]

:::

:::

::: pf-step

Therefore
\[
\boxed{
f_{n+1}f_{n-1}-f_n^2
=
(-1)^{n+1}}.
\]


::: pf-proof

From step <1>8,
\[
C_1=1=(-1)^2.
\]
Step <1>9 says the sign flips at each step, giving
\[
C_n=(-1)^{n+1}.
\]

:::

:::

::: pf-step

For \(n\ge1\),
\[
r_{n+1}-r_n
=
\frac{
f_{n+2}f_n-f_{n+1}^2
}{
f_{n+1}f_n
}.
\]


::: pf-proof

Subtract:
\[
\frac{f_{n+2}}{f_{n+1}}
-
\frac{f_{n+1}}{f_n}.
\]

:::

:::

::: pf-step

By part (c),
\[
\boxed{
f_{n+2}f_n-f_{n+1}^2
=
(-1)^n}.
\]


::: pf-proof

Apply step <1>10 with \(n\) replaced by \(n+1\):
\[
f_{n+2}f_n-f_{n+1}^2
=
(-1)^{n+2}
=
(-1)^n.
\]

:::

:::

::: pf-step

Therefore
\[
\boxed{
|r_{n+1}-r_n|
=
\frac1{f_nf_{n+1}}}.
\]


::: pf-proof

Combine steps <1>11--<1>12 and take absolute values.

:::

:::

::: pf-step

For \(n\ge2\),
\[
f_n\ge n
\qquad\text{and}\qquad
f_{n+1}\ge n+1.
\]


::: pf-proof

Apply step <1>7 at indices \(n\) and \(n+1\).

:::

:::

::: pf-step

Hence
\[
|r_{n+1}-r_n|
\le
\frac1{n(n+1)}.
\]


::: pf-proof

Use step <1>13 and the lower bounds in step <1>14.

:::

:::

::: pf-step

For \(n\ge2\),
\[
\frac1{n(n+1)}
\le
\frac1{(n-1)^2}.
\]


::: pf-proof

It suffices to show
\[
(n-1)^2\le n(n+1).
\]
Expanding,
\[
n^2-2n+1\le n^2+n,
\]
equivalent to
\[
1\le3n,
\]
which holds for \(n\ge1\).

:::

:::

::: pf-step

Thus
\[
\boxed{
|r_{n+1}-r_n|
\le
\frac1{(n-1)^2}}
\qquad(n\ge2).
\]


::: pf-proof

Combine steps <1>15--<1>16.

:::

:::

::: pf-step

Let \(m>n\ge2\). Then
\[
r_m-r_n
=
\sum_{k=n}^{m-1}
(r_{k+1}-r_k).
\]


::: pf-proof

The sum telescopes.

:::

:::

::: pf-step

Hence
\[
|r_m-r_n|
\le
\sum_{k=n}^{m-1}
|r_{k+1}-r_k|.
\]


::: pf-proof

Apply the triangle inequality to step <1>18.

:::

:::

::: pf-step

By step <1>17,
\[
|r_m-r_n|
\le
\sum_{k=n}^{m-1}
\frac1{(k-1)^2}.
\]


::: pf-proof

Bound each summand in step <1>19.

:::

:::

::: pf-step

Therefore
\[
|r_m-r_n|
\le
\sum_{j=n-1}^{\infty}
\frac1{j^2}.
\]


::: pf-proof

Extend the finite nonnegative sum to the full tail of the convergent
\(p\)-series.

:::

:::

::: pf-step

The right-hand side in step <1>21 tends to \(0\) as
\[
n\to\infty.
\]


::: pf-proof

The series
\[
\sum_{j=1}^{\infty}\frac1{j^2}
\]
converges, so its tails tend to zero.

:::

:::

::: pf-step

Hence \((r_n)\) is Cauchy.


::: pf-proof

Given \(\varepsilon>0\), choose \(N\) so that the tail in step <1>21 is less
than \(\varepsilon\) for \(n\ge N\). Then every \(m>n\ge N\) satisfies
\[
|r_m-r_n|<\varepsilon.
\]

:::

:::

::: pf-step

Since \(\mathbb R\) is complete, there exists
\[
L\in\mathbb R
\]
such that
\[
\boxed{r_n\to L}.
\]


::: pf-proof

Every real Cauchy sequence converges.

:::

:::

::: pf-step

Each \(r_n\) is positive, and in fact
\[
r_n>1.
\]


::: pf-proof

All Fibonacci numbers are positive. Also
\[
f_{n+1}=f_n+f_{n-1}>f_n
\]
for \(n\ge1\), so
\[
r_n=\frac{f_{n+1}}{f_n}>1.
\]

:::

:::

::: pf-step

Therefore
\[
\boxed{L\ge1}.
\]


::: pf-proof

The limit of a sequence whose terms are all greater than \(1\) is at least
\(1\).

:::

:::

::: pf-step

Passing to the limit in
\[
r_{n+1}=1+\frac1{r_n},
\]
one obtains
\[
\boxed{
L=1+\frac1L}.
\]


::: pf-proof

By step <1>24,
\[
r_{n+1}\to L
\]
as well. By step <1>26, \(L\ne0\), so the reciprocal function is continuous
at \(L\). Take limits in step <1>3.

:::

:::

::: pf-step

Thus
\[
L^2-L-1=0.
\]


::: pf-proof

Multiply step <1>27 by \(L\).

:::

:::

::: pf-step

The two algebraic roots are
\[
\frac{1+\sqrt5}{2}
\qquad\text{and}\qquad
\frac{1-\sqrt5}{2}.
\]


::: pf-proof

Apply the quadratic formula to
\[
L^2-L-1=0.
\]

:::

:::

::: pf-step

Since \(L\ge1\),
\[
\boxed{
L=\frac{1+\sqrt5}{2}}.
\]


::: pf-proof

The second root is negative, while step <1>26 gives \(L\ge1\).

:::

:::

::: pf-step

Therefore
\[
\boxed{
\lim_{n\to\infty}
\frac{f_{n+1}}{f_n}
=
\frac{1+\sqrt5}{2}}.
\]


::: pf-proof

Use the definition \(r_n=f_{n+1}/f_n\) and step <1>30.

:::

:::

::: pf-qed

Step <1>3 proves part (a), step <1>7 proves part (b), step <1>10 proves part
(c), step <1>17 proves part (d), and steps <1>23--<1>31 prove part (e).

:::

:::
