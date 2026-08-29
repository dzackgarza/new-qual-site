---
schema: qual/card@1
id: P-WOHZ6
kind: problem
title: Uniform convergence of $\sum\sin(nz)/2^n$ on $\{\Im z<\ln 2\}$ and on $|z|\le
  r$
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Convergence
  - Convergence Tests
  - Series of Functions
  - Trigonometry
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Consider the series of complex functions:
$$
\sum_{n=1}^\infty \frac{\sin(nz)}{2^n}.
$$
(a) Determine whether the series converges uniformly on the half-plane $\{ z \in \mathbb{C} \mid \operatorname{Im}(z) < \ln 2 \}$, or clarify the correct domain of uniform convergence (such as $\{ \operatorname{Im}(z) \ge -c \}$ or compact subsets $\{ |\operatorname{Im}(z)| \le Y \}$ / disks $\{ |z| \le r \}$).
(b) Prove that for any $r > 0$, the series converges **uniformly on the closed disk** $\{ z \in \mathbb{C} \mid |z| \le r \}$.
:::

::: solution
**Goal:** Analyze the growth of $|\sin(nz)|$ using Euler's formula and apply the Weierstrass $M$-test to prove uniform convergence on compact disks and half-planes bounded below.

<1>1. Modulus of the Sine Function for Complex Arguments:
    *Proof:*
    <2>1. Let $z = x + iy \in \mathbb{C}$ with $x, y \in \mathbb{R}$.
    <2>2. By Euler's formula:
        $$\sin(nz) = \frac{e^{i n (x + iy)} - e^{-i n (x + iy)}}{2i} = \frac{e^{-ny} e^{inx} - e^{ny} e^{-inx}}{2i}.$$
    <2>3. By the triangle inequality:
        $$|\sin(nz)| \le \frac{|e^{-ny} e^{inx}| + |e^{ny} e^{-inx}|}{2} = \frac{e^{-ny} + e^{ny}}{2} = \cosh(ny) \le e^{n|y|} = e^{n|\operatorname{Im}(z)|}.$$
    <2>4. Therefore, the general term is bounded by:
        $$\left| \frac{\sin(nz)}{2^n} \right| \le \frac{e^{n|\operatorname{Im}(z)|}}{2^n} = \left( \frac{e^{|\operatorname{Im}(z)|}}{2} \right)^n.$$

<1>2. Part (b): Uniform Convergence on Compact Disks $|z| \le r$ (for $r < \ln 2$):
    *Proof:*
    <2>1. On the closed disk $\overline{D_r} = \{ z \in \mathbb{C} \mid |z| \le r \}$ where $r < \ln 2$:
        $$|\operatorname{Im}(z)| \le |z| \le r < \ln 2.$$
    <2>2. Thus $e^{|\operatorname{Im}(z)|} \le e^r < e^{\ln 2} = 2$.
    <2>3. Set the ratio $\rho \coloneqq \frac{e^r}{2} < 1$.
    <2>4. For all $z \in \overline{D_r}$ and all $n \ge 1$:
        $$\left| \frac{\sin(nz)}{2^n} \right| \le \rho^n.$$
    <2>5. Since $\rho < 1$, the geometric series $\sum_{n=1}^\infty \rho^n = \frac{\rho}{1 - \rho} < \infty$ converges.
    <2>6. By the **Weierstrass $M$-test**, the series $\sum_{n=1}^\infty \frac{\sin(nz)}{2^n}$ converges **absolutely and uniformly on the closed disk $|z| \le r$** for any $r < \ln 2$.
    <2>7. Since uniform convergence on disks $|z| \le r$ holds for all $r < \ln 2$, the series defines a holomorphic function on the open disk (and strip) $|\operatorname{Im}(z)| < \ln 2$.

<1>3. Part (a): Domain of Convergence and the Strip $|\operatorname{Im}(z)| < \ln 2$:
    *Proof:*
    <2>1. Notice that for $z = -iy$ with $y \to +\infty$ (so $\operatorname{Im}(z) = -y < \ln 2$ is in the lower half-plane):
        $$\sin(n(-iy)) = -i \sinh(ny) = -i \frac{e^{ny} - e^{-ny}}{2}.$$
    <2>2. As $y \to +\infty$, $\frac{|\sin(n(-iy))|}{2^n} \sim \frac{e^{ny}}{2 \cdot 2^n} = \frac{1}{2} (e^y / 2)^n$.
    <2>3. For $y > \ln 2$, $e^y / 2 > 1$, so the terms blow up exponentially as $n \to \infty$.
    <2>4. Thus the series converges if and only if **$|\operatorname{Im}(z)| < \ln 2$** (the horizontal strip of height $2\ln 2$).
    <2>5. On any closed substrip $S_Y = \{ z \in \mathbb{C} \mid |\operatorname{Im}(z)| \le Y \}$ with $0 \le Y < \ln 2$, the Weierstrass $M$-test with $M_n = (e^Y/2)^n$ proves **uniform convergence on the entire strip $S_Y$**.

<1>4. Conclusion:
    The series converges uniformly on any compact subset (and closed substrip) of the strip $|\operatorname{Im}(z)| < \ln 2$, and in particular uniformly on any closed disk $|z| \le r$ with $r < \ln 2$. Q.E.D.
:::
