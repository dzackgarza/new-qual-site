---
title: Complex arithmetic and the logarithm
order: 10
problems:
  topics:
  - Complex Numbers
  - Complex Logarithm
  - Trigonometry
  - Hyperbolic Functions
---

# Complex arithmetic and the logarithm

## Roots

[[D-YKB3V]]

:::{.fact title="Complex roots of a number"}
The $n$th roots of $z \da r e^{i\theta}$ are
\[
z = re^{i\theta} = re^{i\qty{\theta + 2k\pi}} \implies z^{1/n} =
\qty{ re^{i\qty{\theta + 2k\pi}} }^{1\over n} = r^{1\over n} e^{i\qty{\theta + 2k\pi \over n}}
\leadsto
\ts{ \omega_k \da r^{1/n} e^{i \qty{ \theta + 2k\pi \over n} } \st 0 \leq k \leq n-1 }
.\]
One root is $r^{1/n}\in\RR$, and the rest are spaced by angles of $2\pi/n$.
The mnemonic is the first equality: write the angle as $\theta + 2k\pi$ *before* taking the root, and the $n$ roots appear on their own.

:::

:::{.fact}
Since $\CC$ is a field, $\CC[x]$ is a UFD, and every polynomial factors into linear terms.

:::

## The logarithm

:::{.fact title="Complex log"}
For $z = re^{i\theta}\neq 0$, the angle $\theta$ has the form $\Theta + 2k\pi$ with $\Theta = \Arg z$.
Define
\[
\log(z) = \ln\qty{\abs{z}} + i\Arg(z), \qquad z^c \da e^{c\log(z)}
,\]
so that $\log(re^{i\theta}) = \ln\abs r + i\theta$.

:::

:::{.fact}
A common move: $f^{1/n} = e^{{1\over n}\log f}$, taking a principal branch of $\log$ on $\CC\sm(-\infty, 0]$.

:::

[[PR-MWUJS]]

[[D-4CSPM]]

[[D-OMBQT]]

[[D-T6INB]]

[[T-NRSFZ]]

## Branch cuts and branch points

:::{.warnings}
It is tempting to define
\[
z^{1\over n} \da (re^{i\theta})^{1\over n} = r^{1\over n} e^{i\theta \over n}
,\]
but this needs a branch cut to be continuous.

:::

:::{.remark title="Where continuity fails"}
Take $z \da x + i0$ with $x \in \RR^{\leq 0}$, and approach from either side with $z_\pm \da x \pm i\eps$:

- $\log(z_+) = \log\abs x + i\pi$,
- $\log(z_-) = \log\abs x - i\pi$.

So no choice of value at $z$ makes $\log$ continuous across the cut.
The obstruction is the **branch point** at $z=0$, and it is not removable by a better definition: it is the statement that $\log$ has no single-valued continuous branch on any punctured neighborhood of the origin.

:::

[[T-E76LX]]

## Factoring, and the quadratic formula over $\CC$

The discriminant does not change form, but its sign no longer decides anything: $\Delta \da b^2-4ac$ has two square roots in $\CC$ either way, so a quadratic always has two roots counted with multiplicity.

## Exercises

[[P-4GDBQ]]
[[P-LHZGV]]
[[P-Y5SS5]]
[[E-X4MBB]]
[[E-WNNSK]]
[[E-P7SIB]]
[[E-JWO2G]]
[[E-QVMUV]]
