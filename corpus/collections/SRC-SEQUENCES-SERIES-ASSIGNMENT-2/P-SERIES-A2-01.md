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

::: {.solution}
Write
\[
A=\limsup_{n\to\infty}a_n,
\qquad
B=\limsup_{n\to\infty}b_n.
\]

## Part (a)

<1>1. Assume first that
\[
A,B\in\mathbb R.
\]
Fix
\[
\varepsilon>0.
\]

::: {.proof}
This is the main finite-valued case.
:::

<1>2. There exists \(N_1\) such that
\[
\boxed{
a_n\le A+\varepsilon}
\]
for every \(n\ge N_1\).

::: {.proof}
By the definition of \(\limsup\), for every \(\varepsilon>0\), all
sufficiently late terms lie below \(A+\varepsilon\).
:::

<1>3. There exists \(N_2\) such that
\[
\boxed{
b_n\le B+\varepsilon}
\]
for every \(n\ge N_2\).

::: {.proof}
Apply the same property to the sequence \((b_n)\).
:::

<1>4. For
\[
N=\max(N_1,N_2)
\]
and every \(n\ge N\),
\[
a_n+b_n
\le
A+B+2\varepsilon.
\]

::: {.proof}
Add the inequalities from steps <1>2--<1>3.
:::

<1>5. Hence
\[
\limsup_{n\to\infty}(a_n+b_n)
\le
A+B+2\varepsilon.
\]

::: {.proof}
Every sufficiently late term of the sequence \((a_n+b_n)\) is bounded above
by the right-hand side of step <1>4, so its limsup is also bounded above by
that number.
:::

<1>6. Letting \(\varepsilon\downarrow0\),
\[
\boxed{
\limsup_{n\to\infty}(a_n+b_n)
\le
A+B}.
\]

::: {.proof}
Step <1>5 holds for every positive \(\varepsilon\).
:::

<1>7. If
\[
A=+\infty
\]
and
\[
B>-\infty,
\]
then the desired inequality is automatic.

::: {.proof}
In this case
\[
A+B=+\infty.
\]
Every extended real number is at most \(+\infty\).
:::

<1>8. The same conclusion holds if
\[
B=+\infty
\]
and
\[
A>-\infty.
\]

::: {.proof}
The right-hand side is again \(+\infty\).
:::

<1>9. Suppose
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

::: {.proof}
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

<1>10. Therefore, in the situation of step <1>9,
\[
\limsup(a_n+b_n)
=
-\infty
=
A+B.
\]

::: {.proof}
The extended-real sum of \(-\infty\) and a finite real number is
\(-\infty\).
:::

<1>11. The symmetric case
\[
B=-\infty,
\qquad
A\in\mathbb R
\]
is identical.

::: {.proof}
Interchange the roles of the two sequences in step <1>9.
:::

<1>12. If
\[
A=B=-\infty,
\]
then
\[
\boxed{
\limsup(a_n+b_n)=-\infty}.
\]

::: {.proof}
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

<1>13. Combining the finite and extended-real cases,
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

::: {.proof}
The finite case is step <1>6, the \(+\infty\) cases are steps <1>7--<1>8,
the finite-plus-\(-\infty\) cases are steps <1>9--<1>11, and the
\(-\infty-\infty\) case is step <1>12.
:::

## Part (b)

Define
\[
\boxed{
a_n=(-1)^n,
\qquad
b_n=-(-1)^n}.
\]

::: {.proof}
These are two bounded real sequences.
:::

<1>14. One has
\[
\boxed{
\limsup a_n=1}.
\]

::: {.proof}
The sequence \(a_n\) alternates between \(1\) and \(-1\), and the value
\(1\) occurs infinitely often.
:::

<1>15. One also has
\[
\boxed{
\limsup b_n=1}.
\]

::: {.proof}
The sequence \(b_n\) also alternates between \(1\) and \(-1\), with \(1\)
occurring infinitely often.
:::

<1>16. But
\[
\boxed{
a_n+b_n=0}
\]
for every \(n\).

::: {.proof}
By definition,
\[
(-1)^n-(-1)^n=0.
\]
:::

<1>17. Hence
\[
\boxed{
\limsup(a_n+b_n)=0}.
\]

::: {.proof}
The sequence is identically zero by step <1>16.
:::

<1>18. Therefore
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

::: {.proof}
Use steps <1>14--<1>17.
:::

<1>19. Thus the inequality can be strict.

::: {.proof}
Step <1>18 gives an explicit strict example.
:::

<1>20. Q.E.D.

::: {.proof}
Step <1>13 proves part (a), and steps <1>14--<1>19 prove part (b).
:::
:::
