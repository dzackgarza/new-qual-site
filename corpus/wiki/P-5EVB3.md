---
schema: qual/card@1
id: P-5EVB3
kind: problem
title: Hölder, completeness, a.e. uniform convergence, and density of simple functions
  in $L^\infty$
classification:
  areas:
  - real-analysis
  topics:
  - L∞
  - Norms
  - Density
  - Lp Spaces
relations: []
review: draft
---

::: problem
Let $(X, \mathcal{M}, \mu)$ be a measure space and prove the following properties of $L^ \infty (X, \mathcal{M}, \mu)$:

- If $f, g$ are measurable on $X$ then 
\[
\norm{fg}_1 \leq \norm{f}_1 \norm{g}_{\infty }
.\]

- $\norm{\wait}_{\infty }$ is a norm on $L^{\infty }$ making it a Banach space.

- $\norm{f_n - f}_{\infty } \converges{n\to \infty }\to 0 \iff$ there exists an $E\in \mathcal{M}$ such that $\mu(X\sm E) = 0$ and $f_n \to f$ uniformly on $E$. 

- Simple functions are dense in $L^{\infty }$.
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. $\|fg\|_1 \le \|f\|_1\|g\|_\infty$ for measurable $f, g$.
    Proof: $|fg| \le |f|\|g\|_\infty$ a.e., so $\int|fg| \le \|g\|_\infty\int|f|$ (Hölder with $p = 1$, $q = \infty$).

<1>2. $\|\cdot\|_\infty$ is a norm on $L^\infty$ making it a Banach space.
    <2>1. $\|\cdot\|_\infty$ is a norm (after identifying functions equal a.e.).
        Proof: $\|f\|_\infty = 0 \iff f = 0$ a.e.; $\|\alpha f\|_\infty = |\alpha|\|f\|_\infty$; and $\|f + g\|_\infty \le \|f\|_\infty + \|g\|_\infty$ since $|f + g| \le |f| + |g| \le \|f\|_\infty + \|g\|_\infty$ a.e.
    <2>2. $L^\infty$ is complete: a Cauchy sequence $f_n$ converges in $\|\cdot\|_\infty$.
        Proof: for each $k$ choose $N_k$ with $\|f_n - f_m\|_\infty < 1/k$ for $n, m \ge N_k$; then off a null set $Z$ (the union of the exceptional sets), $f_n$ is uniformly Cauchy, hence converges uniformly to a bounded measurable $f$ on $X \sm Z$; extend $f$ arbitrarily on $Z$; then $\|f_n - f\|_\infty \le 1/k$ for $n \ge N_k$, so $f_n \to f$ in $\|\cdot\|_\infty$.
    <2>3. Q.E.D.
        Proof: <2>1 and <2>2.

<1>3. $\|f_n - f\|_\infty \to 0 \iff$ there exists $E \in \mathcal M$ with $\mu(X \sm E) = 0$ and $f_n \to f$ uniformly on $E$.
    <2>1. ($\Leftarrow$): if $f_n \to f$ uniformly on a co-null set $E$, then $\|f_n - f\|_\infty \le \sup_{x \in E}|f_n(x) - f(x)| \to 0$.
        Proof: the essential sup is computed off null sets.
    <2>2. ($\Rightarrow$): for each $k$, choose $N_k$ with $\|f_n - f\|_\infty < 1/k$ for $n \ge N_k$, and let $Z_k$ be a null set with $|f_n(x) - f(x)| < 1/k$ for $n \ge N_k$, $x \notin Z_k$; set $E = X \sm \bigcup_k Z_k$.
        Proof: $Z = \bigcup_k Z_k$ is null; for $x \in E$ and $n \ge N_k$: $|f_n(x) - f(x)| < 1/k$; given $\eps$, choose $k$ with $1/k < \eps$: uniform convergence on $E$.
    <2>3. Q.E.D.
        Proof: <2>1 and <2>2.

<1>4. Simple functions are dense in $L^\infty$.
    <2>1. Every $f \in L^\infty$ is essentially bounded: $|f| \le M$ a.e. for some $M$.
        Proof: definition of the essential supremum; discard the null set where $|f| > \|f\|_\infty$.
    <2>2. The standard dyadic simple approximations $s_k$ satisfy $\|s_k - f\|_\infty \le 2^{-k}$.
        Proof: on the set where $|f| \le M$, approximate $f$ by the simple function $\sum_j \frac{j}{2^k}\chi_{\{\frac{j}{2^k} \le f < \frac{j+1}{2^k}\}}$-type; the error is at most $2^{-k}$ pointwise; extend by $0$ on the null set.
    <2>3. Q.E.D.
        Proof: <2>1 and <2>2.
:::
