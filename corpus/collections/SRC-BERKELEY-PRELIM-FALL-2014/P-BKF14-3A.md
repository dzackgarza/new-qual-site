---
schema: qual/card@1
id: P-BKF14-3A
kind: problem
title: Bounding $f'$ in terms of bounds on $f$ and $f''$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2014 solution packet and its
    triangular lower bound for f' coming from |f''|<=1.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the Lipschitz estimate for f', the area bound M^2<=2, and the
    equality case needed to obtain the strict bound |f'|<sqrt(2).
---

::: {.problem}
Suppose that f is a twice-differentiable real-valued function on the real line such that $| f ( x ) | \leq$ 1 and $| f ^ { \prime \prime } ( x ) | \le 1$ for all x. Find, with proof, a constant b such that $| f ^ { \prime } ( x ) | < b$ for all x.
:::

::: {.solution}
<1>1. For all $x,y\in\RR$,
$$
|f'(x)-f'(y)|\le|x-y|.
$$

::: {.proof}
If $x\ne y$, the mean value theorem applied to $f'$ gives a point
$c$ between $x$ and $y$ such that
$$
f'(x)-f'(y)=f''(c)(x-y).
$$
Since $|f''(c)|\le1$, the claimed estimate follows. The case $x=y$ is
immediate.
:::

<1>2. Fix $x_0\in\RR$ and put $M\coloneqq|f'(x_0)|$. After replacing
$f$ by $-f$ if necessary, one may assume $f'(x_0)=M\ge0$, and then
$$
f'(x_0+t)\ge M-|t|
\qquad
(-M\le t\le M).
$$

::: {.proof}
Replacing $f$ by $-f$ preserves the hypotheses and the value of
$|f'(x_0)|$. Under the resulting assumption $f'(x_0)=M$, step <1>1
gives
$$
f'(x_0+t)
\ge
f'(x_0)-|t|
=
M-|t|.
$$
:::

<1>3. One has
$$
M^2\le2.
$$

::: {.proof}
Since $f'$ is continuous, the fundamental theorem of calculus and step
<1>2 give
$$
\begin{aligned}
f(x_0+M)-f(x_0-M)
&=
\int_{-M}^{M}f'(x_0+t)\,dt\\
&\ge
\int_{-M}^{M}(M-|t|)\,dt\\
&=
M^2.
\end{aligned}
$$
On the other hand, $|f|\le1$, so
$$
f(x_0+M)-f(x_0-M)\le2.
$$
Combining the inequalities yields $M^2\le2$.
:::

<1>4. In fact,
$$
M^2<2.
$$

::: {.proof}
Suppose instead that $M^2=2$. Then every inequality in step <1>3 must
be an equality. In particular, the continuous nonnegative function
$$
q(t)\coloneqq
f'(x_0+t)-(M-|t|)
$$
has integral $0$ on $[-M,M]$, so $q(t)=0$ throughout that interval.
Hence
$$
f'(x_0+t)=
\begin{cases}
M+t,&-M\le t\le0,\\
M-t,&0\le t\le M.
\end{cases}
$$
The left derivative of $f'$ at $x_0$ would then be $1$, while its right
derivative would be $-1$. This contradicts the existence of
$f''(x_0)$. Thus equality is impossible.
:::

<1>5. The choice
$$
\boxed{b=\sqrt2}
$$
works.

::: {.proof}
The point $x_0$ was arbitrary. By step <1>4,
$$
|f'(x_0)|^2=M^2<2,
$$
and therefore $|f'(x_0)|<\sqrt2$ for every $x_0\in\RR$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 supplies the required constant and bound.
:::
:::
