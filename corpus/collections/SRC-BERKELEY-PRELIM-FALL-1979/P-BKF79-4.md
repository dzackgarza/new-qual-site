---
schema: qual/card@1
id: P-BKF79-4
kind: problem
title: Reduce polynomials modulo the ideal $(7,x-3)$ in $\mathbb Z[x]$
classification: {areas: [prelim], topics: []}
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
    For every r, the factor theorem gives r-r(3) in (x-3). Choosing
    the representative alpha of r(3) modulo 7 in {0,...,6} then gives
    r-alpha in (7,x-3). In the stated example r(3) is congruent to 6
    modulo 7.
---

::: {.problem}
Let $I=(7,x-3)$ in $\mathbb Z[x]$.

1. Prove that for every $r\in\mathbb Z[x]$ there is an integer $\alpha$ with $0\le\alpha\le6$ such that
\[
r-\alpha\in I.
\]
2. Find $\alpha$ for
\[
r=x^{250}+15x^{14}+x^2+5.
\]
:::

::: {.solution}
<1>1. For every $r\in\ZZ[x]$,
$$
r(x)-r(3)\in(x-3).
$$

::: {.proof}
By the factor theorem, the polynomial $r(x)-r(3)$ vanishes at $x=3$,
so it is divisible by $x-3$ in $\ZZ[x]$.
:::

<1>2. For every $r\in\ZZ[x]$, there is a unique integer
$\alpha$ with $0\leq\alpha\leq6$ such that
$$
r(3)-\alpha\in(7).
$$

::: {.proof}
The integers $0,1,\ldots,6$ form a complete set of representatives
for the residue classes modulo $7$. Choose $\alpha$ to represent the
class of the integer $r(3)$.
:::

<1>3. The integer $\alpha$ from step <1>2 satisfies
$$
r-\alpha\in I.
$$

::: {.proof}
We can write
$$
r-\alpha
=
\bigl(r-r(3)\bigr)
+
\bigl(r(3)-\alpha\bigr).
$$
By step <1>1, the first summand lies in $(x-3)$, and by step <1>2 the
second lies in $(7)$. Hence their sum lies in
$$
(7,x-3)=I.
$$
This proves part 1.
:::

<1>4. For
$$
r=x^{250}+15x^{14}+x^2+5,
$$
one has
$$
r(3)\equiv6\pmod7.
$$

::: {.proof}
Since
$$
3^6\equiv1\pmod7,
$$
we have
$$
3^{250}\equiv3^4\equiv4\pmod7
$$
and
$$
3^{14}\equiv3^2\equiv2\pmod7.
$$
Also $15\equiv1\pmod7$. Therefore
$$
\begin{aligned}
r(3)
&=
3^{250}+15\cdot3^{14}+3^2+5\\
&\equiv
4+2+2+5\\
&\equiv
6
\pmod7.
\end{aligned}
$$
:::

<1>5. For the polynomial in part 2,
$$
\boxed{\alpha=6}.
$$

::: {.proof}
Step <1>4 shows that the unique representative of $r(3)$ modulo $7$
in the range $0\leq\alpha\leq6$ is $6$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>3 proves part 1, and step <1>5 proves part 2.
:::
:::
