---
schema: qual/card@1
id: P-HCAO57
kind: problem
title: The elimination theorem
classification:
  areas:
  - algebra
  topics:
  - Gröbner Bases
  - Elimination Theory
  - Polynomial Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Commutative Algebra oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
State the elimination theorem and explain why it is called an elimination theorem.
:::

::: solution
Let
\[
I\subseteq k[x_1,\ldots,x_n]
\]
and fix $1\le \ell<n$. Use lexicographic order
\[
x_1>\cdots>x_n.
\]
If $G$ is a Gröbner basis of $I$, the elimination theorem states that
\[
G_\ell=G\cap k[x_{\ell+1},\ldots,x_n]
\]
is a Gröbner basis of the elimination ideal
\[
I_\ell=I\cap k[x_{\ell+1},\ldots,x_n].
\]

<1>1. Why the theorem holds.
::: proof
Take $0\ne f\in I_\ell$. Since $G$ is a Gröbner basis of $I$, some $g\in G$
has $\operatorname{LM}(g)$ dividing $\operatorname{LM}(f)$. The latter contains
none of $x_1,\ldots,x_\ell$. Hence $\operatorname{LM}(g)$ contains none of them.
Under lex order, if $g$ had any term involving one of those variables, that term
would be larger than every term involving only $x_{\ell+1},\ldots,x_n$, so its
leading monomial would also involve an eliminated variable. Therefore
$g\in G_\ell$. Thus the leading monomials of $G_\ell$ generate
$\operatorname{in}(I_\ell)$.
:::

<1>2. It is called elimination because it computes all polynomial consequences
of $I$ involving only the remaining variables $x_{\ell+1},\ldots,x_n$.
::: proof
By definition, those consequences are exactly the elements of the intersection
$I\cap k[x_{\ell+1},\ldots,x_n]$. The theorem obtains generators for that ideal
by discarding from $G$ the polynomials that still involve eliminated variables.
:::
:::
