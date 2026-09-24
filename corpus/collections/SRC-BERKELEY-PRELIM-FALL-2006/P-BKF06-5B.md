---
schema: qual/card@1
id: P-BKF06-5B
kind: problem
title: Entire functions determined by their integrals against $(\sin z)^{-m}$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 5B of the retained Berkeley Fall 2006 preliminary-exam solution packet f06solution.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained residue argument, including the order
    computation at zero and the absence of other zeros of sin(z) in the
    closed unit disk.
---

::: {.problem}
Let $f$ and $g$ be entire functions such that
\[
\int_{|z|=1}\frac{f(z)}{(\sin z)^m}\,dz
=
\int_{|z|=1}\frac{g(z)}{(\sin z)^m}\,dz
\]
for every positive integer $m$.
Prove that $f=g$.
:::

::: {.solution}
Set
$$
h=f-g.
$$

<1>1. For every positive integer $m$,
$$
\int_{\abs z=1}\frac{h(z)}{(\sin z)^m}\,dz=0.
$$

::: {.proof}
This follows by subtracting the two integrals in the hypothesis and
using linearity of contour integration.
:::

<1>2. Suppose, for contradiction, that $h$ is not identically zero.
Let
$$
k=\operatorname{ord}_0 h.
$$
Then there is a holomorphic function $u$ near $0$ such that
$$
h(z)=z^ku(z),
\qquad
u(0)\ne0.
$$

::: {.proof}
Since $h$ is entire and not identically zero, its zero at $0$, if
present, has finite order $k\ge0$. The standard local factorization
at a zero gives the displayed expression.
:::

<1>3. For
$$
m=k+1,
$$
the meromorphic function
$$
\frac{h(z)}{(\sin z)^m}
$$
has a simple pole at $0$ with nonzero residue.

::: {.proof}
Write
$$
\sin z=zv(z),
$$
where $v$ is holomorphic near $0$ and $v(0)=1$. Using step <1>2 and
$m=k+1$,
$$
\frac{h(z)}{(\sin z)^m}
=
\frac{z^ku(z)}{z^{k+1}v(z)^{k+1}}
=
\frac1z\frac{u(z)}{v(z)^{k+1}}.
$$
Thus the pole is simple and its residue is
$$
\frac{u(0)}{v(0)^{k+1}}
=
u(0)
\ne
0.
$$
:::

<1>4. The function in step <1>3 has no other poles in
$\abs z\le1$.

::: {.proof}
The zeros of $\sin z$ are the integer multiples of $\pi$. Since
$\pi>1$, the only zero of $\sin z$ in the closed unit disk is
$z=0$. The numerator $h$ is entire, so there are no other possible
poles.
:::

<1>5. The choice $m=k+1$ contradicts step <1>1.

::: {.proof}
By steps <1>3 and <1>4, the residue theorem gives
$$
\int_{\abs z=1}\frac{h(z)}{(\sin z)^{k+1}}\,dz
=
2\pi i\,u(0)
\ne
0.
$$
But step <1>1 says that this integral is zero for every positive
integer $m$, including $m=k+1$. This is a contradiction.
:::

<1>6. Therefore
$$
\boxed{f=g}.
$$

::: {.proof}
Step <1>5 shows that the assumption $h\not\equiv0$ is impossible.
Hence $h=f-g\equiv0$.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required conclusion.
:::
:::
