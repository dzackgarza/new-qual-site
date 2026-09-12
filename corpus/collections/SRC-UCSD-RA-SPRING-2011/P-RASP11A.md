---
schema: qual/card@1
id: P-RASP11A
kind: problem
title: 'True or false: operator limits, $L^1$ convergence, product compactness, weak $L^2$ subsequences, differentiation of measures'
classification:
  areas:
  - real-analysis
  topics:
  - Bounded Operators
  - L1 Spaces
  - Product Topology
  - Weak Convergence
  - Differentiation of Measures
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 1 of the official UCSD Spring 2011 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Answer True or False.
Support your claim with a short explanation or counterexample.

(a) If $T_n \in L(X, Y)$ is a sequence of bounded linear operators with $X, Y$ Banach spaces, then if $Tx := \lim_n T_n x$ exists in the $Y$ norm for all $x \in X$, one has $T \in L(X, Y)$.

(b) Let $(X, \mathcal{M}, \mu)$ be any measure space.
If $f_n, f \in L^1(d\mu)$ are measurable functions such that $f_n \to f$ $\mu$-a.e. and $\lim_n \int f_n = \int f$, then $f_n \to f$ in $L^1(d\mu)$.

(c) If $\{X_\alpha\}_{\alpha \in A}$ is any collection of compact Hausdorff topological spaces, then $E \subset \prod_{\alpha \in A} X_\alpha$ with the product topology is compact iff it is closed.

(d) If $f_n \in L^2([0, 1])$ converge weakly to $f \in L^2([0, 1])$, then there is a subsequence such that $f_{n_k} \to f$ pointwise a.e. with respect to Lebesgue measure.

(e) If $\mu$ is a positive finite Borel measure on $\mathbb{R}^n$ which is absolutely continuous with respect to Lebesgue measure, and
$$
\lim_{r \to 0} \frac{\mu(B_r(x))}{|B_r(x)|} = 0 \quad \text{for a.e. } x \in \mathbb{R}^n,
$$
then $\mu \equiv 0$.
Here $B_r(x)$ is the ball of radius $r$ at $x$.
:::

::: solution
<1>1. Part (a) is true.
::: proof
For each fixed $x\in X$, the sequence $(T_nx)$ converges in $Y$, hence is bounded. Therefore
\[
\sup_n\|T_nx\|_Y<\infty
\qquad\text{for every }x\in X.
\]
Since $X$ is Banach, the Uniform Boundedness Principle yields
\[
M:=\sup_n\|T_n\|<\infty.
\]
The pointwise limit $T$ is linear, and for every $x\in X$,
\[
\|Tx\|_Y
=\lim_{n\to\infty}\|T_nx\|_Y
\le M\|x\|_X.
\]
Hence $T\in L(X,Y)$.
:::

<1>2. Part (b) is false.
::: proof
Take $X=[0,1]$ with Lebesgue measure, $f\equiv0$, and for $n\ge2$ define
\[
f_n(x)
=n\mathbf1_{(0,1/n)}(x)
-n\mathbf1_{(1/n,2/n)}(x).
\]
For every $x>0$, eventually $2/n<x$, so $f_n(x)=0$ for all sufficiently large $n$; also $f_n(0)=0$. Thus $f_n\to0$ pointwise everywhere. Moreover,
\[
\int_0^1 f_n\,dx=1-1=0=\int_0^1 f\,dx.
\]
However,
\[
\|f_n-f\|_1
=\int_0^1|f_n|\,dx
=2
\]
for every $n$. Hence $f_n$ does not converge to $f$ in $L^1$.
:::

<1>3. Part (c) is true.
::: proof
By Tychonoff's theorem,
\[
K:=\prod_{\alpha\in A}X_\alpha
\]
is compact. Since each $X_\alpha$ is Hausdorff, the product $K$ is Hausdorff.

If $E\subset K$ is closed, then $E$ is compact as a closed subset of the compact space $K$. Conversely, if $E$ is compact, then $E$ is closed because compact subsets of Hausdorff spaces are closed. Thus
\[
\boxed{E\text{ is compact }\Longleftrightarrow E\text{ is closed}.}
\]
:::

<1>4. Part (d) is false.
::: proof
Let $(r_n)$ be the Rademacher functions on $[0,1]$, for example
\[
r_n(x)=\operatorname{sgn}(\sin(2^n\pi x))
\]
away from the dyadic endpoints. They form an orthonormal sequence in $L^2([0,1])$, so
\[
r_n\rightharpoonup0
\]
weakly in $L^2$.

Fix any subsequence $(r_{n_k})$. For each $N$, the set on which
\[
r_{n_k}(x)=1\qquad\text{for all }k\ge N
\]
has measure $0$: for every $m\ge N$, the set where the first $m-N+1$ of these signs are all $1$ has measure $2^{-(m-N+1)}$, and these sets decrease as $m\to\infty$. The same is true with $-1$ in place of $1$.

Since a sequence taking only the values $\pm1$ can converge only if it is eventually constant, the set on which $(r_{n_k}(x))$ converges has measure $0$. Thus no subsequence converges pointwise almost everywhere to $0$.
:::

<1>5. Part (e) is true.
::: proof
Because $\mu\ll m$, the Radon--Nikodym theorem gives a nonnegative
\[
h\in L^1(\mathbb R^n)
\]
such that
\[
d\mu=h\,dm.
\]
The Lebesgue differentiation theorem gives, for almost every $x$,
\[
h(x)
=\lim_{r\downarrow0}\frac1{|B_r(x)|}
\int_{B_r(x)}h(y)\,dy
=\lim_{r\downarrow0}\frac{\mu(B_r(x))}{|B_r(x)|}.
\]
By hypothesis this limit is $0$ almost everywhere, so $h=0$ almost everywhere. Hence
\[
\mu(E)=\int_Eh\,dm=0
\]
for every Borel set $E$, and therefore $\mu\equiv0$.
:::
:::
