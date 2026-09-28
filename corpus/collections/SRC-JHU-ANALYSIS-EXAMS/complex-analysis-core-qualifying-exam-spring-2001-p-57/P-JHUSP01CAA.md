---
schema: qual/card@1
id: P-JHUSP01CAA
kind: problem
title: An entire function dominated by another is its scalar multiple
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Liouville's Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the global domination |f|<=|g| and scalar-multiple conclusion with Spring 2001 Complex Analysis question 1."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Handled g identically zero separately, proved each zero of g occurs in f with at least the same multiplicity, extended f/g entire, and applied Liouville to the bounded quotient."
---

::: {.problem}
Question 1. Suppose that $f , g$ are entire holomorphic functions with $| f ( z ) | \leq | g ( z ) |$ for all $z \in \mathbf { C }$ . Prove that there is a constant $c \in \mathbf { C }$ so that $f = c g$ ·
:::

::: {.solution}
<1>1. If $g\equiv0$, the conclusion is immediate.
::: {.proof}
The inequality gives $|f(z)|\le0$ for every $z$, so $f\equiv0$. Then
$f=cg$ for any constant $c$, for example $c=0$.
:::

<1>2. Otherwise, $f/g$ extends holomorphically across every zero of $g$.
::: {.proof}
Assume $g$ is not identically zero. Let $a$ be a zero of $g$ of order $m$.
Write
$$
g(z)=(z-a)^m u(z),\qquad u(a)\ne0.
$$
If $f$ has a zero of order $k$ at $a$, write
$f(z)=(z-a)^k v(z)$ with $v(a)\ne0$; if $f\equiv0$ locally, then by the
identity theorem $f\equiv0$ globally and the conclusion is again immediate.
For nearby $z\ne a$, the hypothesis gives
$$
|z-a|^k|v(z)|\le |z-a|^m|u(z)|.
$$
If $k<m$, division by $|z-a|^k$ and passage to $z\to a$ would give
$|v(a)|\le0$, a contradiction. Hence $k\ge m$.

Therefore the quotient $h=f/g$, initially holomorphic away from the discrete
zero set of $g$, has a removable singularity at every zero of $g$. Filling in
those values gives an entire function $h$.
:::

<1>3. The extended quotient is bounded and hence constant.
::: {.proof}
Where $g(z)\ne0$, the original inequality gives
$$
|h(z)|=\left|\frac{f(z)}{g(z)}\right|\le1.
$$
By continuity the same bound holds at the removable points. Thus $h$ is a
bounded entire function. Liouville's theorem implies that $h\equiv c$ for some
$c\in\mathbb C$. Consequently
$$
f=cg
$$
on the whole plane, as required.
:::
:::
