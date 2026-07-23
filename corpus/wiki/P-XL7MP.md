---
schema: qual/card@1
id: P-XL7MP
kind: problem
title: "a."
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---
:::{.problem title="?"}
\envlist

a.
Show that
\[
L^2([0, 1]) \subseteq L^1([0, 1]) \qtext{and} \ell^1(\ZZ) \subseteq \ell^2(\ZZ)
.\]

b.
For $f\in L^1([0, 1])$ define
\[
\hat{f}(n) \definedas \int _0^1 f(x) e^{-2\pi i n x} \, dx
.\]
Prove that if $f\in L^1([0, 1])$ and $\theset{\hat f(n)} \in \ell^1(\ZZ)$ then
\[
S_N f(x) \definedas \sum_{\abs n \leq N} \hat f (n) e^{2 \pi i n x}
.\]
converges uniformly on $[0, 1]$ to a continuous function $g$ such that $g = f$ almost everywhere.

> Hint: One approach is to argue that if $f\in L^1([0, 1])$ with $\theset{\hat f (n)} \in \ell^1(\ZZ)$ then $f\in L^2([0, 1])$.

:::

:::{.concept}
From Neil:

1. $\hat{f}$ in $\ell^1$ ensures that $S_N$ converges uniformly to something, call it $g$. 
2. $\hat{f} \in\ell^1$ Implies $\hat{f}\in \ell^2$ which (by characterization of an o.n.b.) implies $f$ is in $L^2$ (Parseval) and (again by characterization of an o.n.b.) that $S_N$ converges to $f$ in $L^2$ (and hence a subsequence converges to f a.e.)
3. By uniqueness of limits $f=g$.

Other stuff:

- For $e_n(x) \definedas e^{2\pi i n x}$, the set $\theset{e_n}$ is an orthonormal basis for $L^2([0, 1])$.
- For any orthonormal sequence in a Hilbert space, we have Bessel's inequality:
  \[
  \sum_{k=1}^{\infty}\left|\left\langle x, e_{k}\right\rangle\right|^{2} \leq\|x\|^{2}
  .\]
- When $\theset{e_n}$ is a basis, the above is an *equality* (Parseval)
- Arguing uniform convergence: since $\theset{\hat f(n)} \in \ell^1(\ZZ)$, we should be able to apply the $M$ test.

:::

:::{.solution title="From Neil"}
Claim: if $f\in L^1[0, 1]$ and $\hat f\in \ell^1(\ZZ)$, then $S_Nf \to f$ uniformly.

- Since $\hat f\in \ell^1(\ZZ)$, we have $S_Nf\to g$ uniformly for some continuous $g$ by the $M\dash$test.
- Now consider $\hat g$.
  We have
  \[
  \hat g(n) = \int_0^1 \sum_m \qty{\hat f(m)e_m(x)}e_{-n}(x) \dx = \hat{f}(n)
  ,\]
  using that $\int_0^1 e_n(x)\dx = \chi_{n=0}$.

- We'll now show $f-g= 0$ a.e. by mollifying against an approximate identity $\varphi\in L^1$, setting 
\[
\varphi_\eps(x) \da \eps\inv\varphi(\eps\inv x) \in L^1[0, 1]
.\]

- A computation:
\[
\hat{f\convolve \varphi_\eps}(n) 
&= \hat{f}\cdot \hat{\varphi_\eps}(n) \\
&= \hat{g}\cdot \hat{\varphi_\eps}(n) \\
&= \hat{g\convolve \varphi_\eps}(n) 
,\]
so 
\[
\hat{(f-g)\convolve \varphi_\eps} = 0 \quad \forall n \implies (f-g)\convolve \varphi_\eps \equiv 0
,\]
using that $(f-g)\convolve \varphi_\eps\in L^2$ and $\ts{e_n}$ for a complete orthonormal basis of $L^2$.

- Now use that $(f-g)\convolve \varphi_\eps \to (f-g)$ in $L^1$ and $(f-g)\convolve \varphi_\eps \equiv 0$ to conclude $f-g = 0$ a.e.


:::

:::{.solution title="Part 1"}
\envlist

:::{.claim}
$\ell^1(\ZZ) \subseteq \ell^2(\ZZ)$.
:::

:::{.proof title="?"}
\envlist

- Set $\vector c = \theset{c_k \suchthat k\in \ZZ} \in \ell^1(\ZZ)$.
- It suffices to show that if $\sum_{k\in \ZZ} \abs{c_k} < \infty$ then $\sum_{k\in \ZZ} \abs {c_k}^2 < \infty$.
- Let $S = \theset{c_k \suchthat \abs{c_k} \leq 1}$, then $c_k \in S \implies \abs{c_k}^2 \leq \abs{c_k}$
- Claim: $S^c$ can only contain finitely many elements, all of which are finite.
  - If not, either $S^c \definedas \theset{c_j}_{j=1}^\infty$ is infinite with every $\abs{c_j} > 1$, which forces $$\sum_{c_k\in S^c} \abs{c_k} = \sum_{j=1}^\infty \abs{c_j} > \sum_{j=1}^\infty 1 = \infty.$$
  - If any $c_j = \infty$, then $\sum_{k\in \ZZ} \abs{c_k} \geq c_j = \infty$.
- So $S^c$ is a finite set of finite integers, let $N = \max \theset{\abs{c_j}^2 \suchthat c_j \in S^c} < \infty$.
- Rewrite the sum
\[
\sum_{k\in \ZZ} \abs{c_k}^2 
&= \sum_{c_k\in S} \abs{c_k}^2 + \sum_{c_k \in S^c} \abs{c_k}^2 \\
&\leq \sum_{c_k\in S} \abs{c_k} + \sum_{c_k \in S^c} \abs{c_k}^2 \\
&\leq \sum_{k\in \ZZ} \abs{c_k} + \sum_{c_k \in S^c} \abs{c_k}^2 \quad\text{since the $\abs{c_k}$ are all positive} \\
&= \norm{\vector c}_{\ell^1} + \sum_{c_k \in S^c} \abs{c_k}^2 \\
&\leq \norm{\vector c}_{\ell^1} + \abs{S^c}\cdot N \\
&< \infty
.\]

:::

:::{.claim}
$L^2([0, 1]) \subseteq L^1([0, 1])$.
:::

:::{.proof title="?"}
\envlist

- It suffices to show that $\int \abs{f}^2 < \infty \implies \int \abs{f} < \infty$.
- Define $S = \theset{x\in [0, 1] \suchthat \abs{f(x)} \leq 1}$, then $x\in S^c \implies \abs{f(x)}^2 \geq \abs{f(x)}$.

- Break up the integral:
\[
\int_\RR \abs f 
&= \int_S \abs f + \int_{S^c} \abs f \\
&\leq \int_S \abs{f} + \int_{S^c} \abs{f}^2 \\
&\leq \int_S \abs{f} + \norm{f}_2 \\
&\leq \sup_{x\in S}\theset{\abs{f(x)}} \cdot \mu(S) + \norm{f}_2 \\
&= 1 \cdot \mu(S) + \norm{f}_2 \quad\text{by definition of } S\\
&\leq 1 \cdot \mu([0, 1]) + \norm{f}_2 \quad\text{since } S\subseteq [0, 1] \\
&= 1 + \norm{f}_2 \\
&< \infty
.\]


:::

> Note: this proof shows $L^2(X) \subseteq L^1(X)$ whenever $\mu(X) < \infty$.
:::

:::{.solution title="Part 2"}
\envlist

- First, $S_Nf$ converges in $\mch$ to something, say $g \da \lim_{n\to\infty} S_n f$, since
\[
\norm{g - S_Nf} = \norm{\sum_{\abs n \geq N} \hat f (n) e_n(x) } \leq \sum_{\abs n \geq N } \abs{\hat f(n)} \convergesto{N\to\infty}0
,\]
where the last term is the tail of a convergent sum since $\ts{\hat f(n)} \in \ell^1$.
- This also shows that $S_N\to g$ uniformly.
- $g$ is continuous, as the uniform limit of continuous functions.
- Showing that $g = f$ a.e.: it suffices to show that $S_N$ converges to $f$ in $L^p$ for some $p$, since this will provide a subsequence that converges to $f$ a.e..

- Claim: $\hat{f}\in \ell^1 \subseteq \ell^2$ implies that $f \in L^2$.
  This follows from Parseval:
\[
\infty > \norm{\hat f}_{\ell^2}^2
= \sum_{n\in \ZZ} \abs{\hat f(n)}^2
= \int_0^1 \abs{f(z)}^2 \dz 
= \norm{f}_{L^2}^2
.\]
- Claim: $S_N\to f$ in $L^2$.
  - This follows from the fact that $\ts{e_n}_{n\in \ZZ}$ is a complete orthonormal basis, so $f = \sum \inner{f}{e_n}e_n$ uniquely, recognizing $\hat{f}(n) = \inner{f}{e_n}$, and writing
  \[
  f = \sum_{n} \inner{f}{e_n}e_n = \sum_n \hat{f}(n) e_n \da \lim_{N\to\infty }S_N f
  .\]
- So a subsequence $\ts{S_{N_k}}_{k\geq 0}$ converges to $f$ a.e..
  Since $S_N\to g$ a.e., $f=g$ a.e. by uniqueness of limits.
:::

