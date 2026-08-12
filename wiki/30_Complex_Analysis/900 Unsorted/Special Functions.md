# Special Functions

## Transforms

:::{.remark}

\[
\hat{f}(\xi) \da \int_\RR e^{-i\xi x} f(x)\dx \\
f(x) = {1\over 2\pi}\int_\RR e^{i\xi x} \hat{f}(\xi) \dxi 
.\]

![](../../../../assets/assets/figures/2021-12-20_07-55-38.png)

:::

## The Gamma Function

[[D-TKGVZ]]

:::{.remark}
Some interesting properties of $\Gamma$:
$\Gamma(z+1) = z\Gamma(z)$ and has simple poles at $z=0,-1,-2,\cdots$ with residues $\Res_{z=-m} \Gamma(z) = (-1)^m/m!$.
There is also a factorization
\[
\Gamma(z) = {1 \over ze^{\gamma z} \prod_{n=1}^\infty \qty{1 + {z\over n}}e^{-z\over n} }
\]
where $\gamma \da \lim_{N\to\infty } \sum_{n=1^N} {1\over n} - \log(N)$

\[
\Gamma(z) \Gamma(1-z) = {\pi \over \sin(\pi z)}
,\]
which yields a product factorization for $\sin(\pi z)$.

$\mcl(t^{z-1}, s=1) = \Gamma(z)$ and $\mcl(t^n, s=1) = \Gamma(n+1)$.

The residues:

![](../../../../assets/assets/figures/2021-12-19_19-59-45.png)

:::

[[PR-NLV6Q]]

[[PR-FBQ6F]]

[[PR-YQZI3]]

## The Beta Function

[[D-2WZLB]]

[[E-I6CYR]]
## Riemann Zeta

[[D-HJYH3]]

[[PR-K4KTF]]

[[PR-QHFCK]]

## Weierstrass $\wp$

[[D-LGP2Q]]

:::{.remark}

![](../../../../assets/assets/figures/2021-12-19_22-34-18.png)

:::

# Elliptic Functions

#todo

## Infinite Series and Products

:::{.fact title="Infinite products"}

![](../../../../assets/assets/figures/2021-12-14_17-36-04.png)

:::


[[T-2WJ4U]]


[[E-DR5LY]]
[[T-IEJFA]]

:::{.remark}
An interesting way to sum infinite series:

\[
\sum_{n=-\infty}^{\infty} f(n) &=-(\operatorname{sum} \quad \text { of } \quad \text { residues } \quad \text { of } \quad \pi \cot \pi z f(z)) \\
\sum_{n=-\infty}^{\infty}(-1)^{n} f(n) &=-(\operatorname{sum} \quad \text { of } \quad \text { residues } \quad \text { of } \quad \pi \csc \pi z f(z)) \\
\sum_{n=-\infty}^{\infty} f\left(\frac{2 n+1}{2}\right) &=(\operatorname{sum} \quad \text { of } \quad \text { residues of } \quad \pi \tan \pi z f(z)) \\
\sum_{n=-\infty}^{\infty}(-1)^{n} f\left(\frac{2 n+1}{2}\right) &=(\operatorname{sum} \quad \text { of residues of } \pi \sec \pi z f(z)) .
.\]

:::

[[E-2GYXM]]
[[E-NTKTA]]
[[E-ARVUV]]
[[E-4WFQM]]
[[E-6XPQW]]
[[E-26QQP]]
[[E-VA3OK]]
