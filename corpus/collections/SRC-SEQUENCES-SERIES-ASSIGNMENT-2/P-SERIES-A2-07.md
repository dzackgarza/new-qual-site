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
$$
f_0=f_1=1,\qquad f_{n+1}=f_n+f_{n-1}\quad(n\ge1),
$$
and for $n\ge1$ define $r_n=f_{n+1}/f_n$.

(a) Find a formula for $r_{n+1}$ in terms of $r_n$.

(b) Show that $f_n\ge n$ for all $n\ge2$.

(c) Show that
$$
f_{n+1}f_{n-1}-f_n^2=(-1)^{n+1}.
$$

(d) Hence show that, for $n\ge2$,
$$
|r_{n+1}-r_n|\le \frac1{(n-1)^2}.
$$

(e) Hence show that $\{r_n\}$ converges and compute its limit.
:::

::: {.solution}

## Part (a)

::: pf

::: {.pf-step #s1-1}

For $n\ge1$,
$$
r_{n+1}
=
\frac{f_{n+2}}{f_{n+1}}.
$$


::: pf-proof

This is the definition of $r_{n+1}$.

:::

:::

::: {.pf-step #s1-2}

Using the Fibonacci recurrence,
$$
f_{n+2}=f_{n+1}+f_n.
$$


::: pf-proof

Apply
$$
f_{m+1}=f_m+f_{m-1}
$$
with $m=n+1$.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{
r_{n+1}
=
1+\frac1{r_n}}.
$$


::: pf-proof

By steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref},
$$
\begin{aligned}
r_{n+1}
&=
\frac{f_{n+1}+f_n}{f_{n+1}}\\
&=
1+\frac{f_n}{f_{n+1}}\\
&=
1+\frac1{r_n}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-4}

One has
$$
\boxed{f_2=2}.
$$


::: pf-proof

$$
f_2=f_1+f_0=1+1=2.
$$

:::

:::

::: {.pf-step #s1-5}

Also,
$$
\boxed{f_3=3}.
$$


::: pf-proof

$$
f_3=f_2+f_1=2+1=3.
$$

:::

:::

::: {.pf-step #s1-6}

Suppose for some $n\ge3$ that
$$
f_n\ge n
$$
and
$$
f_{n-1}\ge n-1.
$$
Then
$$
f_{n+1}\ge n+1.
$$


::: pf-proof

Using the recurrence,
$$
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
$$
because $n\ge2$.

:::

:::

::: {.pf-step #s1-7}

Hence
$$
\boxed{
f_n\ge n
\qquad(n\ge2)}.
$$


::: pf-proof

Steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref} give the initial cases, and step [](#s1-6){.pf-ref} gives the induction
step.

:::

:::

::: {.pf-step #s1-8}

The initial value is
$$
\boxed{C_1=1}.
$$


::: pf-proof

$$
C_1
=
f_2f_0-f_1^2
=
2\cdot1-1
=
1.
$$

:::

:::

::: {.pf-step #s1-9}

The sequence $(C_n)$ satisfies
$$
\boxed{
C_{n+1}=-C_n}.
$$


::: pf-proof

$$
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
$$

:::

:::

::: {.pf-step #s1-10}

Therefore
$$
\boxed{
f_{n+1}f_{n-1}-f_n^2
=
(-1)^{n+1}}.
$$


::: pf-proof

From step [](#s1-8){.pf-ref},
$$
C_1=1=(-1)^2.
$$
Step [](#s1-9){.pf-ref} says the sign flips at each step, giving
$$
C_n=(-1)^{n+1}.
$$

:::

:::

::: {.pf-step #s1-11}

For $n\ge1$,
$$
r_{n+1}-r_n
=
\frac{
f_{n+2}f_n-f_{n+1}^2
}{
f_{n+1}f_n
}.
$$


::: pf-proof

Subtract:
$$
\frac{f_{n+2}}{f_{n+1}}
-
\frac{f_{n+1}}{f_n}.
$$

:::

:::

::: {.pf-step #s1-12}

By part (c),
$$
\boxed{
f_{n+2}f_n-f_{n+1}^2
=
(-1)^n}.
$$


::: pf-proof

Apply step [](#s1-10){.pf-ref} with $n$ replaced by $n+1$:
$$
f_{n+2}f_n-f_{n+1}^2
=
(-1)^{n+2}
=
(-1)^n.
$$

:::

:::

::: {.pf-step #s1-13}

Therefore
$$
\boxed{
|r_{n+1}-r_n|
=
\frac1{f_nf_{n+1}}}.
$$


::: pf-proof

Combine steps [](#s1-11){.pf-ref} through [](#s1-12){.pf-ref} and take absolute values.

:::

:::

::: {.pf-step #s1-14}

For $n\ge2$,
$$
f_n\ge n
\qquad\text{and}\qquad
f_{n+1}\ge n+1.
$$


::: pf-proof

Apply step [](#s1-7){.pf-ref} at indices $n$ and $n+1$.

:::

:::

::: {.pf-step #s1-15}

Hence
$$
|r_{n+1}-r_n|
\le
\frac1{n(n+1)}.
$$


::: pf-proof

Use step [](#s1-13){.pf-ref} and the lower bounds in step [](#s1-14){.pf-ref}.

:::

:::

::: {.pf-step #s1-16}

For $n\ge2$,
$$
\frac1{n(n+1)}
\le
\frac1{(n-1)^2}.
$$


::: pf-proof

It suffices to show
$$
(n-1)^2\le n(n+1).
$$
Expanding,
$$
n^2-2n+1\le n^2+n,
$$
equivalent to
$$
1\le3n,
$$
which holds for $n\ge1$.

:::

:::

::: {.pf-step #s1-17}

Thus
$$
\boxed{
|r_{n+1}-r_n|
\le
\frac1{(n-1)^2}}
\qquad(n\ge2).
$$


::: pf-proof

Combine steps [](#s1-15){.pf-ref} through [](#s1-16){.pf-ref}.

:::

:::

::: {.pf-step #s1-18}

Let $m>n\ge2$. Then
$$
r_m-r_n
=
\sum_{k=n}^{m-1}
(r_{k+1}-r_k).
$$


::: pf-proof

The sum telescopes.

:::

:::

::: {.pf-step #s1-19}

Hence
$$
|r_m-r_n|
\le
\sum_{k=n}^{m-1}
|r_{k+1}-r_k|.
$$


::: pf-proof

Apply the triangle inequality to step [](#s1-18){.pf-ref}.

:::

:::

::: pf-step

By step [](#s1-17){.pf-ref},
$$
|r_m-r_n|
\le
\sum_{k=n}^{m-1}
\frac1{(k-1)^2}.
$$


::: pf-proof

Bound each summand in step [](#s1-19){.pf-ref}.

:::

:::

::: {.pf-step #s1-21}

Therefore
$$
|r_m-r_n|
\le
\sum_{j=n-1}^{\infty}
\frac1{j^2}.
$$


::: pf-proof

Extend the finite nonnegative sum to the full tail of the convergent
$p$-series.

:::

:::

::: pf-step

The right-hand side in step [](#s1-21){.pf-ref} tends to $0$ as
$$
n\to\infty.
$$


::: pf-proof

The series
$$
\sum_{j=1}^{\infty}\frac1{j^2}
$$
converges, so its tails tend to zero.

:::

:::

::: {.pf-step #s1-23}

Hence $(r_n)$ is Cauchy.


::: pf-proof

Given $\varepsilon>0$, choose $N$ so that the tail in step [](#s1-21){.pf-ref} is less
than $\varepsilon$ for $n\ge N$. Then every $m>n\ge N$ satisfies
$$
|r_m-r_n|<\varepsilon.
$$

:::

:::

::: {.pf-step #s1-24}

Since $\RR$ is complete, there exists
$$
L\in\RR
$$
such that
$$
\boxed{r_n\to L}.
$$


::: pf-proof

Every real Cauchy sequence converges.

:::

:::

::: {.pf-step #s1-25}

Each $r_n$ is positive, and in fact
$$
r_n>1.
$$


::: pf-proof

All Fibonacci numbers are positive. Also
$$
f_{n+1}=f_n+f_{n-1}>f_n
$$
for $n\ge1$, so
$$
r_n=\frac{f_{n+1}}{f_n}>1.
$$

:::

:::

::: {.pf-step #s1-26}

Therefore
$$
\boxed{L\ge1}.
$$


::: pf-proof

The limit of a sequence whose terms are all greater than $1$ is at least
$1$.

:::

:::

::: {.pf-step #s1-27}

Passing to the limit in
$$
r_{n+1}=1+\frac1{r_n},
$$
one obtains
$$
\boxed{
L=1+\frac1L}.
$$


::: pf-proof

By step [](#s1-24){.pf-ref},
$$
r_{n+1}\to L
$$
as well. By step [](#s1-26){.pf-ref}, $L\ne0$, so the reciprocal function is continuous
at $L$. Take limits in step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-28}

Thus
$$
L^2-L-1=0.
$$


::: pf-proof

Multiply step [](#s1-27){.pf-ref} by $L$.

:::

:::

::: {.pf-step #s1-29}

The two algebraic roots are
$$
\frac{1+\sqrt5}{2}
\qquad\text{and}\qquad
\frac{1-\sqrt5}{2}.
$$


::: pf-proof

Apply the quadratic formula to
$$
L^2-L-1=0.
$$

:::

:::

::: {.pf-step #s1-30}

Since $L\ge1$,
$$
\boxed{
L=\frac{1+\sqrt5}{2}}.
$$


::: pf-proof

The second root is negative, while step [](#s1-26){.pf-ref} gives $L\ge1$.

:::

:::

::: {.pf-step #s1-31}

Therefore
$$
\boxed{
\lim_{n\to\infty}
\frac{f_{n+1}}{f_n}
=
\frac{1+\sqrt5}{2}}.
$$


::: pf-proof

Use the definition $r_n=f_{n+1}/f_n$ and step [](#s1-30){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves part (a), step [](#s1-7){.pf-ref} proves part (b), step [](#s1-10){.pf-ref} proves part
(c), step [](#s1-17){.pf-ref} proves part (d), and steps [](#s1-23){.pf-ref} through [](#s1-31){.pf-ref} prove part (e).

:::

:::

:::
