---
schema: qual/card@1
id: P-BKS13-9B
kind: problem
title: Squares in finite fields; every element is a sum of two squares
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with page 5 of the retained Spring 2013 solution PDF and independently reviewed the finite-set counting argument.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the square count in odd and even characteristic and the intersection argument proving every element is a sum of two squares.
---

::: {.problem}
If F is a finite field, show that more than half the elements of F are squares. Show that every element is the sum of 2 squares.
:::

::: {.solution}
Let
$$
q\coloneqq\abs{F}
$$
and let
$$
S\coloneqq\{x^2:x\in F\}
$$
be the set of squares in $F$.

<1>1. If $\operatorname{char}F=2$, then
$$
S=F.
$$

::: {.proof}
The squaring map
$$
\varphi:F\longrightarrow F,
\qquad
\varphi(x)=x^2,
$$
is injective: if
$$
x^2=y^2,
$$
then
$$
(x-y)^2=0,
$$
so $x=y$ because a field has no nonzero nilpotents. Since $F$ is finite,
injectivity implies surjectivity. Thus every element is a square.
:::

<1>2. If $\operatorname{char}F\neq2$, then
$$
\abs{S}
=
\frac{q+1}{2}.
$$

::: {.proof}
On $F^\times$, the map
$$
x\longmapsto x^2
$$
has exactly two preimages for each nonzero square: if
$$
x^2=y^2,
$$
then
$$
(x-y)(x+y)=0,
$$
so $y=x$ or $y=-x$. These two values are distinct because the
characteristic is not $2$.

Hence the $q-1$ nonzero elements produce exactly
$$
\frac{q-1}{2}
$$
nonzero squares. Adding the square $0$ gives
$$
\abs{S}
=
1+\frac{q-1}{2}
=
\frac{q+1}{2}.
$$
:::

<1>3. In every finite field,
$$
\boxed{
\abs{S}
>
\frac{q}{2}
}.
$$

::: {.proof}
If the characteristic is $2$, step <1>1 gives
$$
\abs{S}=q.
$$
Otherwise step <1>2 gives
$$
\abs{S}
=
\frac{q+1}{2}
>
\frac q2.
$$
This proves the first assertion.
:::

<1>4. For every
$$
b\in F,
$$
the translated set
$$
b-S
\coloneqq
\{b-s:s\in S\}
$$
has cardinality
$$
\abs{b-S}
=
\abs{S}.
$$

::: {.proof}
The map
$$
S\longrightarrow b-S,
\qquad
s\longmapsto b-s,
$$
is a bijection.
:::

<1>5. For every $b\in F$,
$$
S\cap(b-S)\neq\varnothing.
$$

::: {.proof}
By steps <1>3 and <1>4,
$$
\abs{S}
>
\frac q2
$$
and
$$
\abs{b-S}
>
\frac q2.
$$
If the two subsets were disjoint, their union would have more than $q$
elements, impossible in the $q$-element set $F$.
:::

<1>6. Every element of $F$ is a sum of two squares:
$$
\boxed{
\forall b\in F,\quad
b=x^2+y^2
\text{ for some }x,y\in F
}.
$$

::: {.proof}
Choose
$$
s\in S\cap(b-S)
$$
using step <1>5. Since $s\in S$, write
$$
s=x^2.
$$
Since $s\in b-S$, there is a square
$$
y^2\in S
$$
such that
$$
s=b-y^2.
$$
Therefore
$$
b=x^2+y^2.
$$
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>3 proves that more than half the field elements are squares, and
step <1>6 proves that every field element is a sum of two squares.
:::
:::
