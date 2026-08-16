---
schema: qual/card@1
id: P-A4JGH
kind: problem
title: "Parts: Negating\u2026"
classification:
  areas:
  - prelim
  topics:
  - logic-and-quantifiers
  - uniform-convergence
relations: []
review: draft
---

::: problem
1. Parts:
   1. Negating:
$$\begin{align*}
\neg (f \rightrightarrows f) &\iff \neg (\forall\varepsilon, \exists N(\varepsilon) \suchthat \forall x\in X, \quad & n > N \implies \abs{f_n(x) - f(x)} < \varepsilon)\\
&\iff \neg (\forall\varepsilon, \exists N(\varepsilon) \suchthat \forall x\in X, \quad &\abs{f_n(x) - f(x)} < \varepsilon \text{ or } n \leq N)\\
&\iff \exists \varepsilon \suchthat \forall N, \exists x\in X \suchthat \quad  &n \geq N ~\&~ \abs{f_n(x) - f(x)} \geq \varepsilon  
\end{align*}$$
In words: there is some $\varepsilon$ such that no matter what $N$ you choose, there is at least one point $x$ where $f_n(x)$ is not $\varepsilon\dash$close to $f(x)$ for every $n \geq N$.
   2. Can use any function that converges pointwise but not uniformly. Example on $[0, 1]$:
   $$
   f_n(x) = x^n \implies f_n(x) \to \begin{cases}0 & x\in [0, 1) \\ 1 & x=1 \end{cases} \definedas f(x).
   $$ 
   Proof that $f_n$ converges to $f$ pointwise:
      - Note that $f_n(1) = 1, f_n(0) = 0$, so no issues there.
      - For $x\in (0, 1)$, need to show
      $$
      f_n \to f \iff \forall \varepsilon, \forall x\in X, \exists N(\varepsilon, x) \suchthat n > N \implies \abs{f_n(x) - f(x)} < \varepsilon
      $$
      In this case, $f(x) = 0$, so just need to show $\abs{f_n(x)} < \varepsilon$. To get $x^n < \varepsilon$, just take $n > \frac{\ln\varepsilon}{\ln x}$.
  Proof that $f_n$ does not converge uniformly:
     - Let $\varepsilon = \frac {1}{10}$ and $N$ be arbitrary, so $f_n(x) = x^N$. Then consider $x = \frac{9}{10}^{\frac 1 N}$, so $f_n(x) = \frac{9}{10}$, and we have $\abs{f_n(x)} = \frac 9 {10} \geq \frac 1 {10} = \varepsilon$. 
:::
