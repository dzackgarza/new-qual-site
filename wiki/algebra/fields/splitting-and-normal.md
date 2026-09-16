---
title: Splitting fields and normal extensions
order: 20
topics:
- Splitting Fields
- Field Theory
---

# Splitting fields and normal extensions

An algebraic extension $L/K$ is [[D-LZTAK|normal]] if every irreducible polynomial in $K[x]$ with a root in $L$ splits into linear factors over $L$.
A finite extension $L/K$ is normal if and only if $L$ is the [[FD-LHTRR|splitting field]] over $K$ of some polynomial in $K[x]$.

[[D-LZTAK]]

[[FD-JJFZ3]]

[[FD-LHTRR]]

[[PR-OZYUC]]

[[D-XD5NG]]

[[PR-TZN4M]]

For a finite extension $L = K(\alpha_1,\ldots,\alpha_r)$ inside an algebraic closure $\overline K$, the [[D-XD5NG|normal closure]] of $L/K$ is the splitting field over $K$ of the product of the minimal polynomials of $\alpha_1,\ldots,\alpha_r$; it is the smallest normal extension of $K$ in $\overline K$ containing $L$.
For example, the normal closure of $\QQ(2^{1/4})/\QQ$ is $\QQ(2^{1/4}, i)$, the splitting field of $x^4-2$.

::: {.remark title="Normality is not transitive"}
In the tower $\QQ\subseteq\QQ(\sqrt 2)\subseteq\QQ(2^{1/4})$, both steps have degree $2$ and are therefore normal, and $\QQ(2^{1/4})/\QQ$ is not normal: $x^4-2$ is irreducible over $\QQ$ and has the root $2^{1/4}$ in $\QQ(2^{1/4})\subseteq\RR$, but not its roots $\pm i2^{1/4}$.

For a finite Galois extension $L/K$ and an intermediate field $K\subseteq E\subseteq L$, $E/K$ is normal if and only if $\Gal(L/E)$ is a normal subgroup of $\Gal(L/K)$.
:::
