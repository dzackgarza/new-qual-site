---
schema: qual/card@1
id: PR-73MCN
kind: proposition
title: $x^{p^n}-x$ is the product of the monic irreducibles over $\FF_p$ of degree dividing $n$
slogan: 'An irreducible polynomial over $\FF_p$ divides $x^{p^n}-x$ exactly when its degree divides $n$.'
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Irreducibility Criteria
  - Polynomials
relations: []
review: draft
---

::: {.proposition}
Let $p$ be prime and $n\geq 1$, and set $\rho_n(x) \coloneqq x^{p^n} - x$.
Then
$$
\rho_n(x)
=
\prod_{\substack{f\in\FF_p[x]\text{ monic irreducible}\\ \deg f\mid n}} f(x).
$$
Equivalently, for a monic irreducible $f\in\FF_p[x]$,
$$
f(x)\mid \rho_n(x) \iff \deg f\mid n.
$$
:::

::: {.proof}
The roots of $\rho_n(x)=x^{p^n}-x$ in an algebraic closure of $\FF_p$ are exactly the elements of $\FF_{p^n}$.
If $f$ is monic irreducible of degree $d$ and $\alpha$ is one of its roots, then $\FF_p(\alpha)\cong\FF_{p^d}$.
Hence
$$
f\mid \rho_n
\iff \alpha\in\FF_{p^n}
\iff \FF_{p^d}\subseteq\FF_{p^n}
\iff d\mid n.
$$
Finally, $\rho_n'(x)=-1$, so $\rho_n$ is squarefree; therefore each of these irreducible factors occurs exactly once, giving the displayed product.
:::

::: {.remark title="Divisibility without the product formula"}
The equivalence $f\mid\rho_n\iff\deg f\mid n$ also follows from polynomial divisibility. If $d=\deg f$ and $\alpha$ is a root of $f$, then $\alpha^{p^d}=\alpha$, so $f\mid x^{p^d}-x$. If $d\mid n$, then $x^d-1\mid x^n-1$ ([[E-LUR7G]]); evaluating at $x=p$ gives $p^d-1\mid p^n-1$, so $x^{p^d-1}-1\mid x^{p^n-1}-1$ and $x^{p^d}-x\mid x^{p^n}-x$. Conversely, if $f\mid\rho_n$, then $\FF_p(\alpha)\subseteq\FF_{p^n}$ and the tower law gives $n=[\FF_{p^n}:\FF_p(\alpha)]\cdot d$.
:::
