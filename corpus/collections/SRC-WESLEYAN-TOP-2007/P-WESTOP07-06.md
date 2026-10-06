---
schema: qual/card@1
id: P-WESTOP07-06
kind: problem
title: A homotopy equivalence matches path components by homotopy equivalences
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Let $f:X\to Y$ be a homotopy equivalence.

1. Prove that $f$ induces a bijection between the sets of path components of $X$ and $Y$.
2. Prove that $f$ restricts to a homotopy equivalence from each path component of $X$ to its corresponding path component of $Y$.
:::

::: {.solution}
Choose a homotopy inverse
$$
g:Y\to X
$$
and homotopies
$$
H:X\times I\to X,
\qquad
H(-,0)=g\circ f,
\quad
H(-,1)=\operatorname{id}_X,
$$
and
$$
K:Y\times I\to Y,
\qquad
K(-,0)=f\circ g,
\quad
K(-,1)=\operatorname{id}_Y.
$$

<1>1. The map $f$ sends each path component of $X$ into a single path component of $Y$.

::: {.proof}
Let
$$
x_0,x_1\in X
$$
lie in the same path component. Choose a path
$$
\gamma:I\to X
$$
from
$$
x_0
$$
to
$$
x_1.
$$
Then
$$
f\circ\gamma
$$
is a path in
$$
Y
$$
from
$$
f(x_0)
$$
to
$$
f(x_1).
$$
Thus
$$
f(x_0)
$$
and
$$
f(x_1)
$$
belong to the same path component.
:::

<1>2. Therefore $f$ induces a map
$$
\pi_0(f):
\pi_0(X)
\to
\pi_0(Y)
$$
on the sets of path components.

::: {.proof}
Step <1>1 shows that the path component containing
$$
f(x)
$$
depends only on the path component containing
$$
x.
$$
Hence the induced map is well defined.
:::

<1>3. The homotopy
$$
H:g\circ f\simeq\operatorname{id}_X
$$
implies
$$
\pi_0(g)\circ\pi_0(f)
=
\operatorname{id}_{\pi_0(X)}.
$$

::: {.proof}
For every
$$
x\in X,
$$
the path
$$
t\longmapsto H(x,t)
$$
joins
$$
g(f(x))
$$
to
$$
x.
$$
Hence these two points lie in the same path component of
$$
X.
$$
Thus
$$
[g(f(x))]
=
[x]
$$
in
$$
\pi_0(X).
$$
:::

<1>4. Likewise,
$$
\pi_0(f)\circ\pi_0(g)
=
\operatorname{id}_{\pi_0(Y)}.
$$

::: {.proof}
For every
$$
y\in Y,
$$
the path
$$
t\longmapsto K(y,t)
$$
joins
$$
f(g(y))
$$
to
$$
y.
$$
Hence these points lie in the same path component of
$$
Y.
$$
:::

<1>5. Therefore
$$
\boxed{
\pi_0(f):
\pi_0(X)
\xrightarrow{\sim}
\pi_0(Y)}
$$
is a bijection.

::: {.proof}
Steps <1>3--<1>4 show that
$$
\pi_0(g)
$$
is both a left and right inverse of
$$
\pi_0(f).
$$
:::

<1>6. Let
$$
C\subseteq X
$$
be a path component and let
$$
D\subseteq Y
$$
be the corresponding component
$$
D=\pi_0(f)(C).
$$
Then
$$
f(C)\subseteq D.
$$

::: {.proof}
This is exactly how
$$
D
$$
was defined in step <1>5.
:::

<1>7. One also has
$$
g(D)\subseteq C.
$$

::: {.proof}
Fix
$$
x_0\in C.
$$
Then
$$
f(x_0)\in D.
$$
Let
$$
y\in D.
$$
Because
$$
D
$$
is path-connected, there is a path in
$$
D
$$
from
$$
y
$$
to
$$
f(x_0).
$$
Applying
$$
g
$$
gives a path from
$$
g(y)
$$
to
$$
g(f(x_0)).
$$
The homotopy
$$
H
$$
gives a path from
$$
g(f(x_0))
$$
to
$$
x_0.
$$
Concatenating these paths shows that
$$
g(y)
$$
lies in the same path component as
$$
x_0,
$$
namely
$$
C.
$$
:::

<1>8. The restrictions
$$
f_C
\coloneqq
f|_C:C\to D
$$
and
$$
g_D
\coloneqq
g|_D:D\to C
$$
are well defined.

::: {.proof}
This follows from steps <1>6--<1>7.
:::

<1>9. The homotopy
$$
H
$$
restricts to a homotopy
$$
g_D\circ f_C
\simeq
\operatorname{id}_C.
$$

::: {.proof}
For
$$
x\in C,
$$
the path
$$
t\longmapsto H(x,t)
$$
ends at
$$
x\in C.
$$
Every point on that path is therefore in the same path component as
$$
x,
$$
so the entire path lies in
$$
C.
$$
Hence
$$
H|_{C\times I}
$$
has image in
$$
C
$$
and gives the desired restricted homotopy.
:::

<1>10. Likewise,
$$
K
$$
restricts to a homotopy
$$
f_C\circ g_D
\simeq
\operatorname{id}_D.
$$

::: {.proof}
For
$$
y\in D,
$$
the path
$$
t\longmapsto K(y,t)
$$
ends at
$$
y\in D,
$$
so all of its points lie in the path component
$$
D.
$$
Thus
$$
K|_{D\times I}
$$
is the required homotopy.
:::

<1>11. Therefore
$$
\boxed{
f_C:C\to D
\text{ is a homotopy equivalence}.}
$$

::: {.proof}
Steps <1>9--<1>10 show that
$$
g_D
$$
is a homotopy inverse for
$$
f_C.
$$
:::

<1>12. Q.E.D.

::: {.proof}
Step <1>5 proves part (1), and step <1>11 proves part (2).
:::
:::
