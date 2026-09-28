---
schema: qual/card@1
id: P-BKF03-9A
kind: problem
title: Hölder continuity of the Cantor function with exponent $\log2/\log3$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the lost arrow in f and math delimiters against f03.pdf page 1 problem 9A.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained digit estimate and made its
    arbitrary-point reduction explicit: complementary-gap endpoints preserve
    f-values and lie between x and y, so the Cantor-set estimate transfers
    without enlarging distance.
---

::: {.problem}
Let $f : [0, 1] \to [0, 1]$ be an increasing (not strictly increasing) function such that

$$
f\left( \sum_{j=1}^{\infty} a_j 3^{-j} \right) = \sum_{j=1}^{\infty} \frac{a_j}{2} 2^{-j}
$$

whenever the $a_j$ are $0$ or $2$. Prove that there is a constant $C_0$ such that

$$
|f(x) - f(y)| \leq C_0 |x - y|^{(\log 2)/(\log 3)}
$$

for all $x, y \in [0, 1]$.
:::

::: {.solution}
Set
$$
\alpha=\frac{\log 2}{\log 3},
$$
and let
$$
C=
\left\{
\sum_{j=1}^{\infty} a_j3^{-j}:a_j\in\{0,2\}
\right\}
$$
be the Cantor set.

<1>1. If $x\in[0,1]\sm C$, then there are $\ell,r\in C$ with
$$
\ell<x<r
\qquad\text{and}\qquad
f(\ell)=f(x)=f(r).
$$

::: {.proof}
Choose a ternary expansion
$$
x=\sum_{k=1}^{\infty} a_k3^{-k}
$$
and let $j$ be the first index for which $a_j=1$. Then
$a_1,\ldots,a_{j-1}\in\{0,2\}$. Define
$$
\begin{aligned}
\ell
&=
\sum_{k<j}a_k3^{-k}
+
\sum_{k>j}2\cdot3^{-k},
\\
r
&=
\sum_{k<j}a_k3^{-k}
+
2\cdot3^{-j}.
\end{aligned}
$$
These are the two endpoints of the complementary middle-third interval
containing $x$, so $\ell<x<r$ and $\ell,r\in C$.

Put
$$
s=\sum_{k<j}\frac{a_k}{2}2^{-k}.
$$
Using the prescribed values of $f$ on $C$ gives
$$
f(\ell)
=
s+\sum_{k>j}2^{-k}
=
s+2^{-j},
$$
while
$$
f(r)=s+2^{-j}.
$$
Since $f$ is nondecreasing and $\ell<x<r$,
$$
f(\ell)\le f(x)\le f(r).
$$
The endpoint values are equal, hence
$f(\ell)=f(x)=f(r)$.
:::

<1>2. If $u,v\in C$, then
$$
\abs{f(u)-f(v)}
\le
2\abs{u-v}^{\alpha}.
$$

::: {.proof}
The assertion is immediate when $u=v$. Suppose $u>v$, and choose their
ternary expansions
$$
u=\sum_{k=1}^{\infty}a_k3^{-k},
\qquad
v=\sum_{k=1}^{\infty}b_k3^{-k},
$$
with $a_k,b_k\in\{0,2\}$. Let $j$ be the first index for which
$a_j\ne b_j$. Since $u>v$, one has $a_j=2$ and $b_j=0$. Therefore
$$
\begin{aligned}
u-v
&\ge
2\cdot3^{-j}
-
\sum_{k>j}2\cdot3^{-k}
\\
&=
3^{-j}.
\end{aligned}
$$
On the other hand, the defining formula for $f$ on $C$ gives
$$
\begin{aligned}
\abs{f(u)-f(v)}
&=
\abs{
\sum_{k\ge j}
\frac{a_k-b_k}{2}2^{-k}
}
\\
&\le
\sum_{k\ge j}2^{-k}
\\
&=
2^{1-j}.
\end{aligned}
$$
Since $3^{-\alpha}=2^{-1}$,
$$
2^{1-j}
=
2(3^{-j})^\alpha
\le
2\abs{u-v}^{\alpha}.
$$
The case $v>u$ follows by symmetry.
:::

<1>3. If $0\le x<y\le1$ and $f(x)\ne f(y)$, then there exist
$u,v\in C$ such that
$$
x\le u\le v\le y,
\qquad
f(u)=f(x),
\qquad
f(v)=f(y).
$$

::: {.proof}
If $x\in C$, set $u=x$. If $x\notin C$, let
$[\ell_x,r_x]$ be the closed complementary interval supplied by step
<1>1 and set $u=r_x$. Since $f(x)\ne f(y)$, the point $y$ cannot
belong to $[\ell_x,r_x]$, on which step <1>1 and monotonicity make $f$
constant. Thus $r_x<y$, so in either case
$$
x\le u<y
\qquad\text{and}\qquad
f(u)=f(x).
$$

Similarly, if $y\in C$, set $v=y$. If $y\notin C$, let
$[\ell_y,r_y]$ be its closed complementary interval and set
$v=\ell_y$. The inequality $f(x)\ne f(y)$ implies
$x<\ell_y$, so
$$
x<v\le y
\qquad\text{and}\qquad
f(v)=f(y).
$$

Because $x<y$, monotonicity gives $f(x)\le f(y)$; the hypothesis
$f(x)\ne f(y)$ makes this inequality strict. Thus
$$
f(u)=f(x)<f(y)=f(v).
$$
If $u>v$, monotonicity would instead give $f(u)\ge f(v)$, a
contradiction. Hence $u\le v$.
:::

<1>4. For all $x,y\in[0,1]$,
$$
\abs{f(x)-f(y)}
\le
2\abs{x-y}^{\alpha}.
$$

::: {.proof}
The assertion is trivial if $x=y$ or $f(x)=f(y)$. Otherwise, exchange
$x$ and $y$ if necessary so that $x<y$, and choose $u,v$ as in step
<1>3. Then step <1>2 gives
$$
\begin{aligned}
\abs{f(x)-f(y)}
&=
\abs{f(u)-f(v)}
\\
&\le
2\abs{u-v}^{\alpha}
\\
&\le
2\abs{x-y}^{\alpha},
\end{aligned}
$$
because $x\le u\le v\le y$ and $\alpha>0$.
:::

<1>5. The required estimate holds with
$$
\boxed{C_0=2}.
$$

::: {.proof}
Step <1>4 is the desired Hölder estimate with
$\alpha=(\log2)/(\log3)$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 supplies the required constant.
:::
:::
