---
schema: qual/card@1
id: P-APAS26D
kind: problem
title: An algebra is commutative iff every element is normal
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
relations: []
review: draft
---

::: problem
Let $\mathcal{A}$ be an algebra.
Prove that $\mathcal{A}$ is commutative if and only if all its elements are normal.

Note: On this exam, an algebra is a finite-dimensional complex vector space equipped with an associative, bilinear, unital multiplication and an antilinear, antimultiplicative, involutive conjugation.
:::

::: solution
If $\mathcal A$ is commutative, then for every $a\in\mathcal A$,
\[
aa^*=a^*a,
\]
so every element is normal.

Conversely, suppose every element of $\mathcal A$ is normal. Let $a,b\in\mathcal A$. Since $a+b$ is normal,
\[
(a+b)(a^*+b^*)=(a^*+b^*)(a+b).
\]
Using normality of $a$ and $b$ and cancelling the diagonal terms gives
\[
ab^*+ba^*=a^*b+b^*a. \tag{1}
\]
Since $a+ib$ is also normal,
\[
(a+ib)(a^*-ib^*)=(a^*-ib^*)(a+ib).
\]
Again cancelling $aa^*=a^*a$ and $bb^*=b^*b$ gives
\[
-ab^*+ba^*=a^*b-b^*a. \tag{2}
\]
Adding and subtracting (1) and (2) yields
\[
ab^*=b^*a,
\qquad
ba^*=a^*b.
\]
In particular, $a$ commutes with $b^*$ for every $a,b\in\mathcal A$. Since the involution $b\mapsto b^*$ is bijective, every $a$ commutes with every element of $\mathcal A$. Therefore $\mathcal A$ is commutative.

Hence
\[
\boxed{\mathcal A\text{ is commutative }\Longleftrightarrow\text{ every element of }\mathcal A\text{ is normal}.}
\]
:::
