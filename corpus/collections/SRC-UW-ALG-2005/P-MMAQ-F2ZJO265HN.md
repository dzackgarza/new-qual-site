---
schema: qual/card@1
id: P-MMAQ-F2ZJO265HN
kind: problem
title: Generators of $\mathbb F_{p^6}$ inside $\mathbb F_{p^n}$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Field Extensions
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-10
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: problem
For each prime number $p$ and each positive integer $n$, how many elements $\alpha$ are there in $\mathbb F_{p^n}$ such that $F_p(\alpha)=F_{p^6}$?
:::

::: solution
<1>1. If $6\nmid n$, there are no such elements.
::: {.proof}
Suppose $\alpha\in\mathbb F_{p^n}$ satisfies
\[
\mathbb F_p(\alpha)=\mathbb F_{p^6}.
\]
Then
\[
[\mathbb F_p(\alpha):\mathbb F_p]=6.
\]
Since $\mathbb F_p(\alpha)$ is a subfield of $\mathbb F_{p^n}$, the tower law gives
\[
6\mid n.
\]
Therefore no such $\alpha$ exists when $6\nmid n$.
:::

<1>2. Assume $6\mid n$. Then $\mathbb F_{p^6}$ is the unique subfield of $\mathbb F_{p^n}$ having $p^6$ elements.
::: {.proof}
A finite field $\mathbb F_{p^n}$ has a subfield of order $p^d$ exactly when $d\mid n$, and that subfield is unique. Since $6\mid n$, the stated subfield exists and is unique.
:::

<1>3. Under the assumption $6\mid n$, the desired elements are exactly the elements of $\mathbb F_{p^6}$ having degree $6$ over $\mathbb F_p$.
::: {.proof}
For $\alpha\in\mathbb F_{p^6}$,
\[
\mathbb F_p(\alpha)=\mathbb F_{p^6}
\]
if and only if
\[
[\mathbb F_p(\alpha):\mathbb F_p]=6.
\]
By <1>2, every element satisfying the original condition lies in this distinguished copy of $\mathbb F_{p^6}$ inside $\mathbb F_{p^n}$.
:::

<1>4. The number of elements of degree exactly $2$ over $\mathbb F_p$ is
\[
p^2-p,
\]
and the number of elements of degree exactly $3$ is
\[
p^3-p.
\]
::: {.proof}
The only proper divisor of $2$ is $1$, so the elements of $\mathbb F_{p^2}$ having degree less than $2$ are exactly the $p$ elements of $\mathbb F_p$. Thus the degree-$2$ count is $p^2-p$.

Likewise, the only proper divisor of $3$ is $1$, so the elements of $\mathbb F_{p^3}$ having degree less than $3$ are exactly the elements of $\mathbb F_p$. Thus the degree-$3$ count is $p^3-p$.
:::

<1>5. The number of elements of degree exactly $6$ over $\mathbb F_p$ is
\[
p^6-p^3-p^2+p.
\]
::: {.proof}
For any $\alpha\in\mathbb F_{p^6}$, the degree
\[
d=[\mathbb F_p(\alpha):\mathbb F_p]
\]
divides $6$, so $d\in\{1,2,3,6\}$. These four degree classes are disjoint and exhaust $\mathbb F_{p^6}$. The degree-$1$ class has $p$ elements, while <1>4 gives the degree-$2$ and degree-$3$ counts. Therefore, if $N_6$ denotes the degree-$6$ count,
\[
p^6=p+(p^2-p)+(p^3-p)+N_6.
\]
Solving gives
\[
N_6=p^6-p^3-p^2+p.
\]
:::

<1>6. Hence the requested number is
\[
\boxed{\begin{cases}
0,&6\nmid n,\\[2mm]
p^6-p^3-p^2+p,&6\mid n.
\end{cases}}
\]
::: {.proof}
Combine <1>1 with <1>3 and <1>5.
:::
:::
