---
schema: qual/card@1
id: P-JHUFA14CA5
kind: problem
title: Evaluating $\int_0^\infty\cos(ax)/(1+x^2)^2\,dx$
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Residues
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Read Fall 2014 problem 5 directly on PDF page 14; separated its complete statement from P-8XT05 without dropping the positive parameter hypothesis."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the double-pole derivative, upper-arc estimate, absolute convergence and passage from the full-line exponential integral to the half-line cosine integral."
---

::: {.problem}
For $a>0$, compute and justify
$$
\int_0^\infty\frac{\cos(ax)}{(1+x^2)^2}\,dx
=\frac{\pi(a+1)e^{-a}}4.
$$
:::

::: {.solution}
<1>1. The exponential integrand has one double pole in the upper half-plane.

::: {.proof}
Set $F(z)=e^{iaz}/(1+z^2)^2$. Its only upper-half-plane
pole is $i$, of order two. Differentiating the holomorphic
factor gives its residue [@SS03]:
$$
\begin{aligned}
\operatorname{Res}_{z=i}F
&=\left.\frac{d}{dz}\frac{e^{iaz}}{(z+i)^2}\right|_{z=i}\\
&=e^{-a}\left(\frac{ia}{(2i)^2}-\frac{2}{(2i)^3}\right)
=-\frac{i(a+1)e^{-a}}4.
\end{aligned}
$$
On the positively oriented contour formed by $[-R,R]$
and the upper semicircle $\Gamma_R$, for $R>1$, the
residue theorem gives
$$
\int_{-R}^R\frac{e^{iax}}{(1+x^2)^2}\,dx
+\int_{\Gamma_R}F(z)\,dz
=\frac{\pi(a+1)e^{-a}}2.
$$
:::

<1>2. The semicircle vanishes and symmetry gives the requested value.

::: {.proof}
On $\Gamma_R$, the assumption $a>0$ implies
$|e^{iaz}|=e^{-a\operatorname{Im}z}\leq1$. Also
$|1+z^2|\geq R^2-1$. Hence
$$
\left|\int_{\Gamma_R}F(z)\,dz\right|
\leq\frac{\pi R}{(R^2-1)^2}\longrightarrow0.
$$
The integral on the real line converges absolutely:
its absolute integrand is $(1+x^2)^{-2}$, bounded on
$[-1,1]$ and at most $|x|^{-4}$ outside that interval.
Letting $R\to\infty$ in step <1>1 is therefore justified.
Its real part is
$$
\int_{-\infty}^{\infty}\frac{\cos(ax)}{(1+x^2)^2}\,dx
=\frac{\pi(a+1)e^{-a}}2.
$$
The integrand is even, so the half-line integral is
$\pi(a+1)e^{-a}/4$, as asserted.
:::
:::
