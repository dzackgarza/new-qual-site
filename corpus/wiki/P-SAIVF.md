---
schema: qual/card@1
id: P-SAIVF
kind: problem
title: A function in $L^2([0,1])$ orthogonal to every polynomial vanishes a.e.
classification:
  areas:
  - real-analysis
  topics:
  - stone-weierstrass
  - density
  - l2
relations: []
review: draft
solved: true
---
Let $f\in L^2([0, 1])$ and suppose
$$
\int _{[0,1]} f(x) x^{n} d x=0 \text { for all integers } n \geq 0.
$$
Show that $f = 0$ almost everywhere.

:::{.concept}
\envlist
- Weierstrass Approximation: A continuous function on a compact set can be uniformly approximated by polynomials.
- $C^1([0, 1])$ is dense in $L^2([0, 1])$
- Polynomials are dense in $L^p(X, \mathcal{M}, \mu)$ for any $X\subseteq \RR^n$ compact and $\mu$ a finite measure, for all $1\leq p < \infty$.
  - Use Weierstrass Approximation, then uniform convergence implies $L^p(\mu)$ convergence by DCT.
:::

:::{.solution}
\envlist

:::{.proof title="using Fourier transforms"}
\envlist

- Fix $k \in \ZZ$.
- Since $e^{2\pi i k x}$ is continuous on the compact interval $[0, 1]$, it is uniformly continuous.
- Thus there is a sequence of polynomials $P_\ell$ such that 
$$
P_{\ell, k} \converges{\ell\to\infty}\too e^{2\pi i k x} \text{ uniformly on } [0,1]
.$$

- Note applying linearity to the assumption $\int f(x) \, x^n$, we have
$$
\int f(x) x^n \,dx = 0 ~\forall n \implies \int f(x) p(x) \,dx = 0 
$$
  for any polynomial $p(x)$, and in particular for $P_{\ell, k}(x)$ for every $\ell$ and every $k$.

- But then  
\[
\inner{f}{e_k} 
&= \int_0^1 f(x) e^{-2\pi i k x} ~dx \\
&= \int_0^1 f(x) \lim_{\ell \to \infty} P_\ell(x) \\
&= \lim_{\ell \to \infty}  \int_0^1 f(x) P_\ell(x) \quad\quad \text{by uniform convergence on a compact interval} \\
&= \lim_{\ell \to \infty} 0 \quad\text{by assumption}\\
&= 0 \quad \forall k\in \ZZ
,\]
 so $f$ is orthogonal to every $e_k$. 

- Thus $f\in S^\perp \definedas \spanof_\CC\theset{e_k}_{k\in \ZZ}^\perp \subseteq L^2([0, 1])$, but since this is a basis, $S$ is dense and thus $S^\perp = \theset{0}$ in $L^2([0, 1])$.

- Thus $f\equiv 0$ in $L^2([0, 1])$, which implies that $f$ is zero almost everywhere.

:::

:::{.proof title="Alternative"}
\envlist

- By density of polynomials, for $f\in L^2([0, 1])$ choose $p_\eps(x)$ such that $\norm{f - p_\eps} < \eps$ by Weierstrass approximation.
- Then on one hand,
\[
\norm{f(f-p_\eps)}_1 
&= \norm{f^2}_1 - \norm{f\cdot p_\eps}_1 \\
&= \norm{f^2}_1 - 0 \quad\text{by assumption} \\
&= \norm{f}_2^2
.\]

  - Where we've used that $\norm{f^2}_1 = \int \abs{f^2} = \int \abs{f}^2 = \norm{f}_2^2$.

- On the other hand
\[
\norm{f(f-p_\eps)} 
&\leq \norm{f}_1 \norm{f-p_\eps}_\infty \quad\text{by Holder} \\
&\leq \eps \norm{f}_1  \\
&\leq \eps \norm{f}_2 \sqrt{m(X)} \\ 
&= \eps \norm{f}_2 \quad\text{since } m(X)= 1
.\]
  - Where we've used that $\norm{fg}_1 = \int \abs{fg} = \int \abs{f}\abs{g} \leq \int \norm{f}_\infty \abs{g} = \norm{f}_\infty \norm{g}_1$.

- Combining these,
\[
\norm{f}_2^2 \leq \norm{f}_2 \eps \implies \norm{f}_2 < \eps \to 0,
.\]
  so $\norm{f}_2 = 0$, which implies $f=0$ almost everywhere.


:::

:::
