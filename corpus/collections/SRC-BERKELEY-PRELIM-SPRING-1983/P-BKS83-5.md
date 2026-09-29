---
schema: qual/card@1
id: P-BKS83-5
kind: problem
title: All solutions of $y'=\sqrt{y(y-2)}$ with $y(0)=0$
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
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: Checked the separation on the negative branch, the waiting-time classification, and the converse substitution including differentiability at the joining point.
---

::: {.problem}
Find all real-valued solutions $y:\mathbb R\to\mathbb R$ of
\[
\frac{dy}{dx}=\sqrt{y(y-2)},
\qquad
y(0)=0.
\]
:::

::: {.solution}
For each $a\le 0$, define
$$
y_a(x)\coloneqq
\begin{cases}
1-\cosh(a-x),&x\le a,\\
0,&x\ge a.
\end{cases}
$$

::: pf

::: {.pf-step #monotone-and-zero-forward}
Every real-valued solution $y$ is nondecreasing, satisfies
$y(x)=0$ for $x\ge0$, and satisfies $y(x)\le0$ for $x\le0$.

::: pf-proof
At every $x$ where the differential equation holds, the radicand must be
nonnegative, so
$$
y(x)\in(-\infty,0]\cup[2,\infty).
$$
Moreover,
$$
y'(x)=\sqrt{y(x)(y(x)-2)}\ge0,
$$
so $y$ is nondecreasing. Hence $y(x)\ge y(0)=0$ for $x\ge0$ and
$y(x)\le y(0)=0$ for $x\le0$.

If $y(x_1)\ge2$ for some $x_1>0$, continuity and $y(0)=0$ would force
$y$ to take a value in $(0,2)$ on $[0,x_1]$, where the real square root is
undefined. Therefore $y(x)=0$ for every $x\ge0$.
:::

:::

::: {.pf-step #left-boundary-point-a}
If $y$ is not identically zero, there is a unique $a\le0$ such that
$y(x)<0$ for $x<a$ and $y(x)=0$ for $x\ge a$.

::: pf-proof
By step [](#monotone-and-zero-forward){.pf-ref}, the zero set is nonempty because it contains $[0,\infty)$.
Since $y$ is nondecreasing and never positive on $(-\infty,0]$, whenever
$y(x_0)=0$ one has $y(x)=0$ for every $x\ge x_0$. Thus the zero set is an
upper ray.

If $y$ is not identically zero, choose $x_1<0$ with $y(x_1)<0$. The zero
ray therefore has a finite left endpoint $a\in[x_1,0]$. Continuity gives
$y(a)=0$, and monotonicity then gives precisely
$$
y(x)<0\quad(x<a),
\qquad
y(x)=0\quad(x\ge a).
$$
The endpoint $a$ is unique.
:::

:::

::: {.pf-step #explicit-formula-on-negative-branch}
On the interval $(-\infty,a)$ of step [](#left-boundary-point-a){.pf-ref},
$$
y(x)=1-\cosh(a-x).
$$

::: pf-proof
For $x<a$, set
$$
u(x)\coloneqq1-y(x).
$$
Then $u(x)>1$, and
$$
y(y-2)=(1-u)(-1-u)=u^2-1.
$$
Consequently
$$
u'(x)=-\sqrt{u(x)^2-1}.
$$
Since $u>1$, differentiation of the inverse hyperbolic cosine gives
$$
\frac{d}{dx}\operatorname{arcosh}u(x)
=
\frac{u'(x)}{\sqrt{u(x)^2-1}}
=-1.
$$
Hence $\operatorname{arcosh}u(x)+x$ is constant on $(-\infty,a)$.
As $x\uparrow a$, continuity and $y(a)=0$ imply $u(x)\to1$, so
$\operatorname{arcosh}u(x)\to0$. Therefore the constant is $a$, and
$$
\operatorname{arcosh}u(x)=a-x.
$$
Thus $u(x)=\cosh(a-x)$ and
$$
y(x)=1-\cosh(a-x).
$$
:::

:::

::: {.pf-step #family-verified}
Conversely, every $y_a$ with $a\le0$ is a global solution, and so is
the constant function $y\equiv0$.

::: pf-proof
For $x<a$,
$$
y_a'(x)=\sinh(a-x),
$$
and
$$
y_a(x)(y_a(x)-2)
=
\cosh^2(a-x)-1
=
\sinh^2(a-x).
$$
Because $a-x>0$, one has $\sinh(a-x)>0$, and therefore
$$
y_a'(x)=\sqrt{y_a(x)(y_a(x)-2)}.
$$
For $x>a$, both sides of the differential equation are zero. At $x=a$,
the left derivative is $\sinh0=0$, equal to the right derivative, so $y_a$
is differentiable there and again satisfies the equation. Finally,
$a\le0$ implies $y_a(0)=0$. The constant zero function satisfies
$0'=0=\sqrt{0\cdot(0-2)}$ and the initial condition.
:::

:::

::: {.pf-step #solution-set-boxed}
The complete set of solutions is
$$
\boxed{
y\equiv0
\quad\text{or}\quad
y=y_a\text{ for some }a\le0
}.
$$

::: pf-proof
Steps [](#monotone-and-zero-forward){.pf-ref}, [](#left-boundary-point-a){.pf-ref}, and [](#explicit-formula-on-negative-branch){.pf-ref} show that every nonzero solution must equal exactly one
$y_a$, while step [](#family-verified){.pf-ref} verifies every function in the displayed family.
:::

:::

::: pf-qed
Step [](#solution-set-boxed){.pf-ref} gives all and only the real-valued global solutions satisfying
the prescribed initial condition.
:::

:::
:::
