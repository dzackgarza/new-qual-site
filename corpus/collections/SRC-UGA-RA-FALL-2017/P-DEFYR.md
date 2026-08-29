---
schema: qual/card@1
id: P-DEFYR
kind: problem
title: $nx(1-x)^n\to 0$ pointwise but not uniformly, and $\int n(1-x)^n\sin x\to 0$
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Functions
  - Uniform Convergence
  - Convergence of Integrals
relations: []
review: draft
---

Let
\[
f_{n}(x) = n x(1-x)^{n}, \quad n \in \NN.
\]

a. 
Show that $f_n \to 0$ pointwise but not uniformly on $[0, 1]$.

b. 
Show that
\[
\lim _{n \to \infty} \int _{0}^{1} n(1-x)^{n} \sin x \, dx = 0
\]

> Hint for (a): Consider the maximum of $f_n$.

:::{.solution}
\envlist
:::{.concept}
\envlist
- $\sum f_n < \infty \iff \sup f_n \to 0$.
- Negating uniform convergence: $f_n\not\to f$ uniformly iff $\exists \eps$ such that $\forall N(\eps)$ there exists an $x_N$ such that $\abs{f(x_N) - f(x)} > \eps$.
- Exponential inequality: $1+y \leq e^y$ for all $y\in \RR$.
:::

a.

    $f_n\to 0$ pointwise:

    - Finding the maximum: can check that $\dd{f_n}{x} = x(1-x)^{n-1} \qty{1 + (n^2-1)x}$
    - This has critical points $x=0, 1, {-1 \over n^2 + 1}$, and the latter is a global max on $[0, 1]$.
    - Set $x_n \definedas {-1 \over n^2 + 1}$
    - Compute
    \[  
    \lim f_n(x_n) = \lim_{n\to \infty } {-n \over n^2 + 1} \qty{1 + x_n}^n = 0\cdot 1 = 0
    .\]
    - So $\sup f_n \to 0$, forcing $f_n \to 0$ pointwise.

    The convergence is not uniform:

    - Let $x_n = \frac 1 n$ and $\varepsilon > e\inv$, then
    \[
    \norm{nx(1-x)^n - 0}_\infty
    &\geq \abs{nx_n (1-x_n)^n} \\
    &= \abs{\left( 1 - \frac 1 n\right)^n} \\
    &> e^{-1} \\
    &> \varepsilon
    .\]

      - Here we've used that $(1 + {x\over n})^n \leq e^x$ for all $x\in \RR$ and all $n$.
      - Follows from $1+y \leq e^y$ applied to $y = x/n$.

    - Thus $\norm{f_n - 0}_\infty = \norm{f_n}_\infty > e^{-1} > 0$.

    b. ?

:::{.remark}
Possible to use part a with $\sin(x) \leq x$ on $[0, \pi/2]$?
:::
#todo 

- Noting that $\sin(x) \leq 1$, we have
\[
\abs{\int_0^1  n(1-x)^{n} \sin(x)} 
&\leq \int_0^1  \abs{n(1-x)^n \sin(x)} \\
&\leq \int_0^1  \abs{n (1-x)^n}  \\
&= n\int_0^1 (1-x)^n \\
&= -\frac{n(1-x)^{n+1}}{n+1} \\
&\converges{n\to\infty}\longrightarrow 0
.\]
:::
