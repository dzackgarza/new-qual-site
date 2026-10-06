---
schema: qual/card@1
id: P-SHON-HW11-02
kind: problem
title: An ordered field criterion for algebraic closure after adjoining $i$
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 2 of the retained Algebra HW 11 solution packet.
---

::: {.problem}
Let $R$ be an ordered field whose squares are exactly the nonnegative elements, and suppose polynomials in $R[x]$ satisfy the intermediate value theorem.
Set
\[
C=R[x]/(x^2+1).
\]

1. Show that $R$ has characteristic zero and every odd-degree polynomial over $R$ has a root in $R$.
   Deduce that every nontrivial finite Galois extension of $R$ has even degree.

2. Show that $C$ is a field, every element of $C$ is a square in $C$, and $C$ has no degree-two field extension.

3. If $R\subset C\subset L$ are finite extensions and $L/R$ is Galois with group $G$, show that $G$ is a $2$-group.

4. In the situation of (3), show that $L=C$.

5. Conclude that $C$ is algebraically closed.

6. Deduce the algebraic closedness of the usual complex numbers from the corresponding properties of $\mathbb R$.
:::

::: {.solution}
Let \(R\) be as in the problem, and let
\[
C=R[i],
\qquad
i^2=-1.
\]

## Part 1

<1>1. The ordered field \(R\) has characteristic \(0\).

::: {.proof}
In an ordered field,
\[
1>0.
\]
Hence every positive integer multiple
\[
n\cdot1
\]
is positive, so it cannot equal \(0\). Thus no positive characteristic is possible.
:::

<1>2. Let
\[
f(x)=a_{2m+1}x^{2m+1}+\cdots+a_0
\]
have odd degree, with \(a_{2m+1}\ne0\).

::: {.proof}
This is an arbitrary odd-degree polynomial.
:::

<1>3. There exists \(M>0\) in \(R\) such that for every \(x>M\),
\[
\left|
\sum_{j=0}^{2m}a_jx^j
\right|
<
|a_{2m+1}|x^{2m+1}.
\]

::: {.proof}
Choose
\[
M>
1+
\sum_{j=0}^{2m}
\left|
\frac{a_j}{a_{2m+1}}
\right|.
\]
For \(x>M>1\),
\[
x^{2m+1-j}>M>
\left|
\frac{a_j}{a_{2m+1}}
\right|
\]
for each \(j\le2m\). Hence
\[
|a_j|x^j
<
|a_{2m+1}|x^{2m+1}.
\]
Using the stronger choice with the sum of the coefficient ratios gives the stated bound after summing.
:::

<1>4. Consequently, for sufficiently large positive \(x\), \(f(x)\) has the sign of \(a_{2m+1}\), while for sufficiently large negative \(x\), \(f(x)\) has the opposite sign.

::: {.proof}
By step <1>3, the leading term dominates the sum of all lower-degree terms. Since the degree \(2m+1\) is odd,
\[
(-x)^{2m+1}=-x^{2m+1}.
\]
:::

<1>5. Therefore every odd-degree polynomial in \(R[x]\) has a root in \(R\).

::: {.proof}
Choose \(u<v\) so that \(f(u)\) and \(f(v)\) have opposite signs as in step <1>4. The assumed intermediate value theorem gives \(c\in[u,v]\) with
\[
f(c)=0.
\]
:::

<1>6. Every nontrivial finite Galois extension \(L/R\) has even degree.

::: {.proof}
A finite Galois extension is separable, so by the primitive element theorem
\[
L=R(\alpha).
\]
Let \(m_\alpha\) be the minimal polynomial. Then
\[
[L:R]=\deg m_\alpha.
\]
If this degree were odd and \(>1\), step <1>5 would give a root of \(m_\alpha\) in \(R\), contradicting irreducibility. Hence every nontrivial finite Galois degree is even.
:::

## Part 2

<1>7. The polynomial
\[
x^2+1
\]
is irreducible over \(R\).

::: {.proof}
A root \(r\in R\) would satisfy
\[
r^2=-1.
\]
But squares are exactly the nonnegative elements, whereas
\[
-1<0.
\]
Thus no root exists, and a quadratic without a root is irreducible.
:::

<1>8. Hence
\[
\boxed{C=R[x]/(x^2+1)}
\]
is a field.

::: {.proof}
The quotient of a polynomial ring over a field by an irreducible polynomial is a field.
:::

<1>9. Every element of \(C\) has a unique form
\[
a+bi,
\qquad
a,b\in R.
\]

::: {.proof}
Modulo \(x^2+1\), every polynomial reduces uniquely to degree \(<2\).
:::

<1>10. For \(a,b\in R\), the element
\[
a^2+b^2
\]
is nonnegative, so there exists
\[
r\in R_{\ge0}
\]
with
\[
r^2=a^2+b^2.
\]

::: {.proof}
By hypothesis, the nonnegative elements of \(R\) are exactly the squares.
:::

<1>11. If \(b=0\) and \(a\ge0\), then \(a+bi\) is a square in \(C\).

::: {.proof}
Choose \(u\in R\) with
\[
u^2=a.
\]
Then
\[
(u+0i)^2=a.
\]
:::

<1>12. If \(b=0\) and \(a<0\), then \(a+bi\) is a square in \(C\).

::: {.proof}
Since \(-a>0\), choose \(v\in R\) with
\[
v^2=-a.
\]
Then
\[
(vi)^2=-v^2=a.
\]
:::

<1>13. Assume \(b\ne0\). Then
\[
r>|a|.
\]

::: {.proof}
Since
\[
r^2=a^2+b^2>a^2=|a|^2
\]
and \(r,|a|\ge0\), one has \(r>|a|\).
:::

<1>14. Hence
\[
\frac{r+a}{2}>0,
\]
so choose \(u\in R\) with
\[
\boxed{
u^2=\frac{r+a}{2}}.
\]

::: {.proof}
By step <1>13,
\[
r+a\ge r-|a|>0.
\]
Again use the hypothesis that every nonnegative element is a square.
:::

<1>15. Define
\[
\boxed{
v=\frac{b}{2u}}.
\]

::: {.proof}
Step <1>14 gives \(u\ne0\), so this is well-defined.
:::

<1>16. One has
\[
2uv=b.
\]

::: {.proof}
This is immediate from the definition of \(v\).
:::

<1>17. One has
\[
u^2-v^2=a.
\]

::: {.proof}
From step <1>15,
\[
v^2=\frac{b^2}{4u^2}
=
\frac{b^2}{2(r+a)}.
\]
Since
\[
b^2=r^2-a^2=(r-a)(r+a),
\]
\[
v^2=\frac{r-a}{2}.
\]
Therefore
\[
u^2-v^2
=
\frac{r+a}{2}-\frac{r-a}{2}
=
a.
\]
:::

<1>18. Thus
\[
\boxed{
(u+vi)^2=a+bi}.
\]

::: {.proof}
\[
(u+vi)^2
=
u^2-v^2+2uvi,
\]
and steps <1>16--<1>17 identify the two coefficients.
:::

<1>19. Every element of \(C\) is a square.

::: {.proof}
The cases \(b=0\) are steps <1>11--<1>12, and the case \(b\ne0\) is step <1>18.
:::

<1>20. The field \(C\) has no extension of degree \(2\).

::: {.proof}
Suppose \(E/C\) had degree \(2\). Since \(\operatorname{char}C=0\), the extension is separable and hence simple:
\[
E=C(\alpha)
\]
with \(\alpha\) satisfying an irreducible quadratic
\[
x^2+ux+v.
\]
Completing the square, if
\[
\beta=2\alpha+u,
\]
then
\[
\beta^2=u^2-4v\in C.
\]
By step <1>19, choose \(\gamma\in C\) with
\[
\gamma^2=u^2-4v.
\]
Then
\[
\beta^2=\gamma^2,
\]
so
\[
(\beta-\gamma)(\beta+\gamma)=0.
\]
Since \(E\) is a field, \(\beta=\pm\gamma\in C\), hence \(\alpha\in C\), contradiction.
:::

## Part 3

Assume
\[
R\subset C\subset L
\]
are finite extensions and \(L/R\) is Galois. Let
\[
G=\operatorname{Gal}(L/R).
\]

<1>21. Write
\[
|G|=2^rm
\]
with \(m\) odd.

::: {.proof}
Every positive integer has a unique factorization into a power of \(2\) times an odd integer.
:::

<1>22. Let \(P\le G\) be a Sylow \(2\)-subgroup, so
\[
|P|=2^r.
\]

::: {.proof}
This is Sylow's first theorem.
:::

<1>23. Let
\[
K=L^P
\]
be the fixed field. Then
\[
\boxed{
[K:R]=m}.
\]

::: {.proof}
By the fundamental theorem of Galois theory,
\[
[L:K]=|P|=2^r.
\]
Since
\[
[L:R]=|G|=2^rm,
\]
the tower law gives
\[
[K:R]=m.
\]
:::

<1>24. If \(m>1\), then \(K/R\) is a nontrivial finite extension of odd degree.

::: {.proof}
Step <1>23 gives the odd degree \(m\).
:::

<1>25. Such an extension cannot exist.

::: {.proof}
Because \(L/R\) is Galois, it is separable, so every intermediate extension \(K/R\) is separable. Hence by the primitive element theorem
\[
K=R(\alpha)
\]
for some \(\alpha\), and
\[
[K:R]
\]
is the degree of its irreducible minimal polynomial. If this degree were odd and \(>1\), step <1>5 would force that polynomial to have a root in \(R\), contradiction.
:::

<1>26. Therefore
\[
m=1,
\]
so
\[
\boxed{G\text{ is a }2\text{-group}.}
\]

::: {.proof}
Steps <1>24--<1>25 rule out \(m>1\).
:::

## Part 4

<1>27. Since
\[
[C:R]=2
\]
and
\[
[L:R]=|G|=2^r,
\]
one has
\[
\boxed{
[L:C]=2^{r-1}}.
\]

::: {.proof}
Apply the tower law.
:::

<1>28. The extension \(L/C\) is Galois.

::: {.proof}
Since \(L/R\) is Galois and \(C\) is an intermediate field, \(L/C\) is separable. It is also normal because every \(C\)-embedding of \(L\) fixes \(R\), hence sends \(L\) to itself by normality over \(R\). Thus \(L/C\) is Galois.
:::

<1>29. If \(r\ge2\), then
\[
\operatorname{Gal}(L/C)
\]
is a nontrivial finite \(2\)-group.

::: {.proof}
Its order is
\[
[L:C]=2^{r-1}\ge2
\]
by step <1>27.
:::

<1>30. Every nontrivial finite \(2\)-group has a subgroup of index \(2\).

::: {.proof}
A finite \(p\)-group has a normal subgroup of index \(p\); equivalently, choose a maximal proper subgroup, whose index in a finite \(p\)-group is \(p\). For \(p=2\), the index is \(2\).
:::

<1>31. If \(r\ge2\), there would therefore be an intermediate field
\[
C\subsetneq E\subseteq L
\]
with
\[
[E:C]=2.
\]

::: {.proof}
By step <1>30, choose
\[
H\le\operatorname{Gal}(L/C)
\]
of index \(2\). Its fixed field \(E=L^H\) satisfies
\[
[E:C]
=
[\operatorname{Gal}(L/C):H]
=
2.
\]
:::

<1>32. This contradicts step <1>20.

::: {.proof}
Step <1>20 says \(C\) has no degree-two extension.
:::

<1>33. Therefore
\[
r=1
\]
and hence
\[
\boxed{L=C}.
\]

::: {.proof}
If \(r=1\), then step <1>27 gives
\[
[L:C]=1.
\]
:::

## Part 5

<1>34. Suppose, toward a contradiction, that \(C\) is not algebraically closed.

::: {.proof}
Then there is a nonconstant irreducible polynomial over \(C\) of degree \(>1\).
:::

<1>35. Choose a root \(\alpha\) of such a polynomial in an algebraic closure and set
\[
E=C(\alpha).
\]
Then
\[
[E:C]<\infty
\]
and \(E\ne C\).

::: {.proof}
The degree equals the degree of the irreducible polynomial of \(\alpha\) over \(C\).
:::

<1>36. Since
\[
[R:C]=2
\]
in the tower \(R\subset C\subset E\), the extension \(E/R\) is finite.

::: {.proof}
The tower law gives
\[
[E:R]=[E:C][C:R]<\infty.
\]
:::

<1>37. Because \(\operatorname{char}R=0\), \(E/R\) is separable.

::: {.proof}
Every algebraic extension in characteristic \(0\) is separable.
:::

<1>38. Let \(L\) be the Galois closure of \(E/R\). Then
\[
R\subset C\subset E\subset L,
\]
and \(L/R\) is finite Galois.

::: {.proof}
The Galois closure of a finite separable extension is finite Galois and contains the original extension.
:::

<1>39. By part 4,
\[
\boxed{L=C}.
\]

::: {.proof}
The tower \(R\subset C\subset L\) satisfies the hypotheses of part 4.
:::

<1>40. This is impossible because
\[
C\subsetneq E\subset L.
\]

::: {.proof}
Step <1>35 gives \(E\ne C\), while step <1>39 gives \(L=C\).
:::

<1>41. Therefore
\[
\boxed{C\text{ is algebraically closed}.}
\]

::: {.proof}
The assumption in step <1>34 led to a contradiction.
:::

## Part 6

<1>42. The usual real field \(\mathbb R\) is ordered, its nonnegative elements are exactly its squares, and real polynomials satisfy the intermediate value theorem.

::: {.proof}
These are the standard order and completeness properties of \(\mathbb R\).
:::

<1>43. The quotient
\[
\mathbb R[x]/(x^2+1)
\]
is canonically isomorphic to the usual complex field \(\mathbb C\).

::: {.proof}
Send the class of \(x\) to \(i\).
:::

<1>44. Therefore
\[
\boxed{\mathbb C\text{ is algebraically closed}.}
\]

::: {.proof}
Apply step <1>41 to \(R=\mathbb R\), then use step <1>43.
:::

<1>45. Q.E.D.

::: {.proof}
Steps <1>1--<1>6 prove part 1, steps <1>7--<1>20 prove part 2, steps <1>21--<1>26 prove part 3, steps <1>27--<1>33 prove part 4, steps <1>34--<1>41 prove part 5, and steps <1>42--<1>44 prove part 6.
:::
:::
