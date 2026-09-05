---
schema: qual/card@1
id: P-C62HS
kind: problem
title: A contraction of a compact metric space has a fixed point
classification:
  areas:
  - topology
  topics:
  - Fixed Points
  - Metric Spaces
  - Compactness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: >-
    Restored problem 2 of the official UGA Spring 2007 topology exam verbatim.
    The source omits the necessary nonempty hypothesis; an earlier edit had
    silently inserted it and also strengthened the requested conclusion to
    uniqueness.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: >-
    Verified the displacement-minimization proof after handling the empty-space
    counterexample explicitly. For nonempty X it proves the requested fixed
    point, and the contraction inequality also gives uniqueness.
---

::: problem
Prove that if $(X,d)$ is a compact metric space, $f:X\to X$ is a continuous map, and $C$ is a constant with $0<C<1$ such that
\[
d(f(x),f(y))\leq C d(x,y)
\]
for all $x,y\in X$, then $f$ has a fixed point.
:::

::: {.solution}
<1>1. As written, the source statement has one exceptional case: it is false when $X=\varnothing$.
::: {.proof}
The empty metric space is compact, and its unique self-map satisfies the stated contraction inequality vacuously, but it has no fixed point.
Thus the intended assertion requires $X\neq\varnothing$.
Assume this from now on.
:::

<1>2. Define
\[
g:X\to\RR,
\qquad
g(x)=d(x,f(x)).
\]
Then $g$ is continuous.
::: {.proof}
For $x,y\in X$, the triangle inequality gives
\[
d(x,f(x))
\le d(x,y)+d(y,f(y))+d(f(y),f(x)).
\]
Hence
\[
g(x)-g(y)
\le d(x,y)+d(f(x),f(y))
\le (1+C)d(x,y).
\]
Interchanging $x$ and $y$ yields
\[
|g(x)-g(y)|\le(1+C)d(x,y).
\]
Thus $g$ is Lipschitz, hence continuous.
:::

<1>3. The function $g$ attains a minimum at some point $x_0\in X$.
::: {.proof}
By <1>1, $X$ is nonempty, and by hypothesis it is compact.
The continuous real-valued function $g$ from <1>2 therefore attains its minimum.
Choose $x_0\in X$ such that
\[
g(x_0)\le g(x)
\qquad\text{for all }x\in X.
\]
:::

<1>4. The point $x_0$ from <1>3 is a fixed point of $f$.
::: {.proof}
Suppose $f(x_0)\ne x_0$.
Then $g(x_0)=d(x_0,f(x_0))>0$, while the contraction inequality gives
\[
\begin{aligned}
g(f(x_0))
&=d(f(x_0),f(f(x_0)))\\
&\le C d(x_0,f(x_0))\\
&=C g(x_0)\\
&<g(x_0),
\end{aligned}
\]
because $0<C<1$.
This contradicts the minimality of $g(x_0)$.
Hence $g(x_0)=0$, so $f(x_0)=x_0$.
:::

<1>5. In fact, the fixed point is unique.
::: {.proof}
If $x$ and $y$ are fixed points, then
\[
d(x,y)=d(f(x),f(y))\le C d(x,y).
\]
Since $C<1$, this forces $d(x,y)=0$, hence $x=y$.
:::

<1>6. Under the necessary nonempty interpretation of the source, $f$ has a fixed point.
::: {.proof}
Existence is <1>4; <1>5 gives the stronger uniqueness conclusion.
:::
:::
