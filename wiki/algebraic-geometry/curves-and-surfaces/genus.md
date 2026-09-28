---
title: Genus
order: 1
topics:
- Genus
- Riemann-Hurwitz
- Curves
---

# Genus

[[D-G1AEH]]

The arithmetic genus is read from the Hilbert polynomial, the geometric genus is the genus of the normalization, and over $\CC$ the topological genus of the smooth model equals the geometric genus.
For an integral projective curve $C$ over an algebraically closed field with normalization $\tilde C$, $p_a(C)=g(\tilde C)+\sum_{p\in C}\delta_p$, where $\delta_p=\dim_k\tilde\OO_p/\OO_{C,p}$ and $\tilde\OO_p$ is the integral closure of $\OO_{C,p}$; so $p_a(C)=g(\tilde C)$ exactly when $C$ is smooth.

Both genera are invariants of the curve, while the degree depends on the embedding: the twisted cubic and a line in $\PP^3$ are both isomorphic to $\PP^1$, of genus $0$, and have degrees $3$ and $1$.

## Computing the genus

- **Plane curves.** A plane curve of degree $d$ has $p_a=\binom{d-1}{2}$, and its geometric genus is $p_a-\sum_p\delta_p$.

- **Hilbert polynomial.** A curve $C\subseteq\PP^n$ of degree $d$ has Hilbert polynomial $P_C(m)=dm+1-p_a$.

- **Maps to a known curve.** A finite separable morphism $f\colon X\to Y$ of smooth projective curves satisfies Riemann--Hurwitz.

[[T-LKT0U]]

The ramification divisor $R$ is the divisor of zeros of $f^*\colon f^*\Omega_Y\to\Omega_X$, so $K_X\sim f^*K_Y+R$; taking degrees gives the Riemann--Hurwitz formula.

## The small genera

[[PR-VGA2L]]

## Twisted forms of the line

[[D-VARSEVBRAUER]]

[[P-AGXMISCTSENPONEBUNDLE]]
