---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F08-14
kind: problem
title: Non-surjective maps into a sphere are homotopic
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Degree
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Checked against Part Two, question 2 of the Topology Ph.D. Qualifying Exam
    dated January 17, 2009 in assets/attachments/F08phdtop.pdf. The literal
    statement fails for n=1, since S^0 is disconnected; the intended statement
    is correct for n>=2.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    A non-surjective map misses a point of the sphere and therefore factors
    through a punctured sphere, which is homeomorphic to Euclidean space and is
    contractible. Thus both maps are null-homotopic; for n>=2 their constant
    endpoints are joined by a path in the sphere. Recorded the S^0 counterexample.
---

::: {.problem}
Prove that if $f,g:X\to S^{n-1}$ are continuous and both not surjective then $f$ is homotopic to $g$.
:::

::: {.solution}
For the intended statement assume $n\ge2$.

<1>1. Every non-surjective continuous map
\[
h:X\to S^{n-1}
\]
is null-homotopic.
::: {.proof}
Because $h$ is not surjective, choose
\[
p\in S^{n-1}\setminus h(X).
\]
Then $h$ factors through the punctured sphere
\[
S^{n-1}\setminus\{p\}.
\]
Stereographic projection from $p$ gives a homeomorphism
\[
\sigma:S^{n-1}\setminus\{p\}\longrightarrow\mathbb R^{n-1}.
\]
Choose a point $x_0\in\mathbb R^{n-1}$ and define
\[
H:X\times I\to S^{n-1}\setminus\{p\}
\]
by
\[
H(x,t)
=\sigma^{-1}\bigl((1-t)\sigma(h(x))+t x_0\bigr).
\]
This is continuous, with
\[
H(x,0)=h(x)
\]
and
\[
H(x,1)=\sigma^{-1}(x_0),
\]
independent of $x$.
Thus $h$ is homotopic to a constant map.
:::

<1>2. The maps $f$ and $g$ are homotopic to constant maps
\[
c_a(x)=a,
\qquad
c_b(x)=b
\]
for some $a,b\in S^{n-1}$.
::: {.proof}
Apply <1>1 separately to the two non-surjective maps $f$ and $g$.
:::

<1>3. For $n\ge2$, any two constant maps $X\to S^{n-1}$ are homotopic.
::: {.proof}
Since
\[
n-1\ge1,
\]
the sphere $S^{n-1}$ is path-connected.
Choose a path
\[
\gamma:I\to S^{n-1}
\]
from $a$ to $b$.
Then
\[
K:X\times I\to S^{n-1},
\qquad
K(x,t)=\gamma(t),
\]
is a homotopy from $c_a$ to $c_b$.
:::

<1>4. Hence for $n\ge2$,
\[
f\simeq g.
\]
::: {.proof}
By <1>2,
\[
f\simeq c_a
\qquad\text{and}\qquad
g\simeq c_b.
\]
By <1>3,
\[
c_a\simeq c_b.
\]
Symmetry and transitivity of homotopy give
\[
f\simeq c_a\simeq c_b\simeq g.
\]
:::

<1>5. The source statement is false when $n=1$.
::: {.proof}
Let $X=\{*\}$ and identify
\[
S^0=\{-1,1\}.
\]
Define
\[
f(*)=1,
\qquad
g(*)=-1.
\]
Both maps are non-surjective.
If they were homotopic, a homotopy
\[
X\times I\to S^0
\]
would give a path in $S^0$ from $1$ to $-1$.
No such path exists because $S^0$ is discrete.
Thus the unqualified statement fails for $n=1$.
:::
:::
