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

::: pf

::: {.pf-step #s1}

If $v_0=0$, then
$$
f(A)=0
$$
for every $A\in O(n)$.

::: pf-proof

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

:::

::: {.pf-step #s2}

Assume from now on that $v_0\neq0$. For every $A\in O(n)$,
$$
\norm{Av_0}=\norm{v_0}.
$$

::: pf-proof

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

:::

::: {.pf-step #s3}

For every $A\in O(n)$,
$$
f(A)\leq\norm{v_0}^2,
$$
with equality if and only if
$$
Av_0=v_0.
$$

::: pf-proof

By step [](#s2){.pf-ref},
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

:::

::: {.pf-step #s4}

For every $A\in O(n)$,
$$
f(A)\geq-\norm{v_0}^2,
$$
with equality if and only if
$$
Av_0=-v_0.
$$

::: pf-proof

Again using step [](#s2){.pf-ref},
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

:::

::: {.pf-step #s5}

The maximum and minimum values are
$$
\boxed{
\max_{A\in O(n)}f(A)=\norm{v_0}^2,
\qquad
\min_{A\in O(n)}f(A)=-\norm{v_0}^2.
}
$$

::: pf-proof

Step [](#s3){.pf-ref} gives the upper bound, attained for example by $A=I$. Step
[](#s4){.pf-ref} gives the lower bound, attained for example by the orthogonal
reflection which sends $v_0$ to $-v_0$ and fixes $v_0^\perp$.

:::

:::

::: {.pf-step #s6}

Relative to the orthogonal decomposition
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

::: pf-proof

By step [](#s3){.pf-ref}, a maximizer is exactly an orthogonal map satisfying
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

For a minimizer, step [](#s4){.pf-ref} gives
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

:::

::: pf-qed

Step [](#s1){.pf-ref} handles $v_0=0$, while steps [](#s5){.pf-ref} and [](#s6){.pf-ref} give the values and all
extremizing matrices when $v_0\neq0$.

:::

:::

:::
