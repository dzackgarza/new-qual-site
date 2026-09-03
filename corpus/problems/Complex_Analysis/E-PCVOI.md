---
schema: qual/card@1
id: E-PCVOI
kind: problem
title: $\frac{\pi^2}{\sin^2(\pi z)}=\sum_{n\in\mathbb{Z}}\frac{1}{(z-n)^2}$ by matching
  singularities, principal parts, and decay in a period strip
classification:
  areas:
  - complex-analysis
  topics:
  - Meromorphic Functions
  - Poles
  - Principal Parts
  - Identity Theorem
  - Trigonometry
relations: []
review: draft
---

:::{.problem}
Define
\[
f(z) &= {\pi^2 \over \sin^2 \qty{\pi z} } \\
g(z) &= \sum_{n\in \ZZ} {1\over (z-n)^2}
.\]

a. Show that $f$ and $g$ have the same singularities in $\CC$.
b. Show that $f$ and $g$ have the same singular parts at each of their singularities.
c. Show that $f, g$ each have period one and approach zero uniformly on $0\leq x \leq 1$ as $\abs{y}\to \infty$.
d. Conclude that $f = g$.


:::

:::{.solution}
**Part 1**:
This is clear: $\sin^2(\pi z) = 0 \iff z = k$ for $k\in \ZZ$, and this is a pole of order 2 for $f$.
Every $k\in \ZZ$ is visibly an order 2 pole of $g$.

**Part 2**:
By periodicity, it suffices to consider the singularity at $z_0 = 0$.
Expanding $\sin(\pi z) = \pi z - {1\over 3!}(\pi z)^3 + {1\over 5!} (\pi z)^5 + \cdots$ and considering $\sin(\pi z)^2$ shows that $z=0$ is a pole of order 2.
So $z^2f(z)$ has a removable singularity at $z=0$, and can be expanded:
\[
z^2f(z) 
&= \qty{\pi z\over \sin(\pi z)}^2 \\
&= (\pi z)^2 \qty{ (\pi z) \inv + {1\over 3!}(\pi z) + {7\over 360} (\pi z^3) +  \cdots}^2 \\
&= (\pi z)^2 \qty{ (\pi z)^{-2} + \bigo(1)  } \\
&= 1 + \bigo(z^2) \\
\implies f(z) &= z^{-2} + \bigo(1)
,\]
so the singular part of $f$ at $z=0$ is $z^{-2}$.
This coincides with the ${1\over z^2}$ term in $g$.
The remaining principal parts at $z=k$ are ${1\over (z-k)^2},$ using the fact that $f(z+1) = f(z)$, so $f(k) = f(0)$ and the Laurent expansions are gotten by substituting $z-k$ in for $z$ everywhere.

**Part 3**:
Periodicity is clear for $f$.
For $g$,
\[
g(z+1) = \sum_{k\in \ZZ} ((z-1)-k)^{-2} = \sum_{k'\in \ZZ} (z-k)^{-2}
,\]
where $k' \da k+1$, and the equality is true since both sums run over all of $\ZZ$.

For convergence: take $z=it$, then for $f$
\[
f(it) \sim \csc^2(i\pi t) &\sim \qty{ e^{i\pi (it) } - e^{-i\pi (it)}}^{-2} \\
&= \qty{e^{-\pi t} - e^{\pi t}}^{-2} \\ 
&\leq {1\over e^{-\pi t} + e^{\pi t} } \\
&\sim e^{-\pi t} \\
&\to 0
,\]
using the reverse triangle inequality and that the $e^{-\pi t}$ term in the denominator is negligible for large $t$.

For $g$, 
\[
g(it) 
&\sim t^{-2} + \sum_{k\geq 1} (t^2 + k^2)\inv \\
&\leq t^{-2} + \sum_{1\leq k \leq N}(t^2 + k^2)\inv + \sum_{k\geq N}(t^2 + k^2)\inv \\
&\leq t^{-2} + \sum_{1\leq k \leq N}(t\cdot k^2)\inv + \sum_{k\geq N}(k^2)\inv \\
&\leq t^{-2} + t\inv \sum_{1\leq k \leq N}(k^2)\inv + \sum_{k\geq N}(k^2)\inv \\
&\convergesto{N\to\infty\implies t\to\infty} 0
,\]
where given $N$ we can pick $t$ large enough so that $t^2 + k^2 \geq tk^2$ for all $k\leq N$.
These converge to zero as $N\to\infty$ since $\sum k^{-2} < \infty$, making the last term the tail of a convergent sum.


**Part 4**:
Since $f,g$ uniformly converge to zero on the strip $0<\Re(x) < 1$, they are bounded on this strip.
Since this is a fundamental domain for their periods, they are bounded on $\CC$.
Write $h\da f-g$, then $h$ is entire since $f,g$ have the same singular parts, and bounded since $\abs{h}\leq \abs{f} + \abs{g}$.
By Liouville, $h$ is constant with $\lim_{t\to\infty} h(it) = 0$, so $h\equiv 0$ and $f\equiv g$.
:::

