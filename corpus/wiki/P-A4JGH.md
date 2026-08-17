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
solved: true
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

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** 
(a) State the precise definition of uniform convergence of a sequence of functions $f_n: X \to \mathbb{R}$ to $f: X \to \mathbb{R}$, and find its logical negation.
(b) Give an example of a sequence of functions on $[0,1]$ that converges pointwise but not uniformly, and prove both assertions.

<1>1. Definition of uniform convergence and its negation:
    Proof:
    <2>1. A sequence $(f_n)_{n=1}^\infty$ converges uniformly to $f$ on $X$ if:
        $$\forall \varepsilon > 0, \, \exists N \in \mathbb{N} \text{ such that } \forall n \ge N, \, \forall x \in X, \, |f_n(x) - f(x)| < \varepsilon.$$
    <2>2. The logical negation ($f_n \not\to f$ uniformly) is:
        $$\exists \varepsilon_0 > 0 \text{ such that } \forall N \in \mathbb{N}, \, \exists n \ge N, \, \exists x \in X \text{ such that } |f_n(x) - f(x)| \ge \varepsilon_0.$$

<1>2. Consider the sequence $f_n(x) = x^n$ on $X = [0, 1]$. The pointwise limit is $f(x) = \begin{cases} 0 & x \in [0, 1), \\ 1 & x = 1. \end{cases}$
    Proof:
    <2>1. For $x = 1$, $f_n(1) = 1^n = 1 \to 1 = f(1)$.
    <2>2. For $x = 0$, $f_n(0) = 0^n = 0 \to 0 = f(0)$.
    <2>3. For each fixed $x \in (0, 1)$, since $0 < x < 1$, $\lim_{n \to \infty} x^n = 0 = f(x)$ (given $\varepsilon > 0$, choosing $N > \frac{\ln(\varepsilon)}{\ln(x)}$ guarantees $x^n < \varepsilon$ for all $n \ge N$).
    <2>4. Hence $f_n \to f$ pointwise on $[0,1]$.

<1>3. The convergence $f_n \to f$ is not uniform on $[0, 1]$.
    Proof:
    <2>1. Choose $\varepsilon_0 = 1/2$.
    <2>2. For any $N \in \mathbb{N}$, choose $n = N$ and $x_N = (1/2)^{1/N} \in [0, 1)$.
    <2>3. Then $f(x_N) = 0$, and:
        $$|f_N(x_N) - f(x_N)| = |((1/2)^{1/N})^N - 0| = \frac{1}{2} \ge \varepsilon_0.$$
    <2>4. By <1>1, $f_n$ does not converge uniformly to $f$ on $[0, 1]$. Q.E.D.
:::
