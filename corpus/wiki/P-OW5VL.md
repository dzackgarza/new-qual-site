---
schema: qual/card@1
id: P-OW5VL
kind: problem
title: "Prove that if $f: [0, 1] \\to \\RR$ is continuous then"
classification:
  areas:
  - real-analysis
  topics:
  - convergence-of-integrals
  - continuity
  - stone-weierstrass
relations: []
review: draft
---
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
