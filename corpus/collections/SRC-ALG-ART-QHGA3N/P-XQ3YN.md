---
schema: qual/card@1
id: P-XQ3YN
kind: problem
title: A field of characteristic $p\neq 0$ is perfect iff every element is a $p$-th
  power
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Characteristic
  - Fields
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
Show that a field $k$ of characteristic $p\neq 0$ is perfect $\iff$ for every $x\in k$ there exists a $y\in k$ such that $y^p=x$.
:::


::: {.solution}
<1>1. Suppose first that every element of \(k\) is a \(p\)-th power. Then every irreducible polynomial in \(k[x]\) is separable.
::: {.proof}
Let \(f(x)\in k[x]\) be irreducible and nonconstant. If \(f'(x)=0\), then every exponent occurring in \(f\) is divisible by \(p\), so
\[
f(x)=\sum_i a_i x^{pi}.
\]
By hypothesis, write \(a_i=b_i^p\) with \(b_i\in k\). In characteristic \(p\), Frobenius is additive, hence
\[
f(x)=\left(\sum_i b_i x^i\right)^p,
\]
which is reducible unless \(f\) has degree \(0\), a contradiction. Therefore \(f'\neq0\). Since \(f\) is irreducible, \(\gcd(f,f')=1\), so \(f\) has no repeated root in an algebraic closure and is separable.
:::

<1>2. Hence if every element of \(k\) is a \(p\)-th power, then \(k\) is perfect.
::: {.proof}
A field is perfect exactly when every irreducible polynomial over it is separable. This holds by <1>1.
:::

<1>3. Conversely, suppose some \(a\in k\) is not a \(p\)-th power. Then
\[
f(x)=x^p-a
\]
is irreducible over \(k\).
::: {.proof}
Let \(\alpha\) be the unique root of \(x^p-a\) in an algebraic closure, so
\[
x^p-a=(x-\alpha)^p.
\]
If \(f\) were reducible over \(k\), it would have a monic irreducible factor \(g\) of degree \(m\) with \(1\le m<p\). All roots of \(g\) must equal \(\alpha\), so \(g=(x-\alpha)^m\). The coefficient of \(x^{m-1}\) is \(-m\alpha\). Since \(1\le m<p\), the scalar \(m\) is nonzero in characteristic \(p\); because \(g\in k[x]\), this forces \(\alpha\in k\). Then \(a=\alpha^p\) is a \(p\)-th power in \(k\), contradiction. Thus \(f\) is irreducible.
:::

<1>4. The irreducible polynomial \(x^p-a\) is inseparable.
::: {.proof}
Its derivative is
\[
f'(x)=px^{p-1}=0,
\]
and over an algebraic closure it equals \((x-\alpha)^p\), so its unique root has multiplicity \(p\).
:::

<1>5. Therefore, if \(k\) is perfect, every element of \(k\) is a \(p\)-th power.
::: {.proof}
If some \(a\in k\) were not a \(p\)-th power, then by <1>3 and <1>4 there would be an irreducible inseparable polynomial over \(k\), contradicting perfectness.
:::

<1>6. Hence
\[
k\text{ is perfect}
\iff
\forall x\in k\ \exists y\in k\text{ with }y^p=x.
\]
::: {.proof}
Combine <1>2 and <1>5.
:::
:::
