---
schema: qual/card@1
id: E-6OUJV
kind: problem
title: Irreducible polynomials in characteristic $p$ are $g(x^{p^k})$ for unique separable
  $g$
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Characteristic
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09

---

::: {.exercise}
If $f\in k[x]^{\irr}$ with $\ch k = p$, then there is a unique separable $g\in k[x]^{\irr}$ such that $f(x) = g(x^{p^e})$ for some unique $e \ge 0$.
:::

::: solution
Let $f\in k[x]$ be irreducible and $\operatorname{char}k=p>0$.

For any polynomial $h(x)=\sum a_i x^i$,
\[
h'(x)=0
\quad\Longleftrightarrow\quad
a_i=0\text{ whenever }p\nmid i
\quad\Longleftrightarrow\quad
h(x)=h_1(x^p)
\]
for some $h_1\in k[x]$. If $h$ is irreducible and $h=h_1(x^p)$, then $h_1$ is irreducible, since any factorization of $h_1$ would induce one of $h$.

Choose $e\ge0$ maximal such that
\[
f(x)=g(x^{p^e})
\]
for some $g\in k[x]$. Such an $e$ exists because $e=0$ works and $p^e\mid\deg f$, so $e$ is bounded. The polynomial $g$ is irreducible. By maximality, $g'(x)\ne0$; since $g$ is irreducible, this is equivalent to $g$ being separable. Thus the required representation exists.

For uniqueness, suppose
\[
f(x)=g_1(x^{p^{e_1}})=g_2(x^{p^{e_2}})
\]
with $g_1,g_2$ separable. Assume $e_1<e_2$. Comparing coefficients shows that every exponent occurring in $g_1$ is divisible by $p^{e_2-e_1}$, hence in particular by $p$. Thus $g_1'(x)=0$, contradicting separability. Therefore $e_1=e_2$, and then equality of the two substituted polynomials forces $g_1=g_2$.

Hence both $e$ and the separable irreducible polynomial $g$ are unique.
:::
