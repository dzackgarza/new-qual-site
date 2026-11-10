---
schema: qual/card@1
id: E-39RRX
kind: problem
title: Four topologies on $\ell^2$ and the Hilbert cube
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §20 Exercise 8, printed p. 127, with the uniform
    metric and the definition of the Hilbert cube printed there; the three parts are stored
    as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 20.8, PDF pp. 20-22. The inclusions box contains
    l2 contains uniform are shown by comparing the metrics and by fitting an l2 ball into a
    box product of shrinking intervals; the four topologies on R^infinity are separated by
    one witness each, and on the Hilbert cube the product, uniform and l2 topologies
    coincide, the box topology being strictly finer. (tmp/sources/munkres-solutions-
    positron-ch2.pdf).
---

::: {.exercise}

Let $X$ be the subset of $\RR^\omega$ consisting of all sequences $\mathbf{x}$ such that $\sum x_i^2$ converges.
Then the formula

$$
d(\mathbf{x}, \mathbf{y}) = \left[ \sum_{i=1}^{\infty} (x_i - y_i)^2 \right]^{1/2}
$$

defines a metric on $X$.
(See Exercise 10.) On $X$ we have the three topologies it inherits from the box, uniform, and product topologies on $\RR^\omega$.
We have also the topology given by the metric $d$, which we call the $\ell^2$-topology.

(a) Show that on $X$, we have the inclusions

$$
\text{box topology} \supset \ell^2\text{-topology} \supset \text{uniform topology}.
$$

(b) The set $\RR^\infty$ of all sequences that are eventually zero is contained in $X$.
Show that the four topologies that $\RR^\infty$ inherits as a subspace of $X$ are all distinct.

(c) The set

$$
H = \prod_{n \in \ZZ_+} [0, 1/n]
$$

is contained in $X$; it is called the Hilbert cube.
Compare the four topologies that $H$ inherits as a subspace of $X$.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 20.8, PDF pp. 20--22** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); all three parts are theirs.

Write $d_{\ell^{2}}(\mathbf{x},\mathbf{y})=\big(\sum_{i}(x_{i}-y_{i})^{2}\big)^{1/2}$ on $X$, and recall $\bar\rho(\mathbf{x},\mathbf{y})=\sup_{i}\min\{\abs{x_{i}-y_{i}},1\}$.

(a) *Uniform $\subset\ell^{2}$.* For every $i$, $\abs{x_{i}-y_{i}}\le d_{\ell^{2}}(\mathbf{x},\mathbf{y})$, and if $d_{\ell^{2}}(\mathbf{x},\mathbf{y})\le1$ then $\bar\rho(\mathbf{x},\mathbf{y})\le d_{\ell^{2}}(\mathbf{x},\mathbf{y})$; so $B_{\ell^{2}}(\mathbf{x},\varepsilon)\subset B_{\bar\rho}(\mathbf{x},\varepsilon)$ for $\varepsilon\le1$, and the $\ell^{2}$-topology contains the uniform one.

*$\ell^{2}\subset$ box.* Let $B_{\ell^{2}}(\mathbf{x},\varepsilon)$ be a ball and $\mathbf{y}\in B_{\ell^{2}}(\mathbf{x},\varepsilon)$; put $r=\varepsilon-d_{\ell^{2}}(\mathbf{x},\mathbf{y})>0$ and
$$
U=\prod_{n}\Big(y_{n}-\frac{r}{2^{(n+1)/2}},\ y_{n}+\frac{r}{2^{(n+1)/2}}\Big),
$$
which is open in the box topology and contains $\mathbf{y}$. For $\mathbf{z}\in U$,
$$
d_{\ell^{2}}(\mathbf{y},\mathbf{z})^{2}=\sum_{n}(y_{n}-z_{n})^{2}<\sum_{n}\frac{r^{2}}{2^{n+1}}=r^{2},
$$
so $d_{\ell^{2}}(\mathbf{x},\mathbf{z})\le d_{\ell^{2}}(\mathbf{x},\mathbf{y})+d_{\ell^{2}}(\mathbf{y},\mathbf{z})<\varepsilon$ and $\mathbf{z}\in B_{\ell^{2}}(\mathbf{x},\varepsilon)$. So the ball is box-open and the $\ell^{2}$-topology is contained in the box topology.

(b) The four topologies on $\RR^{\infty}$ are distinct, and it suffices to exhibit, in each of the three finer ones, an open set that is not open in the next coarser one.

*Uniform not product.* $B_{\bar\rho}(\mathbf{0},\varepsilon)\cap\RR^{\infty}$ with $0<\varepsilon<1$ is uniform-open and nonempty; no product-basic set containing a point $\mathbf{y}$ of it is contained in it, because a product-basic set restricts only finitely many coordinates and so contains points with an arbitrarily large coordinate in some unrestricted place, hence of uniform distance $1$ from $\mathbf{y}$.

*$\ell^{2}$ not uniform.* $B_{\ell^{2}}(\mathbf{0},2\varepsilon)\cap\RR^{\infty}$ with $0<\varepsilon<1$ is $\ell^{2}$-open and contains $(\varepsilon,0,0,\dots)$. Any uniform ball $B_{\bar\rho}((\varepsilon,0,\dots),r)\cap\RR^{\infty}$ with $r\le1$ contains, for $t<r$ and $N$ with $Nt^{2}+\varepsilon^{2}>4\varepsilon^{2}$, the point $(s,t,\dots,t,0,\dots)$ with $\varepsilon-r<s<\varepsilon$ and $N$ entries equal to $t$, whose squared norm exceeds $4\varepsilon^{2}$; so no uniform ball at that point is contained in the $\ell^{2}$-ball.

*Box not $\ell^{2}$.* $D=\prod_{n}(-1/n,1/n)\cap\RR^{\infty}$ is box-open and contains $\mathbf{0}$; but for every $r>0$ the point with a single nonzero entry $1/N$ in position $N$, where $1/N<r$, lies in $B_{\ell^{2}}(\mathbf{0},r)$ and not in $D$.

So $\text{product}\subsetneq\text{uniform}\subsetneq\ell^{2}\subsetneq\text{box}$ on $\RR^{\infty}$.

(c) On the Hilbert cube $H=\prod_{n}[0,1/n]$ the topologies are: $\text{product}=\text{uniform}=\ell^{2}\subsetneq\text{box}$.

The box topology is strictly finer: the set $\prod_{n}(-1/n,1/n)\cap H$ is box-open and contains $\mathbf{0}$, but for each $r>0$ the point of $H$ with a single nonzero entry $1/N$ in position $N$ and $1/N<r$ lies in the $\ell^{2}$-ball of radius $r$ around $\mathbf{0}$ and outside that box-open set.

That the product topology is finer than the $\ell^{2}$-topology on $H$: let $B_{\ell^{2}}(\mathbf{x},\varepsilon)\cap H$ be a ball. Choose $N$ with $\sum_{i>N}1/i^{2}<\varepsilon^{2}/2$ and put
$$
U=H\cap\prod_{n}U_{n},\qquad
U_{n}=\Big(x_{n}-\frac{\varepsilon}{2^{(n+1)/2}},\ x_{n}+\frac{\varepsilon}{2^{(n+1)/2}}\Big)\ (n<N),\quad U_{n}=\RR\ (n\ge N).
$$
Then $U$ is a product neighbourhood of $\mathbf{x}$. For $\mathbf{y}\in U$,
$$
\sum_{n}(x_{n}-y_{n})^{2}<\sum_{n<N}\frac{\varepsilon^{2}}{2^{n+1}}+\sum_{n\ge N}\frac{1}{n^{2}}<\frac{\varepsilon^{2}}{2}+\frac{\varepsilon^{2}}{2}=\varepsilon^{2},
$$
using $\abs{x_{n}-y_{n}}\le1/n$ on $H$ for $n\ge N$. So $U\subset B_{\ell^{2}}(\mathbf{x},\varepsilon)\cap H$, the product topology contains the $\ell^{2}$-topology, and with (a) the three coincide.
:::
