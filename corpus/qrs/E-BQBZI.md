---
schema: qual/card@1
id: E-BQBZI
kind: exercise
title: $\|f\|_p\to\|f\|_\infty$ as $p\to\infty$ on finite measure spaces
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - L∞
  - Limits
relations: []
review: draft
solved: true
---

::: exercise
- $\star$: Show that if $X\subseteq \RR$ with $\mu(X) < \infty$ then
\[  
\norm{f}_p \converges{p\to\infty}\to \norm{f}_\infty
.\]
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** For $X \subseteq \mathbb{R}$ with $\mu(X) < \infty$ and $f \in L^p(X)$ for some $p_0 \in [1, \infty)$, show $\|f\|_p \to \|f\|_\infty$ as $p \to \infty$ (both sides allowed to be $+\infty$).

<1>1. $\limsup_{p \to \infty} \|f\|_p \leq \|f\|_\infty$.
    <2>1. If $\|f\|_\infty < \infty$: $\|f\|_p \leq \|f\|_\infty \, \mu(X)^{1/p}$ for all $p \geq p_0$.
        Proof: $|f| \leq \|f\|_\infty$ a.e., so $\int_X |f|^p \leq \|f\|_\infty^p \mu(X)$; raise to the $1/p$.
    <2>2. Taking the limsup: $\limsup_p \|f\|_p \leq \|f\|_\infty \lim_p \mu(X)^{1/p} = \|f\|_\infty$, since $\mu(X) < \infty$.
        Proof: $\mu(X) > 0$ (else $f = 0$ a.e. and both sides are $0$); $\mu(X)^{1/p} \to 1$. If $\|f\|_\infty = \infty$ the inequality is trivial.
<1>2. $\liminf_{p \to \infty} \|f\|_p \geq \|f\|_\infty$.
    <2>1. For every $0 < \alpha < \|f\|_\infty$: $\|f\|_p \geq \alpha \, \mu\theset{|f| \geq \alpha}^{1/p}$.
        Proof: on $A_\alpha := \theset{|f| \geq \alpha}$, $|f| \geq \alpha$, so $\int_X |f|^p \geq \int_{A_\alpha} \alpha^p = \alpha^p \mu(A_\alpha)$.
    <2>2. $\mu(A_\alpha) > 0$ for every $\alpha < \|f\|_\infty$.
        Proof: otherwise $|f| \leq \alpha$ a.e., forcing $\|f\|_\infty \leq \alpha$, contradiction.
    <2>3. Hence $\liminf_p \|f\|_p \geq \alpha$ for every $\alpha < \|f\|_\infty$.
        Proof: by <2>1, $\|f\|_p \geq \alpha \mu(A_\alpha)^{1/p}$ with $\mu(A_\alpha)^{1/p} \to 1$ (a fixed positive constant raised to $1/p$), so $\liminf_p \|f\|_p \geq \alpha$.
    <2>4. Q.E.D.
        Proof: if $\|f\|_\infty < \infty$, let $\alpha \to \|f\|_\infty$ in <2>3; if $\|f\|_\infty = \infty$, <2>3 holds for all $\alpha$, so $\liminf_p \|f\|_p = \infty$.
<1>3. Q.E.D.
    Proof: <1>1 and <1>2 give $\|f\|_\infty \leq \liminf \|f\|_p \leq \limsup \|f\|_p \leq \|f\|_\infty$, so $\lim_p \|f\|_p = \|f\|_\infty$.
:::
