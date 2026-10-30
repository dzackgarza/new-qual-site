---
schema: qual/card@1
id: P-UCLAB11S-08
kind: problem
title: Counterexamples involving Riemann integration and pointwise convergence
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 8 of the retained UCLA Basic Examination, Spring 2011.
---
::: {.problem}
Give examples of the following.

::: pf

::: pf-step

A function $f:[0,1]\to\RR$ that is not Riemann integrable although $\abs{f}$ is Riemann integrable.

:::

::: pf-step

Continuous functions $f_n,f:[0,1]\to\RR$ such that $f_n(t)\to f(t)$ for every $t\in[0,1]$, but

:::

:::

$$
\int_0^1 f_n(t)\,dt
$$
does not converge to
$$
\int_0^1 f(t)\,dt.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #p2-s1}

For part step [](#p2-s1){.pf-ref}, define
$$
f(x)
=
\begin{cases}
1,&x\in\QQ,\\
-1,&x\notin\QQ.
\end{cases}
$$
Then
$$
\boxed{\abs{f(x)}=1}
$$
for every
$$
x\in[0,1].
$$

::: pf-proof

Both possible values of $f$ have absolute value $1$.

:::

:::

::: {.pf-step #p2-s2}

The function $\abs{f}$ is Riemann integrable.

::: pf-proof

By step [](#p2-s1){.pf-ref},
$$
\abs{f}\equiv1.
$$
Constant functions are Riemann integrable, with
$$
\int_0^1\abs{f(x)}\,dx=1.
$$

:::

:::

::: {.pf-step #p2-s3}

The function $f$ is discontinuous at every point of $[0,1]$.

::: pf-proof

Fix
$$
x_0\in[0,1].
$$
Every neighborhood of $x_0$ contains rational and irrational numbers because both sets are dense in $\RR$.
Along rational points approaching $x_0$, the function value is $1$.
Along irrational points approaching $x_0$, the function value is $-1$.
Hence
$$
\lim_{x\to x_0}f(x)
$$
does not exist.
Thus $f$ is discontinuous at $x_0$.
Since $x_0$ was arbitrary, $f$ is discontinuous everywhere.

:::

:::

::: {.pf-step #p2-s4}

The function $f$ is not Riemann integrable.

::: pf-proof

On every nondegenerate subinterval of $[0,1]$, both rational and irrational points occur.
Hence on every such interval,
$$
\sup f=1
\qquad\text{and}\qquad
\inf f=-1.
$$
Therefore for every partition $P$ of $[0,1]$,
$$
U(f,P)=1
$$
and
$$
L(f,P)=-1.
$$
The upper and lower Darboux integrals are different.
Thus $f$ is not Riemann integrable.
This completes part step [](#p2-s1){.pf-ref}.

:::

:::

::: {.pf-step #p2-s5}

For part step [](#p2-s2){.pf-ref}, define for
$$
n\ge2
$$
the continuous function
$$
f_n(x)
=
\begin{cases}
n^2x,
&0\le x\le \frac1n,\\[1mm]
n^2\left(\frac2n-x\right),
&\frac1n\le x\le\frac2n,\\[1mm]
0,
&\frac2n\le x\le1.
\end{cases}
$$
Also define
$$
\boxed{f(x)=0}.
$$

::: pf-proof

At
$$
x=\frac1n,
$$
the first two formulas both equal
$$
n.
$$
At
$$
x=\frac2n,
$$
the second formula equals $0$.
Thus $f_n$ is continuous on $[0,1]$.
The limiting function $f\equiv0$ is also continuous.

:::

:::

::: {.pf-step #p2-s6}

For every fixed
$$
x\in[0,1],
$$
one has
$$
f_n(x)\to0=f(x).
$$

::: pf-proof

If
$$
x=0,
$$
then
$$
f_n(0)=0
$$
for every $n$.

Fix
$$
x>0.
$$
Since
$$
\frac2n\to0,
$$
for all sufficiently large $n$ one has
$$
\frac2n<x.
$$
Then
$$
f_n(x)=0.
$$
Hence
$$
f_n(x)\to0.
$$
Thus the convergence is pointwise on all of $[0,1]$.

:::

:::

::: {.pf-step #p2-s7}

For every $n\ge2$,
$$
\boxed{
\int_0^1f_n(x)\,dx=1.
}
$$

::: pf-proof

The graph of $f_n$ is a triangle with base
$$
\frac2n
$$
and height
$$
n.
$$
Therefore its area is
$$
\frac12\cdot\frac2n\cdot n
=1.
$$

:::

:::

::: {.pf-step #p2-s8}

The integrals do not converge to the integral of the pointwise limit.

::: pf-proof

By step [](#p2-s7){.pf-ref},
$$
\int_0^1f_n(x)\,dx
=1
$$
for every $n$.
Thus
$$
\lim_{n\to\infty}
\int_0^1f_n(x)\,dx
=1.
$$
But
$$
f\equiv0,
$$
so
$$
\int_0^1f(x)\,dx=0.
$$
Therefore
$$
\boxed{
\lim_{n\to\infty}\int_0^1f_n
\ne
\int_0^1f.
}
$$

:::

:::

::: pf-qed

Steps [](#p2-s1){.pf-ref}, [](#p2-s2){.pf-ref}, [](#p2-s3){.pf-ref} and [](#p2-s4){.pf-ref} give the example required in part step [](#p2-s1){.pf-ref}, and steps [](#p2-s5){.pf-ref}, [](#p2-s6){.pf-ref}, [](#p2-s7){.pf-ref} and [](#p2-s8){.pf-ref} give the example required in part step [](#p2-s2){.pf-ref}.

:::

:::

:::
