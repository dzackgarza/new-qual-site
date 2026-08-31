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

Degree theory assigns an integer to a map $f: S^n \to S^n$ that measures "how many times $f$ wraps the sphere around itself." This integer is a homotopy invariant — two maps with the same degree can be continuously deformed into each other — and it controls the existence of fixed points: if the degree is wrong, every map in the homotopy class must have a fixed point.

The main theorems form a chain. Brouwer says every self-map of the ball has a fixed point. Lefschetz generalizes this to arbitrary compact spaces via the trace on homology. Borsuk-Ulam says every map $S^n \to \RR^n$ identifies some antipodal pair. The Hairy Ball theorem — that even-dimensional spheres admit no non-vanishing vector field — is a corollary of Borsuk-Ulam.

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

The Lefschetz number $\Lambda_f$ is computed from the induced maps on homology. If $\Lambda_f \neq 0$, the map $f$ must have a fixed point — a nonzero trace means the map "wraps" homology around itself in a way that cannot be achieved without a fixed point. The converse holds for triangulable spaces: if $\Lambda_f = 0$, a small perturbation can remove all fixed points.

:::{.proof}
*[Proof of Brouwer via Lefschetz]* Suppose $f: B^n \to B^n$ has no fixed points. Define $g: B^n \to S^{n-1}$ by sending $x$ to the intersection of the ray from $f(x)$ through $x$ with $\partial B^n = S^{n-1}$. Then $g$ restricted to $S^{n-1}$ is a retraction $r: S^{n-1} \to S^{n-1}$, and $r$ is homotopic to the identity via the straight-line homotopy. But $\deg r = \deg \id = 1$, while any retraction $S^{n-1} \to S^{n-1}$ factors through the contractible $B^n$, giving $\deg r = 0$. Contradiction.
:::

## Borsuk-Ulam

[[T-WNOWY]]

Borsuk-Ulam says that antipodal symmetry forces agreement somewhere. The $n=1$ case is the intermediate value theorem: a continuous function $f: S^1 \to \RR$ that satisfies $f(-x) = f(x)$ must hit the same value at some pair of antipodal points. The general case follows from degree arguments.

Applications include:

- **Ham sandwich theorem**: $n$ measurable sets in $\RR^n$ can be simultaneously bisected by a single hyperplane. Apply Borsuk-Ulam to the map that sends a direction on $S^{n-1}$ to the $n$-tuple of measures on each side of the perpendicular hyperplane.
- **Brouwer as corollary**: If $f: B^n \to B^n$ had no fixed points, define $g: S^{n-1} \to S^{n-1}$ by $g(x) = \frac{x - f(x)}{\|x - f(x)\|}$. Then $g$ is odd ($g(-x) = -g(x)$), contradicting Borsuk-Ulam for $n \geq 1$.

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

The odd-dimensional spheres ($S^1, S^3, S^7$) *do* admit non-vanishing vector fields — $S^1$ has the unit tangent field, and $S^3 \subset \HH$ admits a family of them via quaternionic multiplication. This is specific to the Hopf structure.

:::{.remark}
The Hairy Ball theorem is often stated as "you can't comb a hairy ball flat without a cowlick." The mathematical content is stronger: there is no continuous choice of tangent direction at every point. The "cowlick" is a zero of the vector field, and the theorem says it must exist.
:::
