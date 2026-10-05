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

<1>1. A function $f:[0,1]\to\mathbb R$ that is not Riemann integrable although $|f|$ is Riemann integrable.
<1>2. Continuous functions $f_n,f:[0,1]\to\mathbb R$ such that $f_n(t)\to f(t)$ for every $t\in[0,1]$, but
\[
\int_0^1 f_n(t)\,dt
\]
does not converge to
\[
\int_0^1 f(t)\,dt.
\]
:::

::: {.solution}
<1>1. For part <1>1, define
\[
f(x)
=
\begin{cases}
1,&x\in\mathbb Q,\\
-1,&x\notin\mathbb Q.
\end{cases}
\]
Then
\[
\boxed{|f(x)|=1}
\]
for every
\[
x\in[0,1].
\]

::: {.proof}
Both possible values of $f$ have absolute value $1$.
:::

<1>2. The function $|f|$ is Riemann integrable.

::: {.proof}
By step <1>1,
\[
|f|\equiv1.
\]
Constant functions are Riemann integrable, with
\[
\int_0^1|f(x)|\,dx=1.
\]
:::

<1>3. The function $f$ is discontinuous at every point of $[0,1]$.

::: {.proof}
Fix
\[
x_0\in[0,1].
\]
Every neighborhood of $x_0$ contains rational and irrational numbers because both sets are dense in $\mathbb R$.
Along rational points approaching $x_0$, the function value is $1$.
Along irrational points approaching $x_0$, the function value is $-1$.
Hence
\[
\lim_{x\to x_0}f(x)
\]
does not exist.
Thus $f$ is discontinuous at $x_0$.
Since $x_0$ was arbitrary, $f$ is discontinuous everywhere.
:::

<1>4. The function $f$ is not Riemann integrable.

::: {.proof}
On every nondegenerate subinterval of $[0,1]$, both rational and irrational points occur.
Hence on every such interval,
\[
\sup f=1
\qquad\text{and}\qquad
\inf f=-1.
\]
Therefore for every partition $P$ of $[0,1]$,
\[
U(f,P)=1
\]
and
\[
L(f,P)=-1.
\]
The upper and lower Darboux integrals are different.
Thus $f$ is not Riemann integrable.
This completes part <1>1.
:::

<1>5. For part <1>2, define for
\[
n\ge2
\]
the continuous function
\[
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
\]
Also define
\[
\boxed{f(x)=0}.
\]

::: {.proof}
At
\[
x=\frac1n,
\]
the first two formulas both equal
\[
n.
\]
At
\[
x=\frac2n,
\]
the second formula equals $0$.
Thus $f_n$ is continuous on $[0,1]$.
The limiting function $f\equiv0$ is also continuous.
:::

<1>6. For every fixed
\[
x\in[0,1],
\]
one has
\[
f_n(x)\to0=f(x).
\]

::: {.proof}
If
\[
x=0,
\]
then
\[
f_n(0)=0
\]
for every $n$.

Fix
\[
x>0.
\]
Since
\[
\frac2n\to0,
\]
for all sufficiently large $n$ one has
\[
\frac2n<x.
\]
Then
\[
f_n(x)=0.
\]
Hence
\[
f_n(x)\to0.
\]
Thus the convergence is pointwise on all of $[0,1]$.
:::

<1>7. For every $n\ge2$,
\[
\boxed{
\int_0^1f_n(x)\,dx=1.
}
\]

::: {.proof}
The graph of $f_n$ is a triangle with base
\[
\frac2n
\]
and height
\[
n.
\]
Therefore its area is
\[
\frac12\cdot\frac2n\cdot n
=1.
\]
:::

<1>8. The integrals do not converge to the integral of the pointwise limit.

::: {.proof}
By step <1>7,
\[
\int_0^1f_n(x)\,dx
=1
\]
for every $n$.
Thus
\[
\lim_{n\to\infty}
\int_0^1f_n(x)\,dx
=1.
\]
But
\[
f\equiv0,
\]
so
\[
\int_0^1f(x)\,dx=0.
\]
Therefore
\[
\boxed{
\lim_{n\to\infty}\int_0^1f_n
\ne
\int_0^1f.
}
\]
:::

<1>9. Q.E.D.

::: {.proof}
Steps <1>1--<1>4 give the example required in part <1>1, and steps <1>5--<1>8 give the example required in part <1>2.
:::
:::
