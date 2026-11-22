---
title: Counterexamples
order: 9
topics:
- Counterexamples
---

# Counterexamples

Each section names a theorem or a topic; the blocks under it show a theorem failing when one of its hypotheses is dropped, or gather the examples that separate the cases.

## Liouville's theorem

[[T-QHIHJ]]

::: {.example title="Holomorphy on a proper subset"}
The function $f(z) = z$ is holomorphic and bounded on $\DD$ and not constant.
Liouville's theorem requires $f$ to be entire.
:::

::: {.example title="Boundedness on the real axis only"}
The function $f(z) = \sin z$ is entire and bounded on $\RR$, and $\abs{\sin(iy)} = \sinh\abs y\to\infty$ as $\abs y\to\infty$.
:::

::: {.remark}
The [[T-PG7ZK|polynomial-growth criterion]] does not force constancy: $f(z)=z^n$ satisfies its bound with $k=n$ and is not constant.
:::

## The identity principle

[[T-SVF2W]]

::: {.example title="A limit point outside the domain"}
The function $f(z) = \sin(\pi/z)$ is holomorphic on $\CC\smz$ and vanishes at the points $1/k$, which accumulate at $0\notin\CC\smz$, while $f\not\equiv 0$.
:::

::: {.example title="No limit point"}
Two distinct polynomials of degree at most $n$ can agree at $n$ points, and a finite set has no [[D-TFSPT|limit point]].
:::

## The maximum and minimum modulus principles

[[T-BYNL5]]

[[T-YLI6Y]]

::: {.example title="Zeros in the minimum modulus principle"}
The function $f(z) = z$ is nonconstant on $\DD$, and $\abs f$ attains its minimum at the interior point $0$, a zero of $f$.
:::

::: {.example title="An unbounded domain"}
On the strip $S\coloneqq\theset{\abs{\Im z}<\pi/2}$ the function $f(z) = \exp(e^z)$ is holomorphic on $\overline S$ with $\abs f = 1$ on $\bd S$, since $e^z = \pm ie^x$ there, and $f(x) = \exp(e^x)$ is unbounded on $\RR\subseteq S$.
So a bound on $\bd S$ does not extend to $S$, and no form of the [[T-QX4MB|Phragmén--Lindelöf principle]] can drop its growth hypothesis: the sector form of the principle is on that card, and here the growth is $\abs{f(z)} = \exp(e^{\Re z}\cos\Im z)\leq\exp(e^{\abs{\Re z}})$, of the critical order that the hypothesis excludes.
:::

## The Phragmén--Lindelöf principle

[[T-QX4MB]]

## Runge's approximation theorem

[[T-8NGWE]]

## Singularities

::: {.example title="All three types on one punctured disc"}
On $\DD\smz$ the constant $1$ has a removable singularity, $1/z$ a pole, and $e^{1/z}$ an essential singularity at $0$.
:::

::: {.example title="Bounded near an undefined point"}
The function $\sin(z)/z$ is holomorphic and bounded on a punctured disc about $0$, and by [[T-ZZJDP|Riemann's removable singularity theorem]] it extends holomorphically with value $1$ at $0$.
:::

::: {.example title="Singularities outside the classification"}
The functions $\sqrt z$ and $\Log z$ have branch points at $0$ and no Laurent expansion on any punctured disc about $0$, so the classification into removable singularities, poles, and essential singularities does not apply.
The function $1/\sin(\pi/z)$ has a non-isolated singularity at $0$.
:::

## Convergence

::: {.remark}
[[T-4ALS2|Montel's theorem]] turns a family bounded on compact subsets into a locally uniformly convergent subsequence, so a sequence without such a bound is where a pointwise limit can differ from a locally uniform one.
:::

::: {.example title="Univalent maps with a constant limit"}
The functions $f_n(z) = z/n$ are injective and converge locally uniformly to $0$, so the limit of univalent functions is univalent or constant ([[T-SULVA]]).
:::

## Conformal maps

::: {.example title="$\CC$ and $\DD$ are not biholomorphic"}
A holomorphic map $\CC\to\DD$ is a bounded entire function, hence constant by [[T-QHIHJ|Liouville's theorem]]; the [[T-4MDS6|Riemann mapping theorem]] requires $\Omega\neq\CC$.
:::

::: {.example title="Nonvanishing derivative without injectivity"}
The exponential $e^z$ has derivative $e^z\neq 0$ everywhere and $e^0 = e^{2\pi i}$, so a nonvanishing derivative gives only local injectivity.
:::

::: {.example title="Injective with vanishing derivative, over $\RR$"}
The map $x\mapsto x^3$ is injective on $\RR$ with derivative $0$ at $0$, and its inverse $x^{1/3}$ is not differentiable at $0$.
An injective holomorphic function has nonvanishing derivative ([[P-Z776N]]).
:::

## Holomorphy

::: {.example title="Real differentiable and not holomorphic"}
The function $f(z) = \bar z$ is real differentiable everywhere and fails the [[complex-analysis/holomorphic-functions/the-cauchy-riemann-equations|Cauchy--Riemann equations]]; its difference quotient $\bar h/h$ depends on the direction of $h$.
:::

::: {.example title="Cauchy--Riemann equations at one point"}
The function $f(x+iy) = \sqrt{\abs{xy}}$ has $u_x = u_y = v_x = v_y = 0$ at $0$, so the Cauchy--Riemann equations hold there, while along $y = x$ the difference quotient is $\abs x/\bigl((1+i)x\bigr)$, which has no limit as $x\to 0$.
:::

::: {.example title="Invertible real Jacobian without conformality"}
The function $f(z) = \bar z$ has invertible real Jacobian at every point and reverses signed angles, whereas a [[D-TM4TE|conformal map]] is holomorphic with nonvanishing derivative.
:::
