---
schema: qual/card@1
id: P-BERK81S-19
kind: problem
title: Number of roots in the right half-plane of $z^{2n}+\alpha^2z^{2n-1}+\beta^2$
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
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Applied the argument principle on a large right half-disk. On the
    semicircle the polynomial is z^{2n}(1+O(1/z)), so the argument change
    tends to 2n pi. On the imaginary axis,
    P(iy)=beta^2+(-1)^n y^{2n}
    +i(-1)^{n+1}alpha^2 y^{2n-1}. There are no imaginary-axis zeros.
    Traversed downward, this curve has argument change 0 when n is even and
    -2 pi when n is odd, giving n and n-1 right-half-plane roots.
---

::: {.problem}
Let $n$ be a positive integer and let $\alpha,\beta\in\mathbb R\setminus\{0\}$.
Prove that the number of roots, counted with multiplicity, of
\[
z^{2n}+\alpha^2z^{2n-1}+\beta^2=0
\]
having positive real part is

1. $n$ if $n$ is even;

2. $n-1$ if $n$ is odd.
:::

::: {.solution}
Set
$$
P(z)
=
z^{2n}
+
\alpha^2z^{2n-1}
+
\beta^2.
$$

::: pf

::: {.pf-step #s1}

The polynomial $P$ has no zero on the imaginary axis.

::: pf-proof

For $y\in\RR$,
$$
\begin{aligned}
P(iy)
&=
(-1)^n y^{2n}
+
\alpha^2(-1)^{n+1}i\,y^{2n-1}
+
\beta^2\\
&=
\bigl(
\beta^2+(-1)^ny^{2n}
\bigr)
+
i(-1)^{n+1}\alpha^2y^{2n-1}.
\end{aligned}
$$
If $P(iy)=0$, its imaginary part vanishes. Since $\alpha\neq0$, this
forces $y=0$. But then
$$
P(0)=\beta^2\neq0.
$$
Thus no such zero exists.

:::

:::

::: {.pf-step #s2}

For all sufficiently large $R$, every zero of $P$ lies in
$$
\{z:\abs{z}<R\},
$$
and the positively oriented boundary of the right half-disk consists of
the semicircle
$$
\Gamma_R:
z=Re^{i\theta},
\qquad
-\frac\pi2\leq\theta\leq\frac\pi2,
$$
followed by the imaginary segment
$$
I_R:
z=iy,
\qquad
R\geq y\geq-R.
$$

::: pf-proof

The polynomial has finitely many zeros, so choose $R$ larger than the
modulus of every zero. Step [](#s1){.pf-ref} shows that no zero lies on the imaginary
segment. The stated orientation keeps the right half-disk on the left
while traversing its boundary.

:::

:::

::: {.pf-step #s3}

Let $N_+$ be the number of zeros of $P$ with positive real part,
counted with multiplicity. For every sufficiently large $R$,
$$
2\pi N_+
=
\Delta_{\Gamma_R}\arg P
+
\Delta_{I_R}\arg P.
$$

::: pf-proof

For $R$ as in step [](#s2){.pf-ref}, the boundary contains no zero of $P$, and the
right half-disk contains exactly the zeros with positive real part. The
argument principle says that the total change of a continuous argument of
$P$ around this positively oriented boundary equals $2\pi$ times the
number of enclosed zeros, counted with multiplicity.

:::

:::

::: {.pf-step #s4}

Along the semicircle,
$$
\Delta_{\Gamma_R}\arg P
\longrightarrow
2n\pi
$$
as $R\to\infty$.

::: pf-proof

For $z\in\Gamma_R$,
$$
P(z)
=
z^{2n}
\left(
1+\frac{\alpha^2}{z}
+\frac{\beta^2}{z^{2n}}
\right).
$$
The factor in parentheses converges uniformly to $1$ on $\Gamma_R$ as
$R\to\infty$. For sufficiently large $R$, it lies in the disk
$$
\{w:\abs{w-1}<1/2\},
$$
which admits a continuous argument converging uniformly to $0$. Hence the
argument change contributed by this factor tends to $0$.

Meanwhile, on
$$
z=Re^{i\theta},
\qquad
-\frac\pi2\leq\theta\leq\frac\pi2,
$$
the factor $z^{2n}$ has continuous argument $2n\theta$, whose change is
$$
2n
\left(
\frac\pi2-\left(-\frac\pi2\right)
\right)
=
2n\pi.
$$
Adding the two argument changes proves the limit.

:::

:::

::: {.pf-step #s5}

If $n$ is even, then
$$
\Delta_{I_R}\arg P
\longrightarrow
0
$$
as $R\to\infty$.

::: pf-proof

When $n$ is even, step [](#s1){.pf-ref} gives
$$
P(iy)
=
\bigl(\beta^2+y^{2n}\bigr)
-i\alpha^2y^{2n-1}.
$$
Its real part is strictly positive for every $y$. Thus the path
$$
y\longmapsto P(iy)
$$
lies entirely in the open right half-plane, where the argument has a
single continuous branch taking values in
$$
\left(-\frac\pi2,\frac\pi2\right).
$$

As $y\to\pm\infty$,
$$
\frac{\operatorname{Im}P(iy)}
{\operatorname{Re}P(iy)}
=
\frac{-\alpha^2y^{2n-1}}
{\beta^2+y^{2n}}
\longrightarrow
0.
$$
Hence the arguments at both endpoints of the downward segment
$y=R$ to $y=-R$ tend to $0$. Their difference therefore tends to $0$.

:::

:::

::: {.pf-step #s6}

If $n$ is odd, then
$$
\Delta_{I_R}\arg P
\longrightarrow
-2\pi
$$
as $R\to\infty$.

::: pf-proof

When $n$ is odd,
$$
P(iy)
=
\bigl(\beta^2-y^{2n}\bigr)
+
i\alpha^2y^{2n-1}.
$$
For $y>0$, the imaginary part is positive, so the path lies in the open
upper half-plane. As $y\to+\infty$, its argument tends to $\pi$, because
the real part is negative of order $y^{2n}$ while the imaginary part has
lower order $y^{2n-1}$. As $y\to0^+$,
$$
P(iy)\longrightarrow\beta^2>0,
$$
so its argument tends to $0$. Thus the argument change while traversing
from $+\infty$ down to $0$ is $-\pi$.

For $y<0$, the imaginary part is negative, so the path lies in the open
lower half-plane. As the traversal continues from $0$ down to
$-\infty$, the argument changes from $0$ to $-\pi$. This contributes a
second change of $-\pi$. Hence the full downward imaginary-axis traversal
has limiting argument change
$$
-\pi-\pi=-2\pi.
$$

:::

:::

::: {.pf-step #s7}

If $n$ is even, then
$$
\boxed{
N_+=n.
}
$$

::: pf-proof

By steps [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref},
$$
2\pi N_+
=
\Delta_{\Gamma_R}\arg P
+
\Delta_{I_R}\arg P
\longrightarrow
2n\pi.
$$
The left-hand side is independent of $R$ for all sufficiently large $R$.
Therefore
$$
2\pi N_+=2n\pi,
$$
so $N_+=n$.

:::

:::

::: {.pf-step #s8}

If $n$ is odd, then
$$
\boxed{
N_+=n-1.
}
$$

::: pf-proof

By steps [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s6){.pf-ref},
$$
2\pi N_+
\longrightarrow
2n\pi-2\pi
=
2(n-1)\pi.
$$
Again the left-hand side is independent of sufficiently large $R$, so
$$
N_+=n-1.
$$

:::

:::

::: pf-qed

Step [](#s7){.pf-ref} proves the even case, and step [](#s8){.pf-ref} proves the odd case.

:::

:::

:::
