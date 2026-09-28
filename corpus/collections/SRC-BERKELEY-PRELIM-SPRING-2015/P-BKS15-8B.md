---
schema: qual/card@1
id: P-BKS15-8B
kind: problem
title: Groups of exponent $2$ are abelian; groups of odd prime exponent need not be
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2015 Graduate Preliminary Examination.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the involution argument for p=2, the exponent-p calculation in the upper unitriangular group, and the explicit noncommuting pair.
---

::: {.problem}
Let $p$ be a prime and let $G$ be a group such that $g^p=1$ for all $g\in G$.
Show that if $p=2$ then $G$ is abelian, and give an example with $p>2$ for which $G$ is not abelian.
:::

::: {.solution}
<1>1. If $p=2$, then $G$ is abelian.

::: {.proof}
For every $g\in G$,
$$
g^2=1,
$$
so $g^{-1}=g$. Given $g,h\in G$, the hypothesis also applies to $gh$, hence
$$
gh
=
(gh)^{-1}
=
h^{-1}g^{-1}
=
hg.
$$
Thus every two elements commute.
:::

<1>2. Let $p>2$ be prime, and let $U_3(\FF_p)$ be the subgroup of $\GL_3(\FF_p)$ consisting of matrices
$$
\begin{pmatrix}
1&a&b\\
0&1&c\\
0&0&1
\end{pmatrix},
\qquad
a,b,c\in\FF_p.
$$
Every element of $U_3(\FF_p)$ has $p$th power equal to the identity.

::: {.proof}
Every such matrix has the form
$$
I+X,
$$
where $X$ is strictly upper triangular. Hence
$$
X^3=0.
$$
Since $I$ and $X$ commute, the binomial theorem gives
$$
(I+X)^p
=
I+pX+\binom{p}{2}X^2,
$$
because all terms involving $X^k$ with $k\geq3$ vanish. In the field $\FF_p$,
$$
p=0
$$
and, since $p$ is odd,
$$
\binom{p}{2}
=
\frac{p(p-1)}2
=
0.
$$
Therefore
$$
(I+X)^p=I.
$$
:::

<1>3. The group $U_3(\FF_p)$ is not abelian.

::: {.proof}
Let
$$
g
=
I+E_{12}
=
\begin{pmatrix}
1&1&0\\
0&1&0\\
0&0&1
\end{pmatrix},
\qquad
h
=
I+E_{23}
=
\begin{pmatrix}
1&0&0\\
0&1&1\\
0&0&1
\end{pmatrix}.
$$
Since
$$
E_{12}E_{23}=E_{13}
\qquad\text{and}\qquad
E_{23}E_{12}=0,
$$
one has
$$
gh
=
I+E_{12}+E_{23}+E_{13}
\neq
I+E_{12}+E_{23}
=
hg.
$$
Thus $U_3(\FF_p)$ is nonabelian.
:::

<1>4. Hence exponent $2$ forces a group to be abelian, whereas for every odd prime $p$ there is a nonabelian group all of whose elements satisfy $g^p=1$.

::: {.proof}
Step <1>1 proves the assertion for $p=2$. Steps <1>2 and <1>3 give the required counterexample for every $p>2$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is exactly the required conclusion.
:::
:::
