---
schema: qual/card@1
id: P-DQYX5
kind: problem
title: "Let $f, g\\in L^1(\\RR^n)$ and give a definition of $f\\ast g$."
classification:
  areas:
  - real-analysis
  topics:
  - fourier-analysis
  - convolution
  - l1
relations: []
review: draft
solved: true
---

::: problem
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
> **AI-Generated Solution**

<1>1. (a) Definition: for $f, g \in L^1(\RR^n)$, the convolution is $(f \ast g)(x) = \int_{\RR^n} f(x - y)\,g(y)\,dy = \int f(y)\,g(x-y)\,dy$, defined for almost every $x$; and $f \ast g \in L^1(\RR^n)$ with $\|f \ast g\|_1 \le \|f\|_1\|g\|_1$.
    Proof: Tonelli's theorem gives $\int |f(x-y)||g(y)|\,dy\,dx = \|f\|_1\|g\|_1 < \infty$, so the integral is finite for a.e. $x$ and the $L^1$ norm bound holds.

<1>2. (b) If $f, g$ are integrable and bounded, then $(f \ast g)(x) \to 0$ as $|x| \to \infty$.
    <2>1. Fix $\eps > 0$; choose $R$ with $\int_{|y| \ge R}|f(y)|\,dy < \eps$ and $\int_{|y| \ge R}|g(y)|\,dy < \eps$ (possible since $f, g \in L^1$).
        Proof: dominated convergence / definition of the improper integral.
    <2>2. Split: $|(f\ast g)(x)| \le \int_{|y| < R}|f(x-y)||g(y)|\,dy + \int_{|y| \ge R}|f(x-y)||g(y)|\,dy$.
        Proof: triangle inequality.
    <2>3. Second term: $\int_{|y| \ge R}|f(x-y)||g(y)|\,dy \le \|f\|_\infty \int_{|y| \ge R}|g(y)|\,dy \le \|f\|_\infty \eps$.
        Proof: $|f| \le \|f\|_\infty$ pointwise.
    <2>4. First term: for $|x| \ge 2R$, if $|y| < R$ then $|x - y| \ge |x| - |y| \ge R$, so $\int_{|y| < R}|f(x-y)||g(y)|\,dy \le \|g\|_\infty \int_{|x-y| \ge R}|f(x-y)|\,dy = \|g\|_\infty \int_{|z| \ge R}|f(z)|\,dz \le \|g\|_\infty \eps$.
        Proof: substitute $z = x - y$; the integration domain is contained in $\{|z| \ge R\}$.
    <2>5. Q.E.D.
        Proof: <2>2, <2>3, <2>4 give $|(f\ast g)(x)| \le (\|f\|_\infty + \|g\|_\infty)\eps$ for $|x| \ge 2R$.

<1>3. (c)1. Definition: for $f \in L^1(\RR^n)$, the Fourier transform is $\hat f(\xi) = \int_{\RR^n} f(x)\,e^{-2\pi i x \cdot \xi}\,dx$, $\xi \in \RR^n$.
    Proof: the integral converges absolutely since $|f(x)e^{-2\pi i x\cdot\xi}| = |f(x)|$; $\hat f$ is bounded ($\le \|f\|_1$) and continuous.

<1>4. (c)2. Outline of Fourier inversion: $\check g(x) := \int \hat g(\xi) e^{2\pi i x\cdot\xi}\,d\xi$ satisfies $\check{\hat f} = f$ a.e. for $f \in L^1$ with $\hat f \in L^1$.
    <2>1. For Gaussian mollifiers $\phi_t(x) = t^{-n}\phi(x/t)$, $\phi(x) = e^{-\pi|x|^2}$, the transform is $\hat \phi_t(\xi) = e^{-\pi t^2|\xi|^2}$, and $\int \hat\phi_t = \hat\phi_t(0) = 1$.
        Proof: the Gaussian is its own Fourier transform (standard computation via the heat kernel).
    <2>2. Show $\int f(x-y)\,\phi_t(y)\,dy \to f$ in $L^1$ as $t \to 0$ (approximation to identity).
        Proof: strong continuity of translation in $L^1$ plus $\int\phi_t = 1$.
    <2>3. On the transform side, compute $\int \hat f(\xi)\,\hat\phi_t(\xi)\,e^{2\pi i x\cdot\xi}\,d\xi = (f \ast \phi_t)(x)$ (Fubini on $\int f(y)\int \phi_t(x-y) e^{-2\pi i\xi\cdot(x-y)}\,d\xi\,dy$ — the inner integral is $\check{\hat\phi}_t = \phi_t$).
        Proof: Fubini and the inversion formula for the Gaussian (which is elementary, or by the same argument bootstrapped from the known transform of $\phi_t$).
    <2>4. Let $t \to 0$: the left side converges to $\check{\hat f}(x)$ (dominated by $\|\hat f\|_1$, since $\hat\phi_t(\xi) \to 1$ pointwise) and the right side to $f$ in $L^1$; so $\check{\hat f} = f$ a.e.
        Proof: dominated convergence on the left; <2>2 on the right.

<1>5. (c)3. Example: $f = \chi_{[-1,1]}$ has $\hat f(\xi) = \frac{\sin 2\pi\xi}{\pi\xi} \notin L^1(\RR)$.
    Proof: $\hat f(\xi) = \int_{-1}^1 e^{-2\pi i x \xi}\,dx = \frac{e^{-2\pi i\xi} - e^{2\pi i\xi}}{-2\pi i \xi} = \frac{\sin(2\pi\xi)}{\pi\xi}$; and $|\hat f(\xi)| \sim \frac{1}{|\xi|}$ at infinity, so $\int |\hat f| = \infty$ (the function is $\ge c/|\xi|$ off a bounded set).
:::
