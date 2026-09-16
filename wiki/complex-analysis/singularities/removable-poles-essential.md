---
title: Removable singularities, poles, essential singularities
order: 20
topics:
- Removable Singularities
- Poles
- Essential Singularities
- Zeros and Poles
---

# Removable singularities, poles, essential singularities

Removable singularities, zeros, poles, and essential singularities of holomorphic functions.
Criteria for the type of an isolated singularity are on [[complex-analysis/singularities/classifying-a-singularity|Classifying a singularity]].

[[D-VAXQT]]

[[D-IWIA5]]

[[FF-QZXBS]]

::: {.remark title="The two classifications agree"}
In terms of the Laurent expansion $f(z) = \sum_{k\in \ZZ} c_k (z-z_0)^k$ on a punctured disc about $z_0$:

- removable: $c_{k} = 0$ for $k \leq -1$;

- pole of order $N$: $c_{-N}\neq 0$ and $c_k = 0$ for $k<-N$;

- essential: $c_k\neq 0$ for infinitely many $k<0$.

In terms of limiting behavior:

- removable: $\lim_{z\to z_0} f(z)$ exists in $\CC$, equivalently $f$ is bounded on a punctured neighborhood of $z_0$;

- pole: $\lim_{z\to z_0} \abs{f(z)} = \infty$;

- essential: neither limit exists.

:::

## Removable

[[D-BQLJV]]

[[FD-BRJK5]] [[FD-CCVUQ]]

::: {.example title="Removable singularities"}
\envlist

- $f(z) \coloneqq \sin(z)/z$ has a removable singularity at $z=0$, with extension $f(0) \coloneqq 1$.

- If $f = p/q$ with $p,q$ holomorphic near $z_0$, $p(z_0) = q(z_0) = 0$, and $q'(z_0)\neq 0$, then $z_0$ is removable and the extension has $f(z_0) = p'(z_0)/q'(z_0)$.

:::

[[T-ZZJDP]]

[[FT-5NI77]] [[FT-LGWHM]]

::: {.proof}
If $z_0$ is removable, the extension is continuous at $z_0$, so $f$ is bounded near $z_0$.
Conversely, suppose $\abs f\leq M$ on $0<\abs{z-z_0}<\delta$.
Define $h(z)\coloneqq (z-z_0)^2 f(z)$ for $z\neq z_0$ and $h(z_0)\coloneqq 0$.
Then $\abs{(h(z)-h(z_0))/(z-z_0)} = \abs{(z-z_0)f(z)}\leq M\abs{z-z_0}\to 0$, so $h$ is holomorphic on $D_\delta(z_0)$ with $h(z_0)=h'(z_0)=0$.
Its Taylor series is $h(z) = \sum_{k\geq 2} a_k(z-z_0)^k$, so $f(z) = \sum_{k\geq 0} a_{k+2}(z-z_0)^k$ for $z\neq z_0$, and the right side is holomorphic on $D_\delta(z_0)$.

:::

![](../../../../assets/assets/figures/2021-10-29_01-30-50.png)

![](../../../../assets/assets/figures/2021-10-29_01-31-06.png)

::: {.remark title="Showing a singularity is removable"}
A singularity at $z_0$ is removable if the Laurent expansion $\sum_{k\in\ZZ} c_k (z-z_0)^k$ has $c_k = 0$ for $k<0$, or if $f$ is bounded near $z_0$, by Riemann's theorem [[T-ZZJDP]].

:::

## Zeros and their order

[[D-65VIK]]

[[T-YKVFQ]]

::: {.remark}
By [[T-YKVFQ]], an infinite subset of a compact set $K\subseteq\Omega$ has a limit point in $K$, so a holomorphic $f$ on a connected open set $\Omega$ with infinitely many zeros in $K$ vanishes identically by the identity principle.
Compactness of $K$ inside $\Omega$ is needed: $\sin\bigl(\pi/(1-z)\bigr)$ is holomorphic on $\DD$, not identically zero, and vanishes at the points $1-1/k$, $k\geq 2$, which accumulate at $1\notin\DD$.

:::

[[PR-5A64G]]

::: {.remark}
If $z_0$ is a zero of order $n$ of $f$, then $f$ vanishes to order $n$ at $z_0$.

:::

::: {.proof title="Existence and uniqueness of the order"}
Assume $z_0 = 0$.
Since $f$ is not identically zero on the connected set $\Omega$, the identity principle shows that not every Taylor coefficient of $f$ at $0$ vanishes.
Expand $f$ as a power series on a disc about $0$:
$$
f(z) = \sum_{k\geq 0}c_k z^k = z^n\qty{c_n + c_{n+1}z + \cdots} \coloneqq z^n g(z)
,$$
where $c_n$ is the minimal nonvanishing coefficient.
Since $c_n \neq 0$ and $\lim_{z\to 0} g(z) = c_n$, $g$ is nonvanishing on a neighborhood of $0$.
For uniqueness, $z^n g(z) = z^m h(z)$ with $m > n$ gives $g(z) = z^{m-n}h(z)$, and letting $z\to 0$ forces $g(0) = 0$, a contradiction.

:::

[[PR-VUBCC]]

[[PR-EWOP5]]

::: {.proof}
Suppose not: there are a zero $z_0$ of $f$ and zeros $z_k \neq z_0$ of $f$ with $z_k \to z_0$.
Since $f\not\equiv 0$, the Taylor series of $f$ at $z_0$ has a smallest index $m$ with $c_m\neq 0$:
$$
f(z) = \sum_{k\geq m}c_k (z-z_0)^k = c_m(z-z_0)^m \qty{1 + \sum_{k\geq 1}c_k' (z-z_0)^k } \coloneqq c_m(z-z_0)^m (1 + g(z-z_0))
.$$
Here $g(z-z_0)\to 0$ as $z\to z_0$, so for large $k$, $\abs{g(z_k - z_0)} < 1$ and hence $1 + g(z_k-z_0) \neq 0$.
But then
$$
0 = f(z_k) = c_m(z_k - z_0)^m (1 + g(z_k - z_0)) \neq 0
.$$

$\contradiction$

:::

[[C-F2ZZQ]]

[[PR-ITZIT]]

## Poles

[[D-AUD6K]]

[[FD-C7EQD]] [[FD-EKGLW]]

[[D-C3JIU]]

::: {.remark}
A pole admits a neighborhood on which $f$ is nonvanishing, and in fact bounded below.

:::

[[PR-NITIQ]]

::: {.proof}
Since $\abs f\to\infty$, $f$ has no zeros near $z_0$, and $1/f$ has a removable singularity at $z_0$ with value $0$; it is not identically zero, so by [[PR-5A64G]]
$$
{1\over f(z) } = (z-z_0)^n g(z)
$$
with $g$ holomorphic and nonvanishing near $z_0$, then take reciprocals:
$$
f(z) = (z-z_0)^{-n} h(z), \qquad h(z) \coloneqq {1\over g(z)}
.$$

:::

::: {.example title="The pole of $f(z^2)$"}
If $f$ has a pole of order $m$ at $0$, then $g(z) \coloneqq f(z^2)$ has a pole of order $2m$ at $0$.

By Laurent expansion: writing $f(z) = \sum_{k\geq -m} c_k z^k$ with $c_{-m} \neq 0$, substituting $z^2$ gives
$$
g(z) = \sum_{k\geq -m} c_k z^{2k}
= {c_{-m} \over z^{2m}} + \cdots
,$$
so the lowest power of $z$ appearing is $z^{-2m}$ with nonzero coefficient $c_{-m}$, which is exactly a pole of order $2m$.
Alternatively, by [[PR-NITIQ]], write $f(z) = z^{-m}h(z)$ with $h$ holomorphic and $h(0) \neq 0$; then $f(z^2) = z^{-2m}h(z^2)$ and $h(z^2)\mid_{z=0} = h(0) \neq 0$.

:::

## Essential

[[D-VKP6N]]

[[FD-BACTZ]] [[FD-ZPKLQ]]

::: {.example title="Essential singularities"}
$f(z) \coloneqq e^{1/z}$ has an essential singularity at $z=0$: expanding picks up infinitely many negative terms,
$$
e^{1/z} = 1 + {1\over z} + {1\over 2! z^2} + \cdots
.$$
On every punctured neighborhood $U$ of $0$, $f(U) = \CC\smz$.
Likewise $g(z) \coloneqq \sin\qty{1\over z}$ has an essential singularity at $z=0$, and $g(V) = \CC$ for every punctured neighborhood $V$ of $0$.

:::

The values taken near an essential singularity are described on [[complex-analysis/singularities/casorati-weierstrass-and-picard|Casorati–Weierstrass and Picard]].

## At infinity

[[D-BPBSQ]]

## Exercises

[[P-DO7TE]]
[[E-NVCIF]]
[[E-GRXN4]]
[[E-WE7UT]]
[[E-XPMW5]]
[[E-WNXIR]]
[[E-WAYFS]]
[[E-G3DCH]]
[[E-JOSK3]]
[[E-ALB7C]]
[[E-WXHMJ]]
[[E-LIK72]]
[[E-CLSFF]]
[[E-4GLUR]]
[[E-NT2T3]]
[[E-UWKTZ]]
[[E-TM2Z4]]
[[E-LZTNT]]
[[E-LXPI7]]
[[E-SMOHZ]]
[[E-XQW4K]]
[[E-JUT2P]]
[[E-KUGNH]]
[[E-4J6IB]]
[[E-W2CWJ]]
[[E-QX3VF]]
