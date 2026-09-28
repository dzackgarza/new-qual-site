---
schema: qual/card@1
id: P-BERK78S-09
kind: problem
title: Attainment of distance between subsets of a metric space
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
  note: The retained PDF was checked directly. Parts 1 and 2 are false as printed for an arbitrary metric space; closed subsets need not contain nearest points. The card preserves the source statement rather than silently adding a properness or compactness hypothesis.
- event: source-corrected
  by: chatgpt
  date: 2026-09-21
  note: >-
    The retained PDF really says arbitrary metric space and closed Y.
    This is false: in l^2, the closed set
    {(1+1/n)e_n:n>=1} has distance 1 from 0 but contains no point at that
    distance. The card adds the natural hypothesis that M is proper, i.e.
    every closed bounded subset is compact; this repairs parts 1 and 2
    while leaving part 3 meaningful.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    For a point and a closed set, a minimizing sequence lies in a closed
    bounded ball, hence in a compact set, so a convergent subsequence
    attains the infimum. The point-to-set distance is 1-Lipschitz, so on
    compact X it attains its minimum, reducing part 2 to part 1. In R^2,
    the x-axis ray and the graph y=e^{-x} are closed noncompact disjoint
    sets at distance zero, giving part 3.
---

::: {.problem}
Let $X,Y$ be nonempty subsets of a proper metric space $M$, meaning that
every closed bounded subset of $M$ is compact, and define
\[
d(X,Y)=\inf\{d(x,y):x\in X,\ y\in Y\}.
\]

1. Suppose $X=\{x\}$ consists of one point and $Y$ is closed. Prove that
   \[
   d(X,Y)=d(x,y)
   \]
   for some $y\in Y$.
2. Suppose $X$ is compact and $Y$ is closed. Prove that
   \[
   d(X,Y)=d(x,y)
   \]
   for some $x\in X$ and $y\in Y$.
3. Give an example showing that the conclusion of part 2 can fail if $X$ and $Y$ are closed but not compact.
:::

::: {.solution}
<1>1. Suppose
$$
X=\{x\}
$$
and $Y$ is closed. Set
$$
\delta=d(X,Y).
$$
There is a sequence $(y_n)$ in $Y$ such that
$$
d(x,y_n)\longrightarrow\delta.
$$

::: {.proof}
By the definition of an infimum, for each $n\geq1$ there is
$$
y_n\in Y
$$
with
$$
\delta
\leq
d(x,y_n)
<
\delta+\frac1n.
$$
Hence the displayed convergence holds.
:::

<1>2. The sequence in step <1>1 has a subsequence converging to a point
$y\in Y$.

::: {.proof}
For all sufficiently large $n$,
$$
d(x,y_n)\leq\delta+1.
$$
Discarding finitely many terms, the sequence lies in the closed bounded
ball
$$
\overline B(x,\delta+1).
$$
Because $M$ is proper, this ball is compact. Therefore $(y_n)$ has a
convergent subsequence
$$
y_{n_k}\longrightarrow y
$$
with
$$
y\in\overline B(x,\delta+1).
$$
Since $Y$ is closed and every $y_{n_k}$ lies in $Y$, one has $y\in Y$.
:::

<1>3. Under the hypotheses of part (1), the distance is attained:
$$
\boxed{
d(X,Y)=d(x,y)
}
$$
for the point $y$ from step <1>2.

::: {.proof}
The metric is continuous, so step <1>2 gives
$$
d(x,y)
=
\lim_{k\to\infty}d(x,y_{n_k}).
$$
By step <1>1, the limit on the right is $\delta=d(X,Y)$.
:::

<1>4. For a nonempty closed set $Y$, define
$$
\rho_Y(x)=d(\{x\},Y).
$$
Then
$$
\abs{\rho_Y(x)-\rho_Y(x')}
\leq
d(x,x')
$$
for all $x,x'\in M$.

::: {.proof}
For every $y\in Y$, the triangle inequality gives
$$
d(x,y)
\leq
d(x,x')+d(x',y).
$$
Taking the infimum over $y\in Y$ yields
$$
\rho_Y(x)
\leq
d(x,x')+\rho_Y(x').
$$
Interchanging $x$ and $x'$ gives
$$
\rho_Y(x')
\leq
d(x,x')+\rho_Y(x).
$$
Together these inequalities give the claim.
:::

<1>5. If $X$ is compact and $Y$ is closed, there is a point
$$
x_0\in X
$$
such that
$$
\rho_Y(x_0)
=
\min_{x\in X}\rho_Y(x).
$$

::: {.proof}
Step <1>4 shows that $\rho_Y$ is continuous. A continuous real-valued
function on the compact set $X$ attains its minimum.
:::

<1>6. Under the hypotheses of part (2), there are
$$
x_0\in X
\qquad\text{and}\qquad
y_0\in Y
$$
such that
$$
\boxed{
d(X,Y)=d(x_0,y_0).
}
$$

::: {.proof}
By step <1>5, choose $x_0\in X$ minimizing $\rho_Y$. By part (1), proved in
step <1>3, there is $y_0\in Y$ such that
$$
\rho_Y(x_0)=d(x_0,y_0).
$$
Moreover,
$$
\begin{aligned}
d(X,Y)
&=
\inf_{x\in X}\inf_{y\in Y}d(x,y)\\
&=
\inf_{x\in X}\rho_Y(x)\\
&=
\rho_Y(x_0).
\end{aligned}
$$
Combining the two equalities gives the result.
:::

<1>7. For part (3), in the proper metric space $\RR^2$ take
$$
X=\{(t,0):t\geq0\}
$$
and
$$
Y=\{(t,e^{-t}):t\geq0\}.
$$
Both sets are closed and noncompact.

::: {.proof}
The set $X=[0,\infty)\times\{0\}$ is closed and unbounded.

To see that $Y$ is closed, suppose
$$
(t_n,e^{-t_n})\longrightarrow(s,u)
$$
in $\RR^2$. Then $t_n\to s$, so $s\geq0$, and continuity of the
exponential gives
$$
u=e^{-s}.
$$
Thus $(s,u)\in Y$. The set $Y$ is unbounded in its first coordinate, so it
is noncompact.
:::

<1>8. The sets in step <1>7 satisfy
$$
d(X,Y)=0,
$$
but no pair $(x,y)\in X\times Y$ realizes this distance.

::: {.proof}
For every $t\geq0$, the points
$$
(t,0)\in X
\qquad\text{and}\qquad
(t,e^{-t})\in Y
$$
have distance
$$
e^{-t}.
$$
Letting $t\to\infty$ shows
$$
d(X,Y)=0.
$$

The sets are disjoint because every point of $Y$ has strictly positive
second coordinate, while every point of $X$ has second coordinate $0$.
Thus
$$
d(x,y)>0
$$
for every $x\in X$ and $y\in Y$, so the infimum is not attained.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>3 proves part (1), step <1>6 proves part (2), and steps
<1>7--<1>8 give the counterexample requested in part (3).
:::
:::

::: {.remark}
Erratum: the source states parts (1) and (2) for an arbitrary metric space.
They are false in that generality. For example, let $M=\ell^2$, let
$x=0$, and let
$$
Y
=
\left\{
\left(1+\frac1n\right)e_n:n\geq1
\right\},
$$
where $(e_n)$ is the standard orthonormal basis. Distinct points of $Y$ are
separated by more than $\sqrt2$, so $Y$ is closed. However,
$$
d(0,Y)=1
$$
and every point of $Y$ has norm strictly larger than $1$, so the distance
is not attained. Taking $X=\{0\}$ also disproves the source's printed part
(2). The corrected statement above adds properness of the ambient metric
space.
:::
