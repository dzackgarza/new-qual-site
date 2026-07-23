---
schema: qual/card@1
id: P-I5APR
kind: problem
title: "Let $I$ be an index set and $\\alpha: I \\to (0, \\infty)$."
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---
Let $I$ be an index set and $\alpha: I \to (0, \infty)$.

a.
Show that
\[
\sum_{i \in I} a(i):=\sup _{\substack{ J \subset I \\ J \text { finite }}} \sum_{i \in J} a(i)<\infty \implies I \text{ is countable.}
\]

b.
Suppose $I = \QQ$ and $\sum_{q \in \mathbb{Q}} a(q)<\infty$.
Define
\[
f(x):=\sum_{\substack{q \in \mathbb{Q}\\ q \leq x}} a(q).
\]
Show that $f$ is continuous at $x \iff x\not\in \QQ$.

:::{.concept}
\envlist

- Can always filter sets $X$ with a function $X\to \RR$.
- Countable union of countable sets is still countable.
- Continuity: $\lim_{y\to x} f(y) = f(x)$ from either side.
- Trick: pick enumerations of countable sets and reindex sums
:::

:::{.solution}
\envlist

:::{.proof title="of a"}
\envlist

- Set $S \definedas \sum_{i\in I} \alpha(i)$, we will show that $S<\infty \implies I$ is countable.
- Write 
\[
I = \Union_{n\geq 0} S_n, &&
S_n \definedas \theset{i\in I \suchthat \alpha(i) \geq {1\over n}}
.\]
  - Note that $S_n \subseteq S$ for all $n$, so $\sum_{i\in I}\alpha(i) \geq \sum_{i\in S_n} \alpha(i)$ for all $n$.
  - It suffices to show that $S_n$ is countable, since $I$ is a countable union of $S_n$.
- There is an inequality
\[  
\infty 
&> S \da \sum_{i\in I} \alpha(i) \\
&\geq \sum_{i\in S_n} \alpha(i) \\
&\geq \sum_{i\in S_n} {1\over n} \\
&= {1\over n} \sum_{i\in S_n} 1 \\
&= \qty{1\over n} \# S_n \\ \\
\implies \infty &> n S \geq \# S_n
.\]
:::

:::{.proof title="of b"}
\envlist

- We'll prove something more general: let $Q = \ts{q_k}$ be countable and $\ts{\alpha_k \da \alpha(q_k)}$ be summable, and define
\[
f(x) \da \sum_{q_k\leq x} \alpha_k
.\]
  
  - $f$ is always discontinuous precisely on the countable set $Q$ and continuous on $\RR\sm Q$.

  - $f$ is always left-continuous, is right-continuous at $x\in\RR\sm Q$, and *not* right-continuous at $x\in Q$

  - $f$ has jump discontinuities at every $q_m$, where the jump is precisely $\alpha_m$.

- This follows from computing the left and right limits:
\[
f(x^+) &= \lim_{h\to 0} \sum_{q_k \leq x+h} \alpha_k = \sum_{q_k\leq x} \alpha_k = \sum_{q_k < x} \alpha_k + \sum_{q_k = x} \alpha_k \\
f(x^-) &= \lim_{h\to 0} \sum_{q_k \leq x-h} \alpha_k = \sum_{q_k < x} \alpha_k
,\]
  where we've used that $\ts{q_k \leq x} = \ts{q_k < x} \disjoint \ts{x}$ in the first equality.

- Then if $x=q_m$ for some $m$,
\[
f(x^+) &= f(q_m^+) = \sum_{q_k < q_m} \alpha_k + \alpha_m \\
f(x^-) &= f(a_m^-) = \sum_{q_k< q_m} \alpha_k
,\]
which clearly differ if $\alpha_m \neq 0$.

- Taking $x\not\in Q$, we have $\ts{q_k \leq x} = \ts{q_k < x}$, since $\ts{q_k=x} = \emptyset$, so
\[
f(x^+) &= \sum_{q_k\leq x} \alpha_k = \sum_{q_k < x} \alpha_k \\
f(x^-) &= \sum_{q_k< x} \alpha_k
,\]
  so the limits agree.

- To recover the result in the problem, let $\QQ = \ts{q_k}$ be any enumeration of the rationals.

:::

:::






# General Analysis

## Spring 2020 # 1 $\done$

Prove that if $f: [0, 1] \to \RR$ is continuous then
\[
\lim_{k\to\infty} \int_0^1 kx^{k-1} f(x) \,dx = f(1)
.\]

:::{.concept}
\envlist

- DCT
- Weierstrass Approximation Theorem
  - If $f: [a, b] \to \RR$ is continuous, then for every $\eps>0$ there exists a polynomial $p_\eps(x)$ such that $\norm{f - p_\eps}_\infty < \eps$.
:::

:::{.solution}
\envlist

- Suppose $p$ is a polynomial, then integrate by parts:
\[
\lim_{k\to\infty} \int_0^1 kx^{k-1} p(x) \, dx
&= \lim_{k\to\infty} \int_0^1 \qty{ \dd{}{x}x^k } p(x) \, dx \\
&= \lim_{k\to\infty} \left[ x^k p(x) \evalfrom_0^1 - \int_0^1 x^k \qty{\dd{p}{x}(x) } \, dx \right] \quad\text{IBP}\\
&= p(1) - \lim_{k\to\infty} \int_0^1 x^k \qty{\dd{p}{x}(x) } \, dx
,\]

- Thus it suffices to show that
\[
\lim_{k\to\infty} \int_0^1 x^k \qty{\dd{p}{x} (x) } \, dx = 0
.\]

- Integrating by parts a second time yields
\[
\lim_{k\to\infty} 
\int_0^1 x^k \qty{\dd{p}{x}(x) } \, dx
&= \lim_{k\to\infty} 
{x^{k+1} \over k+1} \dd{p}{x}(x) \evalfrom_0^1 - \int_0^1 {x^{k+1} \over k+1} \qty{ \dd{^2 p}{x^2}(x)} \, dx \\
&= \lim_{k\to\infty} {p'(1) \over k+1} - \lim_{k\to\infty} \int_0^1 {x^{k+1} \over k+1} \qty{ \dd{^2p}{x^2}(x)} \, dx \\
&= - \lim_{k\to\infty} \int_0^1 {x^{k+1} \over k+1} \qty{ \dd{^2p}{x^2}(x)} \, dx \\
&= - \int_0^1 \lim_{k\to\infty}  {x^{k+1} \over k+1} \qty{ \dd{^2p}{x^2}(x)} \, dx \quad\text{by DCT} \\
&= - \int_0^1 0 \qty{ \dd{^2p}{x^2}(x)} \, dx \\
&= 0
.\]

  - The DCT can be applied here because polynomials are smooth and $[0, 1]$ is compact, so $\dd{^2 p}{x^2}$ is bounded on $[0, 1]$ by some constant $M$ and 
  \[ \int_0^1 \abs{x^k \dd{^2 p}{x^2} (x)} \leq \int_0^1 1\cdot M = M < \infty.\]

- So the result holds when $f$ is a polynomial.

- Now use the Weierstrass approximation theorem: 
  - If $f: [a, b] \to \RR$ is continuous, then for every $\eps>0$ there exists a polynomial $p_\eps(x)$ such that $\norm{f - p_\eps}_\infty < \eps$.

- Thus 
\[
\abs{ \int_0^1 kx^{k-1} p_\eps(x)\,dx - \int_0^1 kx^{k-1}f(x)\,dx  } 
&= \abs{ \int_0^1 kx^{k-1} \qty{p_\eps(x) - f(x)} \,dx  } \\
&\leq \abs{ \int_0^1 kx^{k-1} \norm{p_\eps-f}_\infty \,dx  } \\
&= \norm{p_\eps-f}_\infty \cdot \abs{ \int_0^1 kx^{k-1} \,dx  } \\
&= \norm{p_\eps-f}_\infty \cdot x^k \evalfrom_0^1 \\
&= \norm{p_\eps-f}_\infty \\ \\
&\converges{\eps\to 0}\to 0
\]

  and the integrals are equal. 

- By the first argument, $$\int_0^1 kx^{k-1} p_\eps(x) \,dx = p_\eps(1) \text{ for each } \eps$$ 
- Since uniform convergence implies pointwise convergence, $p_\eps(1) \converges{\eps\to 0}\to f(1)$.

:::
