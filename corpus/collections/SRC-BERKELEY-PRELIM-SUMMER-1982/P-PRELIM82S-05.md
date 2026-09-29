---
schema: qual/card@1
id: P-PRELIM82S-05
kind: problem
title: Monotone positive coefficients exclude polynomial roots from the unit disk
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
    Multiplying the polynomial by z-1 expresses a_n as a sum whose
    coefficients are a_0 and the nonnegative successive differences
    a_j-a_{j-1}. At a hypothetical root with r=|z|<1, the triangle
    inequality bounds a_n by r times the telescoping sum a_n, a
    contradiction.
---

::: {.problem}
Let
\[
0<a_0\le a_1\le\cdots\le a_n.
\]
Prove that
\[
a_0z^n+a_1z^{n-1}+\cdots+a_n=0
\]
has no roots in the disk $|z|<1$.
:::

::: {.solution}
Put
$$
P(w)=a_0w^n+a_1w^{n-1}+\cdots+a_n.
$$

::: pf

::: {.pf-step #s1}

If $P(z)=0$ and $\abs{z}<1$, then
$$
0<\abs{z}<1.
$$

::: pf-proof

Since $a_n>0$,
$$
P(0)=a_n\neq0.
$$
Thus a root $z$ cannot equal zero.

:::

:::

::: {.pf-step #s2}

If $P(z)=0$, then
$$
a_n
=
a_0z^{n+1}
+
\sum_{j=1}^n
(a_j-a_{j-1})z^{n-j+1}.
$$

::: pf-proof

Direct expansion gives
$$
\begin{aligned}
(z-1)P(z)
&=
a_0z^{n+1}
+
(a_1-a_0)z^n
+
\cdots\\
&\qquad
+
(a_n-a_{n-1})z
-
a_n.
\end{aligned}
$$
If $P(z)=0$, the left-hand side is zero. Rearranging gives the claimed
identity.

:::

:::

::: {.pf-step #s3}

A root $z$ with $\abs{z}<1$ would satisfy
$$
a_n<a_n,
$$
which is impossible.

::: pf-proof

Let
$$
r=\abs{z}.
$$
By step [](#s1){.pf-ref}, $0<r<1$. Since
$$
a_j-a_{j-1}\geq0
$$
for $1\leq j\leq n$, step [](#s2){.pf-ref} and the triangle inequality give
$$
\begin{aligned}
a_n
&\leq
a_0r^{n+1}
+
\sum_{j=1}^n
(a_j-a_{j-1})r^{n-j+1}\\
&\leq
r
\left(
a_0
+
\sum_{j=1}^n(a_j-a_{j-1})
\right)\\
&=
ra_n\\
&<
a_n.
\end{aligned}
$$
The penultimate equality is the telescoping identity
$$
a_0+\sum_{j=1}^n(a_j-a_{j-1})=a_n,
$$
and the last inequality uses $a_n>0$ and $r<1$.

:::

:::

::: {.pf-step #s4}

Therefore
$$
\boxed{P(z)\neq0\quad\text{whenever }\abs{z}<1}.
$$

::: pf-proof

If such a root existed, step [](#s3){.pf-ref} would give a contradiction.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the required conclusion.

:::

:::

:::
