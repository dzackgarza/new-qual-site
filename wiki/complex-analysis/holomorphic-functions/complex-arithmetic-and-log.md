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

::: {.fact title="Complex roots of a number"}
The $n$th roots of $z \coloneqq r e^{i\theta}\neq 0$ are
$$
z = re^{i\theta} = re^{i\qty{\theta + 2k\pi}} \implies z^{1/n} =
\qty{ re^{i\qty{\theta + 2k\pi}} }^{1\over n} = r^{1\over n} e^{i\qty{\theta + 2k\pi \over n}},
\qquad
\theset{ \omega_k \coloneqq r^{1/n} e^{i \qty{ \theta + 2k\pi \over n} } \st 0 \leq k \leq n-1 }.
$$
The roots have modulus $r^{1/n}$ and are spaced by angles of $2\pi/n$.
Writing the argument as $\theta + 2k\pi$ before taking the root produces all $n$ of them.

:::

::: {.fact}
Since $\CC$ is algebraically closed, every polynomial in $\CC[x]$ factors into linear factors.

:::

## The logarithm

[[D-4CSPM]]

[[D-T6INB]]

::: {.fact}
For $f$ holomorphic with values in $\CC\sm(-\infty, 0]$, $f^{1/n} \coloneqq e^{{1\over n}\Log f}$ with the principal branch $\Log$ is a holomorphic $n$th root of $f$.

:::

[[PR-MWUJS]]

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

[[P-Y5SS5]]

## The quadratic formula over $\CC$

For $a\neq 0$, the roots of $az^2+bz+c$ are $\frac{-b\pm w}{2a}$, where $w$ is either square root of $\Delta \coloneqq b^2-4ac\in\CC$.

## Exercises

[[P-4GDBQ]]
[[P-LHZGV]]
[[E-X4MBB]]
[[E-WNNSK]]
[[E-P7SIB]]
[[E-JWO2G]]
[[E-QVMUV]]
