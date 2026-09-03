---
schema: qual/card@1
id: PR-73MCN
kind: proposition
title: Splits Product of Irreducibles
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
Let $p$ be prime and $n\geq 1$, and set $\rho_n(x) \definedas x^{p^n} - x$.
Then
\[
\rho_n(x)
=
\prod_{\substack{f\in\FF_p[x]\text{ monic irreducible}\\ \deg f\mid n}} f(x).
\]
Equivalently, for a monic irreducible $f\in\FF_p[x]$,
\[
f(x)\mid \rho_n(x) \iff \deg f\mid n.
\]
:::

::: {.proof}
The roots of $\rho_n(x)=x^{p^n}-x$ in an algebraic closure of $\FF_p$ are exactly the elements of $\FF_{p^n}$.
If $f$ is monic irreducible of degree $d$ and $\alpha$ is one of its roots, then $\FF_p(\alpha)\cong\FF_{p^d}$.
Hence
\[
f\mid \rho_n
\iff \alpha\in\FF_{p^n}
\iff \FF_{p^d}\subseteq\FF_{p^n}
\iff d\mid n.
\]
Finally, $\rho_n'(x)=-1$, so $\rho_n$ is squarefree; therefore each of these irreducible factors occurs exactly once, giving the displayed product.
:::
