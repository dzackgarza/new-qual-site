---
schema: qual/card@1
id: P-WESCA12-II2
kind: problem
title: 'Possible values of an integral of $1/(z^2+1)$'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problems, problem 2 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
(a) Find all possible values of
\[
\int_\gamma\frac{dz}{z^2+1},
\]
where $\gamma$ is a closed smooth curve in $\CC\setminus\{i,-i\}$.

(b) Answer the same question when $\gamma$ is a positively oriented circle, and describe which circles give each possible value.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

One has the partial-fraction identity
\[
\frac1{z^2+1}
=
\frac1{2i}
\left(
\frac1{z-i}
-
\frac1{z+i}
\right).
\]


::: pf-proof

Since
\[
z^2+1
=
(z-i)(z+i),
\]
write
\[
\frac1{(z-i)(z+i)}
=
\frac{A}{z-i}
+
\frac{B}{z+i}.
\]
Solving gives
\[
A=\frac1{2i},
\qquad
B=-\frac1{2i}.
\]

:::

:::

::: {.pf-step #s1-2}

For any closed smooth curve
\[
\gamma
\subset
\CC\setminus\{i,-i\},
\]
\[
\boxed{
\int_\gamma
\frac{dz}{z^2+1}
=
\pi
\bigl(
\operatorname{Ind}(\gamma,i)
-
\operatorname{Ind}(\gamma,-i)
\bigr).
}
\]


::: pf-proof

By step [](#s1-1){.pf-ref},
\[
\begin{aligned}
\int_\gamma
\frac{dz}{z^2+1}
&=
\frac1{2i}
\left(
\int_\gamma\frac{dz}{z-i}
-
\int_\gamma\frac{dz}{z+i}
\right).
\end{aligned}
\]
For any point $a$ not on the curve,
\[
\int_\gamma
\frac{dz}{z-a}
=
2\pi i\,
\operatorname{Ind}(\gamma,a).
\]
Substituting
\[
a=i
\quad\text{and}\quad
a=-i
\]
gives the formula.

:::

:::

::: {.pf-step #s1-3}

Every value
\[
\pi m,
\qquad
m\in\ZZ,
\]
occurs.


::: pf-proof

Choose a small positively oriented circle around $i$ that does not enclose
$-i$.
Traversing it $m$ times if $m>0$, or $|m|$ times with reverse orientation if
$m<0$, gives a closed smooth curve with
\[
\operatorname{Ind}(\gamma,i)=m,
\qquad
\operatorname{Ind}(\gamma,-i)=0.
\]
Step [](#s1-2){.pf-ref} then gives
\[
\int_\gamma
\frac{dz}{z^2+1}
=
\pi m.
\]
For
\[
m=0,
\]
take a small circle enclosing neither pole.

:::

:::

::: {.pf-step #s1-4}

These are the only possible values:
\[
\boxed{
\left\{
\int_\gamma
\frac{dz}{z^2+1}
:
\gamma
\text{ closed smooth in }
\CC\setminus\{\pm i\}
\right\}
=
\pi\ZZ.
}
\]


::: pf-proof

Both winding numbers in step [](#s1-2){.pf-ref} are integers, so their difference is an
integer. Step [](#s1-3){.pf-ref} shows every integer difference is realized.

:::

:::

::: {.pf-step #s1-5}

Now let $\gamma$ be a positively oriented circle
\[
|z-c|=R
\]
that does not pass through either pole.
Then
\[
\operatorname{Ind}(\gamma,a)
=
\begin{cases}
1,&|a-c|<R,\\
0,&|a-c|>R.
\end{cases}
\]


::: pf-proof

A positively oriented simple circle winds once around every point in its
interior and zero times around every exterior point.
The equalities
\[
|a-c|=R
\]
are excluded because the curve must avoid
\[
a=\pm i.
\]

:::

:::

::: {.pf-step #s1-6}

If the circle contains $i$ but not $-i$, then
\[
\boxed{
\int_\gamma
\frac{dz}{z^2+1}
=
\pi.
}
\]


::: pf-proof

The condition is
\[
|c-i|<R<|c+i|.
\]
Hence
\[
\operatorname{Ind}(\gamma,i)=1,
\qquad
\operatorname{Ind}(\gamma,-i)=0.
\]
Apply step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

If the circle contains $-i$ but not $i$, then
\[
\boxed{
\int_\gamma
\frac{dz}{z^2+1}
=
-\pi.
}
\]


::: pf-proof

The condition is
\[
|c+i|<R<|c-i|.
\]
Thus
\[
\operatorname{Ind}(\gamma,i)=0,
\qquad
\operatorname{Ind}(\gamma,-i)=1.
\]
Apply step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

If the circle contains both poles or neither pole, then
\[
\boxed{
\int_\gamma
\frac{dz}{z^2+1}
=
0.
}
\]


::: pf-proof

If both poles are inside, then
\[
\operatorname{Ind}(\gamma,i)
=
\operatorname{Ind}(\gamma,-i)
=
1.
\]
If neither is inside, then both winding numbers are zero.
In either case their difference vanishes.

In center-radius language, the two cases are
\[
R>
\max\{|c-i|,|c+i|\}
\]
and
\[
R<
\min\{|c-i|,|c+i|\}.
\]

:::

:::

::: {.pf-step #s1-9}

Hence for positively oriented circles the only possible values are
\[
\boxed{
-\pi, 0, \pi.
}
\]


::: pf-proof

Steps [](#s1-6){.pf-ref} through [](#s1-8){.pf-ref} exhaust the four possibilities for whether each of the two
poles lies inside the circle.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} solves part (a), and steps [](#s1-5){.pf-ref} through [](#s1-9){.pf-ref} solve part (b).

:::

:::

:::
