---
schema: qual/card@1
id: E-PCVOI
kind: problem
title: $\frac{\pi^2}{\sin^2(\pi z)}=\sum_{n\in\ZZ}\frac{1}{(z-n)^2}$ by matching
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

::: {.problem}
Define
$$
\begin{aligned}
f(z) &= {\pi^2 \over \sin^2 \qty{\pi z} } \\
g(z) &= \sum_{n\in \ZZ} {1\over (z-n)^2}.
\end{aligned}
$$

(a) Show that $f$ and $g$ have the same singularities in $\CC$.

(b) Show that $f$ and $g$ have the same singular parts at each of their singularities.

(c) Show that $f, g$ each have period one and approach zero uniformly on $0\leq x \leq 1$ as $\abs{y}\to \infty$.

(d) Conclude that $f = g$.
:::

::: {.solution}

Write $z=x+iy$.

::: pf

::: {.pf-step #g-conv}
The series $g$ converges locally uniformly on $\CC\setminus\ZZ$, and $g(z)-\frac{1}{(z-k)^2}$ is holomorphic near each $k\in\ZZ$.

::: pf-proof
On $\abs{z}\leq R$, the terms with $\abs{n}\geq 2R$ satisfy $\abs{z-n}^{-2}\leq 4n^{-2}$, so by the Weierstrass $M$-test they sum to a holomorphic function there.
The finitely many remaining terms are holomorphic away from $\ZZ$, and near $k$ only $\frac{1}{(z-k)^2}$ is singular.
:::

:::

::: {.pf-step #part-a}
(a) The singularities of $f$ and of $g$ are exactly the points of $\ZZ$.

::: pf-proof
$\sin(\pi z)=0$ iff $z\in\ZZ$, so $f$ is holomorphic exactly off $\ZZ$.
By step [](#g-conv){.pf-ref}, $g$ is holomorphic off $\ZZ$ and has a pole at each $k\in\ZZ$.
:::

:::

::: {.pf-step #periodic}
$f$ and $g$ have period $1$.

::: pf-proof
$\sin^2(\pi(z+1)) = (-\sin(\pi z))^2$, and $g(z+1)=\sum_{n\in\ZZ}(z-(n-1))^{-2} = g(z)$ by reindexing.
:::

:::

::: {.pf-step #part-b}
(b) At each $k\in\ZZ$, $f$ and $g$ both have principal part $\frac{1}{(z-k)^2}$.

::: pf-proof
For $g$ this is step [](#g-conv){.pf-ref}.
By step [](#periodic){.pf-ref} it suffices to treat $f$ at $k=0$, where
$$
f(z) = \frac{1}{z^2}\left(1-\frac{\pi^2z^2}{6}+O(z^4)\right)^{-2} = \frac{1}{z^2}+\frac{\pi^2}{3}+O(z^2).
$$
:::

:::

::: {.pf-step #part-c}
(c) $f(x+iy)\to0$ and $g(x+iy)\to0$ as $\abs{y}\to\infty$, uniformly in $x\in[0,1]$.

::: pf-proof
$\abs{\sin(\pi z)}^2=\sin^2(\pi x)+\sinh^2(\pi y)\geq\sinh^2(\pi y)$, so $\abs{f(z)}\leq\pi^2/\sinh^2(\pi y)$.
For $x\in[0,1]$, $\abs{x-n}\geq\max(0,\abs{n}-1)$, so for $y\neq0$
$$
\abs{g(x+iy)}\leq\sum_{n\in\ZZ}\frac{1}{(x-n)^2+y^2}\leq\frac{3}{y^2}+2\sum_{m\geq1}\frac{1}{m^2+y^2}\leq\frac{3}{y^2}+2\int_0^\infty\frac{dt}{t^2+y^2}=\frac{3}{y^2}+\frac{\pi}{\abs{y}}.
$$
Periodicity is step [](#periodic){.pf-ref}.
:::

:::

::: pf-step
(d) $f=g$.

::: pf-proof
By steps [](#part-a){.pf-ref} and [](#part-b){.pf-ref}, $h\coloneqq f-g$ extends to an entire function, of period $1$ by step [](#periodic){.pf-ref}.
By step [](#part-c){.pf-ref}, $h$ is bounded on $\{0\leq x\leq 1,\ \abs{y}\geq Y\}$ for some $Y$; it is bounded on the compact rectangle $\{0\leq x\leq1,\ \abs{y}\leq Y\}$ by continuity, hence on $\CC$ by periodicity.
By Liouville's theorem $h$ is constant, and by step [](#part-c){.pf-ref} the constant is $0$.
:::

:::

:::

:::

::: {.remark title="Variations"}
The problem is also posed in two other forms.

- Show that $f$ and $g$ have the same principal part at each $k\in\ZZ$, then show that $h=f-g$ is bounded on $\CC$ and conclude $f=g$. Parts (b), (c) and (d) are this argument: the boundedness of $h$ is the first half of the proof of (d).
- Show only that there is an entire function $h$ with $f=g+h$. This is the first sentence of the proof of (d): by (a) and (b), $f-g$ is bounded near each integer, so Riemann's removable singularity theorem extends it over $\ZZ$.
:::
