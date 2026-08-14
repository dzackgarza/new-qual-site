---
title: "Theory and Background: Conformal Maps"
sort: 0
---

# Theory and Background: Conformal Maps

:::{.remark title="Resources"}
Conformal Mapping Dictionary:

  Parts [I](http://mathfaculty.fullerton.edu/mathews/c2003/ConformalMapDictionary.1.html),[II](http://mathfaculty.fullerton.edu/mathews/c2003/ConformalMapDictionary.2.html) ,[III](http://mathfaculty.fullerton.edu/mathews/c2003/ConformalMapDictionary.3.html) ,[IV](http://mathfaculty.fullerton.edu/mathews/c2003/ConformalMapDictionary.4.html), and [V](http://mathfaculty.fullerton.edu/mathews/c2003/ConformalMapDictionary.5.html)

:::

## Conformal Map Facts

:::{.remark}
It's a theorem that holomorphic and $f'\neq 0$ implies conformal.
Write $f(z+\eps) = f(z) + \eps f'(z) + \bigo(\eps^2)$, then
\[
\Arg(f(z+\eps) - f(z)) \approx \Arg(\eps f'(z)) = \Arg(\eps) + \Arg(f'(z))\to \Arg(f'(z))
,\]
so all tangent vectors near $z_0$ are rotated by approximately the same angle $f'(z_0)$, preserving their relative angles.

:::

[[D-TM4TE]]

:::{.fact title="Checking if a map is conformal"}
To check if a map is conformal at $p$, it *suffices* to check that $f'(p)\neq 0$.

:::

:::{.remark}
Conformal implies holomorphic, and a bijective conformal map has conformal inverse automatically.
Importantly, bijective holomorphic maps always have holomorphic inverses.
Self-biholomorphisms of a domain $\Omega$ form a group $\Aut_\CC(\Omega)$.

:::

:::{.remark}
The bijectivity condition can be weakened: an *injective* holomorphic map satisfies $f'(z) \neq 0$ and $f ^{-1}$ is well-defined on its range and holomorphic.

:::

## The Cross-Ratio Construction

[[PR-AQ6YR]]

## Linear Fractional/Mobius Transformations

[[D-FRVBV]]

:::{.remark title="Mobius transformations as projective linear automorphisms"}
Using that $\Aut(\CP^1) \cong \PGL_2(\CC)$, there is a nice matrix representation if you act on projective coordinates:
\[
\matt a b c d \cdot \tv{z: 1}^t = \tv{ {az+b \over cz + d }: 1} = \tv{f(z): 1}
.\]
This yields a quick way of finding $f\inv$: invert the matrix and ignore the determinant that shows up since it just scales every entry:
\[
{az + b\over cz+ d} \leadsto \matt a b c d \inv = \matt d {-b} {-c} a 
\leadsto 
{dw-b \over -cw + a}
.\]

:::

:::{.remark}
An LFT that fixes three points is the identity.

:::


## Blaschke Factors

:::{.remark}
A very useful variant that shows up in applications of the Schwarz' lemma:
\[
\psi_a \da {a-z \over 1-\bar{a} z}
.\]
Some nice properties:

- $\psi_a(a) = 0$ and $\psi_a(0) = a$
- $\psi_a$ has a simple pole at $1/\bar{a}$ and a simple zero at $z=a$.
- $\psi_a(\bd \DD) = \bd \DD$, i.e. $\abs{\psi_a(z)} = \abs{z}$ when $\abs{z} = 1$.
- $\Aut(\DD) = \ts{ e^{i\theta} \psi_{a_k} \st a_k\in \DD}$, i.e. these form the factors of automorphisms of the disc after including rotations.
- $\psi_a'(z) = {\abs{a}^2 - 1\over (1-\bar{a} z)^2}$

:::

## Exercise

[[E-JPAJE]]

[[E-PIB7A]]

[[E-KZB33]]
