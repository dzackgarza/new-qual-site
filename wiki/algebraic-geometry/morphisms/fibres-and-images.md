---
title: Fibres and images
order: 5
topics:
- Fibre Dimension
- Semicontinuity
- Stein Factorisation
---

# Fibres and images

The theorems below bound the dimensions of fibres, give a criterion for flatness from fibre dimension, and describe the connectedness of fibres.

## Dimension

[[T-MORFIBDIM]]

Fibres can jump up over special points and never down; the blowup of a point in $\AA^2$ exhibits the jump from a zero-dimensional generic fibre to a one-dimensional exceptional fibre.
The generic equality computes dimensions by adding the dimension of the generic fibre to the dimension of the base.

[[T-MORMIRACLE]]

If $X$ is Cohen--Macaulay, $Y$ is regular, and $\dim_xX_{f(x)}=\dim\OO_{X,x}-\dim\OO_{Y,f(x)}$ at every point $x$, then $f$ is flat.

## Images

[[T-MORZMT]]

[[T-MORSTEIN]]

A proper morphism $f\colon X\to Y$ of noetherian schemes factors as $X\xrightarrow{f'}Y'\xrightarrow{g}Y$ with $Y'=\underline{\Spec}_Y f_*\OO_X$, $g$ finite, and $f'_*\OO_X=\OO_{Y'}$, so every fibre of $f'$ is connected.
For $X$ integral, $f$ birational, and $Y$ normal, $g$ is finite and birational onto a normal scheme, hence an isomorphism, and every fibre of $f$ is connected.
The normalization of the nodal cubic is finite and birational, and its fibre over the node is two points.
The same map is not flat: its fibre over the node has length $2$ and every other fibre has length $1$.

## Connected fibres and integral closure

[[P-AGXMISCOCONNECTED]]
