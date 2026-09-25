---
schema: qual/card@1
id: P-BKF92-6
kind: problem
title: Completeness under the metric comparison stated in the Fall 1992 source
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: The retained extraction corrupts the comparison between d_1(p,q) and d_2(f(p),f(q)) as the symbol `\in`. No independent transcription of the missing comparison was found, so the relation is not guessed.
- event: source-corrected
  by: chatgpt
  date: 2026-09-25
  note: Restored the comparison d_1(p,q) <= d_2(f(p),f(q)) directly from the retained Fall92.pdf source.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Proved completeness passes from X_1 to X_2 by pulling back Cauchy sequences,
    and disproved the converse with tan(pi(x-1/2)) from (0,1) onto R.
---

::: {.problem}
Let $(X_1,d_1)$ and $(X_2,d_2)$ be metric spaces, and let
\[
f:X_1\to X_2
\]
be a continuous surjection such that
\[
d_1(p,q)\le d_2(f(p),f(q))
\]
for every $p,q\in X_1$.

1. If $X_1$ is complete, must $X_2$ be complete? Give a proof or counterexample.
2. If $X_2$ is complete, must $X_1$ be complete? Give a proof or counterexample.
:::

::: {.solution}
<1>1. The map $f$ is injective, hence bijective.

::: {.proof}
If $f(p)=f(q)$, then the metric comparison gives
$$
d_1(p,q)
\le
d_2(f(p),f(q))
=0.
$$
Thus $p=q$. Since $f$ is surjective by hypothesis, it is bijective.
:::

<1>2. If $X_1$ is complete, then $X_2$ is complete.

::: {.proof}
Let $(y_n)$ be a Cauchy sequence in $X_2$. By step <1>1, define
$$
x_n\coloneqq f^{-1}(y_n).
$$
Then
$$
d_1(x_m,x_n)
\le
d_2(f(x_m),f(x_n))
=
d_2(y_m,y_n),
$$
so $(x_n)$ is Cauchy in $X_1$. If $X_1$ is complete, there is $x\in X_1$ with
$$
x_n\longrightarrow x.
$$
Continuity of $f$ gives
$$
y_n=f(x_n)\longrightarrow f(x)\in X_2.
$$
Thus every Cauchy sequence in $X_2$ converges.
:::

<1>3. Therefore the answer to part 1 is
$$
\boxed{\text{yes}}.
$$

::: {.proof}
This is exactly step <1>2.
:::

<1>4. For part 2, let
$$
X_1=(0,1),
\qquad
X_2=\RR,
$$
with their usual metrics, and define
$$
f(x)=\tan\bigl(\pi(x-1/2)\bigr).
$$
Then $f:X_1\to X_2$ is a continuous surjection satisfying the required metric comparison.

::: {.proof}
The tangent function is continuous and strictly increasing from $-\infty$ to $\infty$ on $(-\pi/2,\pi/2)$, so the displayed $f$ is a continuous bijection from $(0,1)$ onto $\RR$.

Moreover,
$$
f'(x)
=
\pi\sec^2\bigl(\pi(x-1/2)\bigr)
\ge
\pi
>1.
$$
For $x\ne y$, the mean value theorem gives some $c$ between them such that
$$
\abs{f(x)-f(y)}
=
f'(c)\abs{x-y}
\ge
\abs{x-y}.
$$
Thus
$$
d_1(x,y)\le d_2(f(x),f(y)).
$$
:::

<1>5. In the example from step <1>4, $X_2$ is complete but $X_1$ is not complete.

::: {.proof}
The real line with its usual metric is complete. The interval $(0,1)$ is not complete: for example,
$$
x_n=\frac1n
$$
is Cauchy in $(0,1)$ but converges in $\RR$ to $0\notin(0,1)$.
:::

<1>6. Therefore the answer to part 2 is
$$
\boxed{\text{no}}.
$$

::: {.proof}
Steps <1>4 and <1>5 give a counterexample satisfying every hypothesis.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>3 proves part 1, and step <1>6 proves part 2.
:::
:::
