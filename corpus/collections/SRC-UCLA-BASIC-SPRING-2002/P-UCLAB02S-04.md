---
schema: qual/card@1
id: P-UCLAB02S-04
kind: problem
title: Uniform continuity and continuous extension from the open unit interval
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 4 of the official UCLA Basic Exam Spring 2002 PDF.
---

::: {.problem}
(a) Define uniform continuity for a function $F:X\to\RR$, where $X$ is a metric space.

(b) Prove that a function $f:(0,1)\to\RR$ is the restriction to $(0,1)$ of a continuous function $F:[0,1]\to\RR$ if and only if $f$ is uniformly continuous on $(0,1)$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

A function
\[
F:X\to\RR
\]
is uniformly continuous if for every $\varepsilon>0$ there exists $\delta>0$ such that for all $x,y\in X$,
\[
d(x,y)<\delta
\]
implies
\[
|F(x)-F(y)|<\varepsilon.
\]


::: pf-proof

This is the definition of uniform continuity.
The crucial point is that the same $\delta$ works simultaneously for every pair $x,y\in X$.

:::

:::

::: {.pf-step #s1-2}

Suppose there exists a continuous
\[
F:[0,1]\to\RR
\]
whose restriction to $(0,1)$ is $f$.
Then $f$ is uniformly continuous on $(0,1)$.


::: pf-proof

The interval $[0,1]$ is compact.
By the Heine--Cantor theorem, the continuous function $F$ is uniformly continuous on $[0,1]$.
Thus for every $\varepsilon>0$ there is $\delta>0$ such that
\[
|x-y|<\delta
\]
implies
\[
|F(x)-F(y)|<\varepsilon
\]
for all $x,y\in[0,1]$.
In particular, this holds for all $x,y\in(0,1)$.
Since
\[
F|_{(0,1)}=f,
\]
the function $f$ is uniformly continuous.

:::

:::

::: {.pf-step #s1-3}

Conversely, assume $f:(0,1)\to\RR$ is uniformly continuous.
Then for every sequence $(x_n)$ in $(0,1)$ with
\[
x_n\to0,
\]
the sequence $(f(x_n))$ is Cauchy.


::: pf-proof

Let $\varepsilon>0$.
Uniform continuity gives $\delta>0$ such that
\[
|x-y|<\delta
\]
implies
\[
|f(x)-f(y)|<\varepsilon.
\]
Since $x_n\to0$, there exists $N$ such that
\[
0<x_n<\frac{\delta}{2}
\]
for all $n\ge N$.
Thus for $m,n\ge N$,
\[
|x_n-x_m|
\le
x_n+x_m
<
\delta.
\]
Hence
\[
|f(x_n)-f(x_m)|<\varepsilon.
\]
So $(f(x_n))$ is Cauchy.

:::

:::

::: {.pf-step #s1-4}

There exists a real number $L_0$ such that
\[
\lim_{x\to0^+}f(x)=L_0.
\]


::: pf-proof

Choose one sequence
\[
x_n\in(0,1),
\qquad
x_n\to0.
\]
By step [](#s1-3){.pf-ref}, $(f(x_n))$ is Cauchy, so completeness of $\RR$ gives
\[
f(x_n)\to L_0
\]
for some $L_0\in\RR$.

It remains to show that every sequence approaching $0$ has the same image limit.
Let
\[
y_n\to0
\]
with $y_n\in(0,1)$.
Uniform continuity implies
\[
|f(x_n)-f(y_n)|\to0,
\]
because
\[
|x_n-y_n|
\le
x_n+y_n
\to0.
\]
Since
\[
f(x_n)\to L_0,
\]
it follows that
\[
f(y_n)\to L_0.
\]
By the sequential criterion for one-sided limits,
\[
\lim_{x\to0^+}f(x)=L_0.
\]

:::

:::

::: {.pf-step #s1-5}

There exists a real number $L_1$ such that
\[
\lim_{x\to1^-}f(x)=L_1.
\]


::: pf-proof

Apply the same argument as in steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref} to sequences
\[
x_n\to1
\]
inside $(0,1)$.
If
\[
x_n,y_n\to1,
\]
then
\[
|x_n-y_n|
\le
|1-x_n|+|1-y_n|
\to0,
\]
so uniform continuity forces
\[
|f(x_n)-f(y_n)|\to0.
\]
Thus the one-sided limit exists and is finite.

:::

:::

::: {.pf-step #s1-6}

Define
\[
F:[0,1]\to\RR
\]
by
\[
F(x)=
\begin{cases}
L_0,&x=0,\\
f(x),&0<x<1,\\
L_1,&x=1.
\end{cases}
\]
Then $F$ is continuous on $[0,1]$.


::: pf-proof

On $(0,1)$, the function $F$ equals $f$.
Uniform continuity implies ordinary continuity, so $f$ is continuous there.

At $0$, step [](#s1-4){.pf-ref} gives
\[
\lim_{x\to0^+}F(x)
=
\lim_{x\to0^+}f(x)
=
L_0
=
F(0).
\]
Thus $F$ is continuous at $0$.

At $1$, step [](#s1-5){.pf-ref} gives
\[
\lim_{x\to1^-}F(x)
=
\lim_{x\to1^-}f(x)
=
L_1
=
F(1).
\]
Thus $F$ is continuous at $1$.
Hence $F$ is continuous on all of $[0,1]$.

:::

:::

::: {.pf-step #s1-7}

Therefore
\[
\boxed{
f\text{ extends continuously to }[0,1]
\iff
f\text{ is uniformly continuous on }(0,1)
}.
\]


::: pf-proof

Step [](#s1-2){.pf-ref} proves the forward implication.
Steps [](#s1-3){.pf-ref} through [](#s1-6){.pf-ref} prove the reverse implication.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} answers part (a), and step [](#s1-7){.pf-ref} proves part (b).

:::

:::

:::
