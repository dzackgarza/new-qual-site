---
title: Complex arithmetic and the logarithm
order: 10
topics:
- Complex Numbers
- Complex Logarithm
- Trigonometry
- Hyperbolic Functions
---

# Complex arithmetic and the logarithm

## Roots

[[D-YKB3V]]

::: {.fact title="Complex roots of a number"}
The $n$th roots of $z \coloneqq r e^{i\theta}\neq 0$ are
$$
z = re^{i\theta} = re^{i\qty{\theta + 2k\pi}} \implies z^{1/n} =
\qty{ re^{i\qty{\theta + 2k\pi}} }^{1\over n} = r^{1\over n} e^{i\qty{\theta + 2k\pi \over n}},
\qquad
\ts{ \omega_k \coloneqq r^{1/n} e^{i \qty{ \theta + 2k\pi \over n} } \st 0 \leq k \leq n-1 }.
$$
The roots have modulus $r^{1/n}$ and are spaced by angles of $2\pi/n$.
Writing the argument as $\theta + 2k\pi$ before taking the root produces all $n$ of them.

:::

::: {.fact}
Since $\CC$ is algebraically closed, every polynomial in $\CC[x]$ factors into linear factors.

:::

## The logarithm

::: {.fact title="Complex log"}
For $z = re^{i\theta}\neq 0$, the angle $\theta$ has the form $\Theta + 2k\pi$ with $\Theta = \Arg z\in(-\pi,\pi]$.
The principal logarithm and principal powers are
$$
\log(z) = \ln\abs{z} + i\Arg(z), \qquad z^c \coloneqq e^{c\log(z)},
$$
and $\ln r + i\theta$ is a value of $\log(re^{i\theta})$ for every choice of $\theta$.

:::

::: {.fact}
For $f$ holomorphic with values in $\CC\sm(-\infty, 0]$, $f^{1/n} \coloneqq e^{{1\over n}\log f}$ with the principal branch of $\log$ is a holomorphic $n$th root of $f$.

:::

The multivalued formula defines a holomorphic function only on a domain that admits a continuous choice of argument.
On the slit plane $\CC\sm(-\infty,0]$, the choice $-\pi<\arg z<\pi$ gives the principal branch, and every simply connected domain not containing $0$ admits a holomorphic logarithm.
Once a branch of $\log$ is fixed, $z^\alpha\coloneqq e^{\alpha\log z}$, and a different branch of $\log$ multiplies $z^\alpha$ by $e^{2\pi i k\alpha}$ for some $k\in\ZZ$.

[[PR-MWUJS]]

[[D-4CSPM]]

[[D-OMBQT]]

[[D-T6INB]]

For a nonvanishing holomorphic function $f$ on a domain $\Omega$, a holomorphic logarithm $g$ of $f$ satisfies $g'=f'/f$, so $\int_\gamma f'/f = 0$ for every closed curve $\gamma$ in $\Omega$.
Conversely, if $\int_\gamma f'/f=0$ for every closed curve $\gamma$ in $\Omega$, then $f'/f$ has a primitive $g$, and adjusting $g$ by a constant gives $e^g = f$.
On a simply connected domain these integrals vanish by Cauchy's theorem, which gives the existence theorem for logarithms and roots of nonvanishing functions:

[[T-NRSFZ]]

## Branch cuts and branch points

::: {.warnings}
The formula
$$
z^{1\over n} \coloneqq (re^{i\theta})^{1\over n} = r^{1\over n} e^{i\theta \over n}
$$
depends on the choice of $\theta$, and a choice continuous in $z$ exists only after removing a branch cut.

:::

::: {.remark title="Where continuity fails"}
Take $z \coloneqq x + i0$ with $x <0$, and approach it from either side along $z_\pm \coloneqq x \pm i\varepsilon$ as $\varepsilon\to 0^+$.
For the principal branch:

- $\log(z_+) \to \ln\abs x + i\pi$,
- $\log(z_-) \to \ln\abs x - i\pi$.

So no value at $z$ makes $\log$ continuous across the negative real axis.
The point $z=0$ is a \dfn{branch point}: $\log$ has no continuous branch on any punctured neighborhood of the origin, whatever cut is chosen.

:::

[[T-E76LX]]

## The quadratic formula over $\CC$

For $a\neq 0$, the roots of $az^2+bz+c$ are $\frac{-b\pm w}{2a}$, where $w$ is either square root of $\Delta \coloneqq b^2-4ac\in\CC$.
The sign of $\Delta$ plays no role: a quadratic over $\CC$ has two roots counted with multiplicity.

## Exercises

[[P-4GDBQ]]
[[P-LHZGV]]
[[P-Y5SS5]]
[[E-X4MBB]]
[[E-WNNSK]]
[[E-P7SIB]]
[[E-JWO2G]]
[[E-QVMUV]]
