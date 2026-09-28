---
schema: qual/card@1
id: P-BKS07-8B
kind: problem
title: UC Berkeley Spring 2007 prelim 8B
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with the Spring 2007 exam extraction and independently reviewed the companion source solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Independently verified the conformal-map construction by computing the real and
    imaginary parts of (1+z)/(1-z) and checking both boundary components explicitly.
---

::: {.problem}
Let $A$ be the set of $z\in\mathbb C$ such that $|z|\le1$, $\operatorname{Im}(z)\ge0$, and $z\notin\{1,-1\}$.
Find an explicit continuous function $u:A\to\mathbb R$ such that

- $u$ is harmonic on the interior of $A$,

- $u(z)=3$ for $z\in A\cap\mathbb R$, and

- $u(z)=7$ for $z$ in the intersection of $A$ with the unit circle.
:::

::: {.solution}
Set
$$
\Phi(z)\coloneqq\frac{1+z}{1-z},
$$
and let $\log$ denote the principal holomorphic logarithm on
$\CC\setminus(-\infty,0]$.

<1>1. The map $\Phi$ sends $A$ into the closed first quadrant with the origin
removed; it sends the interior of $A$ into the open first quadrant, the real
boundary segment into the positive real axis, and the semicircular boundary
into the positive imaginary axis.

::: {.proof}
Write $z=x+iy$. Since $z\neq1$ on $A$,
$$
\Phi(z)
=
\frac{(1+x)+iy}{(1-x)-iy}
=
\frac{1-x^2-y^2+2iy}{\abs{1-z}^2}.
$$
Therefore
$$
\operatorname{Re}\Phi(z)
=
\frac{1-\abs z^2}{\abs{1-z}^2}
\geq0,
\qquad
\operatorname{Im}\Phi(z)
=
\frac{2y}{\abs{1-z}^2}
\geq0.
$$
Both inequalities are strict in the interior, where $\abs z<1$ and $y>0$.

If $z\in A\cap\RR$, then $y=0$ and $-1<z<1$, so
$\Phi(z)>0$ is real. If $z\in A$ lies on the unit circle, then
$\operatorname{Re}\Phi(z)=0$ and $y>0$, so $\Phi(z)$ lies on the positive
imaginary axis. Finally, $\Phi(z)=0$ would force $z=-1$, which is excluded
from $A$.
:::

<1>2. The explicit function
$$
\boxed{
u(z)
=
3+\frac{8}{\pi}\operatorname{Im}
\log\left(\frac{1+z}{1-z}\right)
}
$$
is continuous on $A$ and harmonic on the interior of $A$.

::: {.proof}
By step <1>1, $\Phi(A)$ lies in the domain of the principal logarithm, so
$\log\circ\Phi$ is continuous on $A$. Hence $u$ is continuous on $A$.

On the interior of $A$, the image of $\Phi$ lies in the open first quadrant,
and both $\Phi$ and $\log$ are holomorphic there. Thus
$\log\circ\Phi$ is holomorphic on the interior of $A$. Its imaginary part is
therefore harmonic, and so is $u$.
:::

<1>3. The function in step <1>2 has the prescribed boundary values.

::: {.proof}
For $z\in A\cap\RR$, step <1>1 gives $\Phi(z)>0$, so the principal argument
of $\Phi(z)$ is $0$. Hence
$$
u(z)=3.
$$

If $z\in A$ lies on the unit circle, step <1>1 gives
$\Phi(z)\in i\RR_{>0}$, whose principal argument is $\pi/2$. Therefore
$$
u(z)
=
3+\frac{8}{\pi}\frac{\pi}{2}
=
7.
$$
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>2 and <1>3 verify all required properties of the displayed function.
:::
:::
