---
schema: qual/card@1
id: P-BKS04-7A
kind: problem
title: UC Berkeley Spring 2004 prelim 7A
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained UC Berkeley Spring 2004 preliminary exam and its companion solution packet.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Compared the authored solution with the retained `s04solution.pdf` solution packet.
---

::: {.problem}
Evaluate $\int _ { 0 } ^ { \infty } { \frac { \sin { x } } { x } } d x .$
:::

::: {.solution}
For $R>1$, set $\varepsilon=1/R$ and let $\Gamma_R$ be the positively
oriented boundary of the rectangle with vertices
$$
-R,\quad R,\quad R+iR,\quad -R+iR,
$$
with the upper semicircle $|z|=\varepsilon$ removed around the origin.
Thus the small semicircle is traversed clockwise from $-\varepsilon$ to
$\varepsilon$.

<1>1. One has
$$
\int_{\Gamma_R}\frac{e^{iz}}{z}\,dz=0.
$$

::: {.proof}
The indentation removes the only singularity of $e^{iz}/z$ from the
interior of the contour. Hence the integrand is holomorphic on and inside
$\Gamma_R$, so Cauchy's theorem gives the displayed identity.
:::

<1>2. The integrals over the two vertical sides and the top side tend to
zero as $R\to\infty$.

::: {.proof}
On the right side, write $z=R+it$ with $0\le t\le R$. Then
$$
|e^{iz}|=e^{-t},
\qquad
|z|\ge R,
$$
so
$$
\left|
\int_0^R\frac{e^{i(R+it)}}{R+it}\,i\,dt
\right|
\le
\frac1R\int_0^Re^{-t}\,dt
\le\frac1R.
$$
The same estimate applies to the left side.

On the top side $z=x+iR$, $-R\le x\le R$, so
$$
|e^{iz}|=e^{-R},
\qquad
|z|\ge R.
$$
Its length is $2R$, hence the ML estimate gives an absolute value at
most $2e^{-R}$. All three contributions therefore tend to zero.
:::

<1>3. If $C_R$ denotes the small clockwise semicircle, then
$$
\lim_{R\to\infty}
\int_{C_R}\frac{e^{iz}}{z}\,dz
=-\pi i.
$$

::: {.proof}
Write
$$
\frac{e^{iz}}{z}
=\frac1z+h(z),
\qquad
h(z)=\frac{e^{iz}-1}{z}.
$$
The function $h$ extends holomorphically to $z=0$, with $h(0)=i$, so it
is bounded near the origin. Since the length of $C_R$ is
$\pi\varepsilon=\pi/R$, one has
$$
\int_{C_R}h(z)\,dz\longrightarrow0.
$$

Parametrize the clockwise semicircle by
$$
z=\varepsilon e^{it},
\qquad
\pi\ge t\ge0.
$$
Then
$$
\int_{C_R}\frac{dz}{z}
=\int_\pi^0 i\,dt
=-\pi i.
$$
Combining these two facts gives the claim.
:::

<1>4. The two real-axis portions satisfy
$$
\lim_{R\to\infty}
\left(
\int_{-R}^{-1/R}\frac{e^{ix}}x\,dx
+
\int_{1/R}^{R}\frac{e^{ix}}x\,dx
\right)
=\pi i.
$$

::: {.proof}
Decompose the contour integral in step <1>1 into the two real segments,
the three outer sides, and $C_R$. Step <1>2 sends the outer-side
contributions to zero, while step <1>3 sends the indentation contribution
to $-\pi i$. Taking limits in the identity from step <1>1 therefore gives
the displayed formula.
:::

<1>5. Taking imaginary parts in step <1>4 yields
$$
\lim_{R\to\infty}
2\int_{1/R}^{R}\frac{\sin x}{x}\,dx
=\pi.
$$

::: {.proof}
The imaginary part of $e^{ix}/x$ is $\sin x/x$, which is an even
function. Therefore
$$
\Im\left(
\int_{-R}^{-1/R}\frac{e^{ix}}x\,dx
+
\int_{1/R}^{R}\frac{e^{ix}}x\,dx
\right)
=2\int_{1/R}^{R}\frac{\sin x}{x}\,dx.
$$
The imaginary part of the limit $\pi i$ is $\pi$.
:::

<1>6. The required improper integral is
$$
\boxed{
\int_0^\infty\frac{\sin x}{x}\,dx=\frac\pi2}.
$$

::: {.proof}
The function $\sin x/x$ has a removable singularity at $0$, with limit
$1$. Hence
$$
\int_0^{1/R}\frac{\sin x}{x}\,dx\longrightarrow0.
$$
Step <1>5 therefore implies
$$
\lim_{R\to\infty}
\int_0^R\frac{\sin x}{x}\,dx
=\frac\pi2,
$$
which is precisely the improper integral.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 gives the required value.
:::
:::
