---
title: Splitting fields and normal extensions
order: 20
topics:
- Splitting Fields
- Field Theory
---

# Splitting fields and normal extensions

Normality says that algebraic conjugates do not escape the extension.
Equivalently, an irreducible polynomial over the base that has one root in a normal extension has all of its roots there.
Splitting fields are therefore the concrete models to keep in mind: finite normal extensions are precisely splitting fields of suitable polynomials over the base.

[[D-LZTAK]]

[[FD-TP2IZ]] [[FD-JJFZ3]]

[[FD-LHTRR]]

[[PR-OZYUC]]

[[D-XD5NG]]

[[PR-TZN4M]]

When an extension is not normal, its normal closure is obtained by adjoining the missing conjugates.
Computationally this means replacing $K(\alpha)$ by the splitting field of the minimal polynomial of $\alpha$ (and doing the same for a finite generating set in a general finite extension).
That enlargement is exactly what turns an extension problem into a Galois-group problem on the later pages.

::: {.remark title="Normality is not transitive"}
A tower $M/L/K$ with $M/L$ and $L/K$ both normal need not have $M/K$ normal.
The standard example is $\QQ(2^{1/4})/\QQ(\sqrt 2)/\QQ$: each step is quadratic hence normal, but $\QQ(2^{1/4})/\QQ$ omits the complex fourth roots of $2$.

Under the Galois correspondence, an intermediate field is normal over the base exactly when its corresponding subgroup is normal.
:::
