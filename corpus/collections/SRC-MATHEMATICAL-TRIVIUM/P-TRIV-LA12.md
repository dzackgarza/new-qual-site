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
W _ { x } ( y _ { 1 } , . . . , y _ { n } ) = \operatorname * { d e t } \left[ \begin{array} { c c c c c c } { y _ { 1 } } & { y _ { 2 } } & { y _ { 3 } } & { . . . } & { y _ { n } } \\ { y _ { 1 } ^ { \prime } } & { y _ { 2 } ^ { \prime } } & { y _ { 3 } ^ { \prime } } & { . . . } & { y _ { n } ^ { \prime } } \\ { y _ { 1 } ^ { \prime \prime } } & { y _ { 2 } ^ { \prime \prime } } & { y _ { 3 } ^ { \prime \prime } } & { . . . } & { y _ { n } ^ { \prime \prime } } \\ { \vdots } & { \vdots } & { \vdots } & { \ddots } & { \vdots } \\ { y _ { 1 } ^ { ( n - 1 ) } } & { y _ { 2 } ^ { ( n - 1 ) } } & { y _ { 3 } ^ { ( n - 1 ) } } & { . . . } & { y _ { n } ^ { ( n - 1 ) } } \end{array} \right] ,\tag{5}
$$

where $y _ { 1 } , . . . , y _ { n }$ are $C ^ { n - 1 }$ functions of x.

(a) Let $y _ { 1 }$ and $y _ { 2 }$ be two solutions of the differential equation $y ^ { \prime \prime } - a y ^ { \prime } - b y = 0$ where a and b are some known functions of x. Find an expression for the Wronskian $W _ { x } ( y _ { 1 } , y _ { 2 } )$ depending on a and b. Then, show that if one of the solutions, say, $y _ { 1 }$ , is known, then another can be found from the first order equation $y _ { 1 } ^ { \prime } - { \frac { y _ { 2 } ^ { \prime } } { y _ { 2 } } } y _ { 1 } + { \frac { W _ { x } ( y _ { 1 } , y _ { 2 } ) } { y _ { 2 } } } = 0$

(b) Show that under change of variable $x \to t ( x )$ the Wronskian transforms as follows,

$$
W _ { x } ( y _ { 1 } , . . . , y _ { n } ) = \left( \frac { d t } { d x } \right) ^ { \frac { n ( n - 1 ) } { 2 } } W _ { t } ( y _ { 1 } , . . . , y _ { n } ) .\tag{6}
$$

(c) Show that $W _ { x } ( y y _ { 1 } , . . . , y y _ { n } ) = y ^ { n } W _ { x } ( y _ { 1 } , . . . , y _ { n } )$ , where y is some $C ^ { n - 1 }$ function.
:::

::: pf

::: pf-step

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

::: pf-step

If $y_1,y_2$ solve
$$
y''-a(x)y'-b(x)y=0,
$$
then
$$
W'(x)=a(x)W(x).
$$


::: pf-proof

Differentiate step <1>1:
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

::: pf-step

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

Step <1>2 is the first-order equation
$$
W'=aW.
$$
Separating variables gives the stated solution. The coefficient $b$ does not
enter the Wronskian equation.

:::

:::

::: pf-step

If $y_1$ is known, then $y_2$ satisfies the first-order equation
$$
y_1y_2'-y_1'y_2=W.
$$


::: pf-proof

This is simply the defining identity for the Wronskian from step <1>1, with
$W$ already known from step <1>3.

:::

:::

::: pf-step

Wherever $y_1\neq0$, step <1>4 is equivalently
$$
y_2'
-
\frac{y_1'}{y_1}y_2
=
\frac{W}{y_1}.
$$


::: pf-proof

Divide step <1>4 by $y_1$.

:::

:::

::: pf-step

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
which is step <1>4.

:::

:::

::: pf-step

Part (a) follows.


::: pf-proof

Step <1>3 gives Abel's formula, and steps <1>4--<1>6 give the requested
first-order reduction.

:::

:::

::: pf-step

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

::: pf-step

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
holds at order $k$, differentiate it using step <1>8. The derivative of the
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

::: pf-step

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
Step <1>9 says that this row equals
$$
\left(\frac{dt}{dx}\right)^k
$$
times the $k$th-derivative row in the $t$-Wronskian, plus a linear combination
of earlier rows. This is exactly a lower-triangular row transformation.

:::

:::

::: pf-step

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

By step <1>10, the determinant multiplier is the product of the diagonal
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

::: pf-step

Part (b) follows.


::: pf-proof

This is step <1>11.

:::

:::

::: pf-step

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

::: pf-step

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

Apply step <1>13 to each derivative row. The $k$th derivative row equals
$y$ times the corresponding original row plus a linear combination of earlier
rows.

:::

:::

::: pf-step

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
<1>14 is the product of its $n$ diagonal entries, namely $y^n$.

:::

:::

::: pf-step

Part (c) follows.


::: pf-proof

This is step <1>15.

:::

:::

::: pf-qed

Steps <1>7, <1>12, and <1>16 establish parts (a), (b), and (c), respectively.

:::

:::
