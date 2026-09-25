---
schema: qual/card@1
id: P-BKF86-2
kind: problem
title: Three unit complex numbers with zero sum form an equilateral triangle
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
---

::: {.problem}
Let the points $a$, $b$, and $c$ lie on the unit circle of the complex plane and satisfy $a+b+c=0$.
Prove that $a$, $b$, and $c$ form the vertices of an equilateral triangle.
:::

::: {.solution}
<1>1. One has
$$
\operatorname{Re}(a\overline b)
=
\operatorname{Re}(b\overline c)
=
\operatorname{Re}(c\overline a)
=
-\frac12.
$$

::: {.proof}
Since $a+b=-c$ and $\abs{a}=\abs{b}=\abs{c}=1$,
$$
1
=
\abs{a+b}^2
=
(a+b)(\overline a+\overline b)
=
2+2\operatorname{Re}(a\overline b).
$$
Hence
$$
\operatorname{Re}(a\overline b)=-\frac12.
$$
The same argument applied to $b+c=-a$ and $c+a=-b$ gives the other two identities.
:::

<1>2. The three pairwise distances are equal:
$$
\abs{a-b}
=
\abs{b-c}
=
\abs{c-a}
=
\sqrt3.
$$

::: {.proof}
Using step <1>1,
$$
\begin{aligned}
\abs{a-b}^2
&=
(a-b)(\overline a-\overline b)\\
&=
2-2\operatorname{Re}(a\overline b)\\
&=
3.
\end{aligned}
$$
The identical calculation for the pairs $(b,c)$ and $(c,a)$ gives squared distance $3$ in each case.
:::

<1>3. The points $a,b,c$ are the vertices of an equilateral triangle.

::: {.proof}
By step <1>2 all three side lengths are equal to $\sqrt3>0$. In particular the points are distinct, and the triangle they determine is equilateral.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the required conclusion.
:::
:::
