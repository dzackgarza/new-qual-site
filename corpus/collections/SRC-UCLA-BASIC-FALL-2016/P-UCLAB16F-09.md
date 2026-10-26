---
schema: qual/card@1
id: P-UCLAB16F-09
kind: problem
title: Equicontinuity and uniform convergence on $[0,1]$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 9 of the retained UCLA Basic Examination Fall 2016 PDF.
---

::: {.problem}
Let $f _ { n } : [ 0 , 1 ] \to \mathbb { C }$ be a sequence of continuous functions.
Suppose $f _ { n }$ converge pointwise.
Show that the sequence converges uniformly if and only if the collection of functions $\left\{ f _ { n } \right\}$ is equicontinuous.
:::

Let
\[
f(x)=\lim_{n\to\infty}f_n(x)
\]
for
\[
x\in[0,1].
\]

::: pf

::: pf-step

Suppose first that
\[
f_n\to f
\]
uniformly.
Then $f$ is continuous.


::: pf-proof

A uniform limit of continuous functions on a metric space is continuous.

:::

:::

::: pf-step

Under uniform convergence, the family
\[
\{f_n:n\ge1\}
\]
is equicontinuous.


::: pf-proof

Fix $\varepsilon>0$.
Choose $N$ such that
\[
\|f_n-f\|_\infty<\frac{\varepsilon}{3}
\]
for every $n\ge N$.

By step <1>1, $f$ is continuous on the compact interval $[0,1]$, hence uniformly continuous.
Choose $\delta_0>0$ such that
\[
|x-y|<\delta_0
\]
implies
\[
|f(x)-f(y)|<\frac{\varepsilon}{3}.
\]

For each of the finitely many functions
\[
f_1,\ldots,f_{N-1},
\]
uniform continuity on $[0,1]$ gives a number $\delta_j>0$ such that
\[
|x-y|<\delta_j
\]
implies
\[
|f_j(x)-f_j(y)|<\varepsilon.
\]
Set
\[
\delta
=
\min\{\delta_0,\delta_1,\ldots,\delta_{N-1}\}.
\]

If $n<N$, the desired estimate follows from the choice of $\delta_n$.
If $n\ge N$, then
\[
\begin{aligned}
|f_n(x)-f_n(y)|
&\le
|f_n(x)-f(x)|
+
|f(x)-f(y)|
+
|f(y)-f_n(y)|\\
&<
\frac{\varepsilon}{3}
+
\frac{\varepsilon}{3}
+
\frac{\varepsilon}{3}\\
&=
\varepsilon.
\end{aligned}
\]
Thus one $\delta$ works for every $n$, proving equicontinuity.

:::

:::

::: pf-step

Conversely, suppose the family $\{f_n\}$ is equicontinuous.
Then the pointwise limit $f$ is continuous.


::: pf-proof

Fix $\varepsilon>0$.
By equicontinuity, choose $\delta>0$ such that
\[
|x-y|<\delta
\]
implies
\[
|f_n(x)-f_n(y)|<\frac{\varepsilon}{3}
\]
for every $n$.

Fix $x,y$ with
\[
|x-y|<\delta.
\]
Taking $n\to\infty$ in
\[
|f_n(x)-f_n(y)|<\frac{\varepsilon}{3}
\]
gives
\[
|f(x)-f(y)|
\le
\frac{\varepsilon}{3}
<
\varepsilon.
\]
Thus $f$ is uniformly continuous, in particular continuous.

:::

:::

::: pf-step

Fix $\varepsilon>0$.
There exists $\delta>0$ such that
\[
|x-y|<\delta
\]
implies both
\[
|f_n(x)-f_n(y)|<\frac{\varepsilon}{3}
\]
for every $n$ and
\[
|f(x)-f(y)|<\frac{\varepsilon}{3}.
\]


::: pf-proof

Use equicontinuity of the family for tolerance $\varepsilon/3$.
The same $\delta$ works for $f$ by the limiting argument in step <1>3.

:::

:::

::: pf-step

There exist finitely many points
\[
x_1,\ldots,x_m\in[0,1]
\]
such that every $x\in[0,1]$ satisfies
\[
|x-x_j|<\delta
\]
for some $j$.


::: pf-proof

The open intervals
\[
(x-\delta,x+\delta),
\qquad
x\in[0,1],
\]
form an open cover of the compact interval $[0,1]$.
Choose a finite subcover and let its centers be $x_1,\ldots,x_m$.

:::

:::

::: pf-step

There exists $N$ such that for every $n\ge N$ and every
\[
j=1,\ldots,m,
\]
one has
\[
|f_n(x_j)-f(x_j)|<\frac{\varepsilon}{3}.
\]


::: pf-proof

For each fixed $x_j$, pointwise convergence gives an index $N_j$ such that the displayed estimate holds for $n\ge N_j$.
Take
\[
N=\max_jN_j.
\]

:::

:::

::: pf-step

For every $n\ge N$ and every $x\in[0,1]$,
\[
|f_n(x)-f(x)|<\varepsilon.
\]


::: pf-proof

Choose $x_j$ with
\[
|x-x_j|<\delta
\]
as in step <1>5.
Then steps <1>4 and <1>6 give
\[
\begin{aligned}
|f_n(x)-f(x)|
&\le
|f_n(x)-f_n(x_j)|
+
|f_n(x_j)-f(x_j)|
+
|f(x_j)-f(x)|\\
&<
\frac{\varepsilon}{3}
+
\frac{\varepsilon}{3}
+
\frac{\varepsilon}{3}\\
&=
\varepsilon.
\end{aligned}
\]

:::

:::

::: pf-step

Thus equicontinuity plus pointwise convergence implies uniform convergence.


::: pf-proof

Step <1>7 is exactly the definition of uniform convergence.

:::

:::

::: pf-step

Therefore
\[
\boxed{
f_n\to f\text{ uniformly}
\iff
\{f_n\}\text{ is equicontinuous}
}.
\]


::: pf-proof

Step <1>2 proves the forward implication, and step <1>8 proves the reverse implication.

:::

:::

::: pf-qed

Step <1>9 is the required equivalence.

:::

:::
