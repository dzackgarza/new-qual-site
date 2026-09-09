---
schema: qual/card@1
id: P-VTQYH
kind: problem
title: An irreducible in $\FF_p[x]$ divides $x^{p^n}-x$ iff its degree divides $n$
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

::: problem
Let $\pi(x)\in\FF_p[x]$ be irreducible of degree $d$. Prove
\[
\pi(x)\mid x^{p^n}-x
\iff
d\mid n.
\]
:::

::: solution
Let $\alpha$ be a root of $\pi$ in an algebraic closure of $\FF_p$. Since $\pi$ is irreducible of degree $d$,
\[
\FF_p(\alpha)\cong\FF_{p^d}.
\]

Now
\[
\pi(x)\mid x^{p^n}-x
\]
if and only if $\alpha$ is a root of $x^{p^n}-x$, i.e.
\[
\alpha^{p^n}=\alpha.
\]
The roots of $x^{p^n}-x$ are exactly the elements of $\FF_{p^n}$. Hence this is equivalent to
\[
\FF_p(\alpha)=\FF_{p^d}\subseteq\FF_{p^n}.
\]

Finite-field subfields satisfy
\[
\FF_{p^d}\subseteq\FF_{p^n}
\iff
d\mid n.
\]
Therefore
\[
\pi(x)\mid x^{p^n}-x
\iff
d\mid n.
\]
:::
