---
schema: qual/card@1
id: P-APA24E
kind: problem
title: A unital $*$-algebra is commutative iff every element is normal
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-09
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
Let $\mathcal{A}$ be a unital associative algebra over $\mathbb{C}$ equipped with an antilinear and antimultiplicative involution $A \mapsto A^*$.
We say that $A \in \mathcal{A}$ is normal if $A$ and $A^*$ commute (example: normal matrices are normal elements of $\mathbb{C}^{N \times N}$). Prove that $\mathcal{A}$ is a commutative algebra if and only if all its elements are normal.
:::

::: {.solution}
<1>1. If $\mathcal A$ is commutative, then every element of $\mathcal A$ is normal.
::: {.proof}
For $x\in\mathcal A$, commutativity gives $xx^*=x^*x$.
:::

<1>2. Conversely, suppose every element of $\mathcal A$ is normal.
Fix $x,y\in\mathcal A$ and write $[a,b]=ab-ba$.
Normality of $x+y$ implies
\[
[x,y^*]+[y,x^*]=0.
\]
::: {.proof}
Since $x$ and $y$ are individually normal,
\[
0=[x+y,(x+y)^*]
 =[x+y,x^*+y^*]
 =[x,y^*]+[y,x^*].
\]
:::

<1>3. Normality of $x+iy$ implies
\[
-i[x,y^*]+i[y,x^*]=0.
\]
::: {.proof}
Antilinearity of the involution gives $(x+iy)^*=x^*-iy^*$.
Hence, using again the normality of $x$ and $y$,
\[
0=[x+iy,x^*-iy^*]
 =-i[x,y^*]+i[y,x^*].
\]
:::

<1>4. Therefore $[x,y^*]=0$ for all $x,y\in\mathcal A$.
::: {.proof}
Let $A=[x,y^*]$ and $B=[y,x^*]$.
By <1>2, $A+B=0$, while by <1>3, $-A+B=0$.
Adding and subtracting gives $A=B=0$.
:::

<1>5. The algebra $\mathcal A$ is commutative.
::: {.proof}
The involution is bijective because $(z^*)^*=z$.
Thus every $z\in\mathcal A$ has the form $z=y^*$ for some $y\in\mathcal A$.
By <1>4, $[x,z]=[x,y^*]=0$ for every $x,z\in\mathcal A$.
Hence all elements commute.
:::
:::
