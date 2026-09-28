---
schema: qual/card@1
id: P-BERK79S-03
kind: problem
title: Maxima and minima of $\langle v_0,Av_0\rangle$ on the orthogonal group
classification:
  areas: [prelim]
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
    Orthogonality preserves ||v_0||. Expanding
    ||Av_0-v_0||^2 and ||Av_0+v_0||^2 bounds the inner product between
    ±||v_0||^2 and characterizes equality by Av_0=±v_0. Relative to
    Rv_0⊕v_0^perp, the extremizers are exactly 1⊕B and -1⊕B with
    B∈O(v_0^perp), except that if v_0=0 every orthogonal matrix is both.
---

::: {.problem}
Let $X=O(n)$ be the space of real orthogonal $n\times n$ matrices and fix $v_0\in\mathbb R^n$.
Determine and describe the matrices $A\in X$ at which
\[
f(A)=\langle v_0,Av_0\rangle
\]
attains its maximum and minimum values.
:::

::: {.solution}
<1>1. If $v_0=0$, then
$$
f(A)=0
$$
for every $A\in O(n)$.

::: {.proof}
If $v_0=0$, then
$$
Av_0=0
$$
for every linear map $A$, so
$$
\langle v_0,Av_0\rangle=0.
$$
Thus every $A\in O(n)$ is simultaneously a maximizer and a minimizer.
:::

<1>2. Assume from now on that $v_0\neq0$. For every $A\in O(n)$,
$$
\norm{Av_0}=\norm{v_0}.
$$

::: {.proof}
Orthogonality gives
$$
A^TA=I.
$$
Hence
$$
\begin{aligned}
\norm{Av_0}^2
&=
\langle Av_0,Av_0\rangle\\
&=
\langle v_0,A^TAv_0\rangle\\
&=
\langle v_0,v_0\rangle\\
&=
\norm{v_0}^2.
\end{aligned}
$$
Both norms are nonnegative, so they are equal.
:::

<1>3. For every $A\in O(n)$,
$$
f(A)\leq\norm{v_0}^2,
$$
with equality if and only if
$$
Av_0=v_0.
$$

::: {.proof}
By step <1>2,
$$
\begin{aligned}
\norm{Av_0-v_0}^2
&=
\norm{Av_0}^2+\norm{v_0}^2
-2\langle v_0,Av_0\rangle\\
&=
2\norm{v_0}^2-2f(A).
\end{aligned}
$$
The left-hand side is nonnegative, so
$$
f(A)\leq\norm{v_0}^2.
$$
Equality holds exactly when
$$
\norm{Av_0-v_0}=0,
$$
equivalently when $Av_0=v_0$.
:::

<1>4. For every $A\in O(n)$,
$$
f(A)\geq-\norm{v_0}^2,
$$
with equality if and only if
$$
Av_0=-v_0.
$$

::: {.proof}
Again using step <1>2,
$$
\begin{aligned}
\norm{Av_0+v_0}^2
&=
\norm{Av_0}^2+\norm{v_0}^2
+2\langle v_0,Av_0\rangle\\
&=
2\norm{v_0}^2+2f(A).
\end{aligned}
$$
Nonnegativity gives
$$
f(A)\geq-\norm{v_0}^2.
$$
Equality holds exactly when $Av_0+v_0=0$.
:::

<1>5. The maximum and minimum values are
$$
\boxed{
\max_{A\in O(n)}f(A)=\norm{v_0}^2,
\qquad
\min_{A\in O(n)}f(A)=-\norm{v_0}^2.
}
$$

::: {.proof}
Step <1>3 gives the upper bound, attained for example by $A=I$. Step
<1>4 gives the lower bound, attained for example by the orthogonal
reflection which sends $v_0$ to $-v_0$ and fixes $v_0^\perp$.
:::

<1>6. Relative to the orthogonal decomposition
$$
\RR^n
=
\RR v_0\oplus v_0^\perp,
$$
the maximizers are exactly the matrices of the form
$$
\boxed{
1\oplus B,
\qquad
B\in O(v_0^\perp),
}
$$
and the minimizers are exactly the matrices of the form
$$
\boxed{
-1\oplus B,
\qquad
B\in O(v_0^\perp).
}
$$

::: {.proof}
By step <1>3, a maximizer is exactly an orthogonal map satisfying
$$
Av_0=v_0.
$$
For $w\in v_0^\perp$,
$$
\langle Aw,v_0\rangle
=
\langle Aw,Av_0\rangle
=
\langle w,v_0\rangle
=
0,
$$
so $A$ preserves $v_0^\perp$. Its restriction there is orthogonal, giving
the form $1\oplus B$. Conversely every such block map is orthogonal and
fixes $v_0$, hence is a maximizer.

For a minimizer, step <1>4 gives
$$
Av_0=-v_0.
$$
Then for $w\in v_0^\perp$,
$$
\langle Aw,v_0\rangle
=
-\langle Aw,Av_0\rangle
=
-\langle w,v_0\rangle
=
0,
$$
so again the complement is preserved and the restriction is orthogonal.
This gives exactly the form $-1\oplus B$, and every such map is a
minimizer.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>1 handles $v_0=0$, while steps <1>5--<1>6 give the values and all
extremizing matrices when $v_0\neq0$.
:::
:::
