---
schema: qual/card@1
id: P-TIE-F16-08
kind: problem
title: Fourier transform of $1/\cosh\pi x$
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2016, question 8.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Removed the stray d left by extraction and cleaned the LaTeX against Fall 2016, question 8, page 16 of Questions_from_Tie.pdf.
---

::: {.problem}
Compute the integral $\int_{-\infty}^\infty \frac{e^{-2\pi i x\xi}}{\cosh \pi x}\,dx$ where $\cosh z = \frac{e^z + e^{-z}}{2}$.
:::

::: {.remark}
The source does not specify the range of the parameter $\xi$. In the Fourier-transform interpretation one takes $\xi\in\RR$.
The same formula below holds more generally for complex $\xi$ with
$$
\abs{\operatorname{Im}\xi}<\frac12,
$$
which is exactly the strip in which the integral is absolutely convergent.
:::

Fix
$$
\xi\in\CC,
\qquad
\abs{\operatorname{Im}\xi}<\frac12,
$$
and define
$$
F(z)
\coloneqq
\frac{e^{-2\pi i\xi z}}{\cosh\pi z}.
$$

::: pf

::: pf-step

The integral
$$
I(\xi)
\coloneqq
\int_{-\infty}^{\infty}
\frac{e^{-2\pi i x\xi}}{\cosh\pi x}\,dx
$$
converges absolutely.


::: pf-proof

Write
$$
\xi=u+iv.
$$
As $x\to+\infty$,
$$
\abs{e^{-2\pi i x\xi}}
=
e^{2\pi vx},
$$
while
$$
\cosh\pi x
\sim
\frac12e^{\pi x}.
$$
Thus the integrand has modulus
$$
O\left(
e^{-(\pi-2\pi v)x}
\right),
$$
which is integrable because $v<1/2$.

As $x\to-\infty$, the modulus is
$$
O\left(
e^{-(\pi+2\pi v)\abs{x}}
\right),
$$
which is integrable because $v>-1/2$. Hence the full integral converges absolutely.

:::

:::

::: pf-step

The function $F$ satisfies
$$
F(z+i)
=
-e^{2\pi\xi}F(z).
$$


::: pf-proof

One has
$$
\cosh\pi(z+i)
=
\cosh(\pi z+\pi i)
=
-\cosh\pi z,
$$
while
$$
e^{-2\pi i\xi(z+i)}
=
e^{2\pi\xi}
e^{-2\pi i\xi z}.
$$
Dividing gives the identity.

:::

:::

::: pf-step

The only pole of $F$ in the strip
$$
0<\operatorname{Im}z<1
$$
is the simple pole
$$
z=\frac{i}{2},
$$
and
$$
\operatorname{Res}_{z=i/2}F
=
\frac{e^{\pi\xi}}{\pi i}.
$$


::: pf-proof

The zeros of $\cosh\pi z$ occur when
$$
\pi z
=
i\pi\left(k+\frac12\right),
$$
that is,
$$
z
=
i\left(k+\frac12\right),
\qquad
k\in\ZZ.
$$
Exactly one such zero lies in the strip $0<\operatorname{Im}z<1$, namely
$$
z=i/2.
$$
Since
$$
\frac{d}{dz}\cosh\pi z
=
\pi\sinh\pi z,
$$
the residue is
$$
\begin{aligned}
\operatorname{Res}_{z=i/2}F
&=
\frac{
e^{-2\pi i\xi(i/2)}
}{
\pi\sinh(\pi i/2)
}\\
&=
\frac{e^{\pi\xi}}{\pi i}.
\end{aligned}
$$

:::

:::

::: pf-step

Let $\Gamma_R$ be the positively oriented rectangle with vertices
$$
-R,\quad R,\quad R+i,\quad -R+i.
$$
The two vertical-edge integrals tend to $0$ as $R\to\infty$.


::: pf-proof

For
$$
z=\pm R+iy,
\qquad
0\le y\le1,
$$
one has
$$
\abs{\cosh\pi z}^2
=
\sinh^2(\pi R)
+
\cos^2(\pi y)
\ge
\sinh^2(\pi R).
$$
Hence
$$
\abs{\cosh\pi z}
\ge
\sinh(\pi R).
$$

The numerator
$$
e^{-2\pi i\xi z}
$$
has modulus bounded on each vertical edge by a constant times
$$
e^{2\pi R\abs{\operatorname{Im}\xi}}.
$$
Since
$$
\abs{\operatorname{Im}\xi}<\frac12,
$$
while
$$
\sinh(\pi R)
\asymp
e^{\pi R},
$$
the quotient tends uniformly to $0$ on each unit-length vertical edge. Therefore both vertical integrals tend to $0$.

:::

:::

::: pf-step

The bottom and top edges satisfy
$$
\lim_{R\to\infty}
\int_{\partial\Gamma_R}
F(z)\,dz
=
\left(
1+e^{2\pi\xi}
\right)
I(\xi).
$$


::: pf-proof

The bottom edge contributes
$$
\int_{-R}^{R}
F(x)\,dx.
$$
The top edge is traversed from $R+i$ to $-R+i$, so by step <1>2 its contribution is
$$
\begin{aligned}
\int_R^{-R}
F(x+i)\,dx
&=
-\int_{-R}^{R}
F(x+i)\,dx\\
&=
e^{2\pi\xi}
\int_{-R}^{R}
F(x)\,dx.
\end{aligned}
$$
By step <1>4, the vertical contributions vanish as $R\to\infty$, and by step <1>1 the horizontal integrals converge to $I(\xi)$. This gives the displayed limit.

:::

:::

::: pf-step

The residue theorem gives
$$
\left(
1+e^{2\pi\xi}
\right)
I(\xi)
=
2e^{\pi\xi}.
$$


::: pf-proof

For sufficiently large $R$, step <1>3 shows that $\Gamma_R$ encloses exactly the one pole $i/2$. Hence
$$
\int_{\partial\Gamma_R}
F(z)\,dz
=
2\pi i
\operatorname{Res}_{z=i/2}F
=
2e^{\pi\xi}.
$$
Letting $R\to\infty$ and applying step <1>5 yields the identity.

:::

:::

::: pf-step

Therefore
$$
\boxed{
I(\xi)
=
\frac1{\cosh\pi\xi}.
}
$$


::: pf-proof

Since
$$
1+e^{2\pi\xi}
=
2e^{\pi\xi}\cosh\pi\xi,
$$
step <1>6 gives
$$
I(\xi)
=
\frac{
2e^{\pi\xi}
}{
2e^{\pi\xi}\cosh\pi\xi
}
=
\frac1{\cosh\pi\xi}.
$$
In particular, this holds for every real $\xi$, which is the Fourier-transform case requested by the problem.

:::

:::

::: pf-qed

Step <1>7 is the required evaluation.

:::

:::
