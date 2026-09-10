---
schema: qual/card@1
id: E-STYPO
kind: problem
title: Finite fields are perfect; example of an imperfect field
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Fields
  - Finite Fields
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Kept the Frobenius criterion and the standard F_p(t) counterexample.
---

::: {.exercise}
1. Define a perfect field.
2. Give an imperfect field and an inseparable polynomial over it.
3. Prove that every finite field is perfect.
:::

::: {.solution}
A field $K$ is **perfect** if every irreducible polynomial over $K$ is separable. In characteristic $p>0$, this is equivalent to surjectivity of Frobenius
\[
F:K\to K,\qquad x\mapsto x^p.
\]

<1>1. Every finite field is perfect.
::: {.proof}
Let $K=\mathbb F_{p^m}$. Frobenius is injective because $x^p=0$ implies $x=0$. Since $K$ is finite, every injective self-map is surjective. Hence $K^p=K$, so $K$ is perfect.
:::

<1>2. The field $\mathbb F_p(t)$ is imperfect.
::: {.proof}
Its $p$th powers form
\[
\mathbb F_p(t)^p=\mathbb F_p(t^p),
\]
which does not contain $t$. Thus $t$ has no $p$th root in $\mathbb F_p(t)$. The polynomial
\[
x^p-t
\]
is irreducible over $\mathbb F_p(t)$ (for example by Eisenstein at $t$ in $\mathbb F_p[t]$ and Gauss's lemma), while its derivative is zero. In an algebraic closure it is
\[
(x-t^{1/p})^p,
\]
so it is inseparable. Hence $\mathbb F_p(t)$ is not perfect.
:::
:::
