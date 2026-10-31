---
schema: qual/card@1
id: P-SERIES-A2-12
kind: problem
title: Epsilon-delta continuity of $x^n$ and $x^{1/n}$
classification:
  areas:
  - real-analysis
  topics:
  - Continuity
  - Epsilon-Delta Arguments
relations: []
review: draft
---

::: {.problem}
(a) For any $n\in\NN$, show that $p_n(x)=x^n$ is continuous on all of $\RR$. Give the explicit dependence of $\delta$ on $\varepsilon$ and the point of continuity.

(b) Show that $f(x)=\sqrt x$ is continuous on $(0,\infty)$.

(c) Show that $f_n(x)=x^{1/n}$ is continuous on $(0,\infty)$.

Hint: the identity
$$
a^n-b^n=(a-b)(a^{n-1}+a^{n-2}b+\cdots+ab^{n-2}+b^{n-1})
$$
may be useful.
:::

::: {.solution}

## Part (a)

Fix
$$
n\in\NN
$$
and
$$
a\in\RR.
$$
Let
$$
p_n(x)=x^n.
$$

::: pf

::: {.pf-step #s1-1}

The algebraic identity
$$
x^n-a^n
=
(x-a)
\left(
x^{n-1}+x^{n-2}a+\cdots+xa^{n-2}+a^{n-1}
\right)
$$
holds for all real $x,a$.


::: pf-proof

This is the standard factorization of a difference of $n$th powers.

:::

:::

::: {.pf-step #s1-2}

If
$$
\abs{x-a}<1,
$$
then
$$
\boxed{\abs{x}<\abs{a}+1}.
$$


::: pf-proof

By the triangle inequality,
$$
\abs{x}
\le
\abs{x-a}+\abs{a}
<
1+\abs{a}.
$$

:::

:::

::: {.pf-step #s1-3}

Under the same hypothesis,
$$
\abs{
x^{n-1}+x^{n-2}a+\cdots+a^{n-1}
}
\le
n(\abs{a}+1)^{n-1}.
$$


::: pf-proof

There are $n$ terms. Each term has total degree $n-1$ in $x$ and $a$.
By step [](#s1-2){.pf-ref},
$$
\abs{x}<\abs{a}+1,
$$
and trivially
$$
\abs{a}\le\abs{a}+1.
$$
Hence the modulus of each term is at most
$$
(\abs{a}+1)^{n-1}.
$$
Apply the triangle inequality.

:::

:::

::: {.pf-step #s1-4}

Therefore, whenever
$$
\abs{x-a}<1,
$$
one has
$$
\boxed{
\abs{x^n-a^n}
\le
n(\abs{a}+1)^{n-1}\abs{x-a}}.
$$


::: pf-proof

Take absolute values in step [](#s1-1){.pf-ref} and apply step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Given
$$
\varepsilon>0,
$$
define
$$
\boxed{
\delta
=
\min\left\{
1,\,
\frac{\varepsilon}
{n(\abs{a}+1)^{n-1}}
\right\}}.
$$


::: pf-proof

The denominator is positive for every $n\ge1$.

:::

:::

::: {.pf-step #s1-6}

If
$$
\abs{x-a}<\delta,
$$
then
$$
\boxed{
\abs{x^n-a^n}<\varepsilon}.
$$


::: pf-proof

Since
$$
\delta\le1,
$$
step [](#s1-4){.pf-ref} applies. Also,
$$
\abs{x-a}
<
\frac{\varepsilon}
{n(\abs{a}+1)^{n-1}}.
$$
Thus
$$
\abs{x^n-a^n}
\le
n(\abs{a}+1)^{n-1}\abs{x-a}
<
\varepsilon.
$$

:::

:::

::: {.pf-step #s1-7}

Hence
$$
\boxed{
p_n(x)=x^n
\text{ is continuous at every }a\in\RR}.
$$


::: pf-proof

Step [](#s1-6){.pf-ref} is the $\varepsilon$-$\delta$ definition of continuity, with
the explicit $\delta$ from step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

Therefore $p_n$ is continuous on all of $\RR$.


::: pf-proof

The point $a$ in step [](#s1-7){.pf-ref} was arbitrary.

:::

:::

::: {.pf-step #s1-9}

For $x>0$,
$$
\boxed{
\abs{\sqrt x-\sqrt a}
=
\frac{\abs{x-a}}
{\sqrt x+\sqrt a}}.
$$


::: pf-proof

Rationalize:
$$
(\sqrt x-\sqrt a)(\sqrt x+\sqrt a)=x-a.
$$
The denominator is positive.

:::

:::

::: {.pf-step #s1-10}

Since
$$
\sqrt x+\sqrt a\ge\sqrt a,
$$
one has
$$
\boxed{
\abs{\sqrt x-\sqrt a}
\le
\frac{\abs{x-a}}{\sqrt a}}.
$$


::: pf-proof

Apply the lower bound to the denominator in step [](#s1-9){.pf-ref}.

:::

:::

::: {.pf-step #s1-11}

Given $\varepsilon>0$, choose
$$
\boxed{
\delta=\varepsilon\sqrt a}.
$$


::: pf-proof

Since $a>0$, this $\delta$ is positive.

:::

:::

::: {.pf-step #s1-12}

If
$$
x>0
\qquad\text{and}\qquad
\abs{x-a}<\delta,
$$
then
$$
\boxed{
\abs{\sqrt x-\sqrt a}<\varepsilon}.
$$


::: pf-proof

By step [](#s1-10){.pf-ref},
$$
\abs{\sqrt x-\sqrt a}
\le
\frac{\abs{x-a}}{\sqrt a}
<
\frac{\varepsilon\sqrt a}{\sqrt a}
=
\varepsilon.
$$

:::

:::

::: {.pf-step #s1-13}

Hence
$$
\boxed{
\sqrt x
\text{ is continuous on }(0,\infty)}.
$$


::: pf-proof

Step [](#s1-12){.pf-ref} proves continuity at the arbitrary point $a>0$.

:::

:::

::: {.pf-step #s1-14}

The difference-of-powers identity gives
$$
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
$$


::: pf-proof

Since
$$
u^n=x
\qquad\text{and}\qquad
v^n=a,
$$
apply the identity from the problem to $u^n-v^n$.

:::

:::

::: {.pf-step #s1-15}

Every term in the parenthesized sum is nonnegative, and the last term
equals
$$
\boxed{
v^{n-1}=a^{(n-1)/n}}.
$$


::: pf-proof

Because $x,a>0$,
$$
u,v>0.
$$
Thus all monomials are positive. Also
$$
v^{n-1}
=
(a^{1/n})^{n-1}
=
a^{(n-1)/n}.
$$

:::

:::

::: {.pf-step #s1-16}

Therefore
$$
\abs{
u^{n-1}
+
u^{n-2}v
+\cdots+
v^{n-1}
}
\ge
a^{(n-1)/n}.
$$


::: pf-proof

The sum is positive and contains the positive term from step [](#s1-15){.pf-ref}.

:::

:::

::: {.pf-step #s1-17}

Taking absolute values in step [](#s1-14){.pf-ref},
$$
\boxed{
\abs{x^{1/n}-a^{1/n}}
\le
\frac{\abs{x-a}}
{a^{(n-1)/n}}}.
$$


::: pf-proof

The second factor in step [](#s1-14){.pf-ref} is positive and bounded below as in step
[](#s1-16){.pf-ref}. Divide by it.

:::

:::

::: {.pf-step #s1-18}

Given
$$
\varepsilon>0,
$$
choose
$$
\boxed{
\delta
=
\varepsilon
a^{(n-1)/n}}.
$$


::: pf-proof

Since $a>0$, this is positive.

:::

:::

::: {.pf-step #s1-19}

If
$$
x>0
\qquad\text{and}\qquad
\abs{x-a}<\delta,
$$
then
$$
\boxed{
\abs{x^{1/n}-a^{1/n}}<\varepsilon}.
$$


::: pf-proof

Use step [](#s1-17){.pf-ref}:
$$
\abs{x^{1/n}-a^{1/n}}
\le
\frac{\abs{x-a}}
{a^{(n-1)/n}}
<
\frac{
\varepsilon a^{(n-1)/n}
}{
a^{(n-1)/n}
}
=
\varepsilon.
$$

:::

:::

::: {.pf-step #s1-20}

Hence
$$
\boxed{
f_n(x)=x^{1/n}
\text{ is continuous on }(0,\infty)}.
$$


::: pf-proof

Step [](#s1-19){.pf-ref} proves continuity at the arbitrary point $a>0$.

:::

:::

::: pf-qed

Steps [](#s1-5){.pf-ref} through [](#s1-8){.pf-ref} prove part (a) with explicit $\delta$, steps
[](#s1-9){.pf-ref} through [](#s1-13){.pf-ref} prove part (b), and steps [](#s1-14){.pf-ref} through [](#s1-20){.pf-ref} prove part (c).

:::

:::

:::
