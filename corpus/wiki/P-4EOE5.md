---
schema: qual/card@1
id: P-4EOE5
kind: problem
title: Lebesgue regularity, invariance of the integral, convolution, and $L^p$ norms
classification:
  areas:
  - real-analysis
  topics:
  - measure-theory
  - integrals
relations: []
review: draft
solved: true
---

::: problem
- $\star$: Show that for $E\subseteq \RR^n$, TFAE: 
  1. $E$ is measurable
  2. $E = H\union Z$ here $H$ is $F_\sigma$ and $Z$ is null
  3. $E = V\setminus Z'$ where $V\in G_\delta$ and $Z'$ is null.
- $\star$: Show that if $E\subseteq \RR^n$ is measurable then $m(E) = \sup \theset{ m(K) \suchthat K\subset E\text{ compact}}$ iff for all $\eps> 0$ there exists a compact $K\subseteq E$ such that $m(K) \geq m(E) - \eps$.
- $\star$: Show that cylinder functions are measurable, i.e. if $f$ is measurable on $\RR^s$, then $F(x, y) \definedas f(x)$ is measurable on $\RR^s\cross \RR^t$ for any $t$.
- $\star$: Prove that the Lebesgue integral is translation invariant, i.e. if $\tau_h(x) = x+h$ then $\int \tau_h f = \int f$.
- $\star$: Prove that the Lebesgue integral is dilation invariant, i.e. if $f_\delta(x) = {f({x\over \delta}) \over \delta^n}$ then $\int f_\delta = \int f$.
- $\star$: Prove continuity in $L^1$, i.e.
  \[
  f \in L^{1} \Longrightarrow \lim _{h \rightarrow 0} \int|f(x+h)-f(x)|=0
  .\]
- $\star$: Show that $$f,g \in L^1 \implies f\ast g \in L^1 \qtext{and} \norm{f\ast g}_1 \leq \norm{f}_1 \norm{g}_1.$$

- $\star$: Show that if $X\subseteq \RR$ with $\mu(X) < \infty$ then
\[  
\norm{f}_p \converges{p\to\infty}\to \norm{f}_\infty
.\]
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. TFAE: (1) $E$ is measurable; (2) $E = H \union Z$ with $H \in F_\sigma$ and $Z$ null; (3) $E = V \sm Z'$ with $V \in G_\delta$ and $Z'$ null.
    <2>1. (1) $\implies$ (2): take closed $F_k \subseteq E$ with $m(E \sm F_k) < 1/k$ (inner regularity), set $H = \bigcup_k F_k$ (an $F_\sigma$) and $Z = E \sm H$; then $m(Z) \le m(E \sm F_k) < 1/k$ for all $k$, so $Z$ is null.
        Proof: $H \subseteq E$, and $E = H \union Z$ with $H \cap Z = \emptyset$.
    <2>2. (1) $\implies$ (3): take open $G_k \supseteq E$ with $m(G_k \sm E) < 1/k$ (outer regularity), set $V = \bigcap_k G_k$ (a $G_\delta$) and $Z' = V \sm E$; then $m(Z') \le m(G_k \sm E) < 1/k$ for all $k$.
        Proof: $E \subseteq V$ and $V \sm E = Z'$ null.
    <2>3. (2) $\implies$ (1) and (3) $\implies$ (1): $F_\sigma$ and $G_\delta$ sets are Borel, hence measurable, and adding or removing null sets preserves measurability.
        Proof: measurability is closed under countable unions, intersections, and symmetric differences with null sets.
    <2>4. Q.E.D.
        Proof: <2>1–<2>3.

<1>2. $m(E) = \sup\{m(K) : K \subseteq E \text{ compact}\}$ iff for every $\eps > 0$ there is a compact $K \subseteq E$ with $m(K) \ge m(E) - \eps$.
    Proof: this is the definition of the supremum: the condition says exactly that no number below $m(E)$ is an upper bound for $\{m(K) : K \subseteq E \text{ compact}\}$.

<1>3. Cylinder functions are measurable: if $f$ is measurable on $\RR^s$, then $F(x,y) = f(x)$ is measurable on $\RR^s \cross \RR^t$.
    Proof: $F = f \circ \pi_s$ where $\pi_s(x,y) = x$ is continuous; preimages of Borel sets under continuous maps are Borel.

<1>4. Translation and dilation invariance: $\int \tau_h f = \int f$ ($\tau_h f(x) = f(x+h)$) and $\int f_\delta = \int f$ ($f_\delta(x) = \delta^{-n}f(x/\delta)$).
    Proof: for indicators this is $m(E + h) = m(E)$ and $m(\delta E) = \delta^n m(E)$; extend to simple functions, then non-negative measurable $f$ by monotone convergence, then $L^1$ by positive/negative parts.

<1>5. Continuity in $L^1$: $f \in L^1 \implies \lim_{h\to 0}\int|f(x+h) - f(x)|\,dx = 0$.
    Proof: indicators of measurable sets of finite measure (regularity), then simple functions, then density + $\eps/3$.

<1>6. $f, g \in L^1 \implies f \ast g \in L^1$ with $\|f \ast g\|_1 \le \|f\|_1\|g\|_1$.
    Proof: Tonelli: $\int|f\ast g| \le \iint |f(x-y)||g(y)|\,dy\,dx = \|f\|_1\|g\|_1$.

<1>7. If $\mu(X) < \infty$: $\|f\|_p \to \|f\|_\infty$ as $p \to \infty$.
    Proof: $\|f\|_p \le \|f\|_\infty\mu(X)^{1/p}$ and $\|f\|_p \ge M\mu\{|f|>M\}^{1/p} \to M$ for $M < \|f\|_\infty$; sandwich.
:::
