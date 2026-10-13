---
schema: qual/card@1
id: P-UCLARA12S-05
kind: problem
title: Riesz representation theorem for Hilbert-space functionals
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the Spring 2012 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
State and prove the Riesz representation theorem for linear functionals on a Hilbert space.
:::

::: {.solution}
Assume the inner product is linear in its first variable.

<1>1. Let $H$ be a real or complex Hilbert space and let $L:H\to\mathbb F$ be a bounded linear functional. Then there exists a unique $y\in H$ such that
$$
\boxed{L(x)=\langle x,y\rangle\quad\text{for every }x\in H,}
$$
and moreover
$$
\boxed{\norm L=\norm y.}
$$

::: {.proof}
This is the Riesz representation theorem for Hilbert-space functionals. The remaining steps prove existence, uniqueness, and the norm identity.
:::

<1>2. If $L\ne0$, then $\ker L$ is a proper closed subspace and
$$
H=\ker L\oplus(\ker L)^\perp.
$$

::: {.proof}
Continuity of $L$ makes $\ker L=L^{-1}(\{0\})$ closed. Since $L\ne0$, its kernel is proper. The orthogonal-decomposition theorem for closed subspaces of a Hilbert space gives the displayed decomposition.
:::

<1>3. If $L\ne0$, choose $0\ne u\in(\ker L)^\perp$. Then
$$
y\coloneqq\frac{\overline{L(u)}}{\norm u^2}u
$$
satisfies $L(x)=\langle x,y\rangle$ for every $x\in H$.

::: {.proof}
Since $u\notin\ker L$, one has $L(u)\ne0$. For any $x\in H$, set
$$
v\coloneqq x-\frac{L(x)}{L(u)}u.
$$
Then $L(v)=0$, so $v\in\ker L$. As $u\perp\ker L$,
$$
0
=
\langle v,u\rangle
=
\langle x,u\rangle
-\frac{L(x)}{L(u)}\norm u^2.
$$
Therefore
$$
L(x)
=
\frac{L(u)}{\norm u^2}\langle x,u\rangle.
$$
Because the inner product is conjugate-linear in its second variable,
$$
\langle x,y\rangle
=
\frac{L(u)}{\norm u^2}\langle x,u\rangle
=
L(x).
$$
:::

<1>4. The representing vector exists for every bounded linear functional.

::: {.proof}
If $L=0$, take $y=0$. If $L\ne0$, step <1>3 supplies the required vector.
:::

<1>5. The representing vector is unique.

::: {.proof}
If $y_1,y_2\in H$ both represent $L$, then
$$
\langle x,y_1-y_2\rangle=0
$$
for every $x\in H$. Taking $x=y_1-y_2$ gives
$$
\norm{y_1-y_2}^2=0,
$$
so $y_1=y_2$.
:::

<1>6. The norm identity $\norm L=\norm y$ holds.

::: {.proof}
By Cauchy--Schwarz,
$$
\abs{L(x)}
=
\abs{\langle x,y\rangle}
\le
\norm x\,\norm y,
$$
so $\norm L\le\norm y$. If $y\ne0$, taking $x=y/\norm y$ gives
$$
\abs{L(x)}=\norm y,
$$
hence $\norm L\ge\norm y$. If $y=0$, both norms are zero.
:::

<1>7. Q.E.D.

::: {.proof}
Steps <1>4--<1>6 prove existence, uniqueness, and the norm identity in the theorem stated in step <1>1.
:::
:::
