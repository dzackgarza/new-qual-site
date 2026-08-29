---
order: 5
---

# Advice and Essentials 

- General advice: try swapping the orders of limits, sums, integrals, etc.
- Good set / bad set: for measure theory or integrals, try to break a set up into "good" and "bad" subsets, and put bounds on each piece separately.
- Limits:
  - Take the $\limsup$ or $\liminf$, which always exist, and aim for an inequality like
  \[  
  c \leq \liminf a_n \leq \limsup a_n \leq c
  .\]
  - $\lim f_n = \limsup f_n = \liminf f_n$ iff the limit exists, so to show some $g$ is a limit, show
  \[  
\limsup f_n \leq g \leq \liminf f_n \qquad (\implies g = \lim f) 
  .\]
  - A  limit does *not* exist if $\liminf a_n > \limsup a_n$.

- Sequences and Series
  - If $f_n$ has a global maximum (computed using $f_n'$ and the first derivative test) $M_n \to 0$, then $f_n \to 0$ uniformly.
  - For a fixed $x$, if $f = \sum f_n$ converges *uniformly* on some $B_r(x)$ and each $f_n$ is continuous at $x$, then $f$ is also continuous at $x$ .

- Equalities
  - Split into upper and lower bounds:
  \[  
  a=b \iff a\leq b \text{ and }  a\geq b
  .\]
  - Use an epsilon of room:
  \[  
  \qty{ \forall \epsilon, \,\,a < b + \eps} \implies a\leq b 
  .\]
  - Showing something is zero:
  \[  
  \qty{ \forall \epsilon, \,\, \norm{a} < \eps} \implies a = 0
  .\]

- Continuity / differentiability: 
  - Show it holds on $[-M, M]$ for all $M$ to get it to hold on $\RR$.
  - In higher dimensions: intersect with a ball $B_R(\vector 0)\subset \RR^n$ about zero.

- Simplifications:
  - To show something for a measurable set, show it for bounded/compact/elementary sets and use approximations in measure.
  - To show something for an arbitrary function, try various dense classes of functions: 
    continuous, bounded, compactly supported, simple, indicator functions, etc and use approximations in norm.
  - Replace $\eps\to 0$ with an arbitrary countable sequence ($x_n \to 0$)
    - Note: this is not always helpful, since you now have to predicate over all such sequences.

- Integrals
  - Calculus techniques: Taylor series, IVT, MVT, etc.
  - Break up $\RR^n = \theset{\abs{x} \leq 1} \coprod \theset{\abs{x} > 1}$.

    - Or break integration region into disjoint annuli.
    - Or break integration region into disjoint annuli: 
    \[
    \int_\RR f = \sum_{k\geq 0}\int_{2^k}^{2^{k+1}} d
    .\]

  - For pairs of functions $f, g$: break up into $\theset{f>g} \disjoint \theset{f=g} \disjoint \theset{f< g}$.
  - Tail estimates!
  - Most of what works for integrals will work for sums.

- Measure theory:

  - Always consider bounded sets, and if $E$ is unbounded write $E = \Union_{n\geq 0} \qty{ B_{n}(0) \intersect E}$ and use countable subadditivity or continuity of measure.

  - $F_\sigma$ sets are Borel, so establish something for Borel sets and use this to extend it to Lebesgue.

  - $s = \inf\theset{x\in X} \implies$ for every $\varepsilon$ there is an $x\in X$ such that $x \leq s + \varepsilon$ or $x\in [s, s+\eps]$.

- Useful facts about continuous compactly supported ($C_c^0(\RR)$) functions:
  - Uniformly continuous
  - Bounded almost everywhere

- Pass to a subsequence!

- Add and subtract a thing. 
  Eg, $\norm{T_nx_n - Tx} = \norm{T_nx_n - Tx_n + Tx_n - Tx}$.

- $(a_k) \in \ell^2(\ZZ)$ is much weaker than $(a_k) \in \ell^1(\ZZ)$.
- Littlewood's principles:
  - Measurable sets are almost finite unions of intervals,
  - Measurable functions are almost continuous,
  - Pointwise convergent sequences of measurable functions are almost uniformly convergent.

- $L^p$ spaces shrink as $p\nearrow \infty$ (by Holder).

- Nesting of $L^p$ spaces: let $p< q$
  - For $\mu(X) = \infty$: no general containments.
  - For $\mu(X) < \infty: p < p+1 < \cdots \implies L^p \supseteq L^{p+1} \supseteq \cdots$.
    Why? Holder.
  - For $X=\ZZ: L^p \subseteq L^{p+1} \subseteq \cdots$
- Failing to be in $L^p$: singularities away from infinity, or long tails.

- Every Borel is $F_\sigma$ up to a null set.

- Proving uniform convergence: use the $M\dash$test.

- A problem using absolute continuity will often be used to imply bounded variation (which allow using FTC)

- If two functions are in conjugate $L^p$ spaces, try Holder.

- $\mu(X) = \norm{\id}_{L^1(X)} = \int_X 1 \dmu$


# The Absolute Essentials

[[PR-IGVTV]]

[[T-ERNLN]]

:::{.proof}
\envlist
- Follows from an $\varepsilon/3$ argument: 
  \[  
  \abs{F(x) - F(y} \leq 
  \abs{F(x) - F_N(x)} + \abs{F_N(x) - F_N(y)} + \abs{F_N(y) - F(y)} 
  \leq \eps \to 0
  .\]

  - The first and last $\eps/3$ come from uniform convergence of $F_N\to F$.
  - The middle $\eps/3$ comes from continuity of each $F_N$.
- So just need to choose $N$ large enough and $\delta$ small enough to make all 3 $\varepsilon$ bounds hold.

:::

[[PR-L7LNZ]]

[[PR-6WMSR]]

[[PR-O2XFF]]

[[PR-PIVFR]]

:::{.proof title="of Borel characterization"}
For every $\frac 1 n$ there exists a closed set $K_{n} \subset E$ such that $m(E\setminus K_{n}) \leq \frac 1 n$.
Take $K = \union K_{n}$, wlog $K_{n} \nearrow K$ so $m(K) = \lim m(K_{n}) = m(E)$.
Take $N\da E\setminus K$, then $m(N) = 0$.

:::

[[T-IIKSW]]

:::{.proof title="that measurable sets can be approximated"}
\envlist

- (1): Take $\theset{Q_{i}} \covers E$ and set $O = \union Q_{i}$.
- (2): Since $E^c$ is measurable, produce $O\supset E^c$ with $m(O\setminus E^c) < \eps$.
  - Set $F = O^c$, so $F$ is closed.
  - Then $F\subset E$ by taking complements of $O\supset E^c$
  - $E\setminus F = O\setminus E^c$ and taking measures yields $m(E\setminus F) < \eps$
- (3): Pick $F\subset E$ with $m(E\setminus F) < \eps/2$.
  - Set $K_{n} = F\intersect \DD_{n}$, a ball of radius $n$ about $0$.
  - Then $E\setminus K_{n} \searrow E\setminus F$
  - Since $m(E) < \infty$, there is an $N$ such that $n\geq N \implies m(E\setminus K_{n}) < \eps$.

:::

# Quintessential Qual Problems

[[E-OMK54]]
[[PR-6NDTF]]

:::{.proof title="of measurable slices"}
\envlist

$\implies$:

- Let $f$ be measurable on $\RR^n$.
- Then the cylinders $F(x, y) = f(x)$ and $G(x, y) = f(y)$ are both measurable on $\RR^{n+1}$.
- Write $\mathcal{A} = \theset{G \leq F} \intersect \theset{G \geq 0}$; both are measurable.

$\impliedby$:

- Let $A$ be measurable in $\RR^{n+1}$.
- Define $A_x = \theset{y\in \RR \mid (x, y) \in \mathcal{A}}$, then $m(A_x) = f(x)$.
- By the corollary, $A_x$ is measurable set, $x \mapsto A_x$ is a measurable function, and $m(A) = \int f(x) ~dx$.
- Then explicitly, $f(x) = \chi_{A}$, which makes $f$ a measurable function.

:::

