---
title: Real integrals by residues
order: 40
topics: [Contour Integration]
---

# Real integrals by residues

Worked evaluations and exercises, grouped by the contour cases on [[complex-analysis/residues-and-contours/which-contour-do-i-close|Which contour do I close?]].
The evaluations every qual expects are on [[complex-analysis/standard-integrals|Standard integrals]], and the estimates that close the arcs are on [[complex-analysis/residues-and-contours/arc-estimates|Arc estimates]].

## Rational, superlinear decay

Upper semicircle; the arc integral tends to $0$ by the [[T-SFXI7|ML estimate]].

::: {.example title="$\displaystyle\int_\RR{\dx\over 1+x^4} = {\pi\over\sqrt 2}$"}
The [[D-AUD6K|poles]] of $1/(1+z^4)$ are the fourth roots of $-1$, of which $e^{i\pi/4}$ and $e^{3i\pi/4}$ lie in $\HH$, and the [[D-C3JIU|residue]] at a [[D-AUD6K|simple pole]] $z_0$ is $1/(4z_0^3) = -z_0/4$ by [[PR-L4Y5F]], since $z_0^4 = -1$.
The two residues sum to $-\qty{e^{i\pi/4}+e^{3i\pi/4}}/4 = -i\sqrt2/4$, so the integral is $2\pi i\cdot(-i\sqrt2/4) = \pi\sqrt2/2 = \pi/\sqrt2$.
:::

[[E-SS3.EX-2]]
[[E-SS3.EX-6]]
[[E-JZNWV]]

## Rational against $e^{iz}$

Upper semicircle applied to $f(z)e^{iz}$; the arc integral tends to $0$ by [[T-ZO5UU|Jordan's lemma]].

::: {.example title="$\displaystyle\int_\RR{x\sin x\over x^2+1}\,\dx = {\pi\over e}$"}
The function $ze^{iz}/(z^2+1)$ has simple poles at $\pm i$, and only $z=i$ lies in $\HH$, with residue
$$
\Res_{z=i}{ze^{iz}\over z^2+1} = {ie^{i\cdot i}\over 2i} = {e^{-1}\over 2}.
$$
The integrand on $\abs z = R$ is $\bigo(1/R)$ and $\abs{e^{iz}}\leq 1$ on $\HH$, so the arc vanishes by Jordan's lemma, and
$$
\int_\RR{xe^{ix}\over x^2+1}\dx = 2\pi i\cdot{e^{-1}\over 2} = {\pi i\over e},
$$
whose imaginary part is the value.
:::

[[E-SS3.EX-4]]
[[E-SS3.EX-3]]

## No clear decay

Sectors and rectangles, determined by a rotation or translation symmetry of the integrand.

[[E-YYRZX]]
[[E-AIQEU]]

## Singularities on the line: principal values

[[T-SSNLT]]

[[D-PV4RQ]]

[[E-ZGZYQ]]
[[E-DUK6M]]

## Rational functions of $\cos$ and $\sin$

The unit circle, through $z = e^{i\theta}$.

::: {.example}
For real $a$ with $\abs a<1$, the only pole of the integrand inside $S^1$ is $z=a$:
$$
\int_{0}^{2 \pi} \frac{\dtheta}{1+a^{2}-2 a \cos \theta}=\int_{S^{1}} \frac{i \dz}{(z-a)(a z-1)}=2 \pi i\left(i /\left(a^{2}-1\right)\right)=\frac{2 \pi}{1-a^{2}}
.$$

:::

[[E-BEIHP]]
[[E-SS3.EX-8]]

## Branch cuts: logarithms

::: {.example title="$\displaystyle\int_0^\infty{\log x\over 1+x^3}\dx = -{2\pi^2\over 27}$"}
The logarithm is the derivative in the exponent of the power integral: for $0<a<n$,
$$
\int_0^\infty{x^{a-1}\over 1+x^n}\dx = {\pi/n\over\sin(\pi a/n)},
$$
whose value for a *single* $a$ comes from the keyhole or sector contour with the branch cut, and differentiating in $a$ gives
$$
\int_0^\infty{x^{a-1}\log x\over 1+x^n}\dx = -{\pi^2\over n^2}{\cos(\pi a/n)\over\sin^2(\pi a/n)}.
$$
At $a=1$ and $n=3$ this is $-(\pi^2/9)\cot(\pi/3)\csc(\pi/3) = -(\pi^2/9)\cdot{1\over\sqrt3}\cdot{2\over\sqrt3} = -2\pi^2/27$, and numerically the integral is $-0.7310818\ldots$ either way.
Differentiating under the integral sign is justified on any compact interval of $a$ inside $(0,n)$, where $x^{a-1}\abs{\log x}/(1+x^n)$ is integrable and bounds the derivative.
:::

[[E-SS3.EX-10]]
[[P-3JE4U]]
[[P-CAEXAMPREP-05]]
[[E-HHSCS]]

## Branch cuts: powers

::: {.example}
For $-1<a<1$ with $a\neq 0$, with the branch $\arg z\in(0,2\pi)$ on the keyhole contour, the poles $i$ and $-i$ have $z^a = e^{\pi i a/2}$ and $e^{3\pi i a/2}$.
Setting $\omega \coloneqq e^{\pi i a \over 2}$,
$$
\int_{0}^{\infty} \frac{x^{a}}{1+x^{2}} \dx =
\frac{2\pi i}{1-e^{2\pi i a}}\left(\frac{\omega}{2i}-\frac{\omega^{3}}{2i}\right)=\pi \frac{\omega-\omega^{3}}{1-\omega^{4}}=\frac{\pi}{\omega+\omega^{-1}}=\frac{\pi}{2 \cos (\pi a / 2)}
.$$

:::

[[E-YAMX6]]
[[E-2HIKG]]

## Square roots and slits

::: {.concept}
For $f(z) = \sqrt{(z-z_1)(z-z_2)\cdots(z-z_n)}$, a branch exists on the complement of slits that prevent closed curves from winding around an odd number of the [[D-9KMTV|branch points]] $z_k$; for $n$ odd, $z=\infty$ is also a branch point.

Continuing the germ of $\sqrt{z}$ at $z_0$ once counterclockwise about $0$ along $\gamma(t) = z_0e^{2\pi it}$, $t\in[0,1]$, returns $-\sqrt{z_0}$: the continuation is $\sqrt{z_0e^{2\pi i}} = e^{i\pi}\sqrt{z_0}$, because the argument has grown by $2\pi$ while the modulus returns to $\abs{z_0}$.

:::

[[E-L3MG4]]
[[E-EBRU5]]
[[E-GPCW2]]
[[E-XYEP4]]
[[E-KZV2Z]]
