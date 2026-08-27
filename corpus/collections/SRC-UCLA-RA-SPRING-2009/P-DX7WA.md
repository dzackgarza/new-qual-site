---
schema: qual/card@1
id: P-DX7WA
kind: problem
title: Jensen's formula and $\sum |a_n|^{-(\lambda+\epsilon)}<\infty$ for entire $f$
  with $|f(z)|\le Ce^{|z|^\lambda}$
classification:
  areas:
  - real-analysis
  topics:
  - Entire Functions
  - Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Let $f(z)$ be an analytic function on the entire complex plane $\mathbb{C}$ and assume $f(0)\ne 0$.
Let $\{a_n\}$ be the zeros of $f$, counted with multiplicity.

a. Let $R>0$ be such that $|f(z)|>0$ on $|z|=R$.
Prove $$\frac{1}{2\pi}\int_0^{2\pi} \log|f(Re^{i\theta})|\,d\theta = \log|f(0)| + \sum_{|a_n|<R} \log\left(\frac{R}{|a_n|}\right).$$

b. Assume $|f(z)|\le Ce^{|z|^\lambda}$ for positive constants $C$ and $\lambda$.
Prove that $$\sum_n \left(\frac{1}{|a_n|}\right)^{\lambda+\epsilon} < \infty$$ for all $\epsilon>0$.
:::

::: {.solution}
**Goal:** For entire $f$ with $f(0) \ne 0$ and zeros $\{a_n\}$ (with multiplicity): (a) prove Jensen's formula $\frac{1}{2\pi}\int_0^{2\pi}\log|f(Re^{i\theta})|\, d\theta = \log|f(0)| + \sum_{|a_n| < R}\log\frac{R}{|a_n|}$; (b) if $|f(z)| \le Ce^{|z|^\lambda}$, prove $\sum_n |a_n|^{-(\lambda+\varepsilon)} < \infty$ for all $\varepsilon > 0$.

<1>1. (a) Assume first that $f$ has no zeros on $|z| = R$, and let $a_1, \dots, a_m$ be the zeros with $|a_k| < R$.
<2>1. Define $F(z) = f(z)\prod_{k=1}^m \frac{R^2 - \bar a_k z}{R(z - a_k)}$; then $F$ is holomorphic and zero-free on $|z| \le R$.
Proof: each factor has a removable singularity at $z = a_k$ (the pole of the denominator cancels the zero of $f$) and no other poles in $|z| \le R$; the factors have no zeros in $|z| \le R$ except the removable points, where $f$'s zero cancels.
<2>2. $|F(z)| = |f(z)|$ for $|z| = R$ and $|F(0)| = |f(0)|\prod_{k=1}^m \frac{R}{|a_k|}$.
Proof: for $|z| = R$, $|R^2 - \bar a_k z| = |R z - R \bar a_k| = R|z - a_k|$ (since $\bar z = R^2/z$), so each factor has modulus 1; at $z = 0$, each factor equals $R^2/(R(-a_k)) = -R/a_k$, with modulus $R/|a_k|$.
<2>3. $\log|F(0)| = \frac{1}{2\pi}\int_0^{2\pi} \log|F(Re^{i\theta})|\, d\theta$.
Proof: $F$ is zero-free and holomorphic on a neighborhood of $\overline{D(0,R)}$, so $\log F$ is holomorphic there; the mean value property for the harmonic function $\log|F| = \Re\log F$ at the center $0$ gives the identity.
<2>4. Jensen's formula (a). Proof: combine <2>2 and <2>3: $\frac{1}{2\pi}\int_0^{2\pi}\log|f(Re^{i\theta})|\,d\theta = \log|F(0)| = \log|f(0)| + \sum_{k=1}^m \log\frac{R}{|a_k|}$.

<1>2. (a) If $f$ has a zero on $|z| = R$, the formula holds by a limiting argument.
Proof: replace $R$ by $R - \varepsilon$; the integrand is continuous in $R$ and the zero-sum is finite for $R' < R$; let $\varepsilon \to 0$.
(Alternatively, the standard proof handles boundary zeros by continuity of both sides.)

<1>3. (b) Setup: apply (a) and the growth bound.
Proof: <1>1 gives $\sum_{|a_n| < R}\log\frac{R}{|a_n|} = \frac{1}{2\pi}\int_0^{2\pi}\log|f(Re^{i\theta})|\,d\theta - \log|f(0)| \le \log C + R^\lambda - \log|f(0)|$.

<1>4. Counting estimate: $N(R) = \#\{n : |a_n| \le R\}$ satisfies $N(R) \le C' R^\lambda$ for $R \ge 1$.
Proof: each zero with $|a_n| \le R/2$ contributes $\ge \log 2$ to the sum in <1>3 (as $\log(R/|a_n|) \ge \log 2$), so $N(R/2)\log 2 \le \log C + R^\lambda - \log|f(0)| \le C'' R^\lambda$; replace $R/2$ by $R$.

<1>5. $\sum_n |a_n|^{-(\lambda+\varepsilon)} < \infty$.
Proof: (Stieltjes integration) with $\alpha = \lambda + \varepsilon > 0$, $\sum_{|a_n| \ge 1} |a_n|^{-\alpha} = \int_{1^-}^\infty t^{-\alpha}\, dN(t) = \qty[t^{-\alpha}N(t)]_1^\infty + \alpha\int_1^\infty t^{-\alpha-1}N(t)\, dt$; by <1>4, $N(t) \le C't^\lambda$, so the integral is $\le \alpha C'\int_1^\infty t^{-\lambda-1-\varepsilon+\lambda}\, dt = \alpha C'\int_1^\infty t^{-1-\varepsilon}\, dt < \infty$ and the boundary term vanishes.

<1>6. Q.E.D. Proof: <1>1–<1>2 prove (a); <1>3–<1>5 prove (b).
:::
