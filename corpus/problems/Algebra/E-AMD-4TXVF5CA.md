---
schema: qual/card@1
id: E-AMD-4TXVF5CA
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
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Prove that an irreducible polynomial $\pi(x)\in \FF_p[x]$ divides $x^{p^n}-x \iff \deg \pi(x)$ divides $n$.
:::

::: {.solution}
Let \(\pi\in\FF_p[x]\) be irreducible of degree \(d\), and let \(\alpha\) be a root in \(\overline{\FF}_p\). Then
\[
\FF_p(\alpha)\cong\FF_{p^d}.
\]
Also, the roots of \(x^{p^n}-x\) in \(\overline{\FF}_p\) are exactly the elements of \(\FF_{p^n}\).

If \(\pi\mid x^{p^n}-x\), then \(\alpha\in\FF_{p^n}\), so
\[
\FF_{p^d}=\FF_p(\alpha)\subseteq\FF_{p^n}.
\]
By the finite-field subfield criterion, \(d\mid n\).

Conversely, if \(d\mid n\), then \(\FF_{p^d}\subseteq\FF_{p^n}\), hence \(\alpha^{p^n}=\alpha\). Therefore \(\alpha\) is a root of \(x^{p^n}-x\). Since \(\pi\) is the minimal polynomial of \(\alpha\) over \(\FF_p\),
\[
\pi(x)\mid x^{p^n}-x.
\]
Thus
\[
\boxed{\pi\mid x^{p^n}-x\iff \deg\pi\mid n}.
\]
:::
