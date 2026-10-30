---
schema: qual/card@1
id: P-TRIV-LA12
kind: problem
title: 'Wronskian: Abel''s formula, change of variables and scaling'
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 12, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Consider the Wronskian
$$
W_x(y_1, \ldots, y_n) = \det \begin{bmatrix} y_1 & y_2 & y_3 & \cdots & y_n \\ y_1' & y_2' & y_3' & \cdots & y_n' \\ y_1'' & y_2'' & y_3'' & \cdots & y_n'' \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ y_1^{(n-1)} & y_2^{(n-1)} & y_3^{(n-1)} & \cdots & y_n^{(n-1)} \end{bmatrix}, \tag{5}
$$
where $y_1, \ldots, y_n$ are $C^{n-1}$ functions of $x$.

(a) Let $y_1$ and $y_2$ be two solutions of the differential equation $y'' - ay' - by = 0$, where $a$ and $b$ are some known functions of $x$. Find an expression for the Wronskian $W_x(y_1, y_2)$ depending on $a$ and $b$. Then, show that if one of the solutions, say, $y_1$, is known, then another can be found from the first order equation $y_1' - \frac{y_2'}{y_2}y_1 + \frac{W_x(y_1, y_2)}{y_2} = 0$.

(b) Show that under change of variable $x \to t(x)$ the Wronskian transforms as follows,
$$
W_x(y_1, \ldots, y_n) = \left( \frac{dt}{dx} \right)^{\frac{n(n-1)}{2}} W_t(y_1, \ldots, y_n). \tag{6}
$$

(c) Show that $W_x(yy_1, \ldots, yy_n) = y^n W_x(y_1, \ldots, y_n)$, where $y$ is some $C^{n-1}$ function.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For two functions,
$$
W(x)
=
W_x(y_1,y_2)
=
y_1y_2'-y_2y_1'.
$$


::: pf-proof

This is the determinant of the $2\times2$ Wronskian matrix.

:::

:::

::: {.pf-step #s1-2}

If $y_1,y_2$ solve
$$
y''-a(x)y'-b(x)y=0,
$$
then
$$
W'(x)=a(x)W(x).
$$


::: pf-proof

Differentiate step [](#s1-1){.pf-ref}:
$$
\begin{aligned}
W'
&=
y_1'y_2'+y_1y_2''-y_2'y_1'-y_2y_1''\\
&=
y_1y_2''-y_2y_1''.
\end{aligned}
$$
Since each solution satisfies
$$
y_j''=a y_j'+b y_j,
$$
one obtains
$$
\begin{aligned}
W'
&=
y_1(ay_2'+by_2)-y_2(ay_1'+by_1)\\
&=
a(y_1y_2'-y_2y_1')\\
&=aW.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

Hence
$$
\boxed{
W_x(y_1,y_2)
=
C\exp\left(\int^x a(s)\,ds\right)
}
$$
for some constant $C$.


::: pf-proof

Step [](#s1-2){.pf-ref} is the first-order equation
$$
W'=aW.
$$
Separating variables gives the stated solution. The coefficient $b$ does not
enter the Wronskian equation.

:::

:::

::: {.pf-step #s1-4}

If $y_1$ is known, then $y_2$ satisfies the first-order equation
$$
y_1y_2'-y_1'y_2=W.
$$


::: pf-proof

This is simply the defining identity for the Wronskian from step [](#s1-1){.pf-ref}, with
$W$ already known from step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Wherever $y_1\neq0$, step [](#s1-4){.pf-ref} is equivalently
$$
y_2'
-
\frac{y_1'}{y_1}y_2
=
\frac{W}{y_1}.
$$


::: pf-proof

Divide step [](#s1-4){.pf-ref} by $y_1$.

:::

:::

::: {.pf-step #s1-6}

The equation printed in the source,
$$
y_1'
-
\frac{y_2'}{y_2}y_1
+
\frac{W}{y_2}
=0,
$$
is the same first-order relation wherever $y_2\neq0$.


::: pf-proof

Multiply the displayed equation by $y_2$:
$$
y_1'y_2-y_1y_2'+W=0.
$$
Rearranging gives
$$
y_1y_2'-y_1'y_2=W,
$$
which is step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

Part (a) follows.


::: pf-proof

Step [](#s1-3){.pf-ref} gives Abel's formula, and steps [](#s1-4){.pf-ref} through [](#s1-6){.pf-ref} give the requested
first-order reduction.

:::

:::

::: {.pf-step #s1-8}

Under a change of variable $t=t(x)$,
$$
\frac{d}{dx}
=
\frac{dt}{dx}
\frac{d}{dt}.
$$


::: pf-proof

This is the chain rule.

:::

:::

::: {.pf-step #s1-9}

For every $k\geq0$,
$$
\frac{d^k y_j}{dx^k}
=
\left(
\frac{dt}{dx}
\right)^k
\frac{d^k y_j}{dt^k}
+
\sum_{r=0}^{k-1}
c_{k,r}(x)
\frac{d^r y_j}{dt^r}
$$
for coefficients $c_{k,r}$ independent of $j$.


::: pf-proof

Proceed by induction on $k$. The case $k=0$ is immediate. If the formula
holds at order $k$, differentiate it using step [](#s1-8){.pf-ref}. The derivative of the
leading term contributes
$$
\left(
\frac{dt}{dx}
\right)^{k+1}
\frac{d^{k+1}y_j}{dt^{k+1}}
$$
plus terms involving only derivatives of order at most $k$. Differentiating
the lower-order terms also produces only derivatives of order at most $k$.
Thus the formula holds at order $k+1$.

:::

:::

::: {.pf-step #s1-10}

The $x$-Wronskian matrix is obtained from the $t$-Wronskian matrix by
left multiplication by a lower-triangular matrix whose diagonal is
$$
1,
\frac{dt}{dx},
\left(\frac{dt}{dx}\right)^2,
\ldots,
\left(\frac{dt}{dx}\right)^{n-1}.
$$


::: pf-proof

Row $k+1$ of the Wronskian contains the $k$th derivatives of all $y_j$.
Step [](#s1-9){.pf-ref} says that this row equals
$$
\left(\frac{dt}{dx}\right)^k
$$
times the $k$th-derivative row in the $t$-Wronskian, plus a linear combination
of earlier rows. This is exactly a lower-triangular row transformation.

:::

:::

::: {.pf-step #s1-11}

Therefore
$$
\boxed{
W_x(y_1,\ldots,y_n)
=
\left(
\frac{dt}{dx}
\right)^{n(n-1)/2}
W_t(y_1,\ldots,y_n).
}
$$


::: pf-proof

By step [](#s1-10){.pf-ref}, the determinant multiplier is the product of the diagonal
entries:
$$
\prod_{k=0}^{n-1}
\left(
\frac{dt}{dx}
\right)^k
=
\left(
\frac{dt}{dx}
\right)^{\sum_{k=0}^{n-1}k}.
$$
Since
$$
\sum_{k=0}^{n-1}k
=
\frac{n(n-1)}2,
$$
the formula follows.

:::

:::

::: {.pf-step #s1-12}

Part (b) follows.


::: pf-proof

This is step [](#s1-11){.pf-ref}.

:::

:::

::: {.pf-step #s1-13}

For every $k\geq0$,
$$
\frac{d^k}{dx^k}(y,y_j)
=
y\,y_j^{(k)}
+
\sum_{r=0}^{k-1}
d_{k,r}(x)y_j^{(r)},
$$
where the coefficients $d_{k,r}$ are independent of $j$.


::: pf-proof

By Leibniz's rule,
$$
\frac{d^k}{dx^k}(y,y_j)
=
\sum_{r=0}^{k}
\binom{k}{r}
y^{(k-r)}y_j^{(r)}.
$$
The term with $r=k$ is $y,y_j^{(k)}$, and every other term involves a
derivative of $y_j$ of order less than $k$.

:::

:::

::: {.pf-step #s1-14}

The Wronskian matrix of
$$
yy_1,\ldots,yy_n
$$
is obtained from the Wronskian matrix of
$$
y_1,\ldots,y_n
$$
by a lower-triangular row transformation with diagonal entries all equal to
$y$.


::: pf-proof

Apply step [](#s1-13){.pf-ref} to each derivative row. The $k$th derivative row equals
$y$ times the corresponding original row plus a linear combination of earlier
rows.

:::

:::

::: {.pf-step #s1-15}

Hence
$$
\boxed{
W_x(yy_1,\ldots,yy_n)
=
y^nW_x(y_1,\ldots,y_n).
}
$$


::: pf-proof

The determinant of the lower-triangular row-transformation matrix in step
[](#s1-14){.pf-ref} is the product of its $n$ diagonal entries, namely $y^n$.

:::

:::

::: {.pf-step #s1-16}

Part (c) follows.


::: pf-proof

This is step [](#s1-15){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1-7){.pf-ref} and [](#s1-12){.pf-ref}, and [](#s1-16){.pf-ref} establish parts (a), (b), and (c), respectively.

:::

:::

:::
