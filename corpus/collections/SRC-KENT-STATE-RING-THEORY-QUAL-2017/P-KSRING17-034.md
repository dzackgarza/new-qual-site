---
schema: qual/card@1
id: P-KSRING17-034
kind: problem
title: The ideal of functions vanishing at infinity in bounded continuous functions
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 34 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let S be the ring of all bounded, continuous functions $f : \mathbb { R } \to \mathbb { R }$ , where R is the set of real numbers.
Let I be the set of functions f in S such that $f ( t ) \to 0 { \mathrm { ~ a s ~ } } | t | \to \infty$

(a) Show that I is an ideal of S.

(b) Suppose $x \in S$ is such that there is an $i \in I$ with ix = x. Show that $x ( t ) = 0$ for all sufficiently large |t|.
:::

::: {.solution}
<1>1. The set $I$ is nonempty and closed under subtraction.

::: {.proof}
The zero function belongs to $I$.

Let
$$
f,g\in I.
$$
Then
$$
f(t)\longrightarrow0
\qquad\text{and}\qquad
g(t)\longrightarrow0
$$
as
$$
\abs t\to\infty.
$$
Therefore
$$
(f-g)(t)
=
f(t)-g(t)
\longrightarrow0.
$$
Since $f-g$ is bounded and continuous, one has
$$
f-g\in I.
$$
:::

<1>2. If
$$
f\in I
$$
and
$$
h\in S,
$$
then
$$
hf\in I.
$$

::: {.proof}
Because $h$ is bounded, there exists
$$
M\ge0
$$
such that
$$
\abs{h(t)}\le M
$$
for all
$$
t\in\RR.
$$

Since
$$
f(t)\to0
$$
as
$$
\abs t\to\infty,
$$
one has
$$
\abs{h(t)f(t)}
\le
M\abs{f(t)}
\longrightarrow0.
$$
The product $hf$ is continuous and bounded, so
$$
hf\in I.
$$
:::

<1>3. Therefore
$$
\boxed{I\trianglelefteq S.}
$$

::: {.proof}
Step <1>1 shows that $I$ is an additive subgroup of $S$, and step <1>2 shows that it absorbs multiplication by arbitrary elements of $S$. Since $S$ is commutative, this is exactly the ideal condition.
:::

<1>4. Suppose
$$
i\in I,
\qquad
x\in S,
$$
and
$$
ix=x.
$$
Then there exists
$$
T>0
$$
such that
$$
\abs{i(t)}<\frac12
$$
whenever
$$
\abs t>T.
$$

::: {.proof}
Since
$$
i\in I,
$$
one has
$$
i(t)\longrightarrow0
$$
as
$$
\abs t\to\infty.
$$
Apply the definition of this limit with
$$
\varepsilon=\frac12.
$$
:::

<1>5. For every
$$
t
$$
with
$$
\abs t>T,
$$
one has
$$
x(t)=0.
$$

::: {.proof}
Evaluating
$$
ix=x
$$
at such a point gives
$$
i(t)x(t)
=
x(t).
$$
Hence
$$
(i(t)-1)x(t)
=
0.
$$
But step <1>4 gives
$$
\abs{i(t)}<\frac12,
$$
so
$$
i(t)\ne1.
$$
Because the values lie in the field $\RR$,
$$
i(t)-1\ne0
$$
implies
$$
x(t)=0.
$$
:::

<1>6. Therefore
$$
\boxed{
x(t)=0
\text{ for all sufficiently large }\abs t.
}
$$

::: {.proof}
Take the constant $T$ from step <1>4 and apply step <1>5.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>3 proves part (a), and step <1>6 proves part (b).
:::
:::
