---
schema: qual/card@1
id: P-RA16M6
kind: problem
title: 'UGA analysis qualifying exam, May 2016, problem 6'
classification:
  areas:
  - real-analysis
  topics:
  - riemann-integrability
  - integrals
  - stone-weierstrass
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
(a) Suppose $f:[-1,1]\to\mathbb R$ is a bounded function that is continuous at $0$.
Let $$\alpha(x)=\begin{cases}-1,&x\in[-1,0],\\1,&x\in(0,1].\end{cases}$$ Prove that $f\in\mathcal R(\alpha)[-1,1]$, i.e., $f$ is Riemann integrable with respect to $\alpha$ on $[-1,1]$, and $$\int_{-1}^{1}f\,d\alpha=2f(0).$$

(b) Let $g:[0,1]\to\mathbb R$ be a continuous function such that $$\int_0^1g(x)x^{3k+2}\,dx=0,\qquad\text{for all }k=0,1,2,\ldots.$$ Prove that $g(x)=0$ for all $x\in[0,1]$.
:::

:::: {.solution}
> **AI-Generated Solution** **Goal:** (a) $f$ bounded and continuous at $0$ is Riemann–Stieltjes integrable w.r.t. the jump $\alpha$ with $\int_{-1}^1 f\,d\alpha = 2f(0)$; (b) $\int_0^1 g(x)x^{3k+2}\,dx = 0$ for all $k \ge 0$ forces $g \equiv 0$.

<1>1. (a) $\int_{-1}^1 f\,d\alpha = 2f(0)$.
<2>1. $\alpha$ is constant on $[-1,0]$ (value $-1$) and constant on $(0,1]$ (value $1$); so $\Delta\alpha_i = 2$ for the unique interval straddling $0$, and $0$ for all others.
Proof: consecutive values of $\alpha$ differ only across the jump at $0$, where the difference is $1 - (-1) = 2$.
<2>2. Every Stieltjes sum is $2f(t_j)$ where $t_j$ is a tag in the interval straddling $0$; as the mesh $\to 0$, $t_j \to 0$ and $f(t_j) \to f(0)$ by continuity at $0$.
Proof: only the straddling interval contributes (by <2>1), its tag $t_j$ lies within $\|P\|$ of $0$; continuity of $f$ at $0$ gives $f(t_j) \to f(0)$.
<2>3. Q.E.D. Proof: <2>2 shows the Stieltjes sums converge to $2f(0)$ as mesh $\to 0$, i.e. $f \in \mathcal R(\alpha)$ with $\int_{-1}^1 f\,d\alpha = 2f(0)$.

<1>2. (b) $g \equiv 0$ on $[0,1]$.
<2>1. Substitute $t = x^3$: $\int_0^1 g(x)x^{3k+2}\,dx = \frac13 \int_0^1 g(t^{1/3}) t^k\,dt$.
Proof: $x = t^{1/3}$, $dx = \frac13 t^{-2/3}dt$, and $x^{3k+2} = t^k\, t^{2/3}$; so $g(x)x^{3k+2}dx = g(t^{1/3})t^k t^{2/3}\cdot\frac13 t^{-2/3}dt = \frac13 g(t^{1/3})t^k dt$.
<2>2. The function $\varphi(t) := g(t^{1/3})$ is continuous on $[0,1]$ and $\int_0^1 \varphi(t) t^k\,dt = 0$ for all $k \ge 0$.
Proof: <2>1 and the hypothesis (the factor $1/3$ is harmless).
<2>3. $\varphi \equiv 0$.
Proof: by Weierstrass, polynomials are dense in $C[0,1]$; hence $\int_0^1 \varphi \, p = 0$ for every polynomial $p$ (linear combination of the vanishing $t^k$-moments); take $p_k \to \varphi$ uniformly to get $\int_0^1 \varphi^2 = \lim_k \int \varphi p_k = 0$; since $\varphi^2 \ge 0$ is continuous, $\varphi \equiv 0$.
<2>4. $g \equiv 0$.
Proof: <2>3 says $g(t^{1/3}) = 0$ for all $t \in [0,1]$; as $t \mapsto t^{1/3}$ is onto $[0,1]$, $g \equiv 0$.
<2>5. Q.E.D. Proof: <2>1–<2>4 prove (b).
:::
