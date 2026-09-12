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
---

::: problem
Compute the following integrals.

\(i\) $\displaystyle \int_0^\infty \frac{\sin x}{x} \, dx$ (ii) $\displaystyle \int_0^\infty (\frac{\sin x}{x})^2 \, dx$ (iii) $\displaystyle \int_0^\infty \frac{x^{a-1}}{(1 + x)^2} \, dx$, $0< a < 2$

\(i\) $\displaystyle \int_0^\infty \frac{\cos a x - \cos bx}{x^2} dx$, $a, b >0$ (ii) $\displaystyle \int_0^\infty \frac{x^{a-1}}{1 + x^n} \, dx$, $0< a < n$

\(iii\) $\displaystyle \int_0^\infty \frac{\log x}{1 + x^n} \, dx$, $n \geq 2$ (iv) $\displaystyle \int_0^\infty \frac{\log x}{(1 + x^2)^2} dx$ (v) $\displaystyle \int_0^{\pi} \log|1 - a \sin \theta| d \theta$, $a \in \mathbb C$
:::

::: {.solution}
**Goal:** Compute a batch of standard integrals: (i) $\int_0^\infty \frac{\sin x}{x}\,dx$; (ii) $\int_0^\infty \qty(\frac{\sin x}{x})^2\,dx$; (iii) $\int_0^\infty \frac{x^{a-1}}{(1+x)^2}\,dx$ for $0 < a < 2$; (iv) $\int_0^\infty \frac{\cos(ax) - \cos(bx)}{x^2}\,dx$ for $a, b > 0$; (v) $\int_0^\infty \frac{x^{a-1}}{1 + x^n}\,dx$ for $0 < a < n$; (vi) $\int_0^\infty \frac{\log x}{1 + x^n}\,dx$ for $n \ge 2$; (vii) $\int_0^\infty \frac{\log x}{(1+x^2)^2}\,dx$; (viii) $\int_0^\pi \log\abs{1 - a\sin\theta}\,d\theta$ for $a \in \CC$.

<1>1. (i) $\int_0^\infty \frac{\sin x}{x}\,dx = \frac{\pi}{2}$.
::: {.proof}
Integrate $e^{iz}/z$ over the indented semicircle in the upper half-plane: $\int_{\eps \le \abs{x} \le R} \frac{e^{ix}}{x}\,dx + \text{(arcs)} = 0$ by Cauchy's theorem (no poles inside).
:::
The small semicircle around 0 contributes $-i\pi$ (half of $-2\pi i \Res_0(1/z)$, with sign from indenting above); the large arc vanishes (Jordan's lemma); taking real parts and $\eps \to 0$, $R \to \infty$: $\int_\RR \frac{\cos x}{x}\,dx = 0$ (principal value) and $\int_\RR \frac{\sin x}{x}\,dx = \pi$.
Since $\sin x/x$ is even: $\int_0^\infty \frac{\sin x}{x}\,dx = \pi/2$.

<1>2. (ii) $\int_0^\infty \qty(\frac{\sin x}{x})^2\,dx = \frac{\pi}{2}$.
::: {.proof}
Use $\qty(\frac{\sin x}{x})^2 = \frac{1 - \cos 2x}{2x^2}$, so the integral is $\frac12 \int_0^\infty \frac{1 - \cos(2x)}{x^2}\,dx$.
:::
By (iv) with $a = 0$, $b = 2$ (or by direct evaluation), $\int_0^\infty \frac{1 - \cos(2x)}{x^2}\,dx = \pi$, giving $\pi/2$.
Alternatively, Feynman's trick: $\int_0^\infty \frac{1 - \cos(\lambda x)}{x^2}\,dx = \frac{\pi\lambda}{2}$ (differentiate w.r.t. $\lambda$, integrate $\int_0^\infty \sin(\lambda x)/x\,dx = \pi/2$).

<1>3. (iii) $\int_0^\infty \frac{x^{a-1}}{(1+x)^2}\,dx = \frac{\pi(1-a)}{\sin(\pi a)}$ for $0 < a < 2$.
::: {.proof}
This is the Beta function: substituting $x = t/(1-t)$, $\int_0^\infty \frac{x^{a-1}}{(1+x)^2}\,dx = \int_0^1 t^{a-1}(1-t)^{1-a}\,dt = B(a, 2-a) = \Gamma(a)\Gamma(2-a) = \frac{\pi}{\sin(\pi a)} \cdot \qty(\text{using }\Gamma(2-a) = (1-a)\Gamma(1-a))$ — precisely $\Gamma(a)\Gamma(2-a) = \Gamma(a)(1-a)\Gamma(1-a) = (1-a)\frac{\pi}{\sin\pi a}$.
:::
So the integral equals $\frac{\pi(1-a)}{\sin(\pi a)}$, valid for $0 < a < 2$ (reflection formula; at $a = 1$ the formula gives $0/0$, limit $= 1$, correct as $\int_0^\infty 1/(1+x)^2\,dx = 1$).

<1>4. (iv) $\int_0^\infty \frac{\cos(ax) - \cos(bx)}{x^2}\,dx = \frac{\pi}{2}(b - a)$ for $a, b > 0$.
::: {.proof}
$\frac{\cos(ax) - \cos(bx)}{x^2} = \int_a^b \frac{\sin(tx)}{x}\,dt$, so by Fubini and (i), the integral equals $\int_a^b \frac{\pi}{2}\,dt = \frac{\pi}{2}(b - a)$.
:::

<1>5. (v) $\int_0^\infty \frac{x^{a-1}}{1 + x^n}\,dx = \frac{\pi}{n\sin(\pi a/n)}$ for $0 < a < n$.
::: {.proof}
Sector contour of angle $2\pi/n$ as in the standard computation: the pole at $e^{i\pi/n}$ contributes, and the second ray picks up a factor $e^{2\pi i a/n}$; solving gives $\frac{\pi}{n\sin(\pi a/n)}$.
:::

<1>6. (vi) $\int_0^\infty \frac{\log x}{1 + x^n}\,dx = -\frac{\pi^2}{n^2}\cot\qty(\frac{\pi}{n})\csc\qty(\frac{\pi}{n})$ for $n \ge 2$.
::: {.proof}
For $0<a<n$, part (v) gives
\[
M(a)=\int_0^\infty \frac{x^{a-1}}{1+x^n}\,dx
=\frac{\pi}{n}\csc\qty{\frac{\pi a}{n}}.
\]
Differentiating with respect to $a$ gives
\[
M'(a)
=\int_0^\infty \frac{x^{a-1}\log x}{1+x^n}\,dx
=-\frac{\pi^2}{n^2}
\csc\qty{\frac{\pi a}{n}}
\cot\qty{\frac{\pi a}{n}}.
\]
At $a=1$ this is exactly
\[
\int_0^\infty \frac{\log x}{1+x^n}\,dx
=-\frac{\pi^2}{n^2}
\csc\qty{\frac{\pi}{n}}
\cot\qty{\frac{\pi}{n}}.
\]
:::

<1>7. (vii) $\int_0^\infty \frac{\log x}{(1+x^2)^2}\,dx = -\frac{\pi}{4}$.
::: {.proof}
$H(a) = \int_0^\infty \frac{x^{a-1}}{(1+x^2)^2}\,dx = \frac{\pi}{2}\qty(1 - \frac a2)\csc\qty(\frac{\pi a}{2})$; differentiating at $a = 1$ (as in the companion computation) gives $-\pi/4$.
:::

<1>8. (viii) $\int_0^\pi \log\abs{1 - a\sin\theta}\,d\theta$ for $a \in \CC$.
::: {.proof}
For $a=0$ the integral is $0$. Assume $a\ne0$. Choose a root $r$ of
\[
ar^2-2r+a=0
\]
with $|r|\le1$; such a root exists because the two roots have product $1$.
Then
\[
a={2r\over1+r^2},
\]
and $1+r^2\ne0$ for finite $a$.

With $x=\theta-\pi/2$,
\[
1-a\sin\theta
=1-a\cos x
={\qty(1-re^{ix})\qty(1-re^{-ix})\over1+r^2}.
\]
Consequently
\[
I(a):=\int_0^\pi\log|1-a\sin\theta|\,d\theta
=2\int_{-\pi/2}^{\pi/2}\log|1-re^{ix}|\,dx
-\pi\log|1+r^2|.
\]

For $|r|<1$ the uniformly convergent logarithmic series gives
\[
\log|1-re^{ix}|
=-\Re\sum_{n=1}^\infty{r^ne^{inx}\over n}.
\]
Termwise integration yields
\[
\begin{aligned}
\int_{-\pi/2}^{\pi/2}\log|1-re^{ix}|\,dx
&=-2\Re\sum_{n=1}^\infty
{r^n\sin(n\pi/2)\over n^2}\\
&=-2\Re\left(
{\Li_2(ir)-\Li_2(-ir)\over2i}
\right),
\end{aligned}
\]
where
\[
\Li_2(z)=\sum_{n=1}^\infty {z^n\over n^2},
\qquad |z|\le1.
\]
For $|r|=1$ the same formula follows by radial passage to the limit. The only
possible singularities of the logarithm on the integration interval are
logarithmic and hence integrable, while the dilogarithm series is absolutely
convergent on the closed unit disk.

Thus
\[
\boxed{
I(a)
=-4\Re\left(
{\Li_2(ir)-\Li_2(-ir)\over2i}
\right)
-\pi\log|1+r^2|,
}
\]
where $r$ is either root of $ar^2-2r+a=0$ with $|r|\le1$.
For $a=0$, take $r=0$; the same formula gives $I(0)=0$.
:::

<1>9. Q.E.D.
::: {.proof}
<1>1–<1>8 evaluate all eight integrals.
:::
:::
