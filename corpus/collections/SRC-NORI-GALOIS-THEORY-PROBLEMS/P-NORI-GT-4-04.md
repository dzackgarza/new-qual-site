---
schema: qual/card@1
id: P-NORI-GT-4-04
kind: problem
title: $E(X)/F(X)$ has the same degree as $E/F$
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 4.4 of the retained Nori Galois Theory Problems PDF.
---

::: {.problem}
Let E be a field extension of F of degree n.

(i) Prove that $E [ X ]$ , when regarded as a module over its subring $F [ X ]$ , is free of rank n.

(ii) Let $0 \not = f \in E [ X ]$ . Prove that there is some $g \in E [ X ]$ such that $g f = h$ wher $0 \neq h \in F [ X ]$

Hint: Consider $h = \operatorname { N o r m } _ { F \left[ X \right] } ^ { E \left[ X \right] } ( f )$

(iii) Prove that $E ( X )$ is a field extension of $F ( X )$ of degree n. More precisely, show that if $w _ { 1 } , . . . , w _ { n }$ is a F -basis for $E .$ , then $w _ { 1 } , . . . , w _ { n }$ is also a $F ( X )$ -basis for $E ( X )$ .
:::

::: {.solution}
Let
$$
w_1,\ldots,w_n
$$
be an $F$-basis of $E$.

<1>1. Every polynomial $f\in E[X]$ can be written uniquely in the form
$$
f=\sum_{i=1}^n w_i p_i(X)
$$
with $p_i(X)\in F[X]$.

::: {.proof}
Write
$$
f(X)=\sum_{j=0}^m a_jX^j
$$
with $a_j\in E$. For each coefficient there are unique scalars $c_{ij}\in F$ such that
$$
a_j=\sum_{i=1}^n c_{ij}w_i.
$$
Then
$$
f(X)
=\sum_{i=1}^n w_i\left(\sum_{j=0}^m c_{ij}X^j\right).
$$
Thus existence holds with
$$
p_i(X)=\sum_j c_{ij}X^j\in F[X].
$$
If
$$
\sum_iw_ip_i(X)=0,
$$
then comparison of each power of $X$ gives an $F$-linear relation among $w_1,\ldots,w_n$, so every coefficient of every $p_i$ is zero. Hence the representation is unique.
:::

<1>2. Consequently
$$
\boxed{E[X]\text{ is a free }F[X]\text{-module of rank }n}
$$
with basis $w_1,\ldots,w_n$.

::: {.proof}
Step <1>1 is exactly the assertion that these elements form an $F[X]$-basis.
:::

<1>3. Let $0\ne f\in E[X]$. There exists $g\in E[X]$ such that
$$
gf=h
$$
for some nonzero $h\in F[X]$.

::: {.proof}
Apply Problem 4.3 to the ring extension
$$
F[X]\subset E[X].
$$
By step <1>2, $E[X]$ is free of rank $n$ over $F[X]$. Problem 4.3 gives $g\in E[X]$ with
$$
gf=\operatorname{Norm}_{F[X]}^{E[X]}(f)=:h\in F[X].
$$
Since $E[X]$ is an integral domain and $f\ne0$, the nonvanishing assertion of Problem 4.3 gives
$$
h\ne0.
$$
:::

<1>4. Every element of $E(X)$ is an $F(X)$-linear combination of $w_1,\ldots,w_n$.

::: {.proof}
Let
$$
\frac rs\in E(X),
\qquad
r,s\in E[X],\ s\ne0.
$$
By step <1>3, choose $g\in E[X]$ and $0\ne h\in F[X]$ with
$$
gs=h.
$$
Then
$$
\frac rs=\frac{rg}{h}.
$$
By step <1>1, write
$$
rg=\sum_{i=1}^n w_i p_i(X)
$$
with $p_i\in F[X]$. Therefore
$$
\frac rs
=\sum_{i=1}^n w_i\frac{p_i(X)}{h(X)},
$$
and each coefficient belongs to $F(X)$.
:::

<1>5. The elements $w_1,\ldots,w_n$ are linearly independent over $F(X)$.

::: {.proof}
Suppose
$$
\sum_{i=1}^n q_i(X)w_i=0
$$
with $q_i\in F(X)$. Choose a common nonzero denominator $d(X)\in F[X]$ such that
$$
p_i(X)=d(X)q_i(X)\in F[X]
$$
for every $i$. Multiplying the relation by $d(X)$ gives
$$
\sum_{i=1}^n p_i(X)w_i=0
$$
in $E[X]$. By the $F[X]$-linear independence from step <1>2, every $p_i=0$, hence every $q_i=0$.
:::

<1>6. Therefore
$$
\boxed{[E(X):F(X)]=n}
$$
and $w_1,\ldots,w_n$ is an $F(X)$-basis of $E(X)$.

::: {.proof}
The inclusion $F(X)\subset E(X)$ is induced from $F\subset E$. Step <1>4 gives spanning over $F(X)$ and step <1>5 gives linear independence. Thus these $n$ elements form a basis.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>2 proves part (i), step <1>3 proves part (ii), and step <1>6 proves part (iii).
:::
:::
