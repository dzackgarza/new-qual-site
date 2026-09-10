---
schema: qual/card@1
id: E-AMD-7YJUIMVH
kind: problem
title: A linear operator cycling a basis has minimal polynomial $x^n-1$ and is diagonalizable
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Minimal and Characteristic Polynomials
  - Bases
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
Let $V$ be an $n$-dimensional vector space over a field $F$, with basis $\{v_0,\dots,v_{n-1}\}$ and $T(v_i)=v_{i+1\bmod n}$. Show that $m_T(x)=x^n-1$, and deduce that $T$ is diagonalizable exactly when $x^n-1$ splits into distinct linear factors over $F$ (in particular, over $\CC$).
:::

::: {.solution}
Let \(V\) have basis \(v_0,\dots,v_{n-1}\) and \(T(v_i)=v_{i+1\bmod n}\).

<1>1. The minimal polynomial of \(T\) is \(x^n-1\) over every base field.
::: {.proof}
Since \(T^n(v_i)=v_i\) for every basis vector, \(T^n=I\), so the minimal polynomial \(m_T\) divides \(x^n-1\).

On the other hand,
\[
v_0,Tv_0,\dots,T^{n-1}v_0
=v_0,v_1,\dots,v_{n-1}
\]
is a basis. Thus no nonzero polynomial of degree less than \(n\) can annihilate \(T\): if
\[
\sum_{j=0}^{m}a_jT^j=0,
\qquad m<n,
\]
then applying it to \(v_0\) gives \(\sum_{j=0}^{m}a_jv_j=0\), hence every \(a_j=0\). Therefore \(\deg m_T\ge n\). Since \(m_T\mid x^n-1\), both monic of degree \(n\),
\[
\boxed{m_T(x)=x^n-1}.
\]
:::

<1>2. The operator \(T\) is diagonalizable exactly when \(x^n-1\) splits into distinct linear factors over the base field.
::: {.proof}
A linear operator is diagonalizable iff its minimal polynomial splits into distinct linear factors. By <1>1, the minimal polynomial is \(x^n-1\), so this criterion is immediate.
:::

In particular, over \(\CC\) (or any field containing all \(n\)-th roots of unity with characteristic not dividing \(n\)), \(x^n-1\) has \(n\) distinct roots, hence \(T\) is diagonalizable.
:::
