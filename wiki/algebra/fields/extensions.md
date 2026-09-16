---
title: Field extensions
order: 10
topics:
- Field Extensions
- Fields
---

# Field extensions

## Simple and algebraic extensions

For fields $K\subseteq L$ and $\alpha\in L$, $K(\alpha)$ is the smallest subfield of $L$ containing $K$ and $\alpha$, and $K[\alpha]$ is the smallest subring containing them.
If $\alpha$ is algebraic over $K$ with minimal polynomial $f$, then $K[\alpha]=K(\alpha)\cong K[x]/\gens f$ and $[K(\alpha):K]=\deg f$.
If $\alpha$ is transcendental over $K$, then $K[\alpha]\cong K[x]$ is a polynomial ring and $K(\alpha)\cong K(x)$ is its field of fractions.
Every finite extension is algebraic, and by the primitive element theorem every finite separable extension is simple.

[[D-PUOGJ]]

[[FD-J3HIA]] [[FD-QPNDA]]

[[FD-3V3ZW]]

[[T-3HPWT]]

[[FD-2EVYB]]

[[FD-NS5RF]]

[[T-NGBVC]]

::: {.remark title="Tower law and degree constraints"}
For fields $K\subseteq L\subseteq M$, the tower law is
$$
[M:K]=[M:L][L:K].
$$
Hence an extension of prime degree has no intermediate fields other than its endpoints, and if $f\in\QQ[x]$ is irreducible with root $\alpha$, then $\deg f = [\QQ(\alpha):\QQ]$ divides the degree $[\SF(f):\QQ]$ of the splitting field, which is the order of the Galois group of $f$.
:::

## Finding a minimal polynomial

::: {.remark title="Methods"}
\envlist

- For $x\da \sqrt a + \sqrt b$ with $a,b\in\QQ$, isolate a radical and square: $(x-\sqrt a)^2 = b$ gives $x^2+a-b = 2x\sqrt a$, and squaring again gives $(x^2+a-b)^2 = 4ax^2$, a monic polynomial of degree $4$ with root $x$.

- If $n \da [\QQ(\alpha):\QQ]$ is known, then $1, \alpha, \ldots, \alpha^n$ are $\QQ$-linearly dependent, and a dependence with $\alpha^n$ having coefficient $1$ gives the minimal polynomial.

- For $x\da \sqrt a + \sqrt b$, write $1, x, x^2, x^3, x^4$ as vectors in the $\QQ$-spanning set $1, \sqrt a, \sqrt b, \sqrt{ab}$ of $\QQ(\sqrt a,\sqrt b)$.
  These are five vectors in a space of dimension at most $4$, and a $\QQ$-linear dependence among them is a polynomial of degree at most $4$ with root $x$.

- If $\alpha,\beta\neq0$ and $\alpha\beta \in \QQ$, then $\alpha = (\alpha\beta)/\beta \in \QQ(\beta)$ and $\beta\in\QQ(\alpha)$, so $\QQ(\alpha)=\QQ(\beta)$.
:::

## Algebraic extensions

For fields $K\subseteq L\subseteq M$, if $L/K$ and $M/L$ are algebraic, then $M/K$ is algebraic.

[[PR-ABSJX]]

## Quadratic extensions

If $[L:K]=2$, then $L=K(\alpha)$ for every $\alpha\in L\sm K$.
If $\operatorname{char}K\neq2$, then $L=K(\sqrt d)$ for some $d\in K$ that is not a square in $K$.
The quadratic extensions of $\QQ$ are the fields $\QQ(\sqrt d)$ for squarefree integers $d\neq 1$, and $\FF_p$ has a unique quadratic extension up to isomorphism, $\FF_{p^2}$.

[[PR-OFBRQ]]

[[C-BOM4E]]

[[PR-F2N4L]]

## Distinguished classes

A class of field extensions is [[D-JMATC|distinguished]] if it is closed under towers in both directions and under base change to composita.
Separable extensions form a distinguished class.
Normal extensions satisfy: if $M/K$ is normal and $K\subseteq L\subseteq M$, then $M/L$ is normal; normality is not transitive, by the example on [[algebra/fields/splitting-and-normal|Splitting fields and normal extensions]].

[[D-JMATC]]

[[C-4GQK3]]

[[PR-MHOVR]]
