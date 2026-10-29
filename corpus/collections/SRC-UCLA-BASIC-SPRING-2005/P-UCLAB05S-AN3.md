---
schema: qual/card@1
id: P-UCLAB05S-AN3
kind: problem
title: Proper maps and a derivative criterion on the real line
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Analysis Problem 3 of the official UCLA Basic Exam, May 2005 PDF.
---

::: {.problem}
Let $X,Y$ be topological spaces.
A continuous function $f:X\to Y$ is called *proper* if $f^{-1}(K)$ is compact for every compact set $K\subset Y$.

(a) Give an example of a function that is proper but not a homeomorphism.

(b) Give an example of a function that is continuous but not proper.

(c) Suppose $f:\RR\to\RR$ is $C^1$ and
$$
|f'(x)|\geq1
\qquad\text{for every }x\in\RR.
$$
Show that $f$ is proper.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For part (a), the map
$$
\boxed{f:\RR\to\RR,\qquad f(x)=x^2}
$$
is proper but is not a homeomorphism.


::: pf-proof

The map is not injective because $f(x)=f(-x)$. Let $K\subseteq\RR$ be compact. Then $K$ is closed and bounded, so $K\subseteq[-M,M]$ for some $M\ge0$. The inverse image $f^{-1}(K)$ is closed by continuity of $f$, and if $x\in f^{-1}(K)$ then $x^2\le M$, hence $|x|\le\sqrt M$. Thus $f^{-1}(K)$ is closed and bounded in $\RR$, hence compact by the Heine--Borel theorem.

:::

:::

::: {.pf-step #s1-2}

For part (b), the constant map
$$
\boxed{g:\RR\to\RR,\qquad g(x)=0}
$$
is continuous but not proper.


::: pf-proof

The singleton $\{0\}$ is compact, but
$$
g^{-1}(\{0\})=\RR,
$$
which is not compact.

:::

:::

::: pf-step

Under the hypotheses of part (c), either
$$
f'(x)\ge1\quad\text{for every }x\in\RR
$$
or
$$
f'(x)\le-1\quad\text{for every }x\in\RR.
$$


::: pf-proof

Since $f$ is $C^1$, the derivative $f'$ is continuous. The inequality $|f'(x)|\ge1$ implies that $f'$ never vanishes. If $f'$ took both a positive and a negative value, the intermediate value theorem would force it to vanish somewhere. Hence $f'$ has constant sign. Combining this with $|f'|\ge1$ gives the stated alternatives.

:::

:::

::: {.pf-step #s1-4}

For every $x\in\RR$,
$$
|f(x)-f(0)|\ge|x|.
$$


::: pf-proof

Suppose first that $f'\ge1$ everywhere. If $x>0$, the mean value theorem gives
$$
f(x)-f(0)=f'(c)x\ge x
$$
for some $c\in(0,x)$. If $x<0$, applying the mean value theorem on $[x,0]$ gives
$$
f(0)-f(x)=f'(c)(-x)\ge -x.
$$
Thus the desired inequality holds. The case $f'\le-1$ is identical after replacing $f$ by $-f$.

:::

:::

::: {.pf-step #s1-5}

The function $f$ is proper.


::: pf-proof

Let $K\subseteq\RR$ be compact. Choose $M\ge0$ such that $K\subseteq[-M,M]$. If $x\in f^{-1}(K)$, then $|f(x)|\le M$. By step [](#s1-4){.pf-ref},
$$
|x|\le|f(x)-f(0)|\le |f(x)|+|f(0)|\le M+|f(0)|.
$$
Hence $f^{-1}(K)$ is bounded. It is also closed because $K$ is closed and $f$ is continuous. By Heine--Borel, $f^{-1}(K)$ is compact. Therefore $f$ is proper.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} give the requested examples, and step [](#s1-5){.pf-ref} proves part (c).

:::

:::

:::
