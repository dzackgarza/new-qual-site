---
schema: qual/card@1
id: E-WML5E
kind: exercise
title: "Uniform limits of derivatives, term-by-term differentiation"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="Uniform limits of derivatives, term-by-term differentiation"}
Suppose $f_k: \Omega\to \CC$ is a sequence of differentiable functions converging locally uniformly to $f:\Omega\to \CC$.
Show that

- $f$ is continuous,
- $f$ is differentiable,
- $\ts{f_k'}\to f'$ locally uniformly.

Thus if $f(z) = \sum{k\geq 0} c_k (z-z_0)^k$ is a power series, since $S_N\to f$ locally uniformly, $f$ can be differentiated term-by-term within its radius of convergence.

#complex/exercise/completed

:::

:::{.solution}
That $f$ is continuous is a local question: fixing a point $z_0$, take a closed disc $\DD+z_0$ about $z_0$.
By local uniform convergence $f_k\to f$ uniformly on $\DD+z_0$, and differentiable $\implies$ continuous.
So each $f_k$ is continuous, making $f$ continuous on $\DD+z_0$ by the uniform limit theorem.

That $f$ is differentiable is again a local question: fix $z$ and write $\gamma \da \bar{\DD + z}$ as the boundary of the disc about $z$.
Define $g_k(\xi) \da {f_k\over \xi-z}$, so $g_k \to {f \over \xi-a}$ locally uniformly.
Now apply Cauchy's integral formula at $z$:
\[
f(z) 
&= \lim_k f_k(z) \\
&= \lim_k {1\over 2\pi i}\int_\gamma {f_k(\xi) \over \xi - z}\dxi \\
&= \lim_k {1\over 2\pi i}\int_\gamma g_k(\xi)\dxi\\
&= {1\over 2\pi i}\int_\gamma \lim_k g_k(\xi)\dxi \\
&= {1\over 2\pi i}\int_\gamma g(\xi)\dxi\\
&= {1\over 2\pi i}\int_\gamma {f(\xi) \over \xi - z} \dxi
,\]
where we've used uniform convergence on $\gamma$ to commute the limit and integral.
So $f$ has an integral representation, making it differentiable.

That $f_k'\to f'$: 
\[
\lim_k f_k'(z)
&= \lim_k {1\over 2\pi i}\int_\gamma {f_k(\xi) \over (\xi - z)^2 }\dxi\\
&= {1\over 2\pi i}\int_\gamma \lim_k {f_k(\xi) \over (\xi - z)^2}\dxi\\
&= {1\over 2\pi i}\int_\gamma {f(\xi) \over (\xi - z)^2}\dxi\\
&= f'(z)
.\]

That the convergence is locally uniform:
first consider what happens on an closed discs $K = D$ with $\gamma \da \bd{D}$.
Then for $z\in D$,
\[
\abs{f'(z) - f_k'(z) }
&= \abs{{1\over 2\pi i} \int_{\gamma} {f(\xi) - f_k(\xi) \over (\xi - z)^2}\dxi }\\
&\leq {1\over 2\pi}\int_{\gamma} {\abs{f(\xi) - f_k(\xi) } \over \abs{\xi - z}^2} \dxi\\
&\leq {1\over 2\pi}\int_{\gamma } { \sup_{\xi \in \gamma} \abs{f(\xi) - f_k(\xi) } \over r^2 } \dxi\\
&= {1\over 2\pi} { \sup_{\xi \in \gamma } \abs{f(\xi) - f_k(\xi) } \over r^2} \cdot {2\pi r} \\
&= { \sup_{\xi \in \gamma } \abs{f(\xi) - f_k(\xi) }}/r 
.\]
Since $\gamma$ is compact, using locally uniform convergence of $f_k\to f$, there exists an $n_0$ such that $n\geq n_0$ bounds this $\sup$ by $\eps$.
For $K$ arbitrary, cover $K$ by discs $D_z$ for every $z\in K$ and extract a finite cover $\ts{D_{z_k}}_{k\leq N}$.
Produce $n_0, n_1,\cdots, n_N$ as in the above argument, and take $n\da \max\ts{n_k}_{k\leq N}$ to obtain uniform convergence on every $D_{z_k}$ and thus on $K$.
:::

