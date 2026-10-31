---
schema: qual/card@1
id: P-SERIES-A2-01
kind: problem
title: Subadditivity of $\limsup$
classification:
  areas:
  - real-analysis
  topics:
  - Limit Superior
  - Sequences
relations: []
review: draft
---

::: {.problem}
(a) For any two sequences $\{a_n\}$ and $\{b_n\}$, show that
$$
\limsup_{n\to\infty}(a_n+b_n)\le \limsup_{n\to\infty}a_n+\limsup_{n\to\infty}b_n,
$$
unless the right-hand side is of the form $\infty-\infty$.

(b) Find sequences $\{a_n\}$ and $\{b_n\}$ for which the inequality is strict.
:::

::: {.solution}

Write
$$
A=\limsup_{n\to\infty}a_n,
\qquad
B=\limsup_{n\to\infty}b_n.
$$

## Part (a)

::: pf

::: pf-step

Assume first that
$$
A,B\in\RR.
$$
Fix
$$
\varepsilon>0.
$$


::: pf-proof

This is the main finite-valued case.

:::

:::

::: {.pf-step #s1-2}

There exists $N_1$ such that
$$
\boxed{
a_n\le A+\varepsilon}
$$
for every $n\ge N_1$.


::: pf-proof

By the definition of $\limsup$, for every $\varepsilon>0$, all
sufficiently late terms lie below $A+\varepsilon$.

:::

:::

::: {.pf-step #s1-3}

There exists $N_2$ such that
$$
\boxed{
b_n\le B+\varepsilon}
$$
for every $n\ge N_2$.


::: pf-proof

Apply the same property to the sequence $(b_n)$.

:::

:::

::: {.pf-step #s1-4}

For
$$
N=\max(N_1,N_2)
$$
and every $n\ge N$,
$$
a_n+b_n
\le
A+B+2\varepsilon.
$$


::: pf-proof

Add the inequalities from steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Hence
$$
\limsup_{n\to\infty}(a_n+b_n)
\le
A+B+2\varepsilon.
$$


::: pf-proof

Every sufficiently late term of the sequence $(a_n+b_n)$ is bounded above
by the right-hand side of step [](#s1-4){.pf-ref}, so its limsup is also bounded above by
that number.

:::

:::

::: {.pf-step #s1-6}

Letting $\varepsilon\downarrow0$,
$$
\boxed{
\limsup_{n\to\infty}(a_n+b_n)
\le
A+B}.
$$


::: pf-proof

Step [](#s1-5){.pf-ref} holds for every positive $\varepsilon$.

:::

:::

::: {.pf-step #s1-7}

If
$$
A=+\infty
$$
and
$$
B>-\infty,
$$
then the desired inequality is automatic.


::: pf-proof

In this case
$$
A+B=+\infty.
$$
Every extended real number is at most $+\infty$.

:::

:::

::: {.pf-step #s1-8}

The same conclusion holds if
$$
B=+\infty
$$
and
$$
A>-\infty.
$$


::: pf-proof

The right-hand side is again $+\infty$.

:::

:::

::: {.pf-step #s1-9}

Suppose
$$
A=-\infty
$$
and
$$
B\in\RR.
$$
Then
$$
\boxed{
\limsup_{n\to\infty}(a_n+b_n)=-\infty}.
$$


::: pf-proof

Fix any real number $M$. Since
$$
A=-\infty,
$$
there exists $N_1$ such that
$$
a_n\le M-(B+1)
$$
for all $n\ge N_1$.

Since
$$
B\in\RR,
$$
there exists $N_2$ such that
$$
b_n\le B+1
$$
for all $n\ge N_2$.

Thus for all sufficiently large $n$,
$$
a_n+b_n\le M.
$$
Because $M$ was arbitrary,
$$
\limsup(a_n+b_n)=-\infty.
$$

:::

:::

::: {.pf-step #s1-10}

Therefore, in the situation of step [](#s1-9){.pf-ref},
$$
\limsup(a_n+b_n)
=
-\infty
=
A+B.
$$


::: pf-proof

The extended-real sum of $-\infty$ and a finite real number is
$-\infty$.

:::

:::

::: {.pf-step #s1-11}

The symmetric case
$$
B=-\infty,
\qquad
A\in\RR
$$
is identical.


::: pf-proof

Interchange the roles of the two sequences in step [](#s1-9){.pf-ref}.

:::

:::

::: {.pf-step #s1-12}

If
$$
A=B=-\infty,
$$
then
$$
\boxed{
\limsup(a_n+b_n)=-\infty}.
$$


::: pf-proof

Fix $M\in\RR$. Since both limsups equal $-\infty$, eventually
$$
a_n\le\frac M2
\qquad\text{and}\qquad
b_n\le\frac M2.
$$
Hence eventually
$$
a_n+b_n\le M.
$$
Since $M$ is arbitrary, the limsup is $-\infty$.

:::

:::

::: {.pf-step #s1-13}

Combining the finite and extended-real cases,
$$
\boxed{
\limsup_{n\to\infty}(a_n+b_n)
\le
\limsup_{n\to\infty}a_n
+
\limsup_{n\to\infty}b_n}
$$
whenever the right-hand side is defined, that is, except for the indeterminate
forms
$$
+\infty+(-\infty)
$$
and
$$
(-\infty)+(+\infty).
$$


::: pf-proof

The finite case is step [](#s1-6){.pf-ref}, the $+\infty$ cases are steps [](#s1-7){.pf-ref} through [](#s1-8){.pf-ref},
the finite-plus-$-\infty$ cases are steps [](#s1-9){.pf-ref} through [](#s1-11){.pf-ref}, and the
$-\infty-\infty$ case is step [](#s1-12){.pf-ref}.

:::

:::

::: {.pf-step #s1-14}

One has
$$
\boxed{
\limsup a_n=1}.
$$


::: pf-proof

The sequence $a_n$ alternates between $1$ and $-1$, and the value
$1$ occurs infinitely often.

:::

:::

::: {.pf-step #s1-15}

One also has
$$
\boxed{
\limsup b_n=1}.
$$


::: pf-proof

The sequence $b_n$ also alternates between $1$ and $-1$, with $1$
occurring infinitely often.

:::

:::

::: {.pf-step #s1-16}

But
$$
\boxed{
a_n+b_n=0}
$$
for every $n$.


::: pf-proof

By definition,
$$
(-1)^n-(-1)^n=0.
$$

:::

:::

::: {.pf-step #s1-17}

Hence
$$
\boxed{
\limsup(a_n+b_n)=0}.
$$


::: pf-proof

The sequence is identically zero by step [](#s1-16){.pf-ref}.

:::

:::

::: {.pf-step #s1-18}

Therefore
$$
\boxed{
0
=
\limsup(a_n+b_n)
<
2
=
\limsup a_n+\limsup b_n}.
$$


::: pf-proof

Use steps [](#s1-14){.pf-ref} through [](#s1-17){.pf-ref}.

:::

:::

::: {.pf-step #s1-19}

Thus the inequality can be strict.


::: pf-proof

Step [](#s1-18){.pf-ref} gives an explicit strict example.

:::

:::

::: pf-qed

Step [](#s1-13){.pf-ref} proves part (a), and steps [](#s1-14){.pf-ref} through [](#s1-19){.pf-ref} prove part (b).

:::

:::

:::
