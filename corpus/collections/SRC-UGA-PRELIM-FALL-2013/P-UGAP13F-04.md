---
schema: qual/card@1
id: P-UGAP13F-04
kind: problem
title: Prove $1/(x^2-1)\to1/3$ at $x=2$ from the definition of limit
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Use the definition of a limit to show that
\[
\lim_{x\to2}\frac1{x^2-1}=\frac13.
\]
:::

::: {.solution}
<1>1. For
\[
x\ne\pm1,
\]
one has
\[
\left|
\frac1{x^2-1}
-
\frac13
\right|
=
\frac{|x-2|,|x+2|}
{3|x^2-1|}.
\]

::: {.proof}
Compute
\[
\begin{aligned}
\frac1{x^2-1}
-
\frac13
&=
\frac{3-(x^2-1)}
{3(x^2-1)}\\
&=
\frac{4-x^2}
{3(x^2-1)}\\
&=
-\frac{(x-2)(x+2)}
{3(x^2-1)}.
\end{aligned}
\]
Take absolute values.
:::

<1>2. If
\[
|x-2|<\frac12,
\]
then
\[
|x+2|<\frac92
\]
and
\[
|x^2-1|>\frac54.
\]

::: {.proof}
The inequality
\[
|x-2|<\frac12
\]
gives
\[
\frac32<x<\frac52.
\]
Hence
\[
x+2<\frac92,
\]
so
\[
|x+2|<\frac92.
\]

Also
\[
x>\frac32
\]
implies
\[
x^2-1
>
\frac94-1
=
\frac54.
\]
Since this quantity is positive,
\[
|x^2-1|
>
\frac54.
\]
:::

<1>3. Under the same restriction,
\[
\left|
\frac1{x^2-1}
-
\frac13
\right|
<
\frac65|x-2|.
\]

::: {.proof}
Insert the bounds from step <1>2 into step <1>1:
\[
\begin{aligned}
\left|
\frac1{x^2-1}
-
\frac13
\right|
&=
\frac{|x-2|,|x+2|}
{3|x^2-1|}\\
&<
\frac{|x-2|(9/2)}
{3(5/4)}\\
&=
\frac65|x-2|.
\end{aligned}
\]
:::

<1>4. Let
\[
\varepsilon>0
\]
be given.
Choose
\[
\boxed{
\delta
=
\min
\left\{
\frac12,
\frac{5\varepsilon}{6}
\right\}.
}
\]

::: {.proof}
This choice ensures both:

1. the denominator-control hypothesis
   \[
   |x-2|<\frac12;
   \]
2. the final error bound
   \[
   \frac65|x-2|
   <
   \varepsilon.
   \]
:::

<1>5. If
\[
0<|x-2|<\delta,
\]
then
\[
\left|
\frac1{x^2-1}
-
\frac13
\right|
<
\varepsilon.
\]

::: {.proof}
Since
\[
\delta\le\frac12,
\]
step <1>3 applies:
\[
\left|
\frac1{x^2-1}
-
\frac13
\right|
<
\frac65|x-2|.
\]
Also
\[
|x-2|
<
\delta
\le
\frac{5\varepsilon}{6},
\]
so
\[
\frac65|x-2|
<
\varepsilon.
\]
:::

<1>6. Therefore
\[
\boxed{
\lim_{x\to2}
\frac1{x^2-1}
=
\frac13.
}
\]

::: {.proof}
Step <1>5 is exactly the
\[
\varepsilon\text{--}\delta
\]
definition of the limit.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the desired conclusion.
:::
:::
