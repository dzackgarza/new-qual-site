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
a.
Let $f, g\in L^1(\RR^n)$ and give a definition of $f\ast g$.

b.
Prove that if $f, g$ are integrable and bounded, then
\[
(f\ast g)(x) \converges{\abs x\to\infty}\to 0
.\]


c. In parts:

    1. Define the *Fourier transform* of an integrable function $f$ on $\RR^n$.
    2. Give an outline of the proof of the Fourier inversion formula.
    3. Give an example of a function $f\in L^1(\RR^n)$ such that $\hat{f}$ is not in $L^1(\RR^n)$.
:::
::: {.solution}
(a) For $f, g \in L^1(\RR^n)$, $(f \ast g)(x) = \int_{\RR^n} f(x - y)\,g(y)\,dy$. By Tonelli's theorem $\iint |f(x-y)||g(y)|\,dy\,dx = \|f\|_1\|g\|_1 < \infty$, so the integral converges absolutely for a.e. $x$, and $\|f \ast g\|_1 \le \|f\|_1\|g\|_1$.

(b)

<1>1. Fix $\eps > 0$ and choose $R$ with $\int_{|y| \ge R}|f| < \eps$ and $\int_{|y| \ge R}|g| < \eps$. Then $\int_{|y| \ge R}|f(x-y)||g(y)|\,dy \le \|f\|_\infty\eps$ for every $x$.

::: {.proof}
$R$ exists by dominated convergence, since $|f|\chi_{\theset{|y| \ge R}} \to 0$ pointwise as $R \to \infty$ with dominating function $|f|$, and likewise for $g$. The bound uses $|f| \le \|f\|_\infty$.
:::

<1>2. For $|x| \ge 2R$, $\int_{|y| < R}|f(x-y)||g(y)|\,dy \le \|g\|_\infty\eps$.

::: {.proof}
If $|y| < R$ and $|x| \ge 2R$, then $|x - y| \ge R$. Substituting $z = x - y$ gives $\int_{|y| < R}|f(x-y)||g(y)|\,dy \le \|g\|_\infty\int_{|z| \ge R}|f(z)|\,dz$.
:::

<1>3. Q.E.D.

::: {.proof}
By steps <1>1 and <1>2, $|(f\ast g)(x)| \le (\|f\|_\infty + \|g\|_\infty)\eps$ for $|x| \ge 2R$.
:::

(c)1. For $f \in L^1(\RR^n)$, $\hat f(\xi) = \int_{\RR^n} f(x)\,e^{-2\pi i x \cdot \xi}\,dx$. The integral converges absolutely because $|f(x)e^{-2\pi i x\cdot\xi}| = |f(x)|$.

(c)2. Let $f \in L^1$ with $\hat f \in L^1$. Then $f(x) = \int \hat f(\xi) e^{2\pi i x\cdot\xi}\,d\xi$ for a.e. $x$.

<1>1. For $\phi(x) = e^{-\pi|x|^2}$ and $\phi_t(x) = t^{-n}\phi(x/t)$, $\widehat{\phi_t}(\xi) = e^{-\pi t^2|\xi|^2}$ and $\int \widehat{\phi_t}(\xi) e^{2\pi i x\cdot\xi}\,d\xi = \phi_t(x)$.

::: {.proof}
In one variable, $\hat\phi$ and $\phi$ both solve $u' = -2\pi\xi u$ with $u(0) = 1$, the first by differentiating under the integral and integrating by parts; so $\hat\phi = \phi$. The $n$-variable case factors, and the formulas for $\phi_t$ follow by scaling.
:::

<1>2. $\int \hat f(\xi)\,\widehat{\phi_t}(\xi)\,e^{2\pi i x\cdot\xi}\,d\xi = (f \ast \phi_t)(x)$ for every $x$.

::: {.proof}
Insert $\hat f(\xi) = \int f(y)e^{-2\pi i y\cdot\xi}\,dy$. The double integral converges absolutely, so Fubini's theorem and step <1>1 give $\int f(y)\,\phi_t(x - y)\,dy$.
:::

<1>3. Q.E.D.

::: {.proof}
As $t \to 0$, the left side of step <1>2 tends to $\int \hat f(\xi) e^{2\pi i x\cdot\xi}\,d\xi$ for every $x$, by dominated convergence with dominating function $|\hat f|$, since $\widehat{\phi_t} \to 1$ pointwise and $|\widehat{\phi_t}| \leq 1$. The right side tends to $f$ in $L^1$, because $\phi_t$ is an approximate identity; so a subsequence converges to $f$ a.e. The two limits agree a.e.
:::

(c)3. For $n = 1$, $f = \chi_{[-1,1]}$ is in $L^1$ and $\hat f(\xi) = \frac{\sin 2\pi\xi}{\pi\xi} \notin L^1(\RR)$.

::: {.proof}
$\hat f(\xi) = \int_{-1}^1 e^{-2\pi i x \xi}\,dx = \frac{e^{2\pi i\xi} - e^{-2\pi i\xi}}{2\pi i \xi} = \frac{\sin(2\pi\xi)}{\pi\xi}$. For $k \geq 1$ and $\xi \in [k/2 + 1/8, k/2 + 3/8]$, $|\sin 2\pi\xi| \ge 1/\sqrt2$ and $|\xi| \le k/2 + 1$, so $\int|\hat f| \ge \sum_{k \ge 1}\frac{1}{4\sqrt2\,\pi(k/2+1)} = \infty$.
:::
:::
