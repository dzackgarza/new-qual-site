---
schema: qual/card@1
id: E-SMI-8000E-GG2
kind: problem
title: Constructing the field with 125 elements
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared the statement with Smith 8000e Galois-groups problem 2."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Checked that x^3+x+1 has no root in F5, hence is irreducible, and counted the residue classes in the quotient field."
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared the card with Smith 8000e Galois problem 2."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Checked x^3+x+1 at every element of F5, used the root criterion for cubic irreducibility, and counted the degree-three quotient field."
---

::: {.exercise}
Find an irreducible cubic polynomial mod 5, and hence construct a field with 125 elements.
:::

::: solution
Consider
$$
f(X)=X^3+X+1\in\mathbf F_5[X].
$$

<1>1. The polynomial $f$ is irreducible over $\mathbf F_5$.
::: proof
A cubic over a field is reducible if and only if it has a root in that field.
Evaluate $f$ at the five elements of $\mathbf F_5$:
$$
\begin{array}{c|ccccc}
a&0&1&2&3&4\\ \hline
f(a)&1&3&1&1&4.
\end{array}
$$
None of these values is zero. Thus $f$ has no root in $\mathbf F_5$, and
hence
$$
\boxed{f(X)=X^3+X+1\text{ is irreducible over }\mathbf F_5.}
$$
:::

<1>2. Quotient by $f$ to construct the desired field.
::: proof
Because $f$ is irreducible, the ideal $(f)$ is maximal in
$\mathbf F_5[X]$. Therefore
$$
K=\mathbf F_5[X]/(f)
$$
is a field.

Let $\alpha=X+(f)$. Every residue class has a unique representative of degree
at most two, so every element of $K$ is uniquely
$$
a+b\alpha+c\alpha^2,
\qquad a,b,c\in\mathbf F_5.
$$
There are therefore
$$
5^3=125
$$
elements. Thus
$$
\boxed{K=\mathbf F_5[X]/(X^3+X+1)}
$$
is a field with exactly $125$ elements.
:::
:::

::: solution
Take
$$
f(x)=x^3+x+1\in\mathbf F_5[x].
$$

<1>1. The polynomial $f$ is irreducible over $\mathbf F_5$.
::: proof
A cubic over a field is reducible if and only if it has a root in that field.
Evaluate $f$ on all five elements of $\mathbf F_5$:
$$
\begin{array}{c|ccccc}
a&0&1&2&3&4\\ \hline
f(a)&1&3&1&1&4
\end{array}
$$
where the values are reduced modulo $5$. None is zero. Thus $f$ has no root
in $\mathbf F_5$, so
$$
\boxed{x^3+x+1\text{ is irreducible over }\mathbf F_5.}
$$
:::

<1>2. Form the quotient field and count its elements.
::: proof
Because $f$ is irreducible, the ideal $(f)$ is maximal and
$$
K=\mathbf F_5[x]/(x^3+x+1)
$$
is a field. If
$$
\alpha=x+(f),
$$
then every residue class has a unique representative of degree at most $2$,
so every element of $K$ has a unique expression
$$
a+b\alpha+c\alpha^2,
\qquad
a,b,c\in\mathbf F_5.
$$
There are therefore
$$
5^3=125
$$
elements. Hence
$$
\boxed{\mathbf F_5[x]/(x^3+x+1)}
$$
is an explicit field with $125$ elements.
:::
:::
