---
schema: qual/card@1
id: P-BERK78S-18
kind: problem
title: Every norm on $\RR^n$ is equivalent to the Euclidean norm
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
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Bounded N(x) above by the coordinate l1 norm using the values N(e_i),
    which immediately bounds N on the Euclidean unit sphere. The reverse
    triangle inequality then gives Lipschitz continuity with respect to the
    Euclidean norm. Continuity and positivity on the compact unit sphere
    give a positive minimum A and finite maximum B, and homogeneity extends
    these bounds to all vectors.
---

::: {.problem}
Let $N:\mathbb R^n\to\mathbb R$ be a norm.

1. Prove that $N$ is bounded on the Euclidean unit sphere.
2. Prove that $N$ is continuous.
3. Prove that there are constants $A,B>0$ such that
   \[
   A\|x\|\le N(x)\le B\|x\|
   \]
   for every $x\in\mathbb R^n$.
:::

::: {.solution}
Let
$$
e_1,\ldots,e_n
$$
be the standard basis of $\RR^n$, and let
$$
\norm{x}
$$
denote the Euclidean norm.

<1>1. If
$$
x=\sum_{j=1}^n x_je_j,
$$
then
$$
N(x)
\leq
\sum_{j=1}^n
\abs{x_j}N(e_j).
$$

::: {.proof}
By repeated use of the triangle inequality and absolute homogeneity of
$N$,
$$
\begin{aligned}
N(x)
&=
N\left(
\sum_{j=1}^n x_je_j
\right)\\
&\leq
\sum_{j=1}^n N(x_je_j)\\
&=
\sum_{j=1}^n
\abs{x_j}N(e_j).
\end{aligned}
$$
:::

<1>2. There is a constant $C>0$ such that
$$
N(x)\leq C\norm{x}
$$
for every $x\in\RR^n$.

::: {.proof}
Set
$$
M=\max_{1\leq j\leq n}N(e_j).
$$
Every $e_j$ is nonzero, so $M>0$. By step <1>1,
$$
N(x)
\leq
M\sum_{j=1}^n\abs{x_j}.
$$
The Cauchy--Schwarz inequality gives
$$
\sum_{j=1}^n\abs{x_j}
\leq
\sqrt n
\left(
\sum_{j=1}^n\abs{x_j}^2
\right)^{1/2}
=
\sqrt n\,\norm{x}.
$$
Thus
$$
N(x)\leq M\sqrt n\,\norm{x}.
$$
Take
$$
C=M\sqrt n.
$$
:::

<1>3. The norm $N$ is bounded on the Euclidean unit sphere.

::: {.proof}
If
$$
\norm{x}=1,
$$
then step <1>2 gives
$$
N(x)\leq C.
$$
Thus $N$ is bounded above on the unit sphere. Since every norm is
nonnegative, it is bounded there.
:::

<1>4. For every $x,y\in\RR^n$,
$$
\abs{N(x)-N(y)}
\leq
N(x-y).
$$

::: {.proof}
The triangle inequality gives
$$
N(x)
=
N\bigl((x-y)+y\bigr)
\leq
N(x-y)+N(y),
$$
so
$$
N(x)-N(y)\leq N(x-y).
$$
Interchanging $x$ and $y$ gives
$$
N(y)-N(x)\leq N(y-x)=N(x-y).
$$
Combining the two inequalities proves the claim.
:::

<1>5. The norm $N$ is Lipschitz continuous with respect to the Euclidean
norm:
$$
\abs{N(x)-N(y)}
\leq
C\norm{x-y}.
$$

::: {.proof}
By step <1>4,
$$
\abs{N(x)-N(y)}
\leq
N(x-y).
$$
Apply step <1>2 to $x-y$.
:::

<1>6. The norm $N$ is continuous on $\RR^n$.

::: {.proof}
Every Lipschitz function is continuous, and step <1>5 gives a global
Lipschitz estimate.
:::

<1>7. On the Euclidean unit sphere
$$
S^{n-1}
=
\{x\in\RR^n:\norm{x}=1\},
$$
the function $N$ attains a positive minimum and a finite maximum.

::: {.proof}
The Euclidean unit sphere is compact. By step <1>6, $N$ is continuous, so
there are points $u,v\in S^{n-1}$ such that
$$
N(u)
=
\min_{\norm{x}=1}N(x)
$$
and
$$
N(v)
=
\max_{\norm{x}=1}N(x).
$$
Set
$$
A=N(u),
\qquad
B=N(v).
$$
Every point of the unit sphere is nonzero, and a norm vanishes only at
$0$. Hence
$$
A>0.
$$
Also $B<\infty$ because it is an attained real value.
:::

<1>8. For every $x\in\RR^n$,
$$
\boxed{
A\norm{x}
\leq
N(x)
\leq
B\norm{x}.
}
$$

::: {.proof}
If $x=0$, all three quantities are zero and the inequalities hold.
Suppose $x\neq0$ and set
$$
y=\frac{x}{\norm{x}}.
$$
Then
$$
\norm{y}=1.
$$
By the definitions of $A$ and $B$ in step <1>7,
$$
A\leq N(y)\leq B.
$$
Absolute homogeneity gives
$$
N(x)
=
N(\norm{x}y)
=
\norm{x}N(y).
$$
Multiplying the preceding inequalities by the positive number
$\norm{x}$ gives the desired bounds.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>3 proves part (1), step <1>6 proves part (2), and step <1>8 proves
part (3).
:::
:::
