---
schema: qual/card@1
id: P-APAS04L
kind: problem
title: Radical identities for ideals and radical-membership computations
classification:
  areas:
  - applied-algebra
  topics:
  - Commutative Algebra
  - Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
  note: Repaired the false explicit identity in part (c) and made the characteristic dependence in part (d) explicit.
---

::: problem
Let $I$ and $J$ be ideals in the polynomial ring $R = k[x_1, \dots, x_n]$ where $k$ is a field.

(a) Show that $\sqrt{\sqrt{I}} = \sqrt{I}$.
(b) Show that $\sqrt{I \cap J} = \sqrt{IJ} = \sqrt{I} \cap \sqrt{J}$.
(c) Is $x^2 - y^2 \in \sqrt{\langle x^2 + x, x^2 - y \rangle}$ in $k[x, y]$?
(d) Is $x^2 + y^2 \in \sqrt{\langle x + y, x^2 - y \rangle}$ in $k[x, y]$?
:::

::: {.solution}
<1>1. One has $\sqrt{\sqrt I}=\sqrt I$.
::: {.proof}
The inclusion $\sqrt I\subseteq\sqrt{\sqrt I}$ is immediate from $I\subseteq\sqrt I$.
Conversely, if $f\in\sqrt{\sqrt I}$, then $f^m\in\sqrt I$ for some $m\ge1$. Hence $(f^m)^r=f^{mr}\in I$ for some $r\ge1$, so $f\in\sqrt I$.
:::

<1>2. One has
\[
\sqrt{I\cap J}=\sqrt{IJ}=\sqrt I\cap\sqrt J.
\]
::: {.proof}
Since $IJ\subseteq I\cap J$, we have
\[
\sqrt{IJ}\subseteq\sqrt{I\cap J}.
\]
If $f\in\sqrt{I\cap J}$, then $f^m\in I\cap J$ for some $m$, hence $f\in\sqrt I\cap\sqrt J$.
Finally, if $f\in\sqrt I\cap\sqrt J$, choose $a,b\ge1$ with $f^a\in I$ and $f^b\in J$. Then
\[
f^{a+b}=f^af^b\in IJ,
\]
so $f\in\sqrt{IJ}$. The three containments give equality.
:::

<1>3. For
\[
I_1=\langle x^2+x,\ x^2-y\rangle,
\]
one has $x^2-y^2\in I_1$, hence certainly $x^2-y^2\in\sqrt{I_1}$.
::: {.proof}
In $R/I_1$ we have
\[
y=x^2=-x.
\]
Therefore
\[
y^2=x^2,
\]
so the class of $x^2-y^2$ in $R/I_1$ is zero. Equivalently, $x^2-y^2\in I_1$.
:::

<1>4. For
\[
I_2=\langle x+y,\ x^2-y\rangle,
\]
the answer depends on $\operatorname{char}k$:
\[
x^2+y^2\in\sqrt{I_2}
\quad\Longleftrightarrow\quad
\operatorname{char}k=2.
\]
::: {.proof}
Modulo $I_2$ we have $y=-x$ and $x^2=-x$, hence
\[
x^2+y^2=2x^2=-2x.
\]
If $\operatorname{char}k=2$, this class is zero, so $x^2+y^2\in I_2$.

Assume now $\operatorname{char}k\ne2$. The quotient is
\[
R/I_2\cong k[x]/(x^2+x)=k[x]/(x(x+1)),
\]
under $y\mapsto -x$. Since $x$ and $x+1$ are coprime,
\[
(x(x+1))=(x)\cap(x+1)
\]
is radical. Thus $I_2$ is radical. The class of $x^2+y^2$ is $-2x$, which is nonzero in this quotient (for example its image modulo $(x+1)$ is $2\ne0$). Therefore
\[
x^2+y^2\notin I_2=\sqrt{I_2}.
\]
:::
:::
