---
schema: qual/card@1
id: P-AZOFF-G04
kind: problem
title: $\int_0^\infty\frac{\cos x-\cos 4x}{x^2}\,dx$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Residues, Problem 4, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Integrated (exp(iz)-exp(4iz))/z^2 over an upper-half-plane contour with
    a small semicircular indentation at zero. The outer arc vanishes, the
    indentation contributes -3pi from the residue term -3i/z, and taking
    real parts gives the whole-line integral 3pi and hence 3pi/2 on the
    positive half-line.
---

::: {.problem}
Evaluate $\textstyle \int _ { 0 } ^ { \infty } { \frac { \cos x - \cos 4 x } { x ^ { 2 } } } d x$
:::

::: {.solution}
Set
$$
F(z)=\frac{e^{iz}-e^{4iz}}{z^2}.
$$
For $0<\varepsilon<R$, use the contour consisting of
$$
[-R,-\varepsilon],
$$
the upper semicircle of radius $\varepsilon$ traversed clockwise from
$-\varepsilon$ to $\varepsilon$,
$$
[\varepsilon,R],
$$
and the upper semicircle of radius $R$ traversed counterclockwise.

<1>1. Near $z=0$,
$$
F(z)
=
-\frac{3i}{z}
+\frac{15}{2}
+O(z).
$$

::: {.proof}
The exponential expansions give
$$
e^{iz}
=
1+iz-\frac{z^2}{2}+O(z^3)
$$
and
$$
e^{4iz}
=
1+4iz-8z^2+O(z^3).
$$
Subtracting,
$$
e^{iz}-e^{4iz}
=
-3iz
+\frac{15}{2}z^2
+O(z^3).
$$
Divide by $z^2$.
:::

<1>2. The integral over the small indented semicircle tends to
$$
-3\pi
$$
as $\varepsilon\to0$.

::: {.proof}
Write
$$
F(z)=-\frac{3i}{z}+H(z),
$$
where step <1>1 shows that $H$ is bounded near $0$. On the small
semicircle, parametrize
$$
z=\varepsilon e^{i\theta},
\qquad
\pi\geq\theta\geq0.
$$
Then
$$
\int
-\frac{3i}{z}\,dz
=
\int_\pi^0
(-3i)i\,d\theta
=
-3\pi.
$$
The integral of $H$ tends to zero because $H$ is bounded while the arc
length is $\pi\varepsilon$.
:::

<1>3. The integral over the large upper semicircle tends to zero as
$R\to\infty$.

::: {.proof}
For $z$ in the upper half-plane,
$$
\abs{e^{iz}}\leq1
\qquad\text{and}\qquad
\abs{e^{4iz}}\leq1.
$$
Hence on $\abs{z}=R$,
$$
\abs{F(z)}
\leq
\frac2{R^2}.
$$
The large arc has length $\pi R$, so the ML estimate gives
$$
\abs{
\int_{\text{large arc}}F(z)\,dz
}
\leq
\frac{2\pi}{R}
\longrightarrow0.
$$
:::

<1>4. The symmetric indented real-axis integrals satisfy
$$
\lim_{\substack{R\to\infty\\ \varepsilon\to0^+}}
\left(
\int_{-R}^{-\varepsilon}
\frac{e^{ix}-e^{4ix}}{x^2}\,dx
+
\int_{\varepsilon}^{R}
\frac{e^{ix}-e^{4ix}}{x^2}\,dx
\right)
=
3\pi.
$$

::: {.proof}
The indented contour contains no singularities of $F$, so Cauchy's theorem
gives total contour integral zero. Therefore
$$
\begin{aligned}
&\int_{-R}^{-\varepsilon}F(x)\,dx
+\int_{\varepsilon}^{R}F(x)\,dx\\
&\qquad=
-\int_{\text{small arc}}F(z)\,dz
-\int_{\text{large arc}}F(z)\,dz.
\end{aligned}
$$
Let $R\to\infty$ and $\varepsilon\to0^+$. Steps <1>2 and <1>3 give the
displayed limit $3\pi$.

The real part of the integrand extends continuously across $x=0$, because
$$
\cos x-\cos4x=O(x^2).
$$
Thus no principal-value qualification is needed for the real part used
below.
:::

<1>5. The whole-line real integral is
$$
\int_{-\infty}^{\infty}
\frac{\cos x-\cos4x}{x^2}\,dx
=
3\pi.
$$

::: {.proof}
Take real parts in step <1>4.
:::

<1>6. The requested value is
$$
\boxed{
\int_0^{\infty}
\frac{\cos x-\cos4x}{x^2}\,dx
=
\frac{3\pi}{2}.
}
$$

::: {.proof}
The integrand in step <1>5 is even, so its whole-line integral is twice the
integral over $[0,\infty)$.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the requested evaluation.
:::
:::
