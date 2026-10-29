---
schema: qual/card@1
id: P-3MIIY
kind: problem
title: Dirichlet, Mellin, and logarithmic integrals by residues
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
- event: statement-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: 'The source labels its integrals (i)-(iii) and then again (i)-(v); the statement numbers the eight integrals (i)-(viii) in source order.'
---

::: {.problem}
Compute the following integrals.

(i) $\displaystyle \int_0^\infty \frac{\sin x}{x} \, dx$

(ii) $\displaystyle \int_0^\infty \qty(\frac{\sin x}{x})^2 \, dx$

(iii) $\displaystyle \int_0^\infty \frac{x^{a-1}}{(1 + x)^2} \, dx$, $0< a < 2$

(iv) $\displaystyle \int_0^\infty \frac{\cos a x - \cos bx}{x^2} dx$, $a, b >0$

(v) $\displaystyle \int_0^\infty \frac{x^{a-1}}{1 + x^n} \, dx$, $0< a < n$

(vi) $\displaystyle \int_0^\infty \frac{\log x}{1 + x^n} \, dx$, $n \geq 2$

(vii) $\displaystyle \int_0^\infty \frac{\log x}{(1 + x^2)^2} dx$

(viii) $\displaystyle \int_0^{\pi} \log|1 - a \sin \theta| d \theta$, $a \in \CC$
:::

::: {.solution}

::: pf

::: {.pf-step #dirichlet}
(i) $\displaystyle\int_0^\infty \frac{\sin x}{x}\,dx = \boxed{\frac{\pi}{2}}$, and hence $\displaystyle\int_0^\infty \frac{\sin cx}{x}\,dx = \frac{\pi}{2}$ for every $c>0$.

::: pf-proof
Integrate $e^{iz}/z$ over the upper half-annulus $\varepsilon\leq\abs{z}\leq R$, $\Im z\geq0$.
Cauchy's theorem gives $0$; the large arc tends to $0$ by Jordan's lemma, and the small arc, traversed clockwise, tends to $-i\pi\Res_{z=0}\frac{e^{iz}}{z}=-i\pi$.
So $\int_{\varepsilon<\abs{x}<R}\frac{e^{ix}}{x}\,dx\to i\pi$; its imaginary part is $2\int_\varepsilon^R\frac{\sin x}{x}\,dx$.
The second claim follows by the substitution $x\mapsto cx$.
:::

:::

::: pf-step
(ii) $\displaystyle\int_0^\infty \qty(\frac{\sin x}{x})^2\,dx = \boxed{\frac{\pi}{2}}$.

::: pf-proof
Integrate by parts with $u=\sin^2x$ and $dv=dx/x^2$:
$$
\int_0^\infty \frac{\sin^2 x}{x^2}\,dx=\qty[-\frac{\sin^2x}{x}]_0^\infty+\int_0^\infty\frac{2\sin x\cos x}{x}\,dx=\int_0^\infty\frac{\sin 2x}{x}\,dx,
$$
since $\sin^2x/x\to0$ at both ends, and step [](#dirichlet){.pf-ref} evaluates the last integral.
:::

:::

::: pf-step
(iii) $\displaystyle\int_0^\infty \frac{x^{a-1}}{(1+x)^2}\,dx = \boxed{\frac{\pi(1-a)}{\sin(\pi a)}}$ for $a\neq1$, and the value is $1$ for $a=1$.

::: pf-proof
The substitution $x = t/(1-t)$ has $dx=dt/(1-t)^2$ and $1+x=1/(1-t)$, so the integral is $\int_0^1 t^{a-1}(1-t)^{1-a}\,dt = B(a, 2-a) = \Gamma(a)\Gamma(2-a)$.
Since $\Gamma(2-a)=(1-a)\Gamma(1-a)$, the reflection formula $\Gamma(a)\Gamma(1-a)=\pi/\sin(\pi a)$ gives the value for $a\neq1$, and for $a=1$ the integral is $\int_0^\infty\frac{dx}{(1+x)^2}=1$.
:::

:::

::: pf-step
(iv) $\displaystyle\int_0^\infty \frac{\cos ax - \cos bx}{x^2}\,dx = \boxed{\frac{\pi}{2}(b - a)}$.

::: pf-proof
Integrate by parts with $dv=dx/x^2$:
$$
\int_0^\infty \frac{\cos ax - \cos bx}{x^2}\,dx=\qty[-\frac{\cos ax - \cos bx}{x}]_0^\infty+\int_0^\infty\frac{-a\sin ax+b\sin bx}{x}\,dx.
$$
The bracket vanishes, because $\cos ax-\cos bx=O(x^2)$ at $0$ and is bounded at $\infty$, and step [](#dirichlet){.pf-ref} gives $-a\frac\pi2+b\frac\pi2$ for the last integral.
:::

:::

::: {.pf-step #mellin}
(v) $\displaystyle M(a)\coloneqq\int_0^\infty \frac{x^{a-1}}{1 + x^n}\,dx = \boxed{\frac{\pi}{n\sin(\pi a/n)}}$ for $0 < a < n$.

::: pf-proof
Integrate $z^{a-1}/(1+z^n)$, with $z^{a-1}=\abs{z}^{a-1}e^{i(a-1)\arg z}$, over the boundary of the sector $\varepsilon\leq\abs{z}\leq R$, $0\leq\arg z\leq2\pi/n$.
The only pole inside is $z_0=e^{i\pi/n}$, with residue $\frac{z_0^{a-1}}{nz_0^{n-1}}=-\frac1ne^{i\pi a/n}$.
The ray at angle $2\pi/n$, traversed inward, contributes $-e^{2\pi ia/n}$ times the integral along $[\varepsilon,R]$, and the arcs contribute $O(\varepsilon^a)+O(R^{a-n})\to0$.
Hence $M(a)\qty(1-e^{2\pi ia/n})=-\frac{2\pi i}{n}e^{i\pi a/n}$, so $M(a)=\frac{2\pi i}{n}\cdot\frac{1}{e^{i\pi a/n}-e^{-i\pi a/n}}$.
:::

:::

::: pf-step
(vi) $\displaystyle\int_0^\infty \frac{\log x}{1 + x^n}\,dx = \boxed{-\frac{\pi^2}{n^2}\csc\qty(\frac{\pi}{n})\cot\qty(\frac{\pi}{n})}$ for $n \ge 2$.

::: pf-proof
For $a$ in a compact subinterval of $(0,n)$, $\abs{\frac{\partial}{\partial a}\frac{x^{a-1}}{1+x^n}}=\frac{x^{a-1}\abs{\log x}}{1+x^n}$ is dominated by an integrable function, so $M'(a)=\int_0^\infty\frac{x^{a-1}\log x}{1+x^n}\,dx$.
Differentiating the value in step [](#mellin){.pf-ref} gives $M'(a)=-\frac{\pi^2}{n^2}\csc\qty(\frac{\pi a}{n})\cot\qty(\frac{\pi a}{n})$; take $a=1$.
:::

:::

::: pf-step
(vii) $\displaystyle J\coloneqq\int_0^\infty \frac{\log x}{(1+x^2)^2}\,dx = \boxed{-\frac{\pi}{4}}$.

::: pf-proof
The substitution $x=1/t$ gives $J=-\int_0^\infty\frac{t^2\log t}{(1+t^2)^2}\,dt$, so $2J=\int_0^\infty\log x\,\frac{1-x^2}{(1+x^2)^2}\,dx$.
Since $\frac{d}{dx}\frac{x}{1+x^2}=\frac{1-x^2}{(1+x^2)^2}$, integration by parts gives $2J=\qty[\frac{x\log x}{1+x^2}]_0^\infty-\int_0^\infty\frac{dx}{1+x^2}=-\frac\pi2$.
:::

:::

::: pf-step
(viii) Let $r$ be a root of $ar^2-2r+a=0$ with $\abs{r}\leq1$ ($r=0$ if $a=0$), and let $\operatorname{Li}_2(z)\coloneqq\sum_{n\geq1}z^n/n^2$ for $\abs{z}\leq1$. Then
$$
\int_0^\pi \log\abs{1 - a\sin\theta}\,d\theta=\boxed{-4\Re\qty(\frac{\operatorname{Li}_2(ir)-\operatorname{Li}_2(-ir)}{2i})-\pi\log\abs{1+r^2}}.
$$

::: pf-proof
For $a\neq0$ the two roots have product $1$, so one satisfies $\abs{r}\leq1$; then $1+r^2\neq0$ and $a=\frac{2r}{1+r^2}$.
With $x=\theta-\pi/2$,
$$
1-a\sin\theta=1-a\cos x=\frac{\qty(1-re^{ix})\qty(1-re^{-ix})}{1+r^2},
$$
and since $x\mapsto -x$ preserves $[-\pi/2,\pi/2]$,
$$
\int_0^\pi\log\abs{1-a\sin\theta}\,d\theta=2\int_{-\pi/2}^{\pi/2}\log\abs{1-re^{ix}}\,dx-\pi\log\abs{1+r^2}.
$$
For $\abs{r}<1$, $\log\abs{1-re^{ix}}=-\Re\sum_{n\geq1}\frac{r^ne^{inx}}{n}$ uniformly in $x$, and $\int_{-\pi/2}^{\pi/2}e^{inx}\,dx=\frac{2\sin(n\pi/2)}{n}$, so
$$
\int_{-\pi/2}^{\pi/2}\log\abs{1-re^{ix}}\,dx=-2\Re\sum_{n\geq1}\frac{r^n\sin(n\pi/2)}{n^2}=-2\Re\qty(\frac{\operatorname{Li}_2(ir)-\operatorname{Li}_2(-ir)}{2i}),
$$
using $\sin(n\pi/2)=\frac{i^n-(-i)^n}{2i}$.
For $\abs{r}=1$ the formula follows by letting $r$ tend radially to the circle: the logarithmic singularities of the integrand are integrable, and the series for $\operatorname{Li}_2$ converges absolutely on the closed unit disc.
For $a=0$ both sides are $0$.
:::

:::

:::

:::
