---
schema: qual/card@1
id: P-UMQHV
kind: problem
title: An irreducible over a field of characteristic $p$ is $g(x^{p^d})$ with $g$
  irreducible and separable, and all roots have multiplicity $p^d$
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Characteristic
  - Irreducibility Criteria
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
Let $k$ be a field of characteristic $p\neq 0$ and $f\in k[x]$ irreducible.
Show that $f(x) = g(x^{p^d})$ where $g(x) \in k[x]$ is irreducible and separable.

Conclude that every root of $f$ has the same multiplicity $p^d$ in the splitting field of $f$ over $k$.
:::

::: {.solution}

::: pf

::: pf-step

If \(f'(x)\neq0\), then \(f\) is separable, so the conclusion holds with \(d=0\) and \(g=f\).

::: pf-proof

Because \(f\) is irreducible and \(f'\neq0\), one has \(\gcd(f,f')=1\). Therefore \(f\) has no repeated root in an algebraic closure and is separable.

:::

:::

::: {.pf-step #s2}

If \(f'(x)=0\), then there exists \(h\in k[x]\) such that
\[
f(x)=h(x^p).
\]

::: pf-proof

Write
\[
f(x)=\sum_i a_i x^i.
\]
In characteristic \(p\),
\[
f'(x)=\sum_i i a_i x^{i-1}.
\]
If this is zero, then every exponent \(i\) with \(a_i\neq0\) is divisible by \(p\). Hence
\[
f(x)=\sum_j a_{pj}x^{pj}=h(x^p)
\]
with \(h(y)=\sum_j a_{pj}y^j\in k[y]\).

:::

:::

::: {.pf-step #s3}

In step [](#s2){.pf-ref}, if \(f\) is irreducible, then \(h\) is irreducible.

::: pf-proof

If \(h=ab\) with nonconstant \(a,b\in k[x]\), then
\[
f(x)=h(x^p)=a(x^p)b(x^p)
\]
would be a nontrivial factorization of \(f\), contradicting irreducibility.

:::

:::

::: pf-step

Repeating steps [](#s2){.pf-ref} and [](#s3){.pf-ref} finitely many times gives
\[
f(x)=g(x^{p^d})
\]
for some \(d\ge0\), where \(g\in k[x]\) is irreducible and \(g'\neq0\).

::: pf-proof

Whenever the current irreducible polynomial has zero derivative, step [](#s2){.pf-ref} writes it as \(h(x^p)\), and step [](#s3){.pf-ref} shows \(h\) remains irreducible. Its degree is divided by \(p\), so the process strictly decreases degree and must terminate. At termination the resulting irreducible polynomial \(g\) has nonzero derivative.

:::

:::

::: {.pf-step #s5}

The terminal polynomial \(g\) is separable.

::: pf-proof

Since \(g\) is irreducible and \(g'\neq0\), one has \(\gcd(g,g')=1\). Thus \(g\) has no repeated roots.

:::

:::

::: {.pf-step #s6}

Let \(L\) be a splitting field of \(f\), and let
\[
g(y)=c\prod_{i=1}^r (y-\beta_i)
\]
in an algebraic closure, with the \(\beta_i\) distinct. For each \(i\), choose \(\alpha_i\) with
\[
\alpha_i^{p^d}=\beta_i.
\]
Then
\[
f(x)=c\prod_{i=1}^r (x-\alpha_i)^{p^d}.
\]

::: pf-proof

By step [](#s5){.pf-ref} the roots \(\beta_i\) are distinct. In characteristic \(p\), Frobenius gives
\[
x^{p^d}-\beta_i=x^{p^d}-\alpha_i^{p^d}=(x-\alpha_i)^{p^d}.
\]
Therefore
\[
f(x)=g(x^{p^d})
=c\prod_i (x^{p^d}-\beta_i)
=c\prod_i (x-\alpha_i)^{p^d}.
\]

:::

:::

::: pf-step

Every root of \(f\) has multiplicity exactly \(p^d\).

::: pf-proof

The roots \(\alpha_i\) are distinct: if \(\alpha_i=\alpha_j\), then \(\beta_i=\alpha_i^{p^d}=\alpha_j^{p^d}=\beta_j\), contradicting distinctness of the roots of \(g\). Thus the factorization in step [](#s6){.pf-ref} has distinct linear factors, each occurring with exponent \(p^d\).

:::

:::

:::

:::
