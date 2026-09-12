---
order: 5
---

# Estimates and approximation

- Monotone convergence, dominated convergence, and Fubini–Tonelli give hypotheses for interchanging limits, sums, and integrals.
- Splitting a measurable set into a region with a uniform bound and a region of small measure gives separate estimates for the integral on each region.
- Limits:
  - The extended-real $\limsup$ and $\liminf$ determine convergence through bounds such as
  \[  
  c \leq \liminf a_n \leq \limsup a_n \leq c
  .\]
  - Pointwise convergence to $g$ follows from
  \[  
\limsup f_n \leq g \leq \liminf f_n \qquad (\implies g = \lim_n f_n)
  .\]
  - A sequence has no extended-real limit if $\liminf a_n < \limsup a_n$.

- Sequences and Series
  - If $M_n=\sup_x|f_n(x)|\to0$, then $f_n\to0$ uniformly. For differentiable functions on a compact interval, extrema occur at endpoints or critical points.
  - For a fixed $x$, if $f = \sum f_n$ converges *uniformly* on some $B_r(x)$ and each $f_n$ is continuous at $x$, then $f$ is also continuous at $x$ .

- Equalities
  - Equality is equivalent to matching upper and lower bounds:
  \[  
  a=b \iff a\leq b \text{ and }  a\geq b
  .\]
  - For real $a,b$,
  \[  
  \qty{ \forall \epsilon>0, \,\,a < b + \eps} \implies a\leq b
  .\]
  - In a normed space,
  \[  
  \qty{ \forall \epsilon>0, \,\, \norm{a} < \eps} \implies a = 0
  .\]

- Continuity / differentiability: 
  - Continuity or differentiability on every interval $(-M,M)$ implies the same property on $\RR$.
  - In $\RR^n$, the balls $B_R(0)$ give the corresponding exhaustion.

- Approximation:
  - Regularity of Lebesgue measure gives approximation of finite-measure sets by compact sets and finite unions of boxes, with error measured by symmetric difference.
  - Simple functions are dense in $L^p$ for $1\leq p<\infty$. For Lebesgue measure on $\RR^n$, continuous compactly supported functions are also dense in these spaces.
  - A limit as $t\to0$ is equivalent to convergence along every sequence of nonzero arguments $t_n\to0$.

- Integrals
  - Taylor's theorem gives local estimates for integrands near a singularity or a zero.
  - The decomposition $\RR^n = \theset{\abs{x} \leq 1} \coprod \theset{\abs{x} > 1}$ separates local integrability from integrability at infinity.

    - For nonnegative or integrable $f$, disjoint dyadic annuli give
    \[
    \int_{|x|>1} f(x)\,dx = \sum_{k\geq 0}\int_{2^k<|x|\leq2^{k+1}} f(x)\,dx
    .\]

  - For real-valued measurable $f,g$, the sets $\{f>g\}$, $\{f=g\}$, and $\{f<g\}$ separate the signs of $f-g$.
  - If $f\in L^1(\RR^n)$, then $\int_{|x|>R}|f|\to0$ as $R\to\infty$.
  - Integration against counting measure gives the corresponding statements for sums.

- Measure theory:

  - The bounded exhaustion $E\cap B_n(0)\nearrow E$ gives $\mu(E)=\lim_n\mu(E\cap B_n(0))$ for measurable $E\subseteq\RR^n$.

  - Every Lebesgue measurable set in $\RR^n$ differs from an $F_\sigma$ set by a null set. Properties invariant under null modifications therefore extend from Borel sets to Lebesgue measurable sets.

  - If $X\subseteq\RR$ is nonempty and bounded below, then $s=\inf X$ satisfies: for every $\varepsilon>0$, some $x\in X$ lies in $[s,s+\varepsilon)$.

- Continuous compactly supported ($C_c^0(\RR)$) functions are:
  - Uniformly continuous
  - Bounded

- Convergence in measure implies almost-everywhere convergence along a subsequence.

- Adding and subtracting $Tx_n$ separates operator convergence from vector convergence:
  $\norm{T_nx_n-Tx}\leq\norm{(T_n-T)x_n}+\norm{T(x_n-x)}$.

- $\ell^1(\ZZ)\subsetneq\ell^2(\ZZ)$; for example, $(1/(1+|k|))_{k\in\ZZ}$ belongs to $\ell^2$ but not $\ell^1$.
- Littlewood's principles:
  - Measurable sets are almost finite unions of intervals,
  - Measurable functions are almost continuous,
  - Pointwise convergent sequences of measurable functions are almost uniformly convergent.

- Nesting of $L^p$ spaces: let $p< q$
  - For $\mu(X) = \infty$: no general containments.
  - For $\mu(X) < \infty: p < p+1 < \cdots \implies L^p \supseteq L^{p+1} \supseteq \cdots$.
    This follows from Hölder's inequality.
  - For $X=\ZZ: L^p \subseteq L^{p+1} \subseteq \cdots$
- Failing to be in $L^p$: singularities away from infinity, or long tails.

- The Weierstrass $M$-test gives uniform convergence of $\sum f_n$ when $|f_n|\leq M_n$ and $\sum M_n<\infty$.

- An absolutely continuous function on $[a,b]$ has bounded variation and satisfies $f(x)-f(a)=\int_a^x f'(t)\,dt$. Bounded variation alone does not imply this identity.

- Hölder's inequality gives $\|fg\|_1\leq\|f\|_p\|g\|_q$ for conjugate exponents.

- $\mu(X) = \norm{1}_{L^1(X)} = \int_X 1 \dmu$, with value $+\infty$ allowed.


## Continuity and measure approximation

[[PR-IGVTV]]

[[T-ERNLN]]

:::{.proof}
\envlist
- Follows from an $\varepsilon/3$ argument: 
  \[  
  \abs{F(x) - F(y)} \leq 
  \abs{F(x) - F_N(x)} + \abs{F_N(x) - F_N(y)} + \abs{F_N(y) - F(y)} 
  \leq \eps \to 0
  .\]

  - The first and last $\eps/3$ come from uniform convergence of $F_N\to F$.
  - The middle $\eps/3$ comes from continuity of each $F_N$.
- Uniform convergence fixes $N$ independently of $x,y$; continuity of $F_N$ at $x$ then supplies $\delta$.

:::

[[PR-L7LNZ]]

[[PR-6WMSR]]

[[PR-O2XFF]]

[[PR-PIVFR]]

:::{.proof title="of Borel characterization"}
For every $\frac 1 n$ there exists a closed set $K_{n} \subset E$ such that $m(E\setminus K_{n}) \leq \frac 1 n$.
Set $K=\bigcup_nK_n$. Then $K$ is $F_\sigma$ and $m(E\setminus K)\leq1/n$ for every $n$, so $E\setminus K$ is null.

:::

[[T-IIKSW]]

:::{.proof title="that measurable sets can be approximated"}
\envlist

- (1): Outer regularity gives an open set $O\supseteq E$ with $m(O\setminus E)<\eps$.
- (2): Since $E^c$ is measurable, produce $O\supset E^c$ with $m(O\setminus E^c) < \eps$.
  - Set $F = O^c$, so $F$ is closed.
  - Then $F\subset E$ by taking complements of $O\supset E^c$
  - $E\setminus F = O\setminus E^c$ and taking measures yields $m(E\setminus F) < \eps$
- (3): Pick $F\subset E$ with $m(E\setminus F) < \eps/2$.
  - Set $K_n=F\cap\overline{B_n(0)}$, which is compact.
  - Then $E\setminus K_{n} \searrow E\setminus F$
  - Since $m(E) < \infty$, there is an $N$ such that $n\geq N \implies m(E\setminus K_{n}) < \eps$.

:::

## Subgraphs and measurable slices

[[E-OMK54]]
[[PR-6NDTF]]

:::{.proof title="Subgraph characterization of measurability"}
Let $f:\RR^n\to[0,\infty]$ and $A=\{(x,y):0\leq y\leq f(x)\}$.
If $f$ is Lebesgue measurable, the functions $F(x,y)=f(x)$ and $G(x,y)=y$ are Lebesgue measurable. Thus $A=\{G\leq F\}\cap\{G\geq0\}$ is measurable.

Conversely, suppose $A$ is Lebesgue measurable. Each vertical section $A_x$ is an interval of length $f(x)$. The measurable-slices theorem gives a measurable function equal to $m(A_x)=f(x)$ for almost every $x$. Completeness of Lebesgue measure then implies that $f$ is measurable. Tonelli's theorem gives $m(A)=\int_{\RR^n}f(x)\,dx$.

:::
