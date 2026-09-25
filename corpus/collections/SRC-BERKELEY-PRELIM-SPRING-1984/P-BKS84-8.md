---
schema: qual/card@1
id: P-BKS84-8
kind: problem
title: A linear system with a trajectory decaying forward and diverging backward
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
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Checked the explicit solution along the eigenvector for the negative eigenvalue $-\sqrt2$.
---

::: {.problem}
Show that the system
\[
\frac d{dt}\begin{pmatrix}x\\y\\z\end{pmatrix}
=
\begin{pmatrix}
0&1&0\\
2&0&0\\
0&0&3
\end{pmatrix}
\begin{pmatrix}x\\y\\z\end{pmatrix}
\]
has a solution whose norm tends to $\infty$ as $t\to-\infty$ and tends to $0$ as $t\to+\infty$.
:::

::: {.solution}
Let
$$
M
=
\begin{pmatrix}
0&1&0\\
2&0&0\\
0&0&3
\end{pmatrix}.
$$

<1>1. The vector
$$
v
=
\begin{pmatrix}
1\\
-\sqrt2\\
0
\end{pmatrix}
$$
is an eigenvector of $M$ with eigenvalue $-\sqrt2$.

::: {.proof}
Direct multiplication gives
$$
Mv
=
\begin{pmatrix}
-\sqrt2\\
2\\
0
\end{pmatrix}
=
-\sqrt2
\begin{pmatrix}
1\\
-\sqrt2\\
0
\end{pmatrix}
=
-\sqrt2 v.
$$
:::

<1>2. The function
$$
X(t)
\coloneqq
e^{-\sqrt2 t}v
$$
is a solution of the system.

::: {.proof}
Using step <1>1,
$$
X'(t)
=
-\sqrt2 e^{-\sqrt2 t}v
=
e^{-\sqrt2 t}Mv
=
MX(t).
$$
:::

<1>3. This solution has the required limiting behavior:
$$
\norm{X(t)}\longrightarrow0
\quad(t\to+\infty),
$$
while
$$
\norm{X(t)}\longrightarrow\infty
\quad(t\to-\infty).
$$

::: {.proof}
Since $v\neq0$,
$$
\norm{X(t)}
=
e^{-\sqrt2 t}\norm v.
$$
The scalar factor tends to $0$ as $t\to+\infty$ and to $\infty$ as
$t\to-\infty$.
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>2--<1>3 exhibit the requested solution explicitly.
:::
:::
