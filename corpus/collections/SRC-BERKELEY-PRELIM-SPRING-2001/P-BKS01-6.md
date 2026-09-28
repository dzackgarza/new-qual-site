---
schema: qual/card@1
id: P-BKS01-6
kind: problem
title: Eigenvalue one for special orthogonal matrices in odd and even dimensions
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-13}
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    For odd n, used S^{-1}=S^T and det S=1 to obtain
    det(S-I)=det(I-S)=(-1)^n det(S-I), hence det(S-I)=0. For even n,
    the special orthogonal matrix -I_n has no eigenvalue 1.
---

::: {.problem}
Let $S$ be a real special orthogonal $n\times n$ matrix: $S^TS=I$ and $\det S=1$.

1. Prove that if $n$ is odd, then $1$ is an eigenvalue of $S$.
2. Show that if $n$ is even, then $1$ need not be an eigenvalue.
:::

::: {.solution}
<1>1. One has
$$
\det(S-I)
=
\det(I-S).
$$

::: {.proof}
Since $S$ is orthogonal,
$$
S^{-1}=S^T.
$$
Using also $\det S=1$,
$$
\begin{aligned}
\det(S-I)
&=
\det\bigl(S(I-S^{-1})\bigr)\\
&=
\det S\,\det(I-S^{-1})\\
&=
\det(I-S^T)\\
&=
\det\bigl((I-S)^T\bigr)\\
&=
\det(I-S).
\end{aligned}
$$
:::

<1>2. If $n$ is odd, then
$$
\det(S-I)=0.
$$

::: {.proof}
For every $n$,
$$
\det(I-S)
=
(-1)^n\det(S-I).
$$
Combining this with step <1>1 gives
$$
\det(S-I)
=
(-1)^n\det(S-I).
$$
When $n$ is odd, this becomes
$$
\det(S-I)
=
-\det(S-I),
$$
so $2\det(S-I)=0$. Over $\RR$, this implies $\det(S-I)=0$.
:::

<1>3. If $n$ is odd, then $1$ is an eigenvalue of $S$.

::: {.proof}
By step <1>2, $S-I$ is singular. Hence there exists a nonzero vector
$v$ with
$$
(S-I)v=0,
$$
equivalently $Sv=v$.
:::

<1>4. If $n$ is even, the matrix
$$
S=-I_n
$$
is special orthogonal and has no eigenvalue $1$.

::: {.proof}
One has
$$
S^TS=(-I_n)^2=I_n.
$$
Moreover,
$$
\det S
=
(-1)^n
=1
$$
because $n$ is even. Thus $S$ is special orthogonal. Its only
eigenvalue is $-1$, so $1$ is not an eigenvalue.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>3 proves part 1, and step <1>4 proves part 2.
:::
:::
