---
schema: qual/card@1
id: P-DQYX5
kind: problem
title: Convolution of $L^1$ functions, vanishing at infinity, and the Fourier inversion
  formula
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Analysis
  - Convolution
  - L¹
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
(a) Let $f, g\in L^1(\RR^n)$ and give a definition of $f\ast g$.

(b) Prove that if $f, g$ are integrable and bounded, then
$$
(f\ast g)(x) \converges{\abs x\to\infty}\to 0.
$$

(c)

(i) Define the *Fourier transform* of an integrable function $f$ on $\RR^n$.

(ii) Give an outline of the proof of the Fourier inversion formula.

(iii) Give an example of a function $f\in L^1(\RR^n)$ such that $\hat{f}$ is not in $L^1(\RR^n)$.
:::

::: {.solution}
(a) For $f, g \in L^1(\RR^n)$, $(f \ast g)(x) = \int_{\RR^n} f(x - y)\,g(y)\,dy$. By Tonelli's theorem $\iint \abs{f(x-y)}\abs{g(y)}\,dy\,dx = \norm{f}_1\norm{g}_1 < \infty$, so the integral converges absolutely for a.e. $x$, and $\norm{f \ast g}_1 \le \norm{f}_1\norm{g}_1$.

(b)

::: pf

::: {.pf-step #p1-1}
Fix $\eps > 0$ and choose $R$ with $\int_{\norm{y} \ge R}\abs{f} < \eps$ and $\int_{\norm{y} \ge R}\abs{g} < \eps$. Then $\int_{\norm{y} \ge R}\abs{f(x-y)}\abs{g(y)}\,dy \le \norm{f}_\infty\eps$ for every $x$.

::: pf-proof
$R$ exists by dominated convergence, since $\abs{f}\chi_{\theset{\norm{y} \ge R}} \to 0$ pointwise as $R \to \infty$ with dominating function $\abs{f}$, and likewise for $g$. The bound uses $\abs{f} \le \norm{f}_\infty$.
:::

:::

::: {.pf-step #p1-2}
For $\norm{x} \ge 2R$, $\int_{\norm{y} < R}\abs{f(x-y)}\abs{g(y)}\,dy \le \norm{g}_\infty\eps$.

::: pf-proof
If $\norm{y} < R$ and $\norm{x} \ge 2R$, then $\norm{x - y} \ge R$. Substituting $z = x - y$ gives $\int_{\norm{y} < R}\abs{f(x-y)}\abs{g(y)}\,dy \le \norm{g}_\infty\int_{\norm{z} \ge R}\abs{f(z)}\,dz$.
:::

:::

::: pf-qed
By steps [](#p1-1){.pf-ref} and [](#p1-2){.pf-ref}, $\abs{(f\ast g)(x)} \le (\norm{f}_\infty + \norm{g}_\infty)\eps$ for $\norm{x} \ge 2R$.
:::

:::

(c)(i) For $f \in L^1(\RR^n)$, $\hat f(\xi) = \int_{\RR^n} f(x)\,e^{-2\pi i x \cdot \xi}\,dx$. The integral converges absolutely because $\abs{f(x)e^{-2\pi i x\cdot\xi}} = \abs{f(x)}$.

(c)(ii) Let $f \in L^1$ with $\hat f \in L^1$. Then $f(x) = \int \hat f(\xi) e^{2\pi i x\cdot\xi}\,d\xi$ for a.e. $x$.

::: pf

::: {.pf-step #p2-1}
For $\phi(x) = e^{-\pi\norm{x}^2}$ and $\phi_t(x) = t^{-n}\phi(x/t)$, $\widehat{\phi_t}(\xi) = e^{-\pi t^2\norm{\xi}^2}$ and $\int \widehat{\phi_t}(\xi) e^{2\pi i x\cdot\xi}\,d\xi = \phi_t(x)$.

::: pf-proof
In one variable, $\hat\phi$ and $\phi$ both solve $u' = -2\pi\xi u$ with $u(0) = 1$, the first by differentiating under the integral and integrating by parts; so $\hat\phi = \phi$. The $n$-variable case factors, and the formulas for $\phi_t$ follow by scaling.
:::

:::

::: {.pf-step #p2-2}
$\int \hat f(\xi)\,\widehat{\phi_t}(\xi)\,e^{2\pi i x\cdot\xi}\,d\xi = (f \ast \phi_t)(x)$ for every $x$.

::: pf-proof
Insert $\hat f(\xi) = \int f(y)e^{-2\pi i y\cdot\xi}\,dy$. The double integral converges absolutely, so Fubini's theorem and step [](#p2-1){.pf-ref} give $\int f(y)\,\phi_t(x - y)\,dy$.
:::

:::

::: pf-qed
As $t \to 0$, the left side of step [](#p2-2){.pf-ref} tends to $\int \hat f(\xi) e^{2\pi i x\cdot\xi}\,d\xi$ for every $x$, by dominated convergence with dominating function $\abs{\hat f}$, since $\widehat{\phi_t} \to 1$ pointwise and $\abs{\widehat{\phi_t}} \leq 1$. The right side tends to $f$ in $L^1$, because $\phi_t$ is an approximate identity; so a subsequence converges to $f$ a.e. The two limits agree a.e.
:::

:::

(c)(iii) For $n = 1$, $f = \chi_{[-1,1]}$ is in $L^1$ and $\hat f(\xi) = \frac{\sin 2\pi\xi}{\pi\xi} \notin L^1(\RR)$.

::: {.proof}
$\hat f(\xi) = \int_{-1}^1 e^{-2\pi i x \xi}\,dx = \frac{e^{2\pi i\xi} - e^{-2\pi i\xi}}{2\pi i \xi} = \frac{\sin(2\pi\xi)}{\pi\xi}$. For $k \geq 1$ and $\xi \in [k/2 + 1/8, k/2 + 3/8]$, $\abs{\sin 2\pi\xi} \ge 1/\sqrt2$ and $\abs{\xi} \le k/2 + 1$, so $\int\abs{\hat f} \ge \sum_{k \ge 1}\frac{1}{4\sqrt2\,\pi(k/2+1)} = \infty$.
:::
:::
