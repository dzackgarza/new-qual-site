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
The function $f(z)\coloneqq z^{1\over 2}$ has no holomorphic branch on any punctured disc about $0$, so $f$ has no Laurent expansion there and $z=0$ is not an isolated singularity of a single-valued holomorphic function; it is a branch point.
The same holds at $z=0$ and $z=1$ for $\qty{z(z-1)}^{1\over 2}$, and at $z=0$ for $\Log(z)$.
:::

::: {.example title="Isolated and non-isolated singularities"}
A rational function has only isolated singularities, since a nonzero polynomial has finitely many zeros.

$\Log(z)$ has a singularity at $z=0$ that is not isolated: every neighborhood of $0$ meets the branch cut $(-\infty,0)$, where $\Log$ is not continuous.

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

In terms of the order of [[D-IWIA5]], a zero of order $n$ has $v_{z_0}(f) = n$, a pole of order $n$ has $v_{z_0}(f) = -n$, a removable singularity has $v_{z_0}(f)\geq 0$, and an essential singularity has $v_{z_0}(f) = -\infty$.

## Summary

| Available information | Criterion |
| --- | --- |
| an explicit elementary $f$ | the limit criterion |
| a bound for $\abs f$ near $z_0$ | the boundedness criterion |
| a Laurent series, or the order is needed | the Laurent series criterion |
| $p/q$ with $p(z_0) = q(z_0) = 0$ and $q'(z_0)\neq 0$ | the limit criterion: removable, with value $p'(z_0)/q'(z_0)$ |
| an essential singularity | the Laurent series criterion, or two paths with different limiting behavior |

## Singularities at infinity

[[D-BPBSQ]]

The type of the singularity of $f$ at $\infty$ is the type of the singularity of $g(w)\coloneqq f(1/w)$ at $w=0$, so the limit, boundedness, and Laurent series criteria apply to $g$.
