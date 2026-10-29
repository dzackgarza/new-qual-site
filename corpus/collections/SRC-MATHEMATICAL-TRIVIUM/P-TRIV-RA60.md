---
schema: qual/card@1
id: P-TRIV-RA60
kind: problem
title: Integrable smooth function with a single nonzero derivative at $0$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 60, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Give an example of the $C ^ { \infty } ( \RR )$ function f (x) with the following properties:

$$
\begin{array} { r l } & { \mathrm { 1 ) } \quad f ^ { ( n ) } ( 0 ) = 1 \mathrm { f o r ~ s o m e } n \geqslant 0 , } \\ & { \mathrm { 2 ) } \quad f ^ { ( i ) } ( 0 ) = 0 , i \geqslant 0 , i \neq n , } \\ & { \mathrm { 3 ) } \quad \displaystyle \int _ { 0 } ^ { \infty } | f ( x ) | d x < \infty . } \end{array}\tag{13}
$$
:::

::: {.solution}

Fix any integer
$$
n\geq0.
$$

::: pf

::: {.pf-step #s1-1}

Choose a smooth cutoff function
$$
\chi\in C_c^\infty(\RR)
$$
such that
$$
\chi(x)=1
$$
for
$$
|x|\leq1.
$$


::: pf-proof

Such cutoff functions exist. For example, start from a standard smooth bump
supported in $(-2,2)$ and equal to $1$ on $[-1,1]$.

:::

:::

::: {.pf-step #s1-2}

Define
$$
\boxed{
f(x)=\frac{x^n}{n!}\chi(x).
}
$$


::: pf-proof

This is a product of smooth functions, so
$$
f\in C^\infty(\RR).
$$
Because $\chi$ has compact support, so does $f$.

:::

:::

::: {.pf-step #s1-3}

On the interval
$$
|x|\leq1,
$$
one has
$$
f(x)=\frac{x^n}{n!}.
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, $\chi(x)=1$ on this interval. Substitute into step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{f^{(n)}(0)=1}.
$$


::: pf-proof

By step [](#s1-3){.pf-ref}, $f$ agrees with $x^n/n!$ on a neighborhood of $0$. The $n$th
derivative of this polynomial is identically $1$.

:::

:::

::: {.pf-step #s1-5}

For every integer
$$
i\geq0,
\qquad
i\neq n,
$$
one has
$$
\boxed{f^{(i)}(0)=0}.
$$


::: pf-proof

Again use step [](#s1-3){.pf-ref}. If $i<n$, then the $i$th derivative of $x^n/n!$ still
contains the factor $x^{n-i}$ and vanishes at $0$. If $i>n$, the $i$th
derivative of the degree-$n$ polynomial is identically zero.

:::

:::

::: {.pf-step #s1-6}

The function is absolutely integrable on $[0,\infty)$:
$$
\boxed{
\int_0^\infty |f(x)|\,dx<\infty.
}
$$


::: pf-proof

By step [](#s1-2){.pf-ref}, $f$ has compact support. A continuous compactly supported
function is bounded and vanishes outside a finite interval, hence has finite
absolute integral.

:::

:::

::: {.pf-step #s1-7}

Thus the function in step [](#s1-2){.pf-ref} satisfies all three required properties.


::: pf-proof

Step [](#s1-4){.pf-ref} gives property (1), step [](#s1-5){.pf-ref} gives property (2), and step [](#s1-6){.pf-ref}
gives property (3).

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} verifies the construction.

:::

:::

:::
