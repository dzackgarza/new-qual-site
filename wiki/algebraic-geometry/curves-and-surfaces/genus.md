---
title: Genus
order: 1
topics:
- Genus
- Riemann-Hurwitz
- Curves
---

# Genus

Several notions of genus coexist, and the main task is to identify which one is being computed and how it behaves under singularities and normalization.

[[D-G1AEH]]

The three senses are arithmetic genus from the Hilbert polynomial, geometric genus from the normalization, and topological genus from the smooth model over $\CC$.
They agree for a smooth curve and differ by a sum of local terms otherwise, which is the whole answer to what the geometric genus of a singular curve might be.

Neither genus depends on the embedding; the degree does.
The twisted cubic and a line in $\PP^3$ make the contrast concrete.

## Computing one

Three standard computations are:

- **plane curve of degree $d$**: $p_a = \binom{d-1}{2}$, then subtract $\delta_p$ at each singularity;

- **Hilbert polynomial**: read the constant term, which is $1 - p_a$;

- **a map to a known curve**: Riemann--Hurwitz.

[[T-LKT0U]]

The Riemann--Hurwitz proof is built from the cotangent sequence, the map on differentials, and the resulting ramification divisor.

## The small genera

[[PR-VGA2L]]

## Twisted forms of the line

[[D-VARSEVBRAUER]]

[[P-AGXMISCTSENPONEBUNDLE]]
