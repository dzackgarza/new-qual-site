---
schema: qual/card@1
id: P-BKF12-5B
kind: problem
title: The equation $e^z=z$ has infinitely many complex roots
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
    Checked against Problem 5B in the retained Fall 2012 Berkeley prelim exam
    and independently reviewed the retained solution packet F12_Solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Made the sidewise argument-change estimates explicit, checked that the
    boundary is zero-free, and applied the argument principle to the square.
---

::: {.problem}
Show that as the positive integer N tends to infinity, the change in argument of $e ^ { z } - z$ is bounded on 3 sides of the square with corners $\pm 2 \pi N \pm 2 \pi i N$ but is unbounded on the fourth side.
Show that $e ^ { z } = z$ has infinitely many complex roots.
:::

::: {.solution}
Set
$$
f(z)\coloneqq e^z-z,
\qquad
R\coloneqq 2\pi N,
$$
and let $Q_N$ be the square
$$
\{z\in\CC:\lvert\Re z\rvert\le R,\ \lvert\Im z\rvert\le R\},
$$
whose boundary is oriented counterclockwise.

<1>1. On the bottom side of $Q_N$, the change in argument of $f$
has absolute value at most $\pi$, uniformly in $N$.

::: {.proof}
Write $z=x-iR$, with $-R\le x\le R$. Since
$R=2\pi N$,
$$
e^z=e^x e^{-iR}=e^x.
$$
Hence
$$
f(x-iR)=e^x-x+iR,
$$
whose imaginary part is the positive constant $R$. Thus the image of
the whole side lies in the open upper half-plane. A continuous branch
of the argument therefore takes values in $(0,\pi)$, so its total
change has absolute value less than $\pi$.
:::

<1>2. On the top side of $Q_N$, the change in argument of $f$
has absolute value at most $\pi$, uniformly in $N$.

::: {.proof}
Write $z=x+iR$. Again $e^{iR}=1$, so
$$
f(x+iR)=e^x-x-iR.
$$
Its imaginary part is the negative constant $-R$, so the image lies
in the open lower half-plane. A continuous argument takes values in an
interval of length $\pi$, giving the stated bound.
:::

<1>3. On the left side of $Q_N$, the change in argument of $f$
has absolute value at most $\pi$, uniformly in $N$.

::: {.proof}
Write $z=-R+iy$, with $-R\le y\le R$. Then
$$
\Re f(z)
=e^{-R}\cos y+R
\ge R-e^{-R}
>0.
$$
Thus the image lies in the open right half-plane, where a continuous
argument takes values in $(-\pi/2,\pi/2)$. Its total change therefore
has absolute value less than $\pi$.
:::

<1>4. On the right side of $Q_N$, oriented upward, the change in
argument of $f$ is
$$
4\pi N+E_N,
\qquad
\lvert E_N\rvert<\pi.
$$

::: {.proof}
Write $z=R+iy$, with $-R\le y\le R$. Then
$$
f(R+iy)
=e^{R+iy}h_N(y),
\qquad
h_N(y)\coloneqq
1-(R+iy)e^{-R-iy}.
$$
For $N\ge1$,
$$
\lvert (R+iy)e^{-R-iy}\rvert
\le \sqrt2\,R e^{-R}
<1.
$$
Hence $\Re h_N(y)>0$ for all $y$, so $h_N$ has a continuous argument
with values in $(-\pi/2,\pi/2)$. Its argument changes by some $E_N$
with $\lvert E_N\rvert<\pi$.

The factor $e^{R+iy}$ contributes argument change
$$
R-(-R)=2R=4\pi N.
$$
Adding the two changes gives the formula.
:::

<1>5. The function $f$ has no zeros on $\partial Q_N$.

::: {.proof}
Steps <1>1 and <1>2 place the images of the horizontal sides in open
half-planes not containing $0$, and step <1>3 does the same for the
left side. On the right side, step <1>4 gives
$\Re h_N(y)>0$, so $h_N(y)\ne0$, while
$e^{R+iy}\ne0$. Thus $f\ne0$ everywhere on the boundary.
:::

<1>6. The total change in argument of $f$ around $\partial Q_N$ is
$$
4\pi N+O(1),
$$
and in particular tends to $+\infty$.

::: {.proof}
By step <1>4, the right side contributes $4\pi N+E_N$ with
$\lvert E_N\rvert<\pi$. By steps <1>1--<1>3, the combined
contribution of the other three sides has absolute value less than
$3\pi$. Hence
$$
\Delta_{\partial Q_N}\arg f
=4\pi N+F_N,
\qquad
\lvert F_N\rvert<4\pi.
$$
:::

<1>7. The equation $e^z=z$ has infinitely many complex roots.

::: {.proof}
By step <1>5, the argument principle applies to $f$ on $Q_N$.
Since $f$ is entire, the number $Z_N$ of zeros in $Q_N$, counted with
multiplicity, is
$$
Z_N
=\frac1{2\pi}
\Delta_{\partial Q_N}\arg f.
$$
Step <1>6 shows that $Z_N\to\infty$. Therefore the zero set of
$f(z)=e^z-z$ cannot be finite.
:::

<1>8. Q.E.D.

::: {.proof}
Steps <1>1--<1>4 give the required sidewise behavior of the argument,
and step <1>7 proves that $e^z=z$ has infinitely many roots.
:::
:::
