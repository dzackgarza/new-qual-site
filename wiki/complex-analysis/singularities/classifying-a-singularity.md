---
title: Classifying a singularity
order: 0
topics:
- Singularities
- Isolated Singularities
---

# Classifying a singularity

An isolated singularity of a holomorphic function is removable, a pole, or essential.
Three criteria decide the type: the behavior of $f(z)$ as $z\to z_0$, boundedness near $z_0$, and the negative part of the Laurent series.

## Isolated and non-isolated singularities

The classification into removable singularities, poles, and essential singularities applies to isolated singularities.

::: {.example title="Branch points"}
$f(z) \coloneqq z^{1\over 2}$ has no holomorphic branch on any punctured disc about $0$, so $f$ has no Laurent expansion there and $z=0$ is not an isolated singularity of a single-valued holomorphic function; it is a branch point.
The same holds at $z = 0$ and $z = 1$ for $\qty{z(z-1)}^{1\over 2}$, and at $z=0$ for $\Log(z)$.
:::

::: {.example title="Isolated and non-isolated singularities"}
A rational function has only isolated singularities, since a nonzero polynomial has finitely many zeros.

$\Log(z)$ has a singularity at $z=0$ that is not isolated: every neighborhood of $0$ meets the branch cut $(-\infty, 0)$, where $\Log$ is not continuous.

$G(z) \coloneqq 1/\sin(\pi/z)$ has isolated singularities at the points $1/n$, $n\in\ZZ\sm\ts{0}$, and a non-isolated singularity at $0$, where they accumulate.
:::

## The limit criterion

For an isolated singularity $z_0$ of $f$:

- **Removable.** $\lim_{z\to z_0} f(z)$ exists in $\CC$.

- **Pole.** $\lim_{z\to z_0} \abs{f(z)} = \infty$.

- **Essential.** Neither limit exists.

The cases are exhaustive and mutually exclusive.
For example, $\sin(z)/z \to 1$ as $z\to 0$, and $\abs{1/(z-1)^3}\to\infty$ as $z\to 1$.

Showing that neither limit exists requires, for instance, two paths along which $f$ has different limiting behavior.
For $e^{1/z}$ at $0$: along $\RR_{>0}$, $e^{1/z}\to\infty$, and along $\RR_{<0}$, $e^{1/z}\to 0$.

## The boundedness criterion

By Riemann's removable singularity theorem, if $f$ is bounded on a punctured neighborhood of $z_0$, then the singularity is removable and $f$ extends holomorphically across $z_0$.
The criterion does not require the value of the limit, so it applies when $\abs f$ can be estimated but not evaluated, for instance to show that a function extends to an entire function.

## The Laurent series criterion

Let $f(z) = \sum_{k\in \ZZ} c_k (z-z_0)^k$ on a punctured disc about $z_0$.

- **Removable.** $c_{k} = 0$ for all $k \leq -1$.

- **Pole of order $N$.** $c_{-N}\neq 0$ and $c_k = 0$ for all $k<-N$.

- **Essential.** $c_k \neq 0$ for infinitely many $k<0$.

This criterion also gives the order of a pole and the residue $c_{-1}$.

::: {.remark title="Order as a valuation"}
For $f(z) = \sum_{k\in\ZZ} a_k(z-a)^k$ about $a$, let $v_a(f) \coloneqq \min\ts{k \st a_k\neq 0}$, with $v_a(f) = -\infty$ when infinitely many negative coefficients are nonzero.
Then a zero of order $n$ has $v_a(f) = n$, a pole of order $n$ has $v_a(f) = -n$, a removable singularity has $v_a(f) \geq 0$, and an essential singularity has $v_a(f) = -\infty$.
:::

## Summary

| Available information | Criterion |
| --- | --- |
| an explicit elementary $f$ | the limit criterion |
| a bound for $\abs f$ near $z_0$ | the boundedness criterion |
| a Laurent series, or the order is needed | the Laurent series criterion |
| $p/q$ with $p(z_0) = q(z_0) = 0$ and $q'(z_0)\neq 0$ | the limit criterion: removable, with value $p'(z_0)/q'(z_0)$ |
| an essential singularity | the Laurent series criterion, or two paths with different limiting behavior |

## Singularities at infinity

The type of the singularity of $f$ at $z=\infty$ is the type of the singularity of $g(w) \coloneqq f(1/w)$ at $w = 0$, and each criterion above applies to $g$.
