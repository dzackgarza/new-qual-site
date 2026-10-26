---
schema: qual/card@1
id: P-WESTOP08-I3
kind: problem
title: Explicit path homotopy from a path followed by its reverse to the constant path
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Let $f:I\to X$ be a path in a topological space $X$, and define the reverse path by
\[
\overline f(s)=f(1-s).
\]
Let $e_{x_0}$ be the constant path at $x_0=f(0)$. Construct an explicit path homotopy, described algebraically and in full detail, proving
\[
[f]*[\overline f]=[e_{x_0}].
\]
:::

Write
\[
g=f*\overline f.
\]
Thus
\[
g(s)
=
\begin{cases}
f(2s),&0\le s\le\frac12,\\[1mm]
f(2-2s),&\frac12\le s\le1.
\end{cases}
\]

::: pf

::: pf-step

Define
\[
H:I\times I\to X
\]
by
\[
\boxed{
H(s,t)
=
\begin{cases}
f\bigl(2(1-t)s\bigr),
&0\le s\le\frac12,\\[1mm]
f\bigl(2(1-t)(1-s)\bigr),
&\frac12\le s\le1.
\end{cases}
}
\]


::: pf-proof

At homotopy time $t$, the number
\[
1-t
\]
is the furthest parameter value of $f$ that the loop reaches.
The first half of the loop runs from
\[
f(0)
\]
to
\[
f(1-t),
\]
and the second half runs back along the same segment.

:::

:::

::: pf-step

The two formulas in step <1>1 agree along
\[
s=\frac12.
\]


::: pf-proof

For the first formula,
\[
H\left(\frac12,t\right)
=
f\left(
2(1-t)\frac12
\right)
=
f(1-t).
\]
For the second formula,
\[
H\left(\frac12,t\right)
=
f\left(
2(1-t)
\left(
1-\frac12
\right)
\right)
=
f(1-t).
\]
Thus the two definitions coincide on the overlap.

:::

:::

::: pf-step

The map $H$ is continuous.


::: pf-proof

Let
\[
A
=
\left[0,\frac12\right]\times I,
\qquad
B
=
\left[\frac12,1\right]\times I.
\]
Both are closed in
\[
I\times I.
\]

On $A$, the map
\[
(s,t)
\longmapsto
2(1-t)s
\]
is continuous and takes values in $I$, so
\[
H|_A
=
f\circ
\bigl(
(s,t)\mapsto2(1-t)s
\bigr)
\]
is continuous.

Similarly, on $B$,
\[
(s,t)
\longmapsto
2(1-t)(1-s)
\]
is continuous and takes values in $I$, so $H|_B$ is continuous.

By step <1>2, these two continuous maps agree on
\[
A\cap B
=
\left\{\frac12\right\}\times I.
\]
The pasting lemma therefore gives continuity of $H$ on all of
\[
I\times I.
\]

:::

:::

::: pf-step

At
\[
t=0,
\]
the homotopy is the concatenated loop:
\[
H(s,0)
=
(f*\overline f)(s).
\]


::: pf-proof

If
\[
0\le s\le\frac12,
\]
then
\[
H(s,0)
=
f(2s).
\]

If
\[
\frac12\le s\le1,
\]
then
\[
H(s,0)
=
f(2(1-s))
=
f(2-2s).
\]
These are exactly the two defining pieces of
\[
f*\overline f.
\]

:::

:::

::: pf-step

At
\[
t=1,
\]
the homotopy is the constant loop at
\[
x_0=f(0).
\]


::: pf-proof

For every $s\in I$,
\[
1-t=0
\]
when $t=1$, so both formulas give
\[
H(s,1)
=
f(0)
=
x_0.
\]
Thus
\[
H(-,1)=e_{x_0}.
\]

:::

:::

::: pf-step

The endpoints remain fixed throughout the homotopy:
\[
H(0,t)
=
H(1,t)
=
x_0
\qquad
(t\in I).
\]


::: pf-proof

At $s=0$,
\[
H(0,t)
=
f(0)
=
x_0.
\]
At $s=1$,
\[
H(1,t)
=
f(0)
=
x_0.
\]
Therefore $H$ is a path homotopy relative to the endpoints.

:::

:::

::: pf-step

Hence
\[
f*\overline f
\simeq
e_{x_0}
\]
rel endpoints.


::: pf-proof

Steps <1>3--<1>6 show that $H$ is a continuous homotopy from
\[
f*\overline f
\]
to
\[
e_{x_0}
\]
that fixes both endpoints for all homotopy times.

:::

:::

::: pf-step

Therefore
\[
\boxed{
[f]*[\overline f]
=
[e_{x_0}]
}
\]
in the fundamental groupoid, and in particular in the fundamental group
when $f$ is regarded as a path from $x_0$ to its endpoint and then retraced.


::: pf-proof

Path-homotopic paths rel endpoints define the same homotopy class.
Also,
\[
[f]*[\overline f]
=
[f*\overline f].
\]
Apply step <1>7.

:::

:::

::: pf-qed

Step <1>8 is the desired identity.

:::

:::
