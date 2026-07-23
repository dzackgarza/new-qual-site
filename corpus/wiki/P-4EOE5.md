---
schema: qual/card@1
id: P-4EOE5
kind: problem
title: "- $\\star$: Show that for $E\\subseteq \\RR^n$, TFAE:"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---
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

