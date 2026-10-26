---
schema: qual/card@1
id: P-SERIES-A2-01
kind: problem
title: Subadditivity of $\limsup$
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
(a) For any two sequences $\{a_n\}$ and $\{b_n\}$, show that
\[
\limsup_{n\to\infty}(a_n+b_n)\le \limsup_{n\to\infty}a_n+\limsup_{n\to\infty}b_n,
\]
unless the right-hand side is of the form $\infty-\infty$.

(b) Find sequences $\{a_n\}$ and $\{b_n\}$ for which the inequality is strict.
:::

Write
\[
A=\limsup_{n\to\infty}a_n,
\qquad
B=\limsup_{n\to\infty}b_n.
\]

## Part (a)

::: pf

::: pf-step

Assume first that
\[
A,B\in\mathbb R.
\]
Fix
\[
\varepsilon>0.
\]


::: pf-proof

This is the main finite-valued case.

:::

:::

::: pf-step

There exists \(N_1\) such that
\[
\boxed{
a_n\le A+\varepsilon}
\]
for every \(n\ge N_1\).


::: pf-proof

By the definition of \(\limsup\), for every \(\varepsilon>0\), all
sufficiently late terms lie below \(A+\varepsilon\).

:::

:::

::: pf-step

There exists \(N_2\) such that
\[
\boxed{
b_n\le B+\varepsilon}
\]
for every \(n\ge N_2\).


::: pf-proof

Apply the same property to the sequence \((b_n)\).

:::

:::

::: pf-step

For
\[
N=\max(N_1,N_2)
\]
and every \(n\ge N\),
\[
a_n+b_n
\le
A+B+2\varepsilon.
\]


::: pf-proof

Add the inequalities from steps <1>2--<1>3.

:::

:::

::: pf-step

Hence
\[
\limsup_{n\to\infty}(a_n+b_n)
\le
A+B+2\varepsilon.
\]


::: pf-proof

Every sufficiently late term of the sequence \((a_n+b_n)\) is bounded above
by the right-hand side of step <1>4, so its limsup is also bounded above by
that number.

:::

:::

::: pf-step

Letting \(\varepsilon\downarrow0\),
\[
\boxed{
\limsup_{n\to\infty}(a_n+b_n)
\le
A+B}.
\]


::: pf-proof

Step <1>5 holds for every positive \(\varepsilon\).

:::

:::

::: pf-step

If
\[
A=+\infty
\]
and
\[
B>-\infty,
\]
then the desired inequality is automatic.


::: pf-proof

In this case
\[
A+B=+\infty.
\]
Every extended real number is at most \(+\infty\).

:::

:::

::: pf-step

The same conclusion holds if
\[
B=+\infty
\]
and
\[
A>-\infty.
\]


::: pf-proof

The right-hand side is again \(+\infty\).

:::

:::

::: pf-step

Suppose
\[
A=-\infty
\]
and
\[
B\in\mathbb R.
\]
Then
\[
\boxed{
\limsup_{n\to\infty}(a_n+b_n)=-\infty}.
\]


::: pf-proof

Fix any real number \(M\). Since
\[
A=-\infty,
\]
there exists \(N_1\) such that
\[
a_n\le M-(B+1)
\]
for all \(n\ge N_1\).

Since
\[
B\in\mathbb R,
\]
there exists \(N_2\) such that
\[
b_n\le B+1
\]
for all \(n\ge N_2\).

Thus for all sufficiently large \(n\),
\[
a_n+b_n\le M.
\]
Because \(M\) was arbitrary,
\[
\limsup(a_n+b_n)=-\infty.
\]

:::

:::

::: pf-step

Therefore, in the situation of step <1>9,
\[
\limsup(a_n+b_n)
=
-\infty
=
A+B.
\]


::: pf-proof

The extended-real sum of \(-\infty\) and a finite real number is
\(-\infty\).

:::

:::

::: pf-step

The symmetric case
\[
B=-\infty,
\qquad
A\in\mathbb R
\]
is identical.


::: pf-proof

Interchange the roles of the two sequences in step <1>9.

:::

:::

::: pf-step

If
\[
A=B=-\infty,
\]
then
\[
\boxed{
\limsup(a_n+b_n)=-\infty}.
\]


::: pf-proof

Fix \(M\in\mathbb R\). Since both limsups equal \(-\infty\), eventually
\[
a_n\le\frac M2
\qquad\text{and}\qquad
b_n\le\frac M2.
\]
Hence eventually
\[
a_n+b_n\le M.
\]
Since \(M\) is arbitrary, the limsup is \(-\infty\).

:::

:::

::: pf-step

Combining the finite and extended-real cases,
\[
\boxed{
\limsup_{n\to\infty}(a_n+b_n)
\le
\limsup_{n\to\infty}a_n
+
\limsup_{n\to\infty}b_n}
\]
whenever the right-hand side is defined, that is, except for the indeterminate
forms
\[
+\infty+(-\infty)
\]
and
\[
(-\infty)+(+\infty).
\]


::: pf-proof

The finite case is step <1>6, the \(+\infty\) cases are steps <1>7--<1>8,
the finite-plus-\(-\infty\) cases are steps <1>9--<1>11, and the
\(-\infty-\infty\) case is step <1>12.

:::

:::

::: pf-step

One has
\[
\boxed{
\limsup a_n=1}.
\]


::: pf-proof

The sequence \(a_n\) alternates between \(1\) and \(-1\), and the value
\(1\) occurs infinitely often.

:::

:::

::: pf-step

One also has
\[
\boxed{
\limsup b_n=1}.
\]


::: pf-proof

The sequence \(b_n\) also alternates between \(1\) and \(-1\), with \(1\)
occurring infinitely often.

:::

:::

::: pf-step

But
\[
\boxed{
a_n+b_n=0}
\]
for every \(n\).


::: pf-proof

By definition,
\[
(-1)^n-(-1)^n=0.
\]

:::

:::

::: pf-step

Hence
\[
\boxed{
\limsup(a_n+b_n)=0}.
\]


::: pf-proof

The sequence is identically zero by step <1>16.

:::

:::

::: pf-step

Therefore
\[
\boxed{
0
=
\limsup(a_n+b_n)
<
2
=
\limsup a_n+\limsup b_n}.
\]


::: pf-proof

Use steps <1>14--<1>17.

:::

:::

::: pf-step

Thus the inequality can be strict.


::: pf-proof

Step <1>18 gives an explicit strict example.

:::

:::

::: pf-qed

Step <1>13 proves part (a), and steps <1>14--<1>19 prove part (b).

:::

:::
