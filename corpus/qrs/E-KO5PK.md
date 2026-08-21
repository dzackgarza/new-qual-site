---
schema: qual/card@1
id: E-KO5PK
kind: exercise
title: Translation is continuous in $L^p$ for uniformly continuous functions
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - Uniform Continuity
relations: []
review: draft
solved: true
---

::: exercise
- Prove continuity in $L^p$: If $f$ is uniformly continuous then for all $p$, $$\norm{\tau_h f - f}_p \converges{h\to 0}\to 0.$$
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** If $f$ is uniformly continuous (and $f \in L^p(\RR^n)$, which the statement presupposes), then $\norm{\tau_h f - f}_p \to 0$ as $h \to 0$ for $1 \leq p < \infty$.

<1>1. The claim holds for continuous functions with compact support.
<2>1. $|\tau_h \varphi(x) - \varphi(x)| \leq \omega(|h|)$ where $\omega$ is the modulus of continuity, with $\omega(|h|) \to 0$.
Proof: uniform continuity of the compactly supported continuous $\varphi$.
<2>2. $\norm{\tau_h \varphi - \varphi}_p \leq \omega(|h|)\, \mu(\supp \varphi \cup (\supp \varphi + h))^{1/p} \to 0$.
Proof: the difference vanishes outside the (bounded) union of the two supports, whose measure is bounded independent of small $h$; <2>1 bounds the integrand pointwise.
<1>2. A uniformly continuous function in $L^p$ is bounded.
Proof: choose $\delta > 0$ with $|f(x) - f(y)| \leq 1$ for $|x - y| \leq \delta$; then on each cube $Q$ of side $\delta$, $\sup_Q |f| \leq |f(x_Q)| + 1$ for any point $x_Q \in Q$, so $\|f\|_\infty^{p} \leq \|f\|_p^p/\delta^n + 1$ (integrating $|f(x_Q)|^p$ over the cube and summing the finite contribution) — hence $f$ is essentially bounded.
<1>3. The claim holds for a uniformly continuous $f \in L^p$ on a bounded cube $Q$.
<2>1. Restrict to $Q$; for $|h| < \frac{1}{2}\dist(x, \partial Q)$ the translated function stays inside an enlarged cube.
Proof: work on a slightly enlarged cube so translations are well defined, then pass to $Q$; or convolve with a bump function.
<2>2. Given $\eps > 0$, pick a compactly supported continuous $\varphi$ with $\norm{f - \varphi}_{L^p(Q)} < \eps/3$.
Proof: continuous compactly supported functions are dense in $L^p(Q)$.
<2>3. For small $h$: $\norm{\tau_h \varphi - \varphi}_p < \eps/3$ by <1>1, and $\norm{\tau_h f - \tau_h \varphi}_p = \norm{f - \varphi}_p < \eps/3$ by translation invariance of the integral.
Proof: density and <1>1. <2>4. Q.E.D. Proof: triangle inequality: $\norm{\tau_h f - f}_p \leq \norm{\tau_h f - \tau_h \varphi}_p + \norm{\tau_h \varphi - \varphi}_p + \norm{\varphi - f}_p < \eps$ for all small $h$, uniformly in the translation.
<1>4. The claim holds on all of $\RR^n$.
Proof: with $f$ bounded (<1>2) and $|f|^p$ integrable, split $\RR^n$ into the cube $Q_R = [-R, R]^n$ and its complement; on $Q_R$ apply <1>3, and on the complement $\int_{\RR^n \setminus Q_R} |\tau_h f - f|^p \leq 2^p \int_{\RR^n \setminus Q_R} (|\tau_h f|^p + |f|^p) = 2^{p+1}\int_{\RR^n \setminus Q_R} |f|^p \to 0$ as $R \to \infty$, using translation invariance and integrability of $|f|^p$.
<1>5. Q.E.D. Proof: <1>3 and <1>4 combine to give $\norm{\tau_h f - f}_p \to 0$.
:::
