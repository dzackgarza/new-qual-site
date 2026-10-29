---
schema: qual/card@1
id: P-UCLAB17F-11
kind: problem
title: Young inequality
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
  note: Checked against the vendored UCLA Basic Examination, Fall 2017, `assets/attachments/basic-17F.pdf`.
---

::: {.problem}
Let $p,q\in(1,\infty)$ satisfy $1/p+1/q=1$. Prove that for all $a,b\ge0$,
$$
ab\le \frac{a^p}{p}+\frac{b^q}{q}.
$$
:::

::: {.solution}

Fix
$$
b\ge0
$$
and define
$$
\phi(a)
=
\frac{a^p}{p}
-ab
+
\frac{b^q}{q},
\qquad
a\ge0.
$$

::: pf

::: {.pf-step #s1-1}

If $b=0$, then
$$
\phi(a)\ge0
$$
for every $a\ge0$.


::: pf-proof

When $b=0$,
$$
\phi(a)
=
\frac{a^p}{p}
\ge0.
$$

:::

:::

::: {.pf-step #s1-2}

Assume $b>0$.
Then
$$
\phi'(a)
=
a^{p-1}-b.
$$


::: pf-proof

Differentiate:
$$
\frac d{da}\frac{a^p}{p}
=
a^{p-1},
$$
$$
\frac d{da}(-ab)
=
-b,
$$
and the last term is constant in $a$.

:::

:::

::: {.pf-step #s1-3}

The derivative $\phi'$ vanishes at exactly one point,
$$
a_0=b^{1/(p-1)}.
$$


::: pf-proof

The equation
$$
\phi'(a)=0
$$
is
$$
a^{p-1}=b.
$$
Since $p-1>0$, the function
$$
a\mapsto a^{p-1}
$$
is strictly increasing on $[0,\infty)$.
Hence the unique solution is
$$
a_0=b^{1/(p-1)}.
$$

:::

:::

::: {.pf-step #s1-4}

The point $a_0$ is the global minimum of $\phi$ on $[0,\infty)$.


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
\phi'(a)<0
$$
for
$$
0\le a<a_0,
$$
and
$$
\phi'(a)>0
$$
for
$$
a>a_0.
$$
Thus $\phi$ decreases up to $a_0$ and increases afterward.
Therefore $a_0$ is the unique global minimum.

:::

:::

::: {.pf-step #s1-5}

The conjugacy relation
$$
\frac1p+\frac1q=1
$$
implies
$$
q=\frac p{p-1}
\qquad\text{and}\qquad
q-1=\frac1{p-1}.
$$


::: pf-proof

From
$$
\frac1q
=
1-\frac1p
=
\frac{p-1}{p},
$$
one obtains
$$
q=\frac p{p-1}.
$$
Subtracting $1$ gives
$$
q-1
=
\frac1{p-1}.
$$

:::

:::

::: {.pf-step #s1-6}

At the minimizing point,
$$
a_0=b^{q-1},
$$
$$
a_0^p=b^q,
$$
and
$$
a_0b=b^q.
$$


::: pf-proof

The first identity follows from steps [](#s1-3){.pf-ref} and [](#s1-5){.pf-ref}.
Then
$$
a_0^p
=
b^{p(q-1)}
=
b^q
$$
because
$$
p(q-1)=q.
$$
Also
$$
a_0b
=
b^{q-1}b
=
b^q.
$$

:::

:::

::: {.pf-step #s1-7}

One has
$$
\phi(a_0)=0.
$$


::: pf-proof

Using step [](#s1-6){.pf-ref},
$$
\begin{aligned}
\phi(a_0)
&=
\frac{b^q}{p}
-
b^q
+
\frac{b^q}{q}\\
&=
b^q
\left(
\frac1p+\frac1q-1
\right)\\
&=
0.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-8}

Therefore
$$
\phi(a)\ge0
$$
for all
$$
a,b\ge0.
$$


::: pf-proof

If $b=0$, use step [](#s1-1){.pf-ref}.
If $b>0$, step [](#s1-4){.pf-ref} says that $\phi$ is minimized at $a_0$, and step [](#s1-7){.pf-ref} gives the minimum value $0$.

:::

:::

::: {.pf-step #s1-9}

Rearranging step [](#s1-8){.pf-ref} gives Young's inequality:
$$
\boxed{
ab
\le
\frac{a^p}{p}
+
\frac{b^q}{q}
}.
$$


::: pf-proof

The inequality
$$
\phi(a)\ge0
$$
is exactly
$$
\frac{a^p}{p}
-ab
+
\frac{b^q}{q}
\ge0.
$$
Move the term $ab$ to the other side.

:::

:::

::: pf-qed

Step [](#s1-9){.pf-ref} is the required inequality.

:::

:::

:::
