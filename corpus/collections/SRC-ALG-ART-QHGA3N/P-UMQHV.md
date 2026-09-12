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

::: problem
Let $k$ be a field of characteristic $p\neq 0$ and $f\in k[x]$ irreducible.
Show that $f(x) = g(x^{p^d})$ where $g(x) \in k[x]$ is irreducible and separable.

Conclude that every root of $f$ has the same multiplicity $p^d$ in the splitting field of $f$ over $k$.
:::


::: {.solution}
<1>1. If \(f'(x)\neq0\), then \(f\) is separable, so the conclusion holds with \(d=0\) and \(g=f\).
::: {.proof}
Because \(f\) is irreducible and \(f'\neq0\), one has \(\gcd(f,f')=1\). Therefore \(f\) has no repeated root in an algebraic closure and is separable.
:::

<1>2. If \(f'(x)=0\), then there exists \(h\in k[x]\) such that
\[
f(x)=h(x^p).
\]
::: {.proof}
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

<1>3. In <1>2, if \(f\) is irreducible, then \(h\) is irreducible.
::: {.proof}
If \(h=ab\) with nonconstant \(a,b\in k[x]\), then
\[
f(x)=h(x^p)=a(x^p)b(x^p)
\]
would be a nontrivial factorization of \(f\), contradicting irreducibility.
:::

<1>4. Repeating <1>2 and <1>3 finitely many times gives
\[
f(x)=g(x^{p^d})
\]
for some \(d\ge0\), where \(g\in k[x]\) is irreducible and \(g'\neq0\).
::: {.proof}
Whenever the current irreducible polynomial has zero derivative, <1>2 writes it as \(h(x^p)\), and <1>3 shows \(h\) remains irreducible. Its degree is divided by \(p\), so the process strictly decreases degree and must terminate. At termination the resulting irreducible polynomial \(g\) has nonzero derivative.
:::

<1>5. The terminal polynomial \(g\) is separable.
::: {.proof}
Since \(g\) is irreducible and \(g'\neq0\), one has \(\gcd(g,g')=1\). Thus \(g\) has no repeated roots.
:::

<1>6. Let \(L\) be a splitting field of \(f\), and let
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
::: {.proof}
By <1>5 the roots \(\beta_i\) are distinct. In characteristic \(p\), Frobenius gives
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

<1>7. Every root of \(f\) has multiplicity exactly \(p^d\).
::: {.proof}
The roots \(\alpha_i\) are distinct: if \(\alpha_i=\alpha_j\), then \(\beta_i=\alpha_i^{p^d}=\alpha_j^{p^d}=\beta_j\), contradicting distinctness of the roots of \(g\). Thus the factorization in <1>6 has distinct linear factors, each occurring with exponent \(p^d\).
:::
:::
