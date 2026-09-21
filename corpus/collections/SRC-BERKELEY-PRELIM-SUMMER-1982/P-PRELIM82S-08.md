---
schema: qual/card@1
id: P-PRELIM82S-08
kind: problem
title: Divisibility of the central binomial coefficient by two and four
classification:
  areas:
  - prelim
  topics: []
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
    Counting factors of 2 in factorials gives
    v_2((2n choose n)) equal to the sum of the binary digits of n.
    Since n>0 this sum is at least one, proving evenness; it equals one
    exactly when n is a power of 2, giving the divisibility-by-4
    criterion.
---

::: {.problem}
Let $n$ be a positive integer and set
\[
c_n=\binom{2n}{n}.
\]

(a) Show that $c_n$ is even.

(b) Prove that $c_n$ is divisible by $4$ if and only if $n$ is not a power of $2$.
:::

::: {.solution}
For a positive integer $m$, let $v_2(m)$ denote the largest integer $r$
such that $2^r$ divides $m$. Write the binary expansion of $n$ as
$$
n=\sum_{j=0}^N\varepsilon_j2^j,
\qquad
\varepsilon_j\in\{0,1\},
\qquad
\varepsilon_N=1.
$$

<1>1. For every positive integer $m$,
$$
v_2(m!)
=
\sum_{r\geq1}
\left\lfloor\frac{m}{2^r}\right\rfloor.
$$

::: {.proof}
Each integer in $\{1,\ldots,m\}$ contributes one factor of $2$ for
each $r\geq1$ for which it is divisible by $2^r$. There are exactly
$$
\left\lfloor\frac{m}{2^r}\right\rfloor
$$
multiples of $2^r$ in this set. Summing these contributions over $r$
counts every factor of $2$ in $m!$ exactly once. Only finitely many
terms are nonzero.
:::

<1>2. One has
$$
v_2(c_n)
=
\sum_{j=0}^N\varepsilon_j.
$$

<2>1. One has
$$
v_2(c_n)
=
\sum_{r\geq1}
\left(
\left\lfloor\frac{n}{2^{r-1}}\right\rfloor
-
2\left\lfloor\frac{n}{2^r}\right\rfloor
\right).
$$

::: {.proof}
Since
$$
c_n=\frac{(2n)!}{(n!)^2},
$$
step <1>1 gives
$$
\begin{aligned}
v_2(c_n)
&=
\sum_{r\geq1}
\left(
\left\lfloor\frac{2n}{2^r}\right\rfloor
-
2\left\lfloor\frac{n}{2^r}\right\rfloor
\right)\\
&=
\sum_{r\geq1}
\left(
\left\lfloor\frac{n}{2^{r-1}}\right\rfloor
-
2\left\lfloor\frac{n}{2^r}\right\rfloor
\right).
\end{aligned}
$$
:::

<2>2. For every $j\geq0$,
$$
\left\lfloor\frac{n}{2^j}\right\rfloor
-
2\left\lfloor\frac{n}{2^{j+1}}\right\rfloor
=
\varepsilon_j.
$$

::: {.proof}
From the binary expansion,
$$
\left\lfloor\frac{n}{2^j}\right\rfloor
=
\varepsilon_j
+
2\sum_{k=j+1}^N\varepsilon_k2^{k-j-1},
$$
whereas
$$
\left\lfloor\frac{n}{2^{j+1}}\right\rfloor
=
\sum_{k=j+1}^N\varepsilon_k2^{k-j-1}.
$$
Subtracting twice the second equality from the first gives the claim.
:::

<2>3. One has
$$
v_2(c_n)
=
\sum_{j=0}^N\varepsilon_j.
$$

::: {.proof}
In step <2>1, set $j=r-1$ and apply step <2>2 term by term. For
$j>N$, the binary digit $\varepsilon_j$ is zero, so the resulting sum
is exactly
$$
\sum_{j=0}^N\varepsilon_j.
$$
:::

<2>4. Q.E.D.

::: {.proof}
Step <2>3 proves the claim of step <1>2.
:::

<1>3. (a) The coefficient $c_n$ is even.

::: {.proof}
Since $n>0$, its binary expansion has at least one digit equal to $1$.
Thus step <1>2 gives
$$
v_2(c_n)\geq1,
$$
so $2$ divides $c_n$.
:::

<1>4. (b) One has
$$
\boxed{
4\mid c_n
\quad\Longleftrightarrow\quad
n\text{ is not a power of }2
}.
$$

::: {.proof}
By step <1>2,
$$
4\mid c_n
\quad\Longleftrightarrow\quad
v_2(c_n)\geq2
\quad\Longleftrightarrow\quad
\sum_{j=0}^N\varepsilon_j\geq2.
$$
A positive integer has exactly one nonzero binary digit if and only if it
is a power of $2$. Hence the binary digit sum is at least two exactly
when $n$ is not a power of $2$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>3 proves part (a), and step <1>4 proves part (b).
:::
:::
