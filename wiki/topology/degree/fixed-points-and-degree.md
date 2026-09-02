---
order: 240
problems:
  topics:
  - Degree
  - Fixed Points
  - Fixed Point Theorems
  - Fixed Point Theory
  - Borsuk-Ulam Theorem
  - Antipodal Map
  - Lefschetz Fixed Point Theorem
  - Invariance of Domain
---

# Fixed Points and Degree Theory

For $n\geq 1$ and $f:S^n\to S^n$, the degree is defined by
\[
f_*[S^n]=\deg(f)[S^n]\in H_n(S^n;\ZZ).
\]
It is homotopy invariant, and self-maps of $S^n$ are homotopic exactly when they have the same degree.

The main theorems form a chain. [[T-S2OLJ|Brouwer]] gives fixed points for self-maps of the ball. [[T-BX4LD|Lefschetz]] detects fixed points by the alternating trace on homology. [[T-WNOWY|Borsuk-Ulam]] forces an antipodal pair to have the same image under every map $S^n \to \RR^n$. [[T-VQTR6|Hairy Ball]] rules out non-vanishing tangent vector fields on even-dimensional spheres.

## The degree

:::{.fact title="Useful properties of the degree of a map between spheres"}
\envlist

- The degree of a constant map is 0.

- $f\homotopic g \iff \deg f = \deg g$, since this implies $f_* = g_*$.

- If $f$ is a homotopy equivalence, $\abs{\deg f} = 1$.
  - This is because $f\homotopic g \implies H_*(f) = H_*(g)$.

- $\deg\id_{S^n} = 1$

- $\text{deg} (f\circ g) = \deg f \cdot \deg g$

- $\deg(H_{x_i}) = -1$ for $H_{x_i}$ the reflection across the hyperplane $x_i = 0$, i.e. 
\[
H_{x_i}: \RR^{n+1} &\to \RR^{n+1} 
\tv{x_1, \cdots, x_i, \cdots, x_{n+1}} 
\mapsto
\tv{x_1, \cdots, - x_i, \cdots, x_{n+1}} 
.\]

- The antipodal map on $S^n\subset \RR^{n+1}$ is the composition of $n+1$ hyperplane reflections, so $\deg\alpha = (-1)^{n+1}$.
  - As a consequence, if $\deg f$ is even then $f$ is not homotopic to the antipodal map.

:::

## Exercises

[[E-EYILL]]

[[E-ZXKDY]]

## Brouwer and Lefschetz

[[T-S2OLJ]]

Brouwer is the special case of Lefschetz for $X = B^n$. Since $B^n$ is contractible, $H_0(B^n) = \QQ$ and all higher homology vanishes, so the Lefschetz number is $\Lambda_f = \Tr(f_* \mid H_0) = 1 \neq 0$ for any self-map. The general statement:

[[T-BX4LD]]

The Lefschetz number $\Lambda_f$ is computed from the induced maps on homology. If $\Lambda_f \neq 0$, the map $f$ must have a fixed point. The converse fails in general: $\Lambda_f=0$ by itself does not imply that $f$ is homotopic to a fixed-point-free map.

:::{.proof}
*[Proof of Brouwer via Lefschetz]* Suppose $f: B^n \to B^n$ has no fixed points. Define $g: B^n \to S^{n-1}$ by sending $x$ to the intersection of the ray from $f(x)$ through $x$ with $\partial B^n = S^{n-1}$. Then $g$ restricted to $S^{n-1}$ is a retraction $r: S^{n-1} \to S^{n-1}$, and $r$ is homotopic to the identity via the straight-line homotopy $H(x,t) = \frac{x - tf(x)}{\|x - tf(x)\|}$, so $\deg r = \deg \id = 1$. On the other hand, $r$ factors as $S^{n-1} \xrightarrow{\iota} B^n \xrightarrow{g} S^{n-1}$ where $\iota$ is the inclusion. Since $B^n$ is contractible, $g_*$ is the zero map on $H_{n-1}$, so $r_* = g_* \circ \iota_* = 0$ on $H_{n-1}(S^{n-1})$. But $\deg r$ is exactly the scalar by which $r_*$ acts on $H_{n-1}(S^{n-1}) \cong \ZZ$, so $\deg r = 0$. Contradiction.
:::

## Borsuk-Ulam

[[T-WNOWY]]

Borsuk-Ulam says that antipodal symmetry forces agreement somewhere. For $n=1$, set $g(x)=f(x)-f(-x)$; then $g(-x)=-g(x)$, so the intermediate value theorem gives some $x$ with $g(x)=0$, i.e. $f(x)=f(-x)$. The general case follows from degree arguments.

Applications include:

- **Ham sandwich theorem**: $n$ measurable sets in $\RR^n$ can be simultaneously bisected by a single hyperplane. Apply Borsuk-Ulam to the map that sends a direction on $S^{n-1}$ to the $n$-tuple of measures on each side of the perpendicular hyperplane.
- **Brouwer as corollary**: The Brouwer fixed-point theorem also follows from Borsuk-Ulam via the degree argument above: if $f: B^n \to B^n$ has no fixed points, the retraction $r: S^{n-1} \to S^{n-1}$ constructed from $f$ has degree $1$ (homotopic to the identity) and degree $0$ (factors through the contractible $B^n$), a contradiction.

## Hairy Ball
 
[[T-VQTR6]]
 
The Hairy Ball theorem is a consequence of degree theory: suppose $S^k$ admits a non-vanishing continuous tangent vector field $v(x)$. Because $v(x)$ is tangent to $S^k$, $x \cdot v(x) = 0$. One can define a homotopy $H: S^k \times [0, 1] \to S^k$ from the identity map to the antipodal map by rotating along great circles:
\[
H(x, t) = x \cos(\pi t) + \frac{v(x)}{\|v(x)\|} \sin(\pi t).
\]
Because $x \perp v(x)$, $\|H(x, t)\|^2 = \cos^2(\pi t) + \sin^2(\pi t) = 1$, so $H(x, t) \in S^k$ for all $t$.
At $t=0$, $H(x, 0) = x = \operatorname{id}_{S^k}(x)$.
At $t=1$, $H(x, 1) = -x = -\operatorname{id}_{S^k}(x)$.
Homotopy invariance of degree implies $\deg(\operatorname{id}_{S^k}) = \deg(-\operatorname{id}_{S^k})$. But $\deg(\operatorname{id}_{S^k}) = 1$ and $\deg(-\operatorname{id}_{S^k}) = (-1)^{k+1}$.
Thus $1 = (-1)^{k+1}$, which is impossible when $k = 2n$ is even ($1 \neq -1$). Hence no non-vanishing continuous vector field exists on even-dimensional spheres $S^{2n}$.

Every odd-dimensional sphere $S^{2n+1}\subset\CC^{n+1}$ admits a non-vanishing tangent vector field, for example $v(z)=iz$. The spheres $S^1$, $S^3$, and $S^7$ are exceptional in the stronger sense that they are parallelizable.
