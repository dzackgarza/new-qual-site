---
title: Polynomial rings
order: 30
problems:
  topics:
  - Polynomials
  - Noetherian Rings
  - Localization
---

# Polynomial rings

## Basics

Treat \(R[x]\) as a ring construction applied to the coefficient ring \(R\): the constant polynomials retain the coefficient-ring arithmetic, while ideals and ring morphisms are the language for passing to quotients, reducing coefficients, and evaluating polynomials.
The point of the section is therefore not to relearn the ring axioms, but to track which properties of \(R\) survive after adjoining a variable.

[[D-GURUB]]

[[D-GXMDW]]

[[D-GOFWL]]

[[D-O26OY]]

[[FD-LXZIW]]

::: {.remark title="What survives passing to $R[x]$"}
$R$ a UFD gives $R[x]$ a UFD, and $R$ Noetherian gives $R[x]$ Noetherian by the Hilbert basis theorem.
$R$ a PID does *not* give $R[x]$ a PID, and $\gens{2,x}\normal\ZZ[x]$ is the counterexample every time.

The rule of thumb: properties defined by factorization survive, properties defined by ideals being principal do not, since adjoining a variable adds a dimension and $\gens{2,x}$ needs two generators.
:::

The irreducibility criteria and the field theory built on $k[x]$ are [[algebra/fields/polynomials|Polynomials over a field]].
