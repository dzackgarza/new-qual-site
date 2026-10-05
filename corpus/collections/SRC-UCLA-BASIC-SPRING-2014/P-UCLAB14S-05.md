---
schema: qual/card@1
id: P-UCLAB14S-05
kind: problem
title: Nonuniqueness of least-squares minimizers
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
  note: Checked against Problem 5 of the retained UCLA Basic Examination, Spring 2014.
---

::: {.problem}
Problem 5. Suppose that $V$ is a finite-dimensional real inner-product space with inner product $(\cdot,\cdot)$, that $L\in\operatorname{Hom}(V,V)$, and that $b\in V$ is fixed.
Suppose that $u,v\in V$ both minimize
\[
D(x)=\lVert L(x)-b\rVert.
\]
Show that $u-v\in\ker L$.
:::

::: {.solution}
<1>1. Let
\[
y=L(u)-b,
\qquad
z=L(v)-b.
\]
Since $u$ and $v$ are both minimizers, there is a number $m\geq0$ such that
\[
\|y\|=\|z\|=m.
\]

::: {.proof}
By definition, $D(u)=\|L(u)-b\|=\|y\|$ and $D(v)=\|L(v)-b\|=\|z\|$. Both equal the minimum value of $D$.
:::

<1>2. The midpoint
\[
w=\frac{u+v}{2}
\]
satisfies
\[
L(w)-b=\frac{y+z}{2}.
\]

::: {.proof}
Linearity of $L$ gives
\[
L(w)-b
=\frac{L(u)+L(v)}2-b
=\frac{(L(u)-b)+(L(v)-b)}2
=\frac{y+z}{2}.
\]
:::

<1>3. Since $u$ is a minimizer,
\[
m\leq D(w)=\left\|\frac{y+z}{2}\right\|.
\]

::: {.proof}
The minimum value of $D$ is $m$ by step <1>1, so $D(x)\geq m$ for every $x\in V$, in particular for $x=w$. Step <1>2 gives the displayed expression.
:::

<1>4. The triangle inequality gives the reverse bound
\[
\left\|\frac{y+z}{2}\right\|
\leq\frac{\|y\|+\|z\|}{2}=m.
\]

::: {.proof}
Apply homogeneity and the triangle inequality, then use $\|y\|=\|z\|=m$ from step <1>1.
:::

<1>5. Hence
\[
\left\|\frac{y+z}{2}\right\|=m.
\]

::: {.proof}
Combine the lower bound in step <1>3 with the upper bound in step <1>4.
:::

<1>6. The parallelogram identity implies
\[
\|y-z\|^2=0.
\]

::: {.proof}
The parallelogram identity is
\[
\|y+z\|^2+\|y-z\|^2
=2\|y\|^2+2\|z\|^2.
\]
By step <1>5, $\|y+z\|=2m$, while step <1>1 gives $\|y\|=\|z\|=m$. Therefore
\[
4m^2+\|y-z\|^2=4m^2,
\]
so $\|y-z\|^2=0$.
:::

<1>7. Thus
\[
y=z,
\]
and consequently
\[
L(u-v)=0.
\]

::: {.proof}
Step <1>6 gives $y-z=0$. By the definitions in step <1>1,
\[
y-z=(L(u)-b)-(L(v)-b)=L(u)-L(v)=L(u-v).
\]
:::

<1>8. Therefore
\[
\boxed{u-v\in\ker L.}
\]

::: {.proof}
This is exactly the statement $L(u-v)=0$ from step <1>7.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>8 proves the claim.
:::
:::
