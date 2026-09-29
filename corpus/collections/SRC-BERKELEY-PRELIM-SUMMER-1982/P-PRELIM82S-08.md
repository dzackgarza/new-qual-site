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

::: pf

::: {.pf-step #s1}

For every positive integer $m$,
$$
v_2(m!)
=
\sum_{r\geq1}
\left\lfloor\frac{m}{2^r}\right\rfloor.
$$

::: pf-proof

Each integer in $\{1,\ldots,m\}$ contributes one factor of $2$ for
each $r\geq1$ for which it is divisible by $2^r$. There are exactly
$$
\left\lfloor\frac{m}{2^r}\right\rfloor
$$
multiples of $2^r$ in this set. Summing these contributions over $r$
counts every factor of $2$ in $m!$ exactly once. Only finitely many
terms are nonzero.

:::

:::

::: {.pf-step #s2}

One has
$$
v_2(c_n)
=
\sum_{j=0}^N\varepsilon_j.
$$

::: pf-proof

::: {.pf-step #s2-1}

One has
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

::: pf-proof

Since
$$
c_n=\frac{(2n)!}{(n!)^2},
$$
step [](#s1){.pf-ref} gives
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

:::

::: {.pf-step #s2-2}

For every $j\geq0$,
$$
\left\lfloor\frac{n}{2^j}\right\rfloor
-
2\left\lfloor\frac{n}{2^{j+1}}\right\rfloor
=
\varepsilon_j.
$$

::: pf-proof

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

:::

::: {.pf-step #s2-3}

One has
$$
v_2(c_n)
=
\sum_{j=0}^N\varepsilon_j.
$$

::: pf-proof

In step [](#s2-1){.pf-ref}, set $j=r-1$ and apply step [](#s2-2){.pf-ref} term by term. For
$j>N$, the binary digit $\varepsilon_j$ is zero, so the resulting sum
is exactly
$$
\sum_{j=0}^N\varepsilon_j.
$$

:::

:::

::: pf-qed

Step [](#s2-3){.pf-ref} proves the claim of step [](#s2){.pf-ref}.

:::

:::

:::

::: {.pf-step #s3}

(a) The coefficient $c_n$ is even.

::: pf-proof

Since $n>0$, its binary expansion has at least one digit equal to $1$.
Thus step [](#s2){.pf-ref} gives
$$
v_2(c_n)\geq1,
$$
so $2$ divides $c_n$.

:::

:::

::: {.pf-step #s4}

(b) One has
$$
\boxed{
4\mid c_n
\quad\Longleftrightarrow\quad
n\text{ is not a power of }2
}.
$$

::: pf-proof

By step [](#s2){.pf-ref},
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

:::

::: pf-qed

Step [](#s3){.pf-ref} proves part (a), and step [](#s4){.pf-ref} proves part (b).

:::

:::

:::
