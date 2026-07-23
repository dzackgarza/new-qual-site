---
schema: qual/card@1
id: P-OD7OS
kind: problem
title: "Let $f$ be a non-negative measurable function on $[0, 1]$."
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---
Let $f$ be a non-negative measurable function on $[0, 1]$. 

Show that
\[
\lim _{p \rightarrow \infty}\left(\int_{[0,1]} f(x)^{p} d x\right)^{\frac{1}{p}}=\|f\|_{\infty}.
\]

:::{.concept}
\envlist
- $\norm{f}_\infty \definedas \inf_t {\theset{ t\suchthat m\qty{\theset{x\in \RR^n \suchthat f(x) > t}} = 0 } }$, i.e. this is the lowest upper bound that holds almost everywhere.
:::

:::{.solution}
\envlist

- $\norm{f}_p \leq \norm{f}_\infty$:
  - Note $\abs{f(x)} \leq \norm{f}_\infty$ almost everywhere and taking $p$th powers preserves this inequality.
  - Thus
  \[
  \abs{f(x)} &\leq \norm{f}_\infty \quad\text{a.e. by definition} \\
  \implies 
  \abs{f(x)}^p &\leq \norm{f}_\infty^p \quad\text{for } p\geq 0 \\  
  \implies
  \norm{f}_p^p 
  &= \int_X \abs{f(x)}^p ~dx \\
  &\leq \int_X \norm{f}_\infty^p ~dx  \\
  &= \norm{f}_\infty^p \int_X 1\,dx \\ 
  &= \norm{f}_\infty^p \cdot m(X) \quad\text{since the norm doesn't depend on }x \\
  &= \norm{f}_\infty^p \qquad \text{since } m(X) = 1
  .\]

    - Thus $\norm{f}_p \leq \norm{f}_\infty$ for all $p$ and taking $\lim_{p\to\infty}$ preserves this inequality.

- $\norm{f}_p \geq \norm{f}_\infty$:
  - Fix $\varepsilon > 0$.

  - Define 
  \[
  S_\varepsilon \definedas \theset{x\in \RR^n \suchthat \abs{f(x)} \geq \norm{f}_\infty - \varepsilon}
  .\]

    - Note that $m(S_\eps) > 0$; otherwise if $m(S_\eps) = 0$, then $t\definedas \norm{f}_\infty - \eps < \norm{f}_\eps$.
    But this produces a *smaller* upper bound almost everywhere than $\norm{f}_\eps$, contradicting the definition of $\norm{f}_\eps$ as an infimum over such bounds.
    


  - Then
  \[
  \norm{f}_p^p 
  &= \int_X \abs{f(x)}^p ~dx \\
  &\geq \int_{S_\varepsilon} \abs{f(x)}^p ~dx \quad\text{since } S_\eps \subseteq X \\
  &\geq \int_{S_\varepsilon} \abs{\norm{f}_\infty - \varepsilon}^p ~dx \quad\text{since on } S_\eps, \abs{f} \geq \norm{f}_\infty - \eps \\
  &= \abs{\norm{f}_\infty - \varepsilon}^p \cdot m(S_\varepsilon) \quad\text{since the integrand is independent of }x \\
  & \geq 0 \quad\text{since } m(S_\eps) > 0
  \]
  
  - Taking $p$th roots for $p\geq 1$ preserves the inequality, so
  \[
  \implies \norm{f}_p &\geq \abs{\norm{f}_\infty - \varepsilon} \cdot m(S_\varepsilon)^{\frac 1 p} 
  \converges{p\to\infty}\too \abs{\norm{f}_\infty - \varepsilon} 
  \converges{\varepsilon \to 0}\too \norm{f}_\infty
  \]
  where we've used the fact that above arguments work 

  - Thus $\norm{f}_p \geq \norm{f}_\infty$.


:::


## Spring 2018.4 #real_analysis/qual/completed
