---
schema: qual/card@1
id: P-UCLAB09S-06
kind: problem
title: Uniform continuity and extension to a closed interval
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 6 of the retained UCLA Basic Examination, Spring 2009.
---

::: {.problem}
Problem 6. Prove that a continuous function $f:[0,1)\to\mathbb R$ is uniformly continuous if and only if there exists a continuous function $g:[0,1]\to\mathbb R$ such that
\[
f(x)=g(x)\qquad(0\le x<1).
\]
:::

::: {.solution}
<1>1. Suppose first that there exists a continuous function
\[
g:[0,1]\to\mathbb R
\]
such that
\[
g|_{[0,1)}=f.
\]
Then $f$ is uniformly continuous on $[0,1)$.

::: {.proof}
The interval
\[
[0,1]
\]
is compact.
By the Heine--Cantor theorem, the continuous function $g$ is uniformly continuous on $[0,1]$.
Thus for every
\[
\varepsilon>0
\]
there exists
\[
\delta>0
\]
such that for all
\[
x,y\in[0,1],
\]
\[
|x-y|<\delta
\]
implies
\[
|g(x)-g(y)|<\varepsilon.
\]
In particular, the same implication holds for
\[
x,y\in[0,1).
\]
Since
\[
f=g
\]
there, $f$ is uniformly continuous.
:::

<1>2. Conversely, suppose $f$ is uniformly continuous on $[0,1)$.
Then the sequence
\[
\left(
f\left(1-\frac1n\right)
\right)_{n\ge2}
\]
is Cauchy.

::: {.proof}
Let
\[
\varepsilon>0.
\]
Choose
\[
\delta>0
\]
from uniform continuity.
For sufficiently large
\[
m,n,
\]
one has
\[
\left|
\left(1-\frac1m\right)
-
\left(1-\frac1n\right)
\right|
=
\left|
\frac1m-\frac1n
\right|
<
\delta.
\]
Hence
\[
\left|
f\left(1-\frac1m\right)
-
f\left(1-\frac1n\right)
\right|
<
\varepsilon.
\]
Thus the displayed sequence is Cauchy.
:::

<1>3. There exists
\[
L\in\mathbb R
\]
such that
\[
f\left(1-\frac1n\right)\to L.
\]

::: {.proof}
The real numbers are complete.
Apply completeness to the Cauchy sequence from step <1>2.
:::

<1>4. One has
\[
\boxed{
\lim_{x\to1^-}f(x)=L
}.
\]

::: {.proof}
Let
\[
\varepsilon>0.
\]
By uniform continuity, choose
\[
\delta>0
\]
such that
\[
|x-y|<\delta
\]
implies
\[
|f(x)-f(y)|<\frac{\varepsilon}{2}.
\]
Choose $N$ sufficiently large that
\[
\frac1N<\frac{\delta}{2}
\]
and
\[
\left|
f\left(1-\frac1N\right)-L
\right|
<
\frac{\varepsilon}{2}.
\]
If
\[
1-\frac{\delta}{2}<x<1,
\]
then
\[
\left|
x-\left(1-\frac1N\right)
\right|
\le
(1-x)+\frac1N
<
\delta.
\]
Therefore
\[
\left|
f(x)-f\left(1-\frac1N\right)
\right|
<
\frac{\varepsilon}{2}.
\]
Hence
\[
\begin{aligned}
|f(x)-L|
&\le
\left|
f(x)-f\left(1-\frac1N\right)
\right|
+
\left|
f\left(1-\frac1N\right)-L
\right|\\
&<
\varepsilon.
\end{aligned}
\]
Thus
\[
f(x)\to L
\]
as $x\to1^-$.
:::

<1>5. Define
\[
g:[0,1]\to\mathbb R
\]
by
\[
\boxed{
g(x)=
\begin{cases}
f(x),&0\le x<1,\\
L,&x=1.
\end{cases}
}
\]

::: {.proof}
The value $L$ is the finite one-sided limit supplied by step <1>4.
Thus the definition makes sense.
:::

<1>6. The function $g$ is continuous on $[0,1]$.

::: {.proof}
On
\[
[0,1),
\]
the function $g$ equals the continuous function $f$.
At the endpoint $1$, step <1>4 gives
\[
\lim_{x\to1^-}g(x)
=
\lim_{x\to1^-}f(x)
=
L
=
g(1).
\]
Thus $g$ is continuous at $1$ as well.
:::

<1>7. Therefore
\[
\boxed{
f\text{ is uniformly continuous on }[0,1)
\iff
f\text{ extends continuously to }[0,1].
}
\]

::: {.proof}
Step <1>1 proves the reverse implication.
Steps <1>2--<1>6 prove the forward implication.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the required equivalence.
:::
:::
