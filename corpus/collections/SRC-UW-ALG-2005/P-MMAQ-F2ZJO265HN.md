---
schema: qual/card@1
id: P-MMAQ-F2ZJO265HN
kind: problem
title: Generators of $\FF_{p^6}$ inside $\FF_{p^n}$
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

::: {.problem}
For each prime number $p$ and each positive integer $n$, how many elements $\alpha$ are there in $\FF_{p^n}$ such that $\FF_p(\alpha)=\FF_{p^6}$?
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $6\nmid n$, there are no such elements.

::: pf-proof

Suppose $\alpha\in\FF_{p^n}$ satisfies
$$
\FF_p(\alpha)=\FF_{p^6}.
$$
Then
$$
[\FF_p(\alpha):\FF_p]=6.
$$
Since $\FF_p(\alpha)$ is a subfield of $\FF_{p^n}$, the tower law gives
$$
6\mid n.
$$
Therefore no such $\alpha$ exists when $6\nmid n$.

:::

:::

::: {.pf-step #s2}

Assume $6\mid n$. Then $\FF_{p^6}$ is the unique subfield of $\FF_{p^n}$ having $p^6$ elements.

::: pf-proof

A finite field $\FF_{p^n}$ has a subfield of order $p^d$ exactly when $d\mid n$, and that subfield is unique. Since $6\mid n$, the stated subfield exists and is unique.

:::

:::

::: {.pf-step #s3}

Under the assumption $6\mid n$, the desired elements are exactly the elements of $\FF_{p^6}$ having degree $6$ over $\FF_p$.

::: pf-proof

For $\alpha\in\FF_{p^6}$,
$$
\FF_p(\alpha)=\FF_{p^6}
$$
if and only if
$$
[\FF_p(\alpha):\FF_p]=6.
$$
By step [](#s2){.pf-ref}, every element satisfying the original condition lies in this distinguished copy of $\FF_{p^6}$ inside $\FF_{p^n}$.

:::

:::

::: {.pf-step #s4}

The number of elements of degree exactly $2$ over $\FF_p$ is
$$
p^2-p,
$$
and the number of elements of degree exactly $3$ is
$$
p^3-p.
$$

::: pf-proof

The only proper divisor of $2$ is $1$, so the elements of $\FF_{p^2}$ having degree less than $2$ are exactly the $p$ elements of $\FF_p$. Thus the degree-$2$ count is $p^2-p$.

Likewise, the only proper divisor of $3$ is $1$, so the elements of $\FF_{p^3}$ having degree less than $3$ are exactly the elements of $\FF_p$. Thus the degree-$3$ count is $p^3-p$.

:::

:::

::: {.pf-step #s5}

The number of elements of degree exactly $6$ over $\FF_p$ is
$$
p^6-p^3-p^2+p.
$$

::: pf-proof

For any $\alpha\in\FF_{p^6}$, the degree
$$
d=[\FF_p(\alpha):\FF_p]
$$
divides $6$, so $d\in\{1,2,3,6\}$. These four degree classes are disjoint and exhaust $\FF_{p^6}$. The degree-$1$ class has $p$ elements, while step [](#s4){.pf-ref} gives the degree-$2$ and degree-$3$ counts. Therefore, if $N_6$ denotes the degree-$6$ count,
$$
p^6=p+(p^2-p)+(p^3-p)+N_6.
$$
Solving gives
$$
N_6=p^6-p^3-p^2+p.
$$

:::

:::

::: pf-step

Hence the requested number is
$$
\boxed{\begin{cases}
0,&6\nmid n,\\[2mm]
p^6-p^3-p^2+p,&6\mid n.
\end{cases}}
$$

::: pf-proof

Combine step [](#s1){.pf-ref} with steps [](#s3){.pf-ref} and [](#s5){.pf-ref}.

:::

:::

:::

:::
