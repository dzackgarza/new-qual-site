---
order: 121
title: Special functions
---

# Special functions

## Transforms

[[D-5LZQ4]]

::: {.remark title="Normalization"}
With the normalization
$$
\hat{f}(\xi) \coloneqq \int_\RR e^{-i\xi x} f(x)\dx = \mcl(f)(i\xi),
$$
where $\mcl$ is the two-sided Laplace transform,
the inversion formula reads
$$
f(x) = {1\over 2\pi}\int_\RR e^{i\xi x} \hat{f}(\xi) \dxi.
$$

The one-sided Laplace transform $\mcl(f)(p)=\int_0^\infty e^{-pt}f(t)\,dt$ of standard functions, for $\Re p$ large enough:

| $f(t)$ | $\mcl(f)(p)$ | $f(t)$ | $\mcl(f)(p)$ |
| --- | --- | --- | --- |
| $1$ | $\dfrac1p$ | $t^n$ | $\dfrac{n!}{p^{n+1}}$ |
| $e^{\lambda t}$ | $\dfrac1{p-\lambda}$ | $t^ne^{\lambda t}$ | $\dfrac{n!}{(p-\lambda)^{n+1}}$ |
| $\sin\omega t$ | $\dfrac{\omega}{p^2+\omega^2}$ | $\cos\omega t$ | $\dfrac{p}{p^2+\omega^2}$ |
| $\sinh\lambda t$ | $\dfrac{\lambda}{p^2-\lambda^2}$ | $\cosh\lambda t$ | $\dfrac{p}{p^2-\lambda^2}$ |
| $e^{\lambda t}\sin\omega t$ | $\dfrac{\omega}{(p-\lambda)^2+\omega^2}$ | $e^{\lambda t}\cos\omega t$ | $\dfrac{p-\lambda}{(p-\lambda)^2+\omega^2}$ |
| $\delta(t)$ | $1$ | $\delta(t-t_0)$ | $e^{-pt_0}$ |

:::

## The Gamma function

[[D-Q3MYK]]

[[PR-NLV6Q]]

[[PR-FBQ6F]]

[[PR-YQZI3]]

The integral defines $\Gamma$ on the right half-plane $\Re z>0$, and the functional equation $\Gamma(z+1) = z\Gamma(z)$, written as $\Gamma(z) = \Gamma(z+n)/\qty{z(z+1)\cdots(z+n-1)}$, continues $\Gamma$ meromorphically to $\Re z > -n$ for each $n$ and locates its poles.

::: {.remark title="Properties of $\Gamma$"}
$\Gamma$ has simple poles at $z=0,-1,-2,\ldots$ with residues $\Res_{z=-m} \Gamma(z) = (-1)^m/m!$, and no other poles.
It has the product expansion
$$
\Gamma(z) = {1 \over ze^{\gamma z} \prod_{n=1}^\infty \qty{1 + {z\over n}}e^{-z/n} },
\qquad
\gamma \coloneqq \lim_{N\to\infty } \qty{\sum_{n=1}^N {1\over n} - \log(N)},
$$
and satisfies the reflection formula
$$
\Gamma(z) \Gamma(1-z) = {\pi \over \sin(\pi z)},
$$
which together with the product expansion gives a product expansion of $\sin(\pi z)$.
In terms of the Laplace transform $\mcl$, $\mcl(t^{z-1})(1) = \Gamma(z)$ for $\Re z>0$, and $\mcl(t^n)(1) = \Gamma(n+1) = n!$.

By the reflection formula, $1/\Gamma(z)=\Gamma(1-z)\sin(\pi z)/\pi$ is entire: the simple poles of $\Gamma(1-z)$ at $z=1,2,3,\ldots$ cancel the simple zeros of $\sin(\pi z)$ there.
So $1/\Gamma$ is entire, and its zeros are exactly the simple zeros at $z=0,-1,-2,\ldots$.

:::

## The Beta function

[[D-2WZLB]]

[[E-SS6.EX-7]]

## The Riemann zeta function

[[D-HJYH3]]

[[PR-K4KTF]]

[[PR-QHFCK]]

The Dirichlet series and the Euler product for $\zeta$ converge absolutely on $\Re s>1$, and the Euler product shows $\zeta(s)\neq 0$ there.
The continuation extends $\zeta$ meromorphically to $\CC$, and the functional equation relates the values, and hence the zeros, at $s$ and $1-s$.

## The Weierstrass $\wp$-function

[[D-LGP2Q]]

::: {.remark}
The series defining $\wp$ converges uniformly on compact subsets of $\CC\setminus\Lambda$, so it can be differentiated term by term:
$$
\wp'(z) = -2\sum_{\omega\in\Lambda}{1\over (z-\omega)^3}.
$$
This series is visibly invariant under $z\mapsto z+\omega$ for $\omega\in\Lambda$, and $\wp$ and all its derivatives are doubly periodic: $\wp(z+\omega)=\wp(z)$ for every $\omega\in\Lambda$.
:::

## Elliptic functions

Recall that for a lattice $\Lambda=\omega_1\ZZ+\omega_2\ZZ$ with $\omega_1/\omega_2\notin\RR$, an [[D-CRVWEIER|elliptic function]] is a meromorphic function $f$ on $\CC$ with $f(z+\omega)=f(z)$ for every $\omega\in\Lambda$.
The Weierstrass $\wp$-function is elliptic, with a double pole at each lattice point and no other poles.

[[E-4NGIV]]

[[E-WXHMJ]]

## Infinite series and products

::: {.fact title="Infinite products"}
Let $z_j\in\CC$ with $z_j\neq -1$ for every $j$, and let $\Log$ be the principal branch of the logarithm.

- $\prod_{j=1}^\infty(1+z_j)$ converges to a nonzero limit if and only if $\sum_{j=1}^\infty\Log(1+z_j)$ converges.

- $\prod_{j=1}^\infty(1+z_j)$ converges absolutely, meaning that $\sum_{j=1}^\infty\abs{\Log(1+z_j)}$ converges, if and only if $\sum_{j=1}^\infty\abs{z_j}$ converges.
:::

[[T-IEJFA]]

[[T-2WJ4U]]

The Weierstrass factorization theorem gives an entire function with prescribed zeros as a convergent product of elementary factors, unique up to multiplication by $e^{g}$ with $g$ entire.
For an entire function of finite order $\rho$, the Hadamard factorization theorem uses elementary factors of degree at most $\lfloor\rho\rfloor$ and restricts $g$ to a polynomial of degree at most $\rho$.

[[E-DR5LY]]

::: {.proposition title="Summing series by residues"}
Let $f$ be meromorphic on $\CC$ with finitely many poles, none at the points where the series below are sampled, and suppose $\abs{z^2 f(z)}$ is bounded for $\abs z$ large.
Then, with each sum on the right taken over the poles of $f$,
$$
\begin{aligned}
\sum_{n=-\infty}^{\infty} f(n) &= -\sum \Res\qty{\pi \cot (\pi z) f(z)}, \\
\sum_{n=-\infty}^{\infty}(-1)^{n} f(n) &= -\sum \Res\qty{\pi \csc (\pi z) f(z)}, \\
\sum_{n=-\infty}^{\infty} f\qty{\frac{2 n+1}{2}} &= \sum \Res\qty{\pi \tan (\pi z) f(z)}, \\
\sum_{n=-\infty}^{\infty}(-1)^{n} f\qty{\frac{2 n+1}{2}} &= \sum \Res\qty{\pi \sec (\pi z) f(z)}.
\end{aligned}
$$
:::

[[E-SS3.EX-12]]
[[P-CM16-S2-14]]
[[E-26QQP]]
[[E-VA3OK]]
