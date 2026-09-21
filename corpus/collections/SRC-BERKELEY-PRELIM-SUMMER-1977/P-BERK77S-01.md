---
schema: qual/card@1
id: P-BERK77S-01
kind: problem
title: Vector-space structure and shifted-power bases in $F[x]$
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
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Verified the vector-space axioms coefficientwise, identified
    1,x,...,x^n as a basis of F_n[x], and proved the shifted powers
    1,(x-a),...,(x-a)^n linearly independent from their distinct leading
    degrees; dimension n+1 then makes them a basis.
---

::: {.problem}
Let $F$ be a field.

1. Prove that $F[x]$ is a vector space over $F$.
2. Prove that the subset $F_n[x]$ of polynomials of degree at most $n$ is a subspace of dimension $n+1$.
3. Prove that for every $a\in F$ the polynomials
   \[
   1,x-a,\dots,(x-a)^n
   \]
   form a basis of $F_n[x]$.
:::

::: {.solution}
<1>1. Part (1): $F[x]$ is a vector space over $F$ under the usual
polynomial addition and scalar multiplication.

::: {.proof}
Write
$$
p(x)=\sum_{j=0}^m p_jx^j,
\qquad
q(x)=\sum_{j=0}^n q_jx^j.
$$
After adjoining zero coefficients as needed, polynomial addition and scalar
multiplication are
$$
(p+q)(x)=\sum_{j\geq0}(p_j+q_j)x^j
$$
and
$$
(cp)(x)=\sum_{j\geq0}(cp_j)x^j
$$
for $c\in F$. Only finitely many coefficients are nonzero, so these
operations remain in $F[x]$.

The zero polynomial is the additive identity, and
$$
-p(x)=\sum_{j\geq0}(-p_j)x^j
$$
is the additive inverse of $p$. Commutativity and associativity of addition,
the distributive laws, compatibility of scalar multiplication, and
$1p=p$ all hold coefficientwise because they hold in the field $F$.
Therefore the vector-space axioms hold.
:::

<1>2. Part (2): $F_n[x]$ is a vector subspace of $F[x]$.

::: {.proof}
The zero polynomial lies in $F_n[x]$. If $p,q\in F_n[x]$, then
$$
\deg(p+q)\leq n
$$
unless $p+q=0$, which is also in $F_n[x]$. If $c\in F$, then either
$cp=0$ or
$$
\deg(cp)=\deg p\leq n.
$$
Thus $F_n[x]$ is closed under addition and scalar multiplication, so it is
a subspace.
:::

<1>3. The list
$$
1,x,\ldots,x^n
$$
is a basis of $F_n[x]$.

::: {.proof}
Every polynomial $p\in F_n[x]$ has a unique expression
$$
p(x)=a_0+a_1x+\cdots+a_nx^n
$$
with $a_j\in F$. Hence the displayed list spans $F_n[x]$. If
$$
c_0+c_1x+\cdots+c_nx^n=0,
$$
equality of polynomial coefficients gives
$$
c_0=c_1=\cdots=c_n=0.
$$
Thus the list is linearly independent and hence a basis.
:::

<1>4. Consequently,
$$
\boxed{
\dim_F F_n[x]=n+1.
}
$$

::: {.proof}
Step <1>3 gives a basis with exactly $n+1$ elements.
:::

<1>5. Part (3): for every $a\in F$, the polynomials
$$
1,\ x-a,\ \ldots,\ (x-a)^n
$$
are linearly independent in $F_n[x]$.

::: {.proof}
Suppose
$$
\sum_{j=0}^n c_j(x-a)^j=0.
$$
If some $c_j$ were nonzero, let $m$ be the largest index with
$c_m\neq0$. The polynomial $(x-a)^m$ has degree $m$ and leading
coefficient $1$, whereas every term with index less than $m$ has degree
less than $m$. Therefore the coefficient of $x^m$ in the displayed sum is
$c_m\neq0$, contradicting that the sum is the zero polynomial. Hence every
$c_j=0$, proving linear independence.
:::

<1>6. For every $a\in F$,
$$
\boxed{
\{1,x-a,\ldots,(x-a)^n\}
}
$$
is a basis of $F_n[x]$.

::: {.proof}
Each $(x-a)^j$ has degree $j\leq n$, so all $n+1$ displayed polynomials
belong to $F_n[x]$. By step <1>5 they are linearly independent, while step
<1>4 shows that $F_n[x]$ has dimension $n+1$. Therefore they form a basis.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>1 proves part (1), steps <1>2--<1>4 prove part (2), and steps
<1>5--<1>6 prove part (3).
:::
:::
