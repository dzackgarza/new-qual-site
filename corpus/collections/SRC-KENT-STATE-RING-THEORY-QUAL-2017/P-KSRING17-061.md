---
schema: qual/card@1
id: P-KSRING17-061
kind: problem
title: Maximal ideals of $C[0,1]$ are evaluation ideals
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 61 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let $R = C [ 0 , 1 ]$ be the ring of all continuous real-valued functions on [0, 1], with addition and multiplication defined as follows.
For $f , g \in R$ and $x \in [ 0 , 1 ]$

$$
\begin{array} { l } { { ( f + g ) ( x ) = f ( x ) + g ( x ) } } \\ { { ( f g ) ( x ) = f ( x ) g ( x ) . } } \end{array}
$$

Prove that if M is a maximal ideal of R, then there is a real number $x _ { 0 } \in [ 0 , 1 ]$ such that $M = \{ f \in R \mid f ( x _ { 0 } ) = 0 \}$ .
:::

::: {.solution}
Let
$$
M
$$
be a maximal ideal of
$$
R=C([0,1],\RR).
$$

<1>1. The functions in $M$ have a common zero in $[0,1]$.

::: {.proof}
Suppose, for contradiction, that there is no common zero.
Then for every
$$
x\in[0,1]
$$
there exists
$$
f_x\in M
$$
such that
$$
f_x(x)\ne0.
$$

By continuity of $f_x$, there exists an open neighborhood
$$
U_x
$$
of $x$ such that
$$
f_x(t)\ne0
$$
for every
$$
t\in U_x.
$$
The sets
$$
\{U_x:x\in[0,1]\}
$$
form an open cover of the compact interval $[0,1]$.
Choose a finite subcover
$$
U_{x_1},\ldots,U_{x_n}.
$$
Set
$$
g
\coloneqq
\sum_{j=1}^{n}f_{x_j}^2.
$$
Because
$$
f_{x_j}\in M
$$
and $M$ is an ideal,
$$
f_{x_j}^2\in M,
$$
so
$$
g\in M.
$$

For each
$$
t\in[0,1],
$$
some
$$
U_{x_j}
$$
contains $t$, and then
$$
f_{x_j}(t)\ne0.
$$
Therefore
$$
g(t)
=
\sum_{j=1}^{n}f_{x_j}(t)^2
>0.
$$
Thus $g$ is nowhere zero.

The reciprocal
$$
\frac1g
$$
is continuous on $[0,1]$, so it lies in $R$, and
$$
g\cdot\frac1g
=
1_R.
$$
Hence $g$ is a unit.
But a proper ideal cannot contain a unit, whereas
$$
g\in M.
$$
This contradicts maximality of $M$.

Therefore there exists
$$
x_0\in[0,1]
$$
such that
$$
f(x_0)=0
$$
for every
$$
f\in M.
$$
:::

<1>2. Define
$$
I_{x_0}
\coloneqq
\{f\in R:f(x_0)=0\}.
$$
Then
$$
M\subseteq I_{x_0}.
$$

::: {.proof}
This is exactly the conclusion of step <1>1.
:::

<1>3. The evaluation map
$$
\operatorname{ev}_{x_0}:R\to\RR,
\qquad
f\longmapsto f(x_0)
$$
is a surjective ring homomorphism with kernel
$$
I_{x_0}.
$$

::: {.proof}
Pointwise addition and multiplication give
$$
\operatorname{ev}_{x_0}(f+g)
=
f(x_0)+g(x_0)
$$
and
$$
\operatorname{ev}_{x_0}(fg)
=
f(x_0)g(x_0).
$$
Also
$$
\operatorname{ev}_{x_0}(1_R)=1.
$$
Thus evaluation is a unital ring homomorphism.

It is surjective because every
$$
c\in\RR
$$
is the value at $x_0$ of the constant function
$$
f(t)=c.
$$

Finally,
$$
\ker\operatorname{ev}_{x_0}
=
\{f\in R:f(x_0)=0\}
=
I_{x_0}.
$$
:::

<1>4. The ideal
$$
I_{x_0}
$$
is maximal.

::: {.proof}
By step <1>3 and the first isomorphism theorem,
$$
R/I_{x_0}
\cong
\RR.
$$
Since
$$
\RR
$$
is a field, the maximal-ideal quotient criterion gives that
$$
I_{x_0}
$$
is maximal.
:::

<1>5. Therefore
$$
M=I_{x_0}.
$$

::: {.proof}
By step <1>2,
$$
M\subseteq I_{x_0}.
$$
Both ideals are maximal by hypothesis and step <1>4.
Since a maximal ideal cannot be properly contained in another proper ideal,
$$
M=I_{x_0}.
$$
:::

<1>6. Hence
$$
\boxed{
M
=
\{f\in R:f(x_0)=0\}
}
$$
for some
$$
x_0\in[0,1].
$$

::: {.proof}
Combine steps <1>1 and <1>5.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required classification.
:::
:::
