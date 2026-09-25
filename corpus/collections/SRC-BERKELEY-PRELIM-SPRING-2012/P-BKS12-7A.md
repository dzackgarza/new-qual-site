---
schema: qual/card@1
id: P-BKS12-7A
kind: problem
title: The unit circle is a natural boundary for $\sum z^{2^n}$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: >-
    Checked page 2 of the retained Spring 2012 solution PDF. Restored the
    source index n>=0; the packet's solution incorrectly writes
    f(z)=1+f(z^2), while the displayed source series satisfies
    f(z)=z+f(z^2).
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Independently checked convergence in the disk, radial blowup at 1,
    propagation to dyadic roots of unity, density on the unit circle, and
    the contradiction with any analytic extension to a larger connected open set.
---

::: {.problem}
Show that the unit circle is a natural boundary of the function $\begin{array} { r } { f ( z ) = \sum _ { n \geq 0 } z ^ { 2 ^ { n } } } \end{array}$ ; in other words, $f ( z )$ cannot be extended to an analytic function on any connected open set strictly larger than the open unit disk.
(Hint: find a relation between $f ( z )$ and $f ( z ^ { 2 } ) . )$
:::

::: {.solution}
Let
$$
\DD\coloneqq\{z\in\CC:\abs{z}<1\}.
$$

<1>1. The series
$$
f(z)=\sum_{n=0}^{\infty}z^{2^n}
$$
defines a holomorphic function on $\DD$.

::: {.proof}
Fix $0<r<1$. If $\abs{z}\leq r$, then
$$
\abs{z^{2^n}}
\leq
r^{2^n}
\leq
r^{n+1},
$$
because $2^n\geq n+1$ for $n\geq0$. The geometric series
$$
\sum_{n=0}^{\infty}r^{n+1}
$$
converges. Hence the defining series for $f$ converges uniformly on every
closed disk $\abs{z}\leq r<1$. Its terms are holomorphic, so its locally
uniform limit $f$ is holomorphic on $\DD$.
:::

<1>2. On $\DD$ one has the functional equation
$$
f(z)=z+f(z^2).
$$

::: {.proof}
Absolute convergence permits reindexing:
$$
\begin{aligned}
f(z)
&=
z+\sum_{n=1}^{\infty}z^{2^n}\\
&=
z+\sum_{m=0}^{\infty}(z^2)^{2^m}\\
&=
z+f(z^2).
\end{aligned}
$$
:::

<1>3. One has
$$
f(r)\longrightarrow+\infty
$$
as $r\to1^-$ through real numbers.

::: {.proof}
Let $M>0$. Choose an integer $N>M$. For $0<r<1$,
$$
f(r)
\geq
\sum_{n=0}^{N-1}r^{2^n}.
$$
As $r\to1^-$, the finite sum on the right tends to $N$. Hence for all
$r$ sufficiently close to $1$,
$$
f(r)>M.
$$
Since $M$ was arbitrary, the claim follows.
:::

<1>4. For every integer $m\geq1$,
$$
f(z)
=
\sum_{j=0}^{m-1}z^{2^j}
+
f(z^{2^m})
$$
for every $z\in\DD$.

::: {.proof}
Iterate the functional equation in step <1>2. After $m$ iterations, the
successive polynomial terms are
$$
z,z^2,z^4,\ldots,z^{2^{m-1}},
$$
and the remaining term is $f(z^{2^m})$.
:::

<1>5. If $\zeta$ is a $2^m$th root of unity, then
$$
\abs{f(r\zeta)}
\longrightarrow\infty
$$
as $r\to1^-$.

::: {.proof}
Since
$$
\zeta^{2^m}=1,
$$
step <1>4 gives
$$
f(r\zeta)
=
\sum_{j=0}^{m-1}
r^{2^j}\zeta^{2^j}
+
f(r^{2^m}).
$$
The finite sum satisfies
$$
\abs{
\sum_{j=0}^{m-1}
r^{2^j}\zeta^{2^j}
}
\leq
m.
$$
By step <1>3,
$$
f(r^{2^m})\longrightarrow+\infty.
$$
Therefore
$$
\abs{f(r\zeta)}
\geq
f(r^{2^m})-m
\longrightarrow\infty.
$$
:::

<1>6. The set
$$
E
\coloneqq
\left\{
e^{2\pi i k/2^m}
:
m\geq1,\ k\in\ZZ
\right\}
$$
is dense in the unit circle.

::: {.proof}
For each $m$, the arguments of the $2^m$th roots of unity are spaced by
$$
\frac{2\pi}{2^m}.
$$
Given any nonempty open arc of the unit circle, choose $m$ so large that
this spacing is smaller than the angular length of the arc. At least one
$2^m$th root of unity then lies in that arc.
:::

<1>7. The function $f$ cannot extend holomorphically to any open
neighborhood of any point of the unit circle.

::: {.proof}
Suppose that a holomorphic extension existed on an open neighborhood
$U$ of some
$$
\xi\in\CC,
\qquad
\abs{\xi}=1.
$$
Choose $\delta>0$ such that
$$
B(\xi,\delta)\subseteq U.
$$
By step <1>6, choose a dyadic root of unity
$$
\zeta\in E\cap B(\xi,\delta/2).
$$
Then
$$
B(\zeta,\delta/2)\subseteq U.
$$
The extension is continuous at $\zeta$, hence bounded on some smaller
closed disk centered at $\zeta$. For all $r<1$ sufficiently close to
$1$, the point $r\zeta$ lies in that smaller disk and also in $\DD$.
There the extension equals $f$. This contradicts the blowup
$$
\abs{f(r\zeta)}\longrightarrow\infty
$$
from step <1>5.
:::

<1>8. The unit circle is a natural boundary of $f$ in the sense stated in
the problem.

::: {.proof}
Suppose there were a connected open set $\Omega$ strictly larger than
$\DD$ and a holomorphic function on $\Omega$ extending $f$. Because
$\Omega$ is open and connected in the plane, it is path-connected. Choose
$$
w\in\Omega\setminus\DD.
$$
If $\abs{w}=1$, then $\Omega$ is already an open neighborhood of a unit
circle point, contradicting step <1>7. If $\abs{w}>1$, a path in $\Omega$
from $0$ to $w$ has, by continuity of its modulus, a point
$$
\xi\in\Omega
$$
with $\abs{\xi}=1$. Since $\Omega$ is open, it contains a neighborhood of
$\xi$, again contradicting step <1>7.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>8 proves exactly the asserted natural-boundary property.
:::
:::
