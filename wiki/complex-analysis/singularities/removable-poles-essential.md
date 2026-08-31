---
title: Removable singularities, poles, essential singularities
order: 20
problems:
  topics:
  - Removable Singularities
  - Poles
  - Essential Singularities
  - Zeros and Poles
---

# Removable singularities, poles, essential singularities

The three kinds of isolated singularity, and the theory each one carries.
Deciding which one you have is [[complex-analysis/singularities/classifying-a-singularity|Classifying a singularity]].

[[D-VAXQT]]

[[D-IWIA5]]

[[FF-QZXBS]]

:::{.remark title="The two classifications agree"}
By Laurent expansion $f(z) = \sum_{k\in \ZZ} c_k z^k$:

- removable: truncated at $k=0$, so $c_{k} = 0$ for $k \leq -1$;
- pole of order $N$: truncated at $k=-N$;
- essential: infinitely many negative terms.

By limiting behaviour:

- $\lim_{z\to z_0} f(z) < \infty$: removable, equivalently bounded on a neighborhood;
- $\lim_{z\to z_0} f(z) = \infty$: a pole;
- the limit does not exist: essential.

:::

## Removable

[[D-BQLJV]]

[[FD-BRJK5]] [[FD-CCVUQ]]

:::{.example title="Removable singularities"}
\envlist

- $f(z) \da \sin(z)/z$ has a removable singularity at $z=0$, and one may set $f(0) \da 1$.
- If $f = p/q$ with $p(z_0) = q(z_0) = 0$, then $z_0$ is removable and $f(z_0) \da p'(z_0)/q'(z_0)$.

:::

[[T-ZZJDP]]

[[FT-5NI77]] [[FT-LGWHM]]

:::{.proof}
Take $\gamma$ a circle centered at $z_0$ and write
\[
f(z) \da \int_\gamma { f(\xi) \over \xi - z} \dxi
.\]
This is valid for $z \neq z_0$, and the right-hand side is analytic across $z_0$.

:::

![](../../../../assets/assets/figures/2021-10-29_01-30-50.png)

![](../../../../assets/assets/figures/2021-10-29_01-31-06.png)

:::{.remark title="Showing a singularity is removable"}
Either expand $f(z) = \sum_{k\in\ZZ} c_k z^k$ and show $c_k = 0$ for $k<0$, or show $f$ is bounded near $z_0$ and quote Riemann.
The second is nearly always shorter.

:::

## Zeros and their order

[[D-65VIK]]

[[T-YKVFQ]]

:::{.remark}
Why this matters: every infinite subset of a disc has a limit point, so a holomorphic $f$ with infinitely many zeros in $\DD$ vanishes identically by the identity principle.

:::

[[PR-5A64G]]

:::{.remark}
Terminology: if the order of $z_0$ for $f$ is $n$, then $f$ **vanishes to order $n$** at $z_0$.

:::

:::{.proof title="of existence and uniqueness of the order"}
Use connectedness of $\Omega$ to find a neighborhood $U$ on which $f$ is not identically zero, and assume $z_0 = 0$.
Expand $f$ as an honest power series:
\[
f(z) = \sum_{k\geq 0}c_k z^k = z^n\qty{c_n + c_{n+1}z + \cdots} \da z^n g(z)
,\]
where $c_n$ is the minimal nonvanishing coefficient.
Since $c_n \neq 0$ and $\lim_{z\to z_0} g(z) = c_n$, $g$ is nonvanishing on a neighborhood of $z_0$.
For uniqueness, $z^n g(z) = z^m h(z)$ with $m > n$ gives $g(z) = z^{m-n}h(z)$, and letting $z\to 0$ forces $g(0) = 0$, a contradiction.

:::

[[PR-VUBCC]]

[[PR-EWOP5]]

:::{.proof}
Suppose not, and pick a limit point $z_0$ with $f(z_0)=0$ and a sequence $z_k \to z_0$ with $f(z_k)=0$ for all $k$.
Expanding in a Laurent series, since $f\not\equiv 0$ there is a smallest nonzero coefficient $c_m$:
\[
f(z) = \sum_{k\geq m}c_k (z-z_0)^k = c_m(z-z_0)^m \qty{1 + \sum_{k\geq 1}c_k' (z-z_0)^k } \da c_m(z-z_0)^m (1 + g(z-z_0))
.\]
Here $g(z-z_0)\convergesto{z\to z_0} 0$, so for $k \gg 1$ we have $g(z_k - z_0) < \eps$ and hence $1 + g(z_k-z_0) > 0$.
But then
\[
0 = f(z_k) = c_m(z_k - z_0)^m (1 + g(z_k - z_0)) \neq 0
.\]

$\contradiction$

:::

[[C-F2ZZQ]]

[[PR-ITZIT]]

## Poles

[[D-AUD6K]]

[[FD-C7EQD]] [[FD-EKGLW]]

[[D-C3JIU]]

:::{.remark}
A pole admits a neighborhood on which $f$ is nonvanishing, and in fact bounded below.

:::

[[PR-NITIQ]]

:::{.proof}
Use that $z_0$ is a zero of $1/f$ to write
\[
{1\over f(z) } = (z-z_0)^n g(z)
\]
with $g$ holomorphic and nonvanishing near $z_0$, then take reciprocals:
\[
f(z) = (z-z_0)^{-n} h(z), \qquad h(z) \da {1\over g(z)}
.\]

:::

:::{.example title="Using this characterization"}
Claim: if $f$ has a pole of order $m$ at $z_0$, then $g(z) \da f(z^2)$ has a pole of order $2m$ there.
Assume $z_0 = 0$.

By Laurent expansion: writing $f(z) = \sum_{k\geq -m} c_k z^k$ with $c_{-m} \neq 0$, substituting $z^2$ gives
\[
g(z) = \sum_{k\geq -m} c_k z^{2k}
= {c_{-m} \over z^{2m}} + \cdots
,\]
so the lowest power of $z$ appearing is $z^{-2m}$ with nonzero coefficient $c_{-m}$, which is exactly a pole of order $2m$.
By the characterization above, write $f(z) = z^{-m}h(z)$ with $h$ holomorphic and $h(0) \neq 0$; then $f(z^2) = z^{-2m}h(z^2)$ and $h(z^2)\mid_{z=0} = h(0) \neq 0$.

:::

## Essential

[[D-VKP6N]]

[[FD-BACTZ]] [[FD-ZPKLQ]]

:::{.example title="Essential singularities"}
$f(z) \da e^{1/z}$ has an essential singularity at $z=0$: expanding picks up infinitely many negative terms,
\[
e^{1/z} = 1 + {1\over z} + {1\over 2! z^2} + \cdots
.\]
There is in fact a neighborhood of zero with $f(U) = \CC\smz$.
Likewise $g(z) \da \sin\qty{1\over z}$ is essential at $z=0$, with a neighborhood $V$ satisfying $g(V) = \CC$.

:::

How much of the plane the image must cover is [[complex-analysis/singularities/casorati-weierstrass-and-picard|Casorati–Weierstrass and Picard]].

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
