---
schema: qual/card@1
id: P-SERIES-A2-12
kind: problem
title: Epsilon-delta continuity of $x^n$ and $x^{1/n}$
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
(a) For any $n\in\mathbb N$, show that $p_n(x)=x^n$ is continuous on all of $\mathbb R$. Give the explicit dependence of $\delta$ on $\varepsilon$ and the point of continuity.

(b) Show that $f(x)=\sqrt x$ is continuous on $(0,\infty)$.

(c) Show that $f_n(x)=x^{1/n}$ is continuous on $(0,\infty)$.

Hint: the identity
\[
a^n-b^n=(a-b)(a^{n-1}+a^{n-2}b+\cdots+ab^{n-2}+b^{n-1})
\]
may be useful.
:::

## Part (a)

Fix
\[
n\in\mathbb N
\]
and
\[
a\in\mathbb R.
\]
Let
\[
p_n(x)=x^n.
\]

::: pf

::: pf-step

The algebraic identity
\[
x^n-a^n
=
(x-a)
\left(
x^{n-1}+x^{n-2}a+\cdots+xa^{n-2}+a^{n-1}
\right)
\]
holds for all real \(x,a\).


::: pf-proof

This is the standard factorization of a difference of \(n\)th powers.

:::

:::

::: pf-step

If
\[
|x-a|<1,
\]
then
\[
\boxed{|x|<|a|+1}.
\]


::: pf-proof

By the triangle inequality,
\[
|x|
\le
|x-a|+|a|
<
1+|a|.
\]

:::

:::

::: pf-step

Under the same hypothesis,
\[
\left|
x^{n-1}+x^{n-2}a+\cdots+a^{n-1}
\right|
\le
n(|a|+1)^{n-1}.
\]


::: pf-proof

There are \(n\) terms. Each term has total degree \(n-1\) in \(x\) and \(a\).
By step <1>2,
\[
|x|<|a|+1,
\]
and trivially
\[
|a|\le|a|+1.
\]
Hence the modulus of each term is at most
\[
(|a|+1)^{n-1}.
\]
Apply the triangle inequality.

:::

:::

::: pf-step

Therefore, whenever
\[
|x-a|<1,
\]
one has
\[
\boxed{
|x^n-a^n|
\le
n(|a|+1)^{n-1}|x-a|}.
\]


::: pf-proof

Take absolute values in step <1>1 and apply step <1>3.

:::

:::

::: pf-step

Given
\[
\varepsilon>0,
\]
define
\[
\boxed{
\delta
=
\min\left\{
1,\,
\frac{\varepsilon}
{n(|a|+1)^{n-1}}
\right\}}.
\]


::: pf-proof

The denominator is positive for every \(n\ge1\).

:::

:::

::: pf-step

If
\[
|x-a|<\delta,
\]
then
\[
\boxed{
|x^n-a^n|<\varepsilon}.
\]


::: pf-proof

Since
\[
\delta\le1,
\]
step <1>4 applies. Also,
\[
|x-a|
<
\frac{\varepsilon}
{n(|a|+1)^{n-1}}.
\]
Thus
\[
|x^n-a^n|
\le
n(|a|+1)^{n-1}|x-a|
<
\varepsilon.
\]

:::

:::

::: pf-step

Hence
\[
\boxed{
p_n(x)=x^n
\text{ is continuous at every }a\in\mathbb R}.
\]


::: pf-proof

Step <1>6 is the \(\varepsilon\)-\(\delta\) definition of continuity, with
the explicit \(\delta\) from step <1>5.

:::

:::

::: pf-step

Therefore \(p_n\) is continuous on all of \(\mathbb R\).


::: pf-proof

The point \(a\) in step <1>7 was arbitrary.

:::

:::

::: pf-step

For \(x>0\),
\[
\boxed{
|\sqrt x-\sqrt a|
=
\frac{|x-a|}
{\sqrt x+\sqrt a}}.
\]


::: pf-proof

Rationalize:
\[
(\sqrt x-\sqrt a)(\sqrt x+\sqrt a)=x-a.
\]
The denominator is positive.

:::

:::

::: pf-step

Since
\[
\sqrt x+\sqrt a\ge\sqrt a,
\]
one has
\[
\boxed{
|\sqrt x-\sqrt a|
\le
\frac{|x-a|}{\sqrt a}}.
\]


::: pf-proof

Apply the lower bound to the denominator in step <1>9.

:::

:::

::: pf-step

Given \(\varepsilon>0\), choose
\[
\boxed{
\delta=\varepsilon\sqrt a}.
\]


::: pf-proof

Since \(a>0\), this \(\delta\) is positive.

:::

:::

::: pf-step

If
\[
x>0
\qquad\text{and}\qquad
|x-a|<\delta,
\]
then
\[
\boxed{
|\sqrt x-\sqrt a|<\varepsilon}.
\]


::: pf-proof

By step <1>10,
\[
|\sqrt x-\sqrt a|
\le
\frac{|x-a|}{\sqrt a}
<
\frac{\varepsilon\sqrt a}{\sqrt a}
=
\varepsilon.
\]

:::

:::

::: pf-step

Hence
\[
\boxed{
\sqrt x
\text{ is continuous on }(0,\infty)}.
\]


::: pf-proof

Step <1>12 proves continuity at the arbitrary point \(a>0\).

:::

:::

::: pf-step

The difference-of-powers identity gives
\[
x-a
=
(u-v)
\left(
u^{n-1}
+
u^{n-2}v
+\cdots+
uv^{n-2}
+
v^{n-1}
\right).
\]


::: pf-proof

Since
\[
u^n=x
\qquad\text{and}\qquad
v^n=a,
\]
apply the identity from the problem to \(u^n-v^n\).

:::

:::

::: pf-step

Every term in the parenthesized sum is nonnegative, and the last term
equals
\[
\boxed{
v^{n-1}=a^{(n-1)/n}}.
\]


::: pf-proof

Because \(x,a>0\),
\[
u,v>0.
\]
Thus all monomials are positive. Also
\[
v^{n-1}
=
(a^{1/n})^{n-1}
=
a^{(n-1)/n}.
\]

:::

:::

::: pf-step

Therefore
\[
\left|
u^{n-1}
+
u^{n-2}v
+\cdots+
v^{n-1}
\right|
\ge
a^{(n-1)/n}.
\]


::: pf-proof

The sum is positive and contains the positive term from step <1>15.

:::

:::

::: pf-step

Taking absolute values in step <1>14,
\[
\boxed{
|x^{1/n}-a^{1/n}|
\le
\frac{|x-a|}
{a^{(n-1)/n}}}.
\]


::: pf-proof

The second factor in step <1>14 is positive and bounded below as in step
<1>16. Divide by it.

:::

:::

::: pf-step

Given
\[
\varepsilon>0,
\]
choose
\[
\boxed{
\delta
=
\varepsilon
a^{(n-1)/n}}.
\]


::: pf-proof

Since \(a>0\), this is positive.

:::

:::

::: pf-step

If
\[
x>0
\qquad\text{and}\qquad
|x-a|<\delta,
\]
then
\[
\boxed{
|x^{1/n}-a^{1/n}|<\varepsilon}.
\]


::: pf-proof

Use step <1>17:
\[
|x^{1/n}-a^{1/n}|
\le
\frac{|x-a|}
{a^{(n-1)/n}}
<
\frac{
\varepsilon a^{(n-1)/n}
}{
a^{(n-1)/n}
}
=
\varepsilon.
\]

:::

:::

::: pf-step

Hence
\[
\boxed{
f_n(x)=x^{1/n}
\text{ is continuous on }(0,\infty)}.
\]


::: pf-proof

Step <1>19 proves continuity at the arbitrary point \(a>0\).

:::

:::

::: pf-qed

Steps <1>5--<1>8 prove part (a) with explicit \(\delta\), steps
<1>9--<1>13 prove part (b), and steps <1>14--<1>20 prove part (c).

:::

:::
