---
schema: qual/card@1
id: PR-RRTST
kind: proposition
title: Rational root theorem
slogan: 'Lowest-term rational roots divide the constant and leading coefficients.'
classification:
  areas:
  - algebra
  topics:
  - Polynomials
relations: []
review: draft
---

::: {.proposition}
Let
$$
f(t)=a_nt^n+\cdots+a_1t+a_0\in\ZZ[t],
\qquad
a_n\neq0.
$$
If $p/q\in\QQ$ is a root of $f$, where $p,q\in\ZZ$ are coprime and $q\neq0$, then
$$
p\divides a_0,
\qquad
q\divides a_n.
$$
In particular, if $f$ is monic, every rational root of $f$ is an integer dividing $a_0$.
:::

::: {.proof}
From $f(p/q)=0$, multiplication by $q^n$ gives
$$
a_np^n+a_{n-1}p^{n-1}q+\cdots+a_1pq^{n-1}+a_0q^n=0.
$$
Thus
$$
a_0q^n
=
-p\left(a_np^{n-1}+a_{n-1}p^{n-2}q+\cdots+a_1q^{n-1}\right),
$$
so $p\divides a_0q^n$. Since $p$ and $q$ are coprime, $p\divides a_0$.

Similarly,
$$
a_np^n
=
-q\left(a_{n-1}p^{n-1}+\cdots+a_1pq^{n-2}+a_0q^{n-1}\right),
$$
so $q\divides a_np^n$. Since $p$ and $q$ are coprime, $q\divides a_n$.
If $f$ is monic, then $a_n=1$, so $q=\pm1$ and the root is an integer dividing $a_0$.
:::

::: {.remark}
If $r$ is a root of $f$, polynomial long division gives
$$
f(t)=(t-r)g(t),
\qquad
\deg g=\deg f-1,
$$
and the remaining roots of $f$ are the roots of $g$.
:::
