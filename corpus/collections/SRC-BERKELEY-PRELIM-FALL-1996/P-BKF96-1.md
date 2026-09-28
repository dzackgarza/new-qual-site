---
schema: qual/card@1
id: P-BKF96-1
kind: problem
title: Compact subsets of $C^1[0,1]$ with the $C^1$ norm
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Characterized compact sets as the closed norm-bounded subsets whose
    derivative family is equicontinuous. Necessity uses Arzela-Ascoli on the
    derivative image; sufficiency reconstructs functions from f(0) and f'.
---

::: {.problem}
Let $M$ be the space of real-valued functions $f$ on $[0,1]$ for which $f$ and $f'$ are continuous, with norm
\[
\|f\|=\sup_{0\le x\le1}|f(x)|+\sup_{0\le x\le1}|f'(x)|.
\]
Which subsets of $M$ are compact?
:::

::: {.solution}
For a subset $K\subseteq M$, write
$$
K'
\coloneqq
\{f':f\in K\}
\subseteq C[0,1].
$$

The compact subsets of $M$ are exactly the subsets $K$ satisfying all
three conditions:

1. $K$ is closed in $M$;
2. $K$ is bounded in the given norm;
3. $K'$ is equicontinuous on $[0,1]$.

<1>1. If $K$ is compact in $M$, then $K$ is closed and bounded in $M$.

::: {.proof}
Every compact subset of a metric space is closed and bounded.
:::

<1>2. If $K$ is compact in $M$, then $K'$ is equicontinuous.

::: {.proof}
The derivative map
$$
D:M\longrightarrow C[0,1],
\qquad
D(f)=f',
$$
is continuous when $C[0,1]$ has the uniform norm, because
$$
\norm{f'-g'}_\infty
\leq
\norm{f-g}.
$$
Therefore $K'=D(K)$ is compact in $C[0,1]$. By the Arzelà--Ascoli theorem,
every compact family of continuous functions on $[0,1]$ is
equicontinuous.
:::

<1>3. Conversely, suppose $K$ is closed and bounded in $M$ and $K'$ is
equicontinuous. Then every sequence $(f_n)$ in $K$ has a subsequence for
which $(f_n')$ converges uniformly on $[0,1]$.

::: {.proof}
Boundedness of $K$ in $M$ gives a constant $C$ such that
$$
\norm{f_n'}_\infty\leq C
$$
for every $n$. Thus the derivative family is uniformly bounded, and it is
equicontinuous by hypothesis. The Arzelà--Ascoli theorem gives a uniformly
convergent subsequence of $(f_n')$.
:::

<1>4. After passing to a further subsequence, there are
$a\in\RR$ and $g\in C[0,1]$ such that
$$
f_n(0)\longrightarrow a
$$
and
$$
f_n'\longrightarrow g
$$
uniformly.

::: {.proof}
Use the subsequence from step <1>3. Boundedness of $K$ also gives
$$
\abs{f_n(0)}
\leq
\norm{f_n}_\infty
\leq
\norm{f_n}
\leq C.
$$
Hence the real sequence $(f_n(0))$ has a convergent subsequence. Passing
to it preserves the uniform convergence of the derivatives.
:::

<1>5. Define
$$
f(x)
\coloneqq
a+\int_0^x g(t)\,dt.
$$
Then
$$
f_n\longrightarrow f
$$
in the norm of $M$.

::: {.proof}
The function $f$ is continuously differentiable and
$$
f'=g.
$$
For every $x\in[0,1]$,
$$
f_n(x)
=
f_n(0)+\int_0^x f_n'(t)\,dt.
$$
Therefore
$$
\begin{aligned}
\abs{f_n(x)-f(x)}
&\leq
\abs{f_n(0)-a}
+\int_0^x\abs{f_n'(t)-g(t)}\,dt\\
&\leq
\abs{f_n(0)-a}
+\norm{f_n'-g}_\infty.
\end{aligned}
$$
Taking the supremum over $x$ shows
$$
\norm{f_n-f}_\infty\longrightarrow0.
$$
Step <1>4 also gives
$$
\norm{f_n'-f'}_\infty
=
\norm{f_n'-g}_\infty
\longrightarrow0.
$$
Thus
$$
\norm{f_n-f}
=
\norm{f_n-f}_\infty
+\norm{f_n'-f'}_\infty
\longrightarrow0.
$$
:::

<1>6. The limit $f$ from step <1>5 belongs to $K$.

::: {.proof}
The subsequence consists of points of $K$ and converges to $f$ in $M$.
Since $K$ is closed in $M$, one has $f\in K$.
:::

<1>7. Under the three stated conditions, $K$ is compact.

::: {.proof}
Steps <1>3--<1>6 show that every sequence in $K$ has a subsequence
converging in $M$ to a point of $K$. Thus $K$ is sequentially compact.
Because $M$ is a metric space, sequential compactness is equivalent to
compactness.
:::

<1>8. Q.E.D.

::: {.proof}
Steps <1>1--<1>2 prove that compactness implies the three conditions, and
step <1>7 proves the converse.
:::
:::
