---
title: Field extensions
order: 10
problems:
  topics:
  - Field Extensions
  - Fields
---

# Field extensions

## Basics

[[D-PUOGJ]]

[[FD-J3HIA]] [[FD-QPNDA]]

[[FD-3V3ZW]]

[[T-3HPWT]]

[[FD-2EVYB]]

[[FD-KWXK3]] [[FD-HVSOB]] [[FD-NS5RF]]

[[T-NGBVC]]

:::{.remark title="Degrees multiply, and that is most of the subject"}
The tower law $[M:K] = [M:L][L:K]$ is the single most used fact in field theory, and almost every degree computation is an application of it.
Two standard consequences: a degree that is prime has no proper intermediate fields, and $[\QQ(\alpha):\QQ]$ divides $[\SF(f):\QQ]$ for every root $\alpha$ of $f$, which is what bounds a Galois group's order from below.

:::

## Finding a minimal polynomial

:::{.remark title="The standard techniques"}
\envlist

- Given $x\da \sqrt a + \sqrt b$, compute $x^2, x^3, \dots$ and look for a rational linear combination.
  The general move is to isolate the radicals on one side and raise both sides to that power.

- Better, since it always terminates: find $n \da [\QQ(\alpha):\QQ]$, so that $1, \alpha, \dots, \alpha^n$ must be $\QQ\dash$linearly dependent, then compute those powers and solve for the coefficients.

- For $x\da \sqrt a + \sqrt b$ specifically, write $x, x^2, x^3, x^4$ in the basis $\ts{1, \sqrt a, \sqrt b, \sqrt{ab}}$, so that
 \[
   A\vector v = \vector c \da A \tv{1, \sqrt a, \sqrt b, \sqrt{ab} } = \tv{x, x^2, x^3, x^4}
 ,\]
 and invert: reading the first row of $A\inv$ against $\vector b$ gives a polynomial in $x$.

- If $\alpha\beta \in \QQ$ then $\alpha \in \QQ(\beta)$ and conversely.

:::

## Algebraic extensions

[[PR-ABSJX]]

## Quadratic extensions

[[PR-OFBRQ]]

[[C-BOM4E]]

[[PR-F2N4L]]

## Distinguished classes

[[D-JMATC]]

[[C-4GQK3]]

[[PR-MHOVR]]
