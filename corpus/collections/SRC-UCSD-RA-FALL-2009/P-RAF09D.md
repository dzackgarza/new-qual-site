---
schema: qual/card@1
id: P-RAF09D
kind: problem
title: "Principal value integral and distributional derivatives of log|x|"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 4 of the official UCSD Fall 2009 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
If $f \in L^1((-\infty, -\delta) \cup (\delta, \infty))$ for every $\delta > 0$, define its principal value integral to be
$$
\mathrm{PV} \int_{-\infty}^{\infty} f(x)\,dx = \lim_{\delta \to 0} \left(\int_{-\infty}^{-\delta} + \int_{\delta}^{\infty}\right) f(x)\,dx,
$$
if the limit exists.
For $\phi \in \mathcal{D}(\mathbb{R})$, put $\Lambda(\phi) = \int_{-\infty}^{\infty} \phi(x) \log|x|\,dx$.
Show that

(a) $\Lambda'(\phi) = \mathrm{PV} \int_{-\infty}^{\infty} \frac{\phi(x)}{x}\,dx$,

(b) $\Lambda''(\phi) = -\mathrm{PV} \int_{-\infty}^{\infty} \frac{\phi(x) - \phi(0)}{x^2}\,dx$.
:::

::: solution
<1>1. Compute the first distributional derivative.
::: proof
By definition of the derivative of a distribution,
\[
\Lambda'(\phi)=-\Lambda(\phi')
=-\int_{\mathbb R}\phi'(x)\log|x|\,dx.
\]
Choose $R>0$ so that $\operatorname{supp}\phi\subset(-R,R)$. For $0<\delta<R$, integrate by parts on $[-R,-\delta]$ and $[\delta,R]$:
\[
\begin{aligned}
-\int_{|x|>\delta}\phi'(x)\log|x|\,dx
&=\int_{|x|>\delta}\frac{\phi(x)}x\,dx\\
&\quad+\log\delta\,[\phi(\delta)-\phi(-\delta)].
\end{aligned}
\]
Since $\phi$ is $C^1$,
\[
|\phi(\delta)-\phi(-\delta)|\le C\delta,
\]
and therefore
\[
\log\delta\,[\phi(\delta)-\phi(-\delta)]\to0
\]
as $\delta\downarrow0$.

Hence
\[
\boxed{
\Lambda'(\phi)
=\operatorname{PV}\int_{\mathbb R}\frac{\phi(x)}x\,dx.}
\]
:::

<1>2. Differentiate once more.
::: proof
Using part (a),
\[
\Lambda''(\phi)
=-\Lambda'(\phi')
=-\operatorname{PV}\int_{\mathbb R}\frac{\phi'(x)}x\,dx.
\]
We now rewrite the principal value. Put
\[
h(x):=\phi(x)-\phi(0).
\]
Then $h'(x)=\phi'(x)$ and $h(0)=0$. For $\delta>0$,
\[
\begin{aligned}
\int_{|x|>\delta}\frac{\phi'(x)}x\,dx
&=\int_{|x|>\delta}\frac{h'(x)}x\,dx\\
&=\int_{|x|>\delta}\frac{h(x)}{x^2}\,dx
\; +\; B_\delta,
\end{aligned}
\]
where the boundary terms at $\pm\infty$ vanish because $h$ is bounded and $h(x)/x\to0$, and the inner boundary contribution is
\[
B_\delta
=-\frac{h(-\delta)+h(\delta)}\delta.
\]
Taylor expansion at $0$ gives
\[
h(\delta)=\phi'(0)\delta+O(\delta^2),
\qquad
h(-\delta)=-\phi'(0)\delta+O(\delta^2),
\]
so
\[
B_\delta\to0.
\]
Therefore
\[
\operatorname{PV}\int_{\mathbb R}\frac{\phi'(x)}x\,dx
=\operatorname{PV}\int_{\mathbb R}\frac{\phi(x)-\phi(0)}{x^2}\,dx.
\]
Substituting into the distributional derivative formula yields
\[
\boxed{
\Lambda''(\phi)
=-\operatorname{PV}\int_{\mathbb R}
\frac{\phi(x)-\phi(0)}{x^2}\,dx.}
\]
:::
:::
