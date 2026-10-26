---
schema: qual/card@1
id: P-UCLAB18F-05
kind: problem
title: Lipschitz extension from the boundary of the unit ball
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
  note: Checked against the vendored UCLA Basic Examination, Fall 2018, `assets/attachments/basic-18F.pdf`.
---

::: {.problem}
Let $B=\{x\in\mathbb R^n:|x|\le1\}$ and let $g:\partial B\to\mathbb R$ be $1$-Lipschitz.

(a) Show that
\[
f(x)=\inf_{y\in\partial B}\bigl(g(y)+|x-y|\bigr)
\]
is $1$-Lipschitz on $B$.

(b) Let $M(g)$ be the set of all $1$-Lipschitz $h:B\to\mathbb R$ satisfying $h|_{\partial B}=g$.
Show that $M(g)$ is compact in $C(B)$ with the supremum norm.
:::

Define
\[
f(x)
=
\inf_{y\in\partial B}
\bigl(g(y)+|x-y|\bigr).
\]

::: pf

::: pf-step

The function $f$ is finite-valued on $B$.


::: pf-proof

The sphere $\partial B$ is compact, and $g$ is Lipschitz, hence continuous and bounded.
Thus there is
\[
M>0
\]
such that
\[
|g(y)|\le M
\]
for every $y\in\partial B$.
For $x\in B$ and $y\in\partial B$,
\[
-M
\le
g(y)+|x-y|
\le
M+2.
\]
Hence the infimum is a finite real number.

:::

:::

::: pf-step

For all $x,z\in B$,
\[
f(x)\le f(z)+|x-z|.
\]


::: pf-proof

For every $y\in\partial B$, the triangle inequality gives
\[
|x-y|
\le
|x-z|+|z-y|.
\]
Therefore
\[
g(y)+|x-y|
\le
|x-z|
+
g(y)+|z-y|.
\]
Taking the infimum over $y\in\partial B$ gives
\[
f(x)
\le
|x-z|+f(z).
\]

:::

:::

::: pf-step

The function $f$ is $1$-Lipschitz on $B$.


::: pf-proof

Step <1>2 gives
\[
f(x)-f(z)\le |x-z|.
\]
Interchanging $x$ and $z$ gives
\[
f(z)-f(x)\le |x-z|.
\]
Hence
\[
\boxed{|f(x)-f(z)|\le |x-z|}.
\]

:::

:::

::: pf-step

For every $x\in\partial B$,
\[
\boxed{f(x)=g(x)}.
\]


::: pf-proof

Taking $y=x$ in the defining infimum gives
\[
f(x)\le g(x).
\]

Conversely, since $g$ is $1$-Lipschitz,
\[
g(x)\le g(y)+|x-y|
\]
for every $y\in\partial B$.
Taking the infimum over $y$ gives
\[
g(x)\le f(x).
\]
Thus equality holds.

:::

:::

::: pf-step

In particular,
\[
M(g)\ne\varnothing.
\]


::: pf-proof

By step <1>3, $f$ is $1$-Lipschitz on $B$, and by step <1>4 it restricts to $g$ on $\partial B$.
Therefore
\[
f\in M(g).
\]

:::

:::

::: pf-step

The family $M(g)$ is equicontinuous.


::: pf-proof

Every
\[
h\in M(g)
\]
is $1$-Lipschitz.
Thus for all $x,z\in B$,
\[
|h(x)-h(z)|
\le
|x-z|,
\]
with the same modulus of continuity for every $h$.

:::

:::

::: pf-step

The family $M(g)$ is uniformly bounded.


::: pf-proof

Fix one point
\[
y_0\in\partial B.
\]
For every $h\in M(g)$ and every $x\in B$,
\[
\begin{aligned}
|h(x)|
&\le
|h(x)-h(y_0)|+|h(y_0)|\\
&\le
|x-y_0|+|g(y_0)|\\
&\le
2+|g(y_0)|.
\end{aligned}
\]
Thus a single bound works for all $h\in M(g)$ and all $x\in B$.

:::

:::

::: pf-step

The set $M(g)$ is closed in $C(B)$ with the supremum norm.


::: pf-proof

Let
\[
h_n\in M(g)
\]
and suppose
\[
\|h_n-h\|_\infty\to0
\]
for some $h\in C(B)$.

For $x,z\in B$,
\[
|h_n(x)-h_n(z)|
\le
|x-z|.
\]
Passing to the limit gives
\[
|h(x)-h(z)|
\le
|x-z|.
\]
Thus $h$ is $1$-Lipschitz.

If $x\in\partial B$, then
\[
h_n(x)=g(x)
\]
for every $n$.
Uniform convergence, hence pointwise convergence, gives
\[
h(x)=g(x).
\]
Therefore
\[
h\in M(g),
\]
so $M(g)$ is closed.

:::

:::

::: pf-step

The closure of $M(g)$ in $C(B)$ is compact.


::: pf-proof

The ball
\[
B=\{x\in\mathbb R^n:|x|\le1\}
\]
is compact.
By steps <1>6--<1>7, the family $M(g)$ is equicontinuous and uniformly bounded.
The Arzelà--Ascoli theorem therefore implies that its closure in
\[
C(B)
\]
with the supremum norm is compact.

:::

:::

::: pf-step

Therefore
\[
\boxed{M(g)\text{ is compact in }C(B)}.
\]


::: pf-proof

By step <1>8, $M(g)$ is already closed, so it equals its closure.
Step <1>9 therefore implies compactness.

:::

:::

::: pf-qed

Step <1>3 proves part (a), and steps <1>4--<1>10 prove part (b).

:::

:::

::: pf

::: pf-step

For every $x,x'\in B$ and every $y\in\partial B$,
\[
g(y)+|x-y|
\le
g(y)+|x'-y|+|x-x'|.
\]


::: pf-proof

The Euclidean triangle inequality gives
\[
|x-y|
\le
|x-x'|+|x'-y|.
\]
Add $g(y)$ to both sides.

:::

:::

::: pf-step

Taking the infimum over $y\in\partial B$ in step <1>1 gives
\[
f(x)\le f(x')+|x-x'|.
\]


::: pf-proof

The additive term $|x-x'|$ is independent of $y$, so
\[
\begin{aligned}
f(x)
&=
\inf_{y\in\partial B}
\bigl(g(y)+|x-y|\bigr)\\
&\le
\inf_{y\in\partial B}
\bigl(g(y)+|x'-y|+|x-x'|\bigr)\\
&=
f(x')+|x-x'|.
\end{aligned}
\]

:::

:::

::: pf-step

Therefore
\[
\boxed{|f(x)-f(x')|\le|x-x'|}
\]
for all $x,x'\in B$.


::: pf-proof

Step <1>2 gives
\[
f(x)-f(x')\le|x-x'|.
\]
Interchanging $x$ and $x'$ gives
\[
f(x')-f(x)\le|x-x'|.
\]
Combining yields the absolute-value inequality.
Thus $f$ is $1$-Lipschitz.

:::

:::

::: pf-step

For every $x\in\partial B$,
\[
f(x)\le g(x).
\]


::: pf-proof

In the infimum defining $f(x)$, choose
\[
y=x.
\]
Then
\[
f(x)
\le
g(x)+|x-x|
=
g(x).
\]

:::

:::

::: pf-step

For every $x,y\in\partial B$,
\[
g(y)+|x-y|\ge g(x).
\]


::: pf-proof

Since $g$ is $1$-Lipschitz,
\[
g(x)-g(y)
\le
|x-y|.
\]
Rearranging gives the displayed inequality.

:::

:::

::: pf-step

For every $x\in\partial B$,
\[
f(x)\ge g(x).
\]


::: pf-proof

Step <1>5 holds for every
\[
y\in\partial B.
\]
Taking the infimum over $y$ gives
\[
f(x)
=
\inf_{y\in\partial B}
\bigl(g(y)+|x-y|\bigr)
\ge
g(x).
\]

:::

:::

::: pf-step

Thus
\[
\boxed{f|_{\partial B}=g}
\]
and in particular
\[
f\in M(g).
\]


::: pf-proof

Steps <1>4 and <1>6 give equality on the boundary.
Step <1>3 gives the $1$-Lipschitz property.
Thus $f$ belongs to the set $M(g)$.
In particular, $M(g)$ is nonempty.

:::

:::

::: pf-step

The family $M(g)$ is equicontinuous.


::: pf-proof

Every $h\in M(g)$ is $1$-Lipschitz.
Thus for every $\varepsilon>0$, choosing
\[
\delta=\varepsilon
\]
gives
\[
|x-x'|<\delta
\quad\Longrightarrow\quad
|h(x)-h(x')|
\le
|x-x'|
<
\varepsilon
\]
simultaneously for every $h\in M(g)$.

:::

:::

::: pf-step

The family $M(g)$ is uniformly bounded.


::: pf-proof

Fix one point
\[
y_0\in\partial B.
\]
For any $h\in M(g)$ and $x\in B$,
\[
\begin{aligned}
|h(x)|
&\le
|h(x)-h(y_0)|+|h(y_0)|\\
&\le
|x-y_0|+|g(y_0)|.
\end{aligned}
\]
Since
\[
|x|\le1
\qquad\text{and}\qquad
|y_0|=1,
\]
one has
\[
|x-y_0|
\le
|x|+|y_0|
\le2.
\]
Therefore
\[
\|h\|_\infty
\le
2+|g(y_0)|
\]
for every $h\in M(g)$.

:::

:::

::: pf-step

The set $M(g)$ is closed in $C(B)$ for the supremum norm.


::: pf-proof

Let
\[
h_n\in M(g)
\]
and suppose
\[
h_n\to h
\]
uniformly on $B$.

For any $x,x'\in B$,
\[
|h_n(x)-h_n(x')|
\le
|x-x'|.
\]
Passing to the limit gives
\[
|h(x)-h(x')|
\le
|x-x'|,
\]
so $h$ is $1$-Lipschitz.

For $x\in\partial B$,
\[
h_n(x)=g(x)
\]
for every $n$.
Taking the limit gives
\[
h(x)=g(x).
\]
Thus
\[
h\in M(g).
\]
Hence $M(g)$ is closed.

:::

:::

::: pf-step

The ball $B$ is compact.


::: pf-proof

It is closed and bounded in the finite-dimensional Euclidean space $\mathbb R^n$.
Thus the Heine--Borel theorem applies.

:::

:::

::: pf-step

The closure of $M(g)$ in $C(B)$ is compact.


::: pf-proof

By steps <1>8--<1>9, the family is equicontinuous and uniformly bounded.
By step <1>11, the domain $B$ is compact.
The Arzelà--Ascoli theorem therefore says that the closure of $M(g)$ in the supremum norm is compact.

:::

:::

::: pf-step

Therefore
\[
\boxed{M(g)\text{ is compact in }C(B)}.
\]


::: pf-proof

By step <1>10, the set $M(g)$ is already closed.
Thus its closure is itself.
Step <1>12 then implies compactness.

:::

:::

::: pf-qed

Steps <1>1--<1>7 prove part (a), and steps <1>8--<1>13 prove part (b).

:::

:::
