---
order: 52
title: Summation by parts
---

# Summation by parts

[[PR-2MTPE]]

The identity writes a finite sum as a boundary term plus a sum of differences, so a series converges when the partial sums of one factor are bounded, the other factor tends to $0$, and its successive differences are absolutely summable.
Both [[FT-3ZL25|Dirichlet's test]] and [[L-MYZOX|Abel's test]] are consequences of it, with $b_k$ the factor whose partial sums are bounded.

## Consequences for series

[[FT-3ZL25]]

[[L-MYZOX]]

Abel's test is Dirichlet's test with $b_k = z^k$: for $\abs z = 1$ and $z\neq1$ the partial sums of $z^k$ are bounded by $2/\abs{1-z}$, and the coefficients $c_k$ decrease to $0$.
The boundary behaviour of a power series at $z=1$ is [[T-B7YTE|Abel's theorem]], treated on [[complex-analysis/holomorphic-functions/power-series#Abel's theorem|Power series]].

## Problems

[[E-SS1.EX-19]]
[[E-ORJPT]]
[[E-XIT36]]
