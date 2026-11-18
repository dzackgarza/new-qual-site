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
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps from the retained positron0802 solution (Chapter 2,
    Exercise 20.8, PDF pp. 20-22). Checked against the book: §20 Exercise 8 as printed
    (p. 127); Theorem 20.4 (p. 124) for product inside uniform inside box and for the
    uniform topology being finer than the product topology; the uniform metric of p. 122.
    Repairs: the retained text and the earlier prose of this card concluded "the l2-topology
    contains the uniform one" from the ball containment B_l2 inside B_rho, which gives the
    reverse; the step now argues at a point y of a uniform ball and uses the triangle
    inequality for rho-bar. The witness for "l2 not uniform" was transcribed as
    N t^2 + eps^2 > 4 eps^2 while the source has N t^2 + s^2 > 4 eps^2, and with eps^2 the
    exhibited point need not leave the l2 ball; the source's condition is restored. On the
    Hilbert cube the proof that the product topology contains the l2 topology is kept, with
    Theorem 20.4 supplying product inside uniform so that the three coincide. No repair to
    the printed statement.
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
The argument is the retained published solution, **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 20.8, PDF pp. 20--22** (`tmp/sources/munkres-solutions-positron-ch2.pdf`), restructured into steps; one step is repaired, where that text exhibits a point with $Nt^{2}+s^{2}>4\varepsilon^{2}$ and the earlier transcription of this card had written $Nt^{2}+\varepsilon^{2}$.

Throughout, $X$ is the set of sequences with $\sum x_i^2$ convergent, $d_{\ell^2}(\mathbf{x},\mathbf{y})=\big(\sum_i (x_i-y_i)^2\big)^{1/2}$, and $\bar\rho(\mathbf{x},\mathbf{y})=\sup_i\min\{\abs{x_i-y_i},1\}$ is the uniform metric of §20 (printed p. 122); $B_{\ell^2}$ and $B_{\bar\rho}$ are the balls of these two metrics, and $\RR^\infty$ is the set of eventually zero sequences.

::: pf

::: {.pf-step #a}
(a) On $X$ the box topology contains the $\ell^2$-topology, which contains the uniform topology.

::: pf-proof

::: {.pf-step #a-uniform}
$\bar\rho(\mathbf{x},\mathbf{y})\le d_{\ell^2}(\mathbf{x},\mathbf{y})$ for all $\mathbf{x},\mathbf{y}\in X$, and the uniform topology is contained in the $\ell^2$-topology.

::: pf-proof
For each $i$ we have $(x_i-y_i)^2\le\sum_k(x_k-y_k)^2$, hence $\abs{x_i-y_i}\le d_{\ell^2}(\mathbf{x},\mathbf{y})$. Since $\min\{\abs{x_i-y_i},1\}\le\abs{x_i-y_i}$, taking the supremum over $i$ gives $\bar\rho(\mathbf{x},\mathbf{y})\le d_{\ell^2}(\mathbf{x},\mathbf{y})$. Now let $\mathbf{y}\in B_{\bar\rho}(\mathbf{x},\varepsilon)$ and put $\delta=\varepsilon-\bar\rho(\mathbf{x},\mathbf{y})>0$. For $\mathbf{z}$ with $d_{\ell^2}(\mathbf{y},\mathbf{z})<\delta$ the inequality just proved gives $\bar\rho(\mathbf{y},\mathbf{z})<\delta$, and the triangle inequality for the metric $\bar\rho$ then gives $\bar\rho(\mathbf{x},\mathbf{z})\le\bar\rho(\mathbf{x},\mathbf{y})+\bar\rho(\mathbf{y},\mathbf{z})<\bar\rho(\mathbf{x},\mathbf{y})+\delta=\varepsilon$, so $\mathbf{z}\in B_{\bar\rho}(\mathbf{x},\varepsilon)$. Thus $B_{\ell^2}(\mathbf{y},\delta)\subset B_{\bar\rho}(\mathbf{x},\varepsilon)$, every uniform ball is $\ell^2$-open, and the uniform topology is contained in the $\ell^2$-topology.
:::

:::

::: {.pf-step #a-box}
Every $\ell^2$-ball is open in the box topology, so the $\ell^2$-topology is contained in the box topology, and with step [](#a-uniform){.pf-ref} part (a) is proved.

::: pf-proof
Let $\mathbf{y}\in B_{\ell^2}(\mathbf{x},\varepsilon)$ and put $r=\varepsilon-d_{\ell^2}(\mathbf{x},\mathbf{y})>0$. The set
$$
U=\prod_n\Big(y_n-\frac{r}{2^{(n+1)/2}},\ y_n+\frac{r}{2^{(n+1)/2}}\Big)
$$
is a product of open intervals, hence open in the box topology, and it contains $\mathbf{y}$. For $\mathbf{z}\in U$ we have $\abs{y_n-z_n}<r/2^{(n+1)/2}$ for every $n$, so
$$
d_{\ell^2}(\mathbf{y},\mathbf{z})^2=\sum_n (y_n-z_n)^2<\sum_n\frac{r^2}{2^{n+1}}=r^2,
$$
and therefore $d_{\ell^2}(\mathbf{x},\mathbf{z})\le d_{\ell^2}(\mathbf{x},\mathbf{y})+d_{\ell^2}(\mathbf{y},\mathbf{z})<d_{\ell^2}(\mathbf{x},\mathbf{y})+r=\varepsilon$, that is $\mathbf{z}\in B_{\ell^2}(\mathbf{x},\varepsilon)$. So $U\subset B_{\ell^2}(\mathbf{x},\varepsilon)$, the ball is box-open, and every $\ell^2$-open set is box-open.
:::

:::

:::

:::

::: {.pf-step #b}
(b) The four topologies on $\RR^\infty$ are all distinct.

::: pf-proof

::: {.pf-step #b-uniform}
$B_{\bar\rho}(\mathbf{0},\varepsilon)\cap\RR^\infty$ with $0<\varepsilon<1$ is uniform-open and not product-open.

::: pf-proof
It is uniform-open by definition and it contains $\mathbf{0}$, so it is nonempty. Let $\mathbf{y}\in B_{\bar\rho}(\mathbf{0},\varepsilon)$ and let $U$ be a product-basic neighbourhood of $\mathbf{y}$ in $\RR^\infty$; then $U=\RR^\infty\cap\prod_n U_n$ with $U_n=\RR$ for all $n$ outside a finite set $F$. Choose $i\notin F$ and let $\mathbf{z}$ have $z_n=y_n$ for $n\in F$, $z_i=y_i+2$ and $z_n=0$ otherwise; then $\mathbf{z}\in\RR^\infty\cap\prod_n U_n=U$, while $\bar\rho(\mathbf{y},\mathbf{z})=\min\{2,1\}=1>\varepsilon$, so $\mathbf{z}\notin B_{\bar\rho}(\mathbf{0},\varepsilon)\cap\RR^\infty$. Hence no product-basic neighbourhood of a point of that set lies inside it, and it is not product-open.
:::

:::

::: {.pf-step #b-l2}
$B_{\ell^2}(\mathbf{0},2\varepsilon)\cap\RR^\infty$ with $0<\varepsilon<1$ is $\ell^2$-open and not uniform-open.

::: pf-proof
It is $\ell^2$-open and it contains $\mathbf{x}=(\varepsilon,0,0,\ldots)$, so it is nonempty. Let $U=B_{\bar\rho}(\mathbf{x},r)\cap\RR^\infty$ be a uniform ball about $\mathbf{x}$; if $r\ge1$ then $U=\RR^\infty$ because $\bar\rho\le1$, which is not contained in the given set, so assume $0<r<1$. Choose $s$ with $\varepsilon-r<s<\varepsilon$, then $t$ with $0<t<r$, then $N$ with $Nt^2+s^2>4\varepsilon^2$, and set $\mathbf{y}=(s,t,\ldots,t,0,\ldots)$ with $t$ in positions $2,\ldots,N+1$. Then $\abs{s-\varepsilon}<r$ and $\abs{t-0}=t<r$, so $\bar\rho(\mathbf{x},\mathbf{y})<r$ and $\mathbf{y}\in U$; but $\sum_i y_i^2=s^2+Nt^2>4\varepsilon^2$, so $\mathbf{y}\notin B_{\ell^2}(\mathbf{0},2\varepsilon)$. Hence no uniform ball about $\mathbf{x}$ is contained in the given set, which is therefore not uniform-open.
:::

:::

::: {.pf-step #b-box}
$D=X\cap\prod_n(-1/n,1/n)$ is box-open and not $\ell^2$-open, so on $\RR^\infty$ the chain of part (a) has all three inclusions strict and the four topologies are distinct.

::: pf-proof
$D$ is an intersection of a box-open set with $X$, hence box-open in $X$, so $D\cap\RR^\infty$ is box-open in $\RR^\infty$, and $\mathbf{0}\in D$. Given $r>0$, choose $N$ with $1/N<r$ and let $\mathbf{z}\in\RR^\infty$ have $z_N=1/N$ and $z_n=0$ for $n\ne N$; then $\mathbf{z}\in B_{\ell^2}(\mathbf{0},r)$ because its $\ell^2$ norm is $1/N<r$, while $\mathbf{z}\notin D$ because $1/N$ is the excluded right endpoint of $(-1/N,1/N)$. So no $\ell^2$-ball about $\mathbf{0}$ lies in $D\cap\RR^\infty$, which is not $\ell^2$-open. The chains of inclusions of part (a), step [](#a){.pf-ref}, together with the three failures just proved at steps [](#b-uniform){.pf-ref}, [](#b-l2){.pf-ref} and this one, make the four topologies pairwise distinct.
:::

:::

:::

:::

::: {.pf-step #c}
(c) On the Hilbert cube $H=\prod_n[0,1/n]$ the product, uniform and $\ell^2$-topologies coincide, and the box topology is strictly finer.

::: pf-proof

::: {.pf-step #c-box}
The box topology on $H$ is strictly finer than the $\ell^2$-topology.

::: pf-proof
The set $B=\prod_n(-1/n,1/n)$ is box-open in $\RR^\omega$, so $B\cap H$ is box-open in $H$ and contains $\mathbf{0}$. Given $r>0$, choose $N$ with $1/N<r$ and let $\mathbf{z}\in H$ have $z_N=1/N$ and $z_n=0$ otherwise; since $1/N\in[0,1/N]$ we have $\mathbf{z}\in H$, and $\mathbf{z}\in B_{\ell^2}(\mathbf{0},r)\cap H$ because its $\ell^2$ norm is $1/N<r$, while $\mathbf{z}\notin B\cap H$. So no $\ell^2$-ball about $\mathbf{0}$ lies in $B\cap H$, which is therefore not $\ell^2$-open, and the box topology on $H$ is strictly finer.
:::

:::

::: {.pf-step #c-equal}
The product topology on $H$ is finer than the $\ell^2$-topology, and hence the product, uniform and $\ell^2$-topologies on $H$ coincide.

::: pf-proof
Let $B_{\ell^2}(\mathbf{x},\varepsilon)\cap H$ be a ball and choose $N$ with $\sum_{i\ge N}1/i^2<\varepsilon^2/2$, possible because $\sum 1/i^2$ converges. Put
$$
U=H\cap\prod_n U_n,\qquad U_n=\Big(x_n-\frac{\varepsilon}{2^{(n+1)/2}},\ x_n+\frac{\varepsilon}{2^{(n+1)/2}}\Big)\ \text{for }n<N,\qquad U_n=\RR\ \text{for }n\ge N;
$$
this is a product-basic neighbourhood of $\mathbf{x}$ because all but finitely many of the factors are $\RR$, and for $\mathbf{y}\in U$ we have $y_n\in[0,1/n]$ as well as $x_n\in[0,1/n]$, so $\abs{x_n-y_n}\le 1/n$ for $n\ge N$, and then
$$
\sum_n (x_n-y_n)^2<\sum_{n<N}\frac{\varepsilon^2}{2^{n+1}}+\sum_{n\ge N}\frac{1}{n^2}<\frac{\varepsilon^2}{2}+\frac{\varepsilon^2}{2}=\varepsilon^2
$$
because $\sum_{n<N}2^{-(n+1)}<1/2$. So $U\subset B_{\ell^2}(\mathbf{x},\varepsilon)\cap H$ and the product topology contains the $\ell^2$-topology. By step [](#a-uniform){.pf-ref} the uniform topology is contained in the $\ell^2$-topology, and by Theorem 20.4 (printed p. 124) the product topology is contained in the uniform topology; so the three are equal, while the box topology is strictly finer by step [](#c-box){.pf-ref}.
:::

:::

:::

:::

:::

:::
