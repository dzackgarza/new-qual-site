---
schema: qual/card@1
id: P-PRELIM82S-14
kind: problem
title: Equality of the kernels of $A$ and $A^T$ under a nonnegative quadratic form
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
    If q(u)=<Au,u>=0, expanding q(u+tx)>=0 shows that the coefficient
    of t must vanish for every x, hence (A+A^T)u=0. If Au=0 this gives
    A^T u=0; if A^T u=0 then q(u)=0 and the same identity gives Au=0.
---

::: {.problem}
Let $A$ be a real $n\times n$ matrix such that
\[
\langle Ax,x\rangle\ge0
\]
for every $x\in\mathbb R^n$.
Show that, for every $u\in\mathbb R^n$,
\[
Au=0
\quad\Longleftrightarrow\quad
A^Tu=0.
\]
:::

::: {.solution}
Define
$$
q(x)=\inner{Ax}{x}.
$$

<1>1. If $q(u)=0$, then
$$
(A+A^T)u=0.
$$

<2>1. For every $x\in\RR^n$ and every $t\in\RR$,
$$
q(u+tx)
=
t\inner{(A+A^T)u}{x}
+
t^2q(x).
$$

::: {.proof}
Since $q(u)=0$,
$$
\begin{aligned}
q(u+tx)
&=
\inner{A(u+tx)}{u+tx}\\
&=
t\inner{Au}{x}
+
t\inner{Ax}{u}
+
t^2\inner{Ax}{x}\\
&=
t\inner{Au+A^Tu}{x}
+
t^2q(x).
\end{aligned}
$$
:::

<2>2. For every $x\in\RR^n$,
$$
\inner{(A+A^T)u}{x}=0.
$$

::: {.proof}
Fix $x$ and set
$$
c=\inner{(A+A^T)u}{x},
\qquad
d=q(x)\geq0.
$$
By the hypothesis and step <2>1,
$$
tc+t^2d\geq0
$$
for every real $t$. If $c\neq0$, choose $t$ with sign opposite to
$c$ and with
$$
0<\abs{t}<\frac{\abs{c}}{d+1}.
$$
Then
$$
tc+t^2d
\leq
-\abs{t}\abs{c}
+
\abs{t}^2d
<0,
$$
a contradiction. Hence $c=0$.
:::

<2>3. One has
$$
(A+A^T)u=0.
$$

::: {.proof}
Apply step <2>2 with
$$
x=(A+A^T)u.
$$
Then
$$
\norm{(A+A^T)u}^2=0,
$$
so $(A+A^T)u=0$.
:::

<2>4. Q.E.D.

::: {.proof}
Step <2>3 proves step <1>1.
:::

<1>2. If $Au=0$, then $A^Tu=0$.

::: {.proof}
If $Au=0$, then
$$
q(u)=\inner{Au}{u}=0.
$$
Step <1>1 therefore gives
$$
Au+A^Tu=0.
$$
Since $Au=0$, it follows that $A^Tu=0$.
:::

<1>3. If $A^Tu=0$, then $Au=0$.

::: {.proof}
If $A^Tu=0$, then
$$
q(u)
=
\inner{Au}{u}
=
\inner{u}{A^Tu}
=0.
$$
Step <1>1 therefore gives
$$
Au+A^Tu=0.
$$
Since $A^Tu=0$, it follows that $Au=0$.
:::

<1>4. Therefore, for every $u\in\RR^n$,
$$
\boxed{Au=0\quad\Longleftrightarrow\quad A^Tu=0}.
$$

::: {.proof}
The forward implication is step <1>2 and the reverse implication is
step <1>3.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required equivalence.
:::
:::
