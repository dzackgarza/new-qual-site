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
\[
ab\le \frac{a^p}{p}+\frac{b^q}{q}.
\]
:::

::: {.solution}
Fix
\[
b\ge0
\]
and define
\[
\phi(a)
=
\frac{a^p}{p}
-ab
+
\frac{b^q}{q},
\qquad
a\ge0.
\]

<1>1. If $b=0$, then
\[
\phi(a)\ge0
\]
for every $a\ge0$.

::: {.proof}
When $b=0$,
\[
\phi(a)
=
\frac{a^p}{p}
\ge0.
\]
:::

<1>2. Assume $b>0$.
Then
\[
\phi'(a)
=
a^{p-1}-b.
\]

::: {.proof}
Differentiate:
\[
\frac d{da}\frac{a^p}{p}
=
a^{p-1},
\]
\[
\frac d{da}(-ab)
=
-b,
\]
and the last term is constant in $a$.
:::

<1>3. The derivative $\phi'$ vanishes at exactly one point,
\[
a_0=b^{1/(p-1)}.
\]

::: {.proof}
The equation
\[
\phi'(a)=0
\]
is
\[
a^{p-1}=b.
\]
Since $p-1>0$, the function
\[
a\mapsto a^{p-1}
\]
is strictly increasing on $[0,\infty)$.
Hence the unique solution is
\[
a_0=b^{1/(p-1)}.
\]
:::

<1>4. The point $a_0$ is the global minimum of $\phi$ on $[0,\infty)$.

::: {.proof}
By step <1>2,
\[
\phi'(a)<0
\]
for
\[
0\le a<a_0,
\]
and
\[
\phi'(a)>0
\]
for
\[
a>a_0.
\]
Thus $\phi$ decreases up to $a_0$ and increases afterward.
Therefore $a_0$ is the unique global minimum.
:::

<1>5. The conjugacy relation
\[
\frac1p+\frac1q=1
\]
implies
\[
q=\frac p{p-1}
\qquad\text{and}\qquad
q-1=\frac1{p-1}.
\]

::: {.proof}
From
\[
\frac1q
=
1-\frac1p
=
\frac{p-1}{p},
\]
one obtains
\[
q=\frac p{p-1}.
\]
Subtracting $1$ gives
\[
q-1
=
\frac1{p-1}.
\]
:::

<1>6. At the minimizing point,
\[
a_0=b^{q-1},
\]
\[
a_0^p=b^q,
\]
and
\[
a_0b=b^q.
\]

::: {.proof}
The first identity follows from steps <1>3 and <1>5.
Then
\[
a_0^p
=
b^{p(q-1)}
=
b^q
\]
because
\[
p(q-1)=q.
\]
Also
\[
a_0b
=
b^{q-1}b
=
b^q.
\]
:::

<1>7. One has
\[
\phi(a_0)=0.
\]

::: {.proof}
Using step <1>6,
\[
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
\]
:::

<1>8. Therefore
\[
\phi(a)\ge0
\]
for all
\[
a,b\ge0.
\]

::: {.proof}
If $b=0$, use step <1>1.
If $b>0$, step <1>4 says that $\phi$ is minimized at $a_0$, and step <1>7 gives the minimum value $0$.
:::

<1>9. Rearranging step <1>8 gives Young's inequality:
\[
\boxed{
ab
\le
\frac{a^p}{p}
+
\frac{b^q}{q}
}.
\]

::: {.proof}
The inequality
\[
\phi(a)\ge0
\]
is exactly
\[
\frac{a^p}{p}
-ab
+
\frac{b^q}{q}
\ge0.
\]
Move the term $ab$ to the other side.
:::

<1>10. Q.E.D.

::: {.proof}
Step <1>9 is the required inequality.
:::
:::
