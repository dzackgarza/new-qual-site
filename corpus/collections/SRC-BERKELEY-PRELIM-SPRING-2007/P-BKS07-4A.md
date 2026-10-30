---
schema: qual/card@1
id: P-BKS07-4A
kind: problem
title: Isomorphisms among $\QQ(\sqrt[3]{2})$, the splitting field of $x^3-2$, $\overline{\FF}_2$, its roots-of-unity subfield, $\RR$, and $\QQ((T))$
classification:
  areas: [prelim]
  topics:
  - Abstract Algebra
relations: []
review: draft
---

::: {.problem}
Define six fields as follows:

- Let $A = \QQ(\alpha)$ where $\QQ$ is the field of rational numbers and $\alpha$ is the real cube root of $2$.
- Let $B$ be a splitting field of $x^{3} - 2$ over $\QQ$.
- Let $C$ be an algebraic closure of the field $\FF_{2}$ of $2$ elements.
- Let $D$ be the subfield of $C$ generated over $\FF_{2}$ by the set of $a \in C$ such that there exists $n \geq 1$ with $a^{n} = 1$.
- Let $E$ be the field $\RR$ of real numbers.
- Let $F$ be the field $\QQ[[T]](T^{-1})$ of formal Laurent series with rational coefficients.

For each pair of these, determine with proof whether or not they are isomorphic.
:::

::: {.solution}

The only isomorphic pair is $C$ and $D$; in fact $C=D$.

::: pf

::: {.pf-step #s1}

No field in one of the sets $\{A,B\}$, $\{C,D\}$, $\{E,F\}$ is isomorphic to a field in another.

::: pf-proof

$A$ and $B$ are finite extensions of $\QQ$, so they are countable of characteristic $0$. $C$ and $D$ have characteristic $2$. $E$ and $F$ have characteristic $0$ and are uncountable; for $F$, the series $\sum_{n\ge0}\epsilon_nT^n$ with $\epsilon_n\in\{0,1\}$ are already uncountably many.

:::

:::

::: {.pf-step #s2}

$A\not\cong B$.

::: pf-proof

By Eisenstein's criterion at $2$, $x^3-2$ is irreducible, so $[A:\QQ]=3$. The roots of $x^3-2$ are $\omega^j\alpha$ with $\omega$ a primitive cube root of unity, so $B$ contains $\omega=(\omega\alpha)/\alpha$, and $[\QQ(\omega):\QQ]=2$ divides $[B:\QQ]$. An isomorphism of fields of characteristic $0$ fixes $\QQ$, so it preserves the degree over $\QQ$.

:::

:::

::: {.pf-step #s3}

$C=D$.

::: pf-proof

$D\subseteq C$ by definition. If $a\in C$ is nonzero, then $\FF_2(a)$ is a finite field, say with $q$ elements, so $a^{q-1}=1$ and $a\in D$. Also $0\in D$.

:::

:::

::: {.pf-step #s4}

$E\not\cong F$.

::: pf-proof

$2=(\sqrt2)^2$ in $\RR$. In $F$, a nonzero element is $cT^m+(\text{higher terms})$ with $c\in\QQ^\times$, and its square is $c^2T^{2m}+(\text{higher terms})$. If this equals $2$, then $c^2=2$, which has no rational solution. So $2$ is not a square in $F$. An isomorphism fixes $2$ and preserves squares.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} to [](#s4){.pf-ref} settle every pair.

:::

:::

:::
