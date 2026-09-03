---
title: Classifying a singularity
order: 0
topics:
- Singularities
- Isolated Singularities
---

# Classifying a singularity

A point where $f$ misbehaves is one of four things, and the exam question is almost always which one.
There are three tests, they cost different amounts, and the right one depends on what you can compute.

## First: is it isolated?

The removable/pole/essential classification applies only to an *isolated* singularity, and a problem that hands you a branch is testing whether you noticed.

::: {.warnings title="Branch singularities"}
$f(z) \da z^{1\over 2}$ has a singularity at $z=0$ that admits no Laurent expansion, so it is not in the classification at all: $z=0$ is a **branch singularity**. So is each of $z = 0, 1$ for $\qty{z(z-1)}^{1\over 2}$, and $z=0$ for $\Log(z)$.
:::

::: {.example title="Isolated, and not"}
A rational function has only isolated singularities, since a polynomial has finitely many zeros.

$\Log(z)$ has a singularity at $z=0$ that is not isolated: every neighborhood meets the branch cut $(-\infty, 0)$, where $\Log$ is not defined at all.

$G(z) \da 1/\sin(\pi/z)$ has isolated singularities at every $1/n$, and a non-isolated one at $0$, since the others accumulate there.
:::

## The limit test: fastest, and usually enough

Take $z \to z_0$ and see what happens:

- $\lim_{z\to z_0} f(z)$ exists and is finite: **removable**.

- $\lim_{z\to z_0} \abs{f(z)} = \infty$: **pole**.

- the limit does not exist, even as $\infty$: **essential**.

The three cases are exhaustive for an isolated singularity, which is why the test always terminates.
Reach for it first; on $\sin(z)/z$ or $1/(z-1)^3$ it settles the question in one line.

Its weakness is the essential case, where "the limit does not exist" has to be *proved*, usually by exhibiting two paths with different limits.
For $e^{1/z}$ at $0$: along $\RR_{>0}$ it blows up, along $\RR_{<0}$ it goes to $0$.

## The boundedness test: for removability without a limit

Riemann's theorem says bounded near $z_0$ is already enough: the singularity is removable and $f$ extends holomorphically.
You never have to produce the limiting value.

Use this whenever you can estimate $\abs f$ but cannot evaluate it, which is the usual shape of a qual problem that says "show $f$ extends to an entire function".

## The Laurent test: the only one that gives the order

Expand $f(z) = \sum_{k\in \ZZ} c_k (z-z_0)^k$ on a punctured disc and count the negative terms:

- none, so $c_{k} = 0$ for $k \leq -1$: **removable**.

- finitely many, the lowest being $k = -N$: a **pole of order $N$**.

- infinitely many: **essential**.

This is the most expensive test and the most informative: the other two say which kind, this one says which order, and the order is what a residue computation needs next.

::: {.remark title="Order as a valuation"}
Writing $f(z) = \sum_{k\in\ZZ} a_k(z-a)^k$ about $a$, set $v_a(f) = n$ when $a_n \neq 0$ and $a_k = 0$ for all $k < n$: the lowest power of $(z-a)$ that occurs.
Then a zero of order $n$ is $v_a(f) = n$, a pole of order $n$ is $v_a(f) = -n$, removable is $v_a(f) \geq 0$, and essential is $v_a(f) = -\infty$.
The three cases are one number.
:::

## Which test to use

| You are given | Use | Because |
| --- | --- | --- |
| an explicit elementary $f$ | the limit test | one evaluation settles it |
| a bound, or an estimate near $z_0$ | boundedness | Riemann needs nothing else |
| a series, or you need the order | Laurent | it is the only test that returns $N$ |
| $p/q$ with $p(z_0) = q(z_0) = 0$ | the limit test | it is removable, with value $p'(z_0)/q'(z_0)$ |
| a function you must show is *essential* | Laurent, or two paths | non-existence of a limit needs a witness |

## Singularities at infinity

The classification at $z=\infty$ is the classification of $g(w) \da f(1/w)$ at $w = 0$, and every test above applies unchanged after that substitution.
