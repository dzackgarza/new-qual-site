---
title: Inequalities
order: 9
topics:
- Norms
- Bounded Operators
---

# Inequalities

Let $(X,\mathcal M,\mu)$ be a measure space, and let $p,q\in[1,\infty]$ be conjugate exponents, $\frac1p+\frac1q=1$, unless stated otherwise.

## Between integrals

- **Hölder.** $\norm{fg}_1 \leq \norm f_p\norm g_q$ for measurable $f,g$.
  For $1<p<\infty$ and $\norm f_p,\norm g_q<\infty$, equality holds if and only if $\alpha\abs f^p = \beta\abs g^q$ almost everywhere for some constants $\alpha,\beta\geq0$, not both zero.

- **Minkowski.** $\norm{f+g}_p \leq \norm f_p + \norm g_p$ for $1\leq p\leq\infty$.
  For $0<p<1$ the inequality fails: on $[0,2]$, $\norm{\chi_{[0,1]}+\chi_{[1,2]}}_p = 2^{1/p} > 2 = \norm{\chi_{[0,1]}}_p+\norm{\chi_{[1,2]}}_p$.

- **Minkowski's integral inequality.** For $\sigma$-finite measure spaces, measurable $f$ on $X\times Y$, and $1\leq p<\infty$, $\norm{\int_Y f(\cdot, y)\dy}_p \leq \int_Y \norm{f(\cdot,y)}_p \dy$.

- **Jensen.** If $\mu(X)=1$, $f\in L^1(\mu)$ is real-valued, and $\varphi\colon\RR\to\RR$ is convex, then $\varphi\qty(\int f\,d\mu) \leq \int\varphi\circ f\,d\mu$.
  For $\mu$ twice Lebesgue measure on $[0,1]$, $f\equiv1$, and $\varphi(t)=t^2$, the left side is $4$ and the right side is $2$.

- **Young.** For $f\in L^p(\RR^n)$, $g\in L^q(\RR^n)$ with $1\leq p,q,r\leq\infty$ and $\frac1r = \frac1p+\frac1q-1$, $\norm{f*g}_r \leq \norm f_p\norm g_q$.

## Between a norm and a measure

- **Chebyshev.** For $0<p<\infty$ and $t>0$, $\mu(\theset{\abs f > t}) \leq t^{-p}\norm f_p^p$.

- **Borel--Cantelli.** If $\sum_n \mu(E_n) <\infty$, then almost every point lies in only finitely many $E_n$.
  Combined with Chebyshev's inequality: if $\sum_n\norm{f_n}_p^p<\infty$, then $\mu(\theset{\abs{f_n}>t})$ is summable for each $t>0$, so $f_n\to0$ almost everywhere.

## Elementary inequalities

- **Young's inequality for products.** For $a,b\geq0$ and $1<p<\infty$, $ab \leq \frac{a^p}p + \frac{b^q}q$; Hölder's inequality follows by applying it to $\abs f/\norm f_p$ and $\abs g/\norm g_q$ and integrating.

- **Convexity of $t\mapsto t^p$.** For $p\geq1$, $\abs{a+b}^p \leq 2^{p-1}\qty(\abs a^p + \abs b^p)$.

- **Reverse triangle inequality.** $\abs{\norm a - \norm b} \leq \norm{a - b}$ in any normed space.

- **Cauchy--Schwarz.** $\abs{\inner fg}\leq\norm f\norm g$ in an inner product space; in $L^2$ it is Hölder's inequality with $p=q=2$.

- **Bernoulli.** $(1+x)^n \geq 1 + nx$ for $x\geq-1$ and $n\in\NN$.

- **Exponential bound.** $1 + x\leq e^x$ for $x\in\RR$, so $\prod_{i}(1-a_i)\leq \exp\qty{-\sum_i a_i}$ for $a_i\in[0,1]$.

The full statements are on [[real-analysis/appendices/appendix-inequalities|Appendix: common inequalities]].
