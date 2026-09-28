---
schema: qual/card@1
id: P-CASP26F
kind: problem
title: "Simultaneous polynomial approximation and separation on disjoint compact sets"
classification:
  areas:
  - complex-analysis
  topics:
  - Polynomial Approximation
  - Runge Theorem
  - Mergelyan Theorem
relations: []
review: draft
---

::: {.problem}
Let $A, B \subset \mathbb{C}$ be two disjoint nonempty compact sets.
Consider the following property:

**Property (P):** For any two entire functions $f, g$, there exists a polynomial $p$ such that $|p(z) - f(z)| < \frac{1}{1000}$ for $z \in A$ and $|p(z) - g(z)| > 1000$ for $z \in B$.

(i) Assume $\mathbb{C} \setminus (A \cup B)$ is connected.
Show that property (P) is true.

(ii) Show that property (P) holds for the compact sets $A = \{z \in \mathbb{C} : |z| = 1\}$, $B = \{2\}$.
In this case, $\mathbb{C} \setminus (A \cup B)$ is disconnected.

(iii) Exhibit two disjoint nonempty compact sets $A, B$ for which property (P) is false.
:::

::: {.solution}
(i) Let $f,g$ be entire. Since $A$ and $B$ are disjoint compact sets, define
on $K=A\cup B$ the function
\[
h(z)=
\begin{cases}
f(z),&z\in A,\\
g(z)+2000,&z\in B.
\end{cases}
\]
This is continuous on $K$ and holomorphic on its interior. By hypothesis
$\mathbb C\setminus K$ is connected, so Mergelyan's theorem gives a polynomial
$p$ with
\[
\sup_K|p-h|<\frac1{1000}.
\]
Then on $A$,
\[
|p-f|<\frac1{1000},
\]
while on $B$,
\[
|p-g|
\ge2000-\frac1{1000}>1000.
\]
Thus property (P) holds.

(ii) Now let $A=\{|z|=1\}$ and $B=\{2\}$. Since $f$ is entire, choose a
polynomial $q$ such that
\[
\sup_{|z|=1}|q(z)-f(z)|<\frac1{2000}.
\]
Set
\[
c=2001+g(2)-q(2).
\]
For a sufficiently large integer $m$, the polynomial
\[
p(z)=q(z)+c\left(\frac z2\right)^m
\]
satisfies
\[
\sup_{|z|=1}|p(z)-f(z)|
\le \frac1{2000}+\frac{|c|}{2^m}
<\frac1{1000}.
\]
At $z=2$,
\[
p(2)-g(2)=2001,
\]
so the required separation is $>1000$. Hence property (P) holds even though
the complement of $A\cup B$ is disconnected.

(iii) Take
\[
A=\{|z|=1\},
\qquad
B=\{0\},
\]
and choose $f=g=0$. If property (P) held, there would be a polynomial $p$ with
\[
|p(z)|<\frac1{1000}
\qquad(|z|=1)
\]
and simultaneously
\[
|p(0)|>1000.
\]
The maximum modulus principle on the unit disk makes this impossible. Thus
these compact sets do not satisfy property (P).
:::
