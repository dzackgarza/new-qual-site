---
schema: qual/card@1
id: P-BKF08-6A
kind: problem
title: Young's inequality from integrals of a function and its inverse
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 6A of the retained Berkeley Fall 2008 preliminary-exam solution packet f08solutions.pdf. The packet explicitly corrects both inequality directions from the original exam.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the area identity for a function and its inverse, both cases
    relative to b=f(a), and the conjugate-exponent specialization.
---

::: {.problem}
Let $f$ be a continuous strictly increasing function with $f(0)=0$ and inverse $f^{-1}$.
Show that
$$
\int_0^a f(x)\,dx+\int_0^b f^{-1}(x)\,dx\ge ab
$$
for all positive real numbers $a,b$.
Use this to prove Young's inequality: if $p,q>0$ satisfy $1/p+1/q=1$, then for all $a,b>0$,
$$
\frac{a^p}{p}+\frac{b^q}{q}\ge ab.
$$
:::

::: {.hint}
Draw a picture.
:::

::: {.solution}
<1>1. For every $c>0$,
$$
\int_0^c f(x)\,dx
+\int_0^{f(c)} f^{-1}(y)\,dy
=c f(c).
$$

::: {.proof}
Consider the rectangle
$$
R=[0,c]\times[0,f(c)].
$$
Since $f$ is continuous and strictly increasing with $f(0)=0$, its graph
divides $R$ into two regions. The region below the graph has area
$$
\int_0^c f(x)\,dx.
$$
For fixed $y\in[0,f(c)]$, the points of $R$ on or above the graph satisfy
$f(x)\le y$, equivalently $x\le f^{-1}(y)$, so that region has area
$$
\int_0^{f(c)} f^{-1}(y)\,dy.
$$
The graph itself has area zero, so the two areas add to
$\operatorname{area}(R)=cf(c)$.
:::

<1>2. If $b\ge f(a)$, then
$$
\int_0^a f(x)\,dx+\int_0^b f^{-1}(y)\,dy-ab\ge0.
$$

::: {.proof}
By step <1>1 with $c=a$,
$$
\int_0^a f(x)\,dx
+\int_0^{f(a)}f^{-1}(y)\,dy
=a f(a).
$$
Hence
$$
\begin{aligned}
&\int_0^a f(x)\,dx+\int_0^b f^{-1}(y)\,dy-ab\\
&\qquad=\int_{f(a)}^b\bigl(f^{-1}(y)-a\bigr)\,dy.
\end{aligned}
$$
For $y\ge f(a)$, monotonicity of $f^{-1}$ gives
$f^{-1}(y)\ge a$, so the last integral is nonnegative.
:::

<1>3. If $0<b\le f(a)$, then
$$
\int_0^a f(x)\,dx+\int_0^b f^{-1}(y)\,dy-ab\ge0.
$$

::: {.proof}
Again using step <1>1 with $c=a$,
$$
\begin{aligned}
&\int_0^a f(x)\,dx+\int_0^b f^{-1}(y)\,dy-ab\\
&\qquad=\int_b^{f(a)}\bigl(a-f^{-1}(y)\bigr)\,dy.
\end{aligned}
$$
For $y\le f(a)$, monotonicity of $f^{-1}$ gives
$f^{-1}(y)\le a$, so this integral is nonnegative.
:::

<1>4. Therefore, for all $a,b>0$,
$$
\int_0^a f(x)\,dx+\int_0^b f^{-1}(x)\,dx\ge ab.
$$

::: {.proof}
At least one of the two cases in steps <1>2 and <1>3 applies.
:::

<1>5. If $p,q>0$ and $1/p+1/q=1$, then $p,q>1$ and
$$
q-1=\frac1{p-1}.
$$

::: {.proof}
Since $1/q>0$, one has $1/p<1$, hence $p>1$; similarly $q>1$.
Solving
$$
\frac1p+\frac1q=1
$$
for $q$ gives $q=p/(p-1)$, and therefore
$q-1=1/(p-1)$.
:::

<1>6. Taking $f(x)=x^{p-1}$ in step <1>4 gives
$$
\boxed{
\frac{a^p}{p}+\frac{b^q}{q}\ge ab
}.
$$

::: {.proof}
By step <1>5, the function $f(x)=x^{p-1}$ is continuous and strictly
increasing on $[0,\infty)$, with
$$
f^{-1}(y)=y^{1/(p-1)}=y^{q-1}.
$$
Thus step <1>4 becomes
$$
\int_0^a x^{p-1}\,dx
+\int_0^b y^{q-1}\,dy
\ge ab.
$$
Evaluating the two integrals gives the displayed Young inequality.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>4 proves the first requested inequality, and step <1>6 proves
Young's inequality.
:::
:::

::: {.remark}
The retained Fall 2008 solution packet states that the exam originally
printed both inequalities with the wrong direction; the inequalities above
are the packet's explicit correction.
:::
