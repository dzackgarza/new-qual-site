---
schema: qual/card@1
id: E-PHSV5
kind: problem
title: An irreducible $f\in\mathbb{F}_p[x]$ of degree $d$ divides $x^{p^n}-x$ if and
  only if $d$ divides $n$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Irreducibility Criteria
  - Field Extensions
relations: []
review: draft
---

::: {.exercise}
Show that if $f \in \FF_p[x]^{\irr}$ is degree $d$,
\[
f \divides x^{p^n}-x \iff d\divides n
.\]
:::

::: {.solution}
Let $\alpha$ be a root of $f$ in an algebraic closure $\overline{\FF}_p$; then $f$ is (up to a unit) the minimal polynomial of $\alpha$ and $\FF_p(\alpha)\cong\GF(p^d)$.

$\impliedby$:

- If $d\divides n$, then $x^d-1 \divides x^n-1$ ([[E-LUR7G]]), and evaluating at $x=p$ gives $p^d-1 \divides p^n-1$.
- Applying [[E-LUR7G]] again, $x^{p^d-1}-1 \divides x^{p^n-1}-1$; multiplying by $x$ gives $x^{p^d}-x\divides x^{p^n}-x$.
- Every element $a$ of the field $\FF_p(\alpha)$ of order $p^d$ satisfies $a^{p^d}=a$, so $\alpha$ is a root of $x^{p^d}-x$ and $f\divides x^{p^d}-x$.
- Hence $f \divides x^{p^d}-x \divides x^{p^n}-x$.

$\implies$:

- If $f\divides x^{p^n}-x$, then $\alpha^{p^n}=\alpha$, so $\alpha$ lies in the subfield $\GF(p^n)=\{a\in\overline{\FF}_p:a^{p^n}=a\}$, and $\FF_p(\alpha) \subseteq \GF(p^n)$.
- By the tower law,
$$n = [\GF(p^n) : \FF_p] = [\GF(p^n) : \FF_p(\alpha)] \cdot [\FF_p(\alpha) : \FF_p] = [\GF(p^n) : \FF_p(\alpha)]\cdot d,$$
so $d\divides n$.
:::

