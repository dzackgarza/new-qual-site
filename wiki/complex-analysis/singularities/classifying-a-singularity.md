---
title: Classifying a singularity
order: 0
topics:
- Singularities
- Isolated Singularities
---

# Classifying a singularity

An isolated singularity of a holomorphic function is removable, a pole, or essential.
Three criteria decide which: a bound on $\abs f$ near $z_0$, the behaviour of $f(z)$ as $z\to z_0$, and the negative part of the Laurent series; they are the same three conditions, and which one to use depends on what is known about $f$.

## Isolated and non-isolated singularities

[[D-IWIA5]]

::: {.example title="Branch points"}
The function $z\mapsto z^{1/2}$ has no holomorphic branch on any punctured disc about $0$, so it has no Laurent expansion there and $0$ is not an isolated singularity of a single-valued holomorphic function; it is a [[D-9KMTV|branch point]].
The same holds at $z=0$ and $z=1$ for $\qty{z(z-1)}^{1\over 2}$, and at $z=0$ for $\Log(z)$.
:::

::: {.example title="Isolated and non-isolated singularities"}
A rational function has only isolated singularities, since a nonzero polynomial has finitely many zeros.

$\Log(z)$ has a singularity at $z=0$ that is not isolated: every neighborhood of $0$ meets the ray $(-\infty,0]$, on which $\Log$ has no values, so no punctured disc about $0$ lies in its domain.

$G(z)\coloneqq 1/\sin(\pi/z)$ has isolated singularities at the points $1/n$, $n\in\ZZ\sm\theset{0}$, and a non-isolated singularity at $0$, where they accumulate.
:::

## The limit criterion

[[FF-QZXBS]]

::: {.example title="Two paths with different limits"}
For $e^{1/z}$ at $0$ the limit along $\RR_{>0}$ is $\infty$, since $e^{1/x}\to\infty$ as $x\to0^+$, and the limit along $\RR_{<0}$ is $0$.
So $\lim_{z\to0}\abs{e^{1/z}}$ exists neither in $\CC$ nor as $\infty$, and $0$ is an essential singularity.
:::

## The boundedness criterion

[[T-ZZJDP]]

The criterion uses only a bound on $\abs f$, so it applies when $\abs f$ can be estimated but not evaluated, for instance to show that a function extends to an entire function.

## The Laurent series criterion

[[D-C3JIU]]

The [[D-IWIA5|order of $f$ at $z_0$]] reads the type off the expansion: the criterion is the proposition on that card.

## Summary

| Available information | Criterion |
| --- | --- |
| an explicit elementary $f$ | the limit criterion |
| a bound for $\abs f$ near $z_0$ | the boundedness criterion |
| a Laurent series, or the order is needed | the Laurent series criterion |
| an essential singularity | the Laurent series criterion, or two paths with different limiting behavior |

::: {.example title="A quotient with a common zero"}
If $p(z_0) = q(z_0) = 0$ and $q'(z_0)\neq 0$, then $p'(z_0)$ is the limit of $p(z)/(z-z_0)$ and $q'(z_0)$ that of $q(z)/(z-z_0)$, so $p/q$ has the finite limit $p'(z_0)/q'(z_0)$ and $z_0$ is removable, the extension taking that value.
:::

## Singularities at infinity

[[D-BPBSQ]]

So the limit, boundedness, and Laurent series criteria apply to $g$ at $w=0$, and the type at $\infty$ is read off there.
