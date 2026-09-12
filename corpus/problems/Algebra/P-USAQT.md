---
schema: qual/card@1
id: P-USAQT
kind: problem
title: Ideals, $\spec$, $\maxspec$, and radicals
classification:
  areas:
  - algebra
  topics:
  - Ideals
  - Prime Ideals
  - Maximal Ideals
relations: []
review: draft
---

::: problem
Let rings be commutative with identity.

1. Show that every proper ideal is contained in a maximal ideal.
2. If $R$ is a PID and $x\in R$ is a nonzero nonunit, show that $x$ is irreducible iff $(x)$ is maximal.
3. Show that intersections, products, and sums of ideals are ideals.
4. Show that the union of two ideals need not be an ideal.
5. Show that every nonzero ring has a maximal ideal.
6. Show that $I$ is maximal iff $R/I$ is a field.
7. Show that $I$ is prime iff $R/I$ is an integral domain.
8. Show that
   \[
   \bigcup_{\mathfrak m\in\operatorname{MaxSpec}R}\mathfrak m
   =R\setminus R^\times.
   \]
9. Show that $\operatorname{MaxSpec}R\subseteq\operatorname{Spec}R$, and give an example of strict containment and one of equality.
10. Show that every prime ideal is radical.
11. Show that the nilradical is $\sqrt{(0)}$.
12. Show that
    \[
    \sqrt{IJ}=\sqrt I\cap\sqrt J.
    \]
13. If $R$ is an integral domain and $\operatorname{Spec}R\subseteq\operatorname{MaxSpec}R$, show that $R$ is a UFD.
14. Show that a Noetherian ring has every ideal finitely generated.
:::

::: solution
<1>1. Let $I\subsetneq R$. Consider the set of proper ideals containing $I$, ordered by inclusion. The union of a chain is again an ideal, and it is proper: if its union contained $1$, then one member of the chain would contain $1$. By Zorn's lemma there is a maximal member, i.e. a maximal ideal containing $I$.

<1>2. Suppose $x$ is irreducible and
\[
(x)\subseteq(a)\subseteq R.
\]
Then $x=ar$. Irreducibility gives either $a$ a unit, so $(a)=R$, or $r$ a unit, so $(a)=(x)$. Hence $(x)$ is maximal. Conversely, if $(x)$ is maximal and $x=ab$, then
\[
(x)\subseteq(a)\subseteq R.
\]
Maximality forces $(a)=(x)$ or $(a)=R$, so one of $a,b$ is a unit. Thus $x$ is irreducible.

<1>3. Arbitrary intersections of ideals are ideals. For ideals $I,J$,
\[
I+J=\{a+b:a\in I,b\in J\}
\]
is an ideal, and
\[
IJ=\left\{\sum_{k=1}^r a_kb_k:a_k\in I,b_k\in J\right\}
\]
is an ideal by closure under addition and multiplication by arbitrary elements of $R$.

<1>4. In $\ZZ$, the ideals $(2)$ and $(3)$ have union that is not an ideal: $2,3$ lie in the union but
\[
2+3=5
\]
does not.

<1>5. If $R\ne0$, then $(0)$ is proper. By <1>1 it lies in a maximal ideal.

<1>6. Ideals of $R/I$ correspond to ideals of $R$ containing $I$. Thus $I$ is maximal exactly when $R/I$ has no ideals except $0$ and itself. A nonzero commutative ring with identity has this property exactly when it is a field.

<1>7. One has
\[
ab\in I\iff (a+I)(b+I)=0\text{ in }R/I.
\]
Thus $I$ is prime exactly when $R/I$ has no zero divisors, i.e. is an integral domain.

<1>8. A unit cannot lie in a proper ideal, so no unit lies in any maximal ideal. Conversely, if $x$ is a nonunit, then $(x)$ is proper, hence by <1>1 lies in some maximal ideal. Therefore the union of maximal ideals is exactly the set of nonunits.

<1>9. Every maximal ideal is prime by <1>6--<1>7, since every field is a domain. Hence
\[
\operatorname{MaxSpec}R\subseteq\operatorname{Spec}R.
\]
For $R=\ZZ$ the containment is strict because $(0)$ is prime but not maximal. For a field $k$,
\[
\operatorname{Spec}k=\operatorname{MaxSpec}k=\{(0)\}.
\]

<1>10. Let $\mathfrak p$ be prime and suppose $x^n\in\mathfrak p$. Repeated primality applied to
\[
x^n=x\cdot x^{n-1}
\]
shows $x\in\mathfrak p$. Thus $\mathfrak p=\sqrt{\mathfrak p}$.

<1>11. By definition,
\[
\sqrt{(0)}=\{x\in R:x^n=0\text{ for some }n\ge1\},
\]
which is exactly the nilradical.

<1>12. Since $IJ\subseteq I\cap J$,
\[
\sqrt{IJ}\subseteq\sqrt I\cap\sqrt J.
\]
Conversely, if $x\in\sqrt I\cap\sqrt J$, choose $m,n$ with $x^m\in I$ and $x^n\in J$. Then
\[
x^{m+n}=x^mx^n\in IJ,
\]
so $x\in\sqrt{IJ}$.

<1>13. Since $R$ is a domain, $(0)$ is prime. The hypothesis therefore makes $(0)$ maximal. Hence
\[
R/(0)=R
\]
is a field by <1>6. Every field is a UFD.

<1>14. If “Noetherian” is defined by the ascending-chain condition, suppose an ideal $I$ were not finitely generated. Choose $a_1\in I$, then inductively choose
\[
a_{n+1}\in I\setminus(a_1,\ldots,a_n).
\]
This produces a strictly ascending chain
\[
(a_1)\subsetneq(a_1,a_2)\subsetneq(a_1,a_2,a_3)\subsetneq\cdots,
\]
contradicting the ACC. Hence every ideal is finitely generated.
:::
