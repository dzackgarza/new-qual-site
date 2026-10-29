---
schema: qual/card@1
id: P-UCLAB09S-07
kind: problem
title: Differentiability and the multivariable chain rule from the definition
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
  note: Checked against Problem 7 of the retained UCLA Basic Examination, Spring 2009.
---

::: {.problem}
(a) Define what it means for $f:\RR^n\to\RR^m$ to be differentiable at a point $a\in\RR^n$.

(b) Using this definition, formulate and prove the chain rule for the derivative of $g(f(x))$ at $x=a$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

A function
$$
f:\RR^n\to\RR^m
$$
is differentiable at
$$
a\in\RR^n
$$
if there exists a linear map
$$
A:\RR^n\to\RR^m
$$
such that
$$
\boxed{
\lim_{h\to0}
\frac{
\|f(a+h)-f(a)-Ah\|
}{
\|h\|
}
=0.
}
$$
The map $A$ is denoted
$$
Df(a).
$$


::: pf-proof

This is the definition of Fréchet differentiability in finite-dimensional Euclidean spaces.
Equivalently, one may write
$$
f(a+h)
=
f(a)+Df(a)h+r(h),
$$
where
$$
\frac{\|r(h)\|}{\|h\|}
\to0
$$
as $h\to0$.

:::

:::

::: {.pf-step #s1-2}

Differentiability of $f$ at $a$ implies
$$
f(a+h)-f(a)=O(\|h\|).
$$


::: pf-proof

Write
$$
f(a+h)-f(a)
=
Ah+r(h)
$$
as in step [](#s1-1){.pf-ref}.
Since $A$ is linear on a finite-dimensional normed space, it is bounded:
$$
\|Ah\|
\le
\|A\|\,\|h\|.
$$
Also
$$
\|r(h)\|
=
o(\|h\|).
$$
Hence for sufficiently small $h$,
$$
\|f(a+h)-f(a)\|
\le
(\|A\|+1)\|h\|.
$$

:::

:::

::: {.pf-step #s1-3}

Chain Rule: suppose
$$
f:\RR^n\to\RR^m
$$
is differentiable at $a$, and
$$
g:\RR^m\to\RR^p
$$
is differentiable at
$$
b=f(a).
$$
Then
$$
g\circ f
$$
is differentiable at $a$, with
$$
\boxed{
D(g\circ f)(a)
=
Dg(f(a))\circ Df(a).
}
$$


::: pf-proof

This is the statement to be proved in the following steps.

:::

:::

::: {.pf-step #s1-4}

Set
$$
A=Df(a),
\qquad
B=Dg(b).
$$
Then there are remainder functions $r$ and $s$ such that
$$
f(a+h)
=
b+Ah+r(h),
$$
with
$$
\frac{\|r(h)\|}{\|h\|}
\to0,
$$
and
$$
g(b+k)
=
g(b)+Bk+s(k),
$$
with
$$
\frac{\|s(k)\|}{\|k\|}
\to0.
$$


::: pf-proof

This is the differentiability definition from step [](#s1-1){.pf-ref} applied first to $f$ at $a$ and then to $g$ at $b$.

:::

:::

::: {.pf-step #s1-5}

Define
$$
k(h)
=
f(a+h)-f(a)
=
Ah+r(h).
$$
Then
$$
k(h)\to0
$$
and
$$
\|k(h)\|=O(\|h\|).
$$


::: pf-proof

The $O(\|h\|)$ estimate is step [](#s1-2){.pf-ref}.
In particular,
$$
\|k(h)\|\to0,
$$
so
$$
k(h)\to0.
$$

:::

:::

::: {.pf-step #s1-6}

One has
$$
\begin{aligned}
g(f(a+h))-g(f(a))
&=
BAh
+
Br(h)
+
s(k(h)).
\end{aligned}
$$


::: pf-proof

By step [](#s1-5){.pf-ref},
$$
f(a+h)
=
b+k(h).
$$
Apply the expansion for $g$ from step [](#s1-4){.pf-ref}:
$$
\begin{aligned}
g(f(a+h))
&=
g(b+k(h))\\
&=
g(b)+Bk(h)+s(k(h))\\
&=
g(b)
+
B(Ah+r(h))
+
s(k(h)).
\end{aligned}
$$
Since
$$
g(b)=g(f(a)),
$$
subtracting yields the displayed identity.

:::

:::

::: {.pf-step #s1-7}

The term
$$
Br(h)
$$
satisfies
$$
\frac{\|Br(h)\|}{\|h\|}
\to0.
$$


::: pf-proof

Boundedness of the linear map $B$ gives
$$
\frac{\|Br(h)\|}{\|h\|}
\le
\|B\|
\frac{\|r(h)\|}{\|h\|}.
$$
The final factor tends to $0$ by step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

The term
$$
s(k(h))
$$
satisfies
$$
\frac{\|s(k(h))\|}{\|h\|}
\to0.
$$


::: pf-proof

For $h$ such that $k(h)\ne0$,
$$
\frac{\|s(k(h))\|}{\|h\|}
=
\frac{\|s(k(h))\|}{\|k(h)\|}
\frac{\|k(h)\|}{\|h\|}.
$$
By step [](#s1-5){.pf-ref},
$$
k(h)\to0,
$$
so the first factor tends to $0$ by differentiability of $g$.
The second factor is bounded because
$$
\|k(h)\|=O(\|h\|).
$$
Hence the product tends to $0$.
If
$$
k(h)=0,
$$
then
$$
s(k(h))=s(0)=0,
$$
so the conclusion remains valid.

:::

:::

::: {.pf-step #s1-9}

Therefore
$$
\frac{
\|g(f(a+h))-g(f(a))-BAh\|
}{
\|h\|
}
\to0.
$$


::: pf-proof

By step [](#s1-6){.pf-ref},
$$
g(f(a+h))-g(f(a))-BAh
=
Br(h)+s(k(h)).
$$
Divide by $\|h\|$ and use the triangle inequality together with steps [](#s1-7){.pf-ref} through [](#s1-8){.pf-ref}.

:::

:::

::: {.pf-step #s1-10}

Hence
$$
\boxed{
D(g\circ f)(a)
=
B A
=
Dg(f(a))\,Df(a).
}
$$


::: pf-proof

Step [](#s1-9){.pf-ref} is exactly the differentiability criterion from step [](#s1-1){.pf-ref} with derivative
$$
BA.
$$
Thus the chain rule follows.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} answers part (a), and steps [](#s1-3){.pf-ref} through [](#s1-10){.pf-ref} formulate and prove the chain rule requested in part (b).

:::

:::

:::
