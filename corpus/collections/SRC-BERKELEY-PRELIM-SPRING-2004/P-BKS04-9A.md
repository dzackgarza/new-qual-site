---
schema: qual/card@1
id: P-BKS04-9A
kind: problem
title: $(f(x)-f(y)).(x-y)\le L\norm{x-y}^2$ for all $x,y$ iff $Df(x)v.v\le L\norm{v}^2$ for all $x,v$
classification:
  areas: [prelim]
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained UC Berkeley Spring 2004 preliminary exam and its companion solution packet.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Compared the authored solution with the retained `s04solution.pdf` solution packet.
---

::: {.problem}
Let $f\colon\RR^n\to\RR^n$ be a differentiable function, and let $L$ be a nonnegative real number.
Prove that the following are equivalent:

(i) For every $x,y\in\RR^n$,

$$
(f(x)-f(y)).(x-y)\leq L\abs{x-y}^2
$$

(ii) For every $x,v\in\RR^n$,

$$
Df(x)v.v\leq L\abs{v}^2,
$$

where $Df(x)$ is the derivative of $f$ at $x$, and $.$ denotes the standard inner product of vectors in $\RR^n$.
:::

::: {.solution}

The argument is the card's own: (i) gives (ii) on dividing by $t^{2}$ and letting $t\to0$, and (ii) gives (i) by integrating the derivative along the segment from $y$ to $x$.

::: pf

::: {.pf-step #forward}

(i) $\Rightarrow$ (ii).

::: pf-proof

Fix $y,v\in\RR^{n}$ and put $x=y+tv$ with $t\ne0$. Then $x-y=tv$, and (i) reads
$$
t\,\bigl(f(y+tv)-f(y)\bigr)\cdot v\le Lt^{2}\abs{v}^{2}.
$$
Dividing by $t^{2}>0$ gives $\dfrac{f(y+tv)-f(y)}{t}\cdot v\le L\abs{v}^{2}$. As $t\to0$ the difference quotient tends to $Df(y)v$ by differentiability, and the inner product is continuous, so the left side tends to $Df(y)v\cdot v$; hence $Df(y)v\cdot v\le L\abs{v}^{2}$.

:::

:::

::: {.pf-step #path}

For fixed $x,y$ the function $g(s)=\bigl(f(y+s(x-y))-f(y)\bigr)\cdot(x-y)$ on $[0,1]$ satisfies $g'(s)=Df(y+s(x-y))(x-y)\cdot(x-y)$.

::: pf-proof

The map $s\mapsto y+s(x-y)$ is differentiable with derivative $x-y$, and $f$ is differentiable, so by the chain rule $\frac{d}{ds}f(y+s(x-y))=Df(y+s(x-y))(x-y)$; the term $f(y)$ is constant and the inner product with the fixed vector $x-y$ is linear, giving the displayed derivative.

:::

:::

::: {.pf-step #backward}

(ii) $\Rightarrow$ (i).

::: pf-proof

Assume (ii) and let $x,y\in\RR^{n}$. By step [](#path){.pf-ref} and (ii) with $v=x-y$ at the point $y+s(x-y)$,
$$
g'(s)=Df(y+s(x-y))(x-y)\cdot(x-y)\le L\abs{x-y}^{2}
$$
for every $s\in[0,1]$. Integrating over $[0,1]$ by the fundamental theorem of calculus,
$$
\bigl(f(x)-f(y)\bigr)\cdot(x-y)=g(1)-g(0)=\int_{0}^{1}g'(s)\,ds\le L\abs{x-y}^{2}.
$$

:::

:::

::: {.pf-step #conclusion}

(i) and (ii) are equivalent.

::: pf-proof

Steps [](#forward){.pf-ref} and [](#backward){.pf-ref} give the two implications for every differentiable $f:\RR^{n}\to\RR^{n}$ and every $L\ge0$:
$$
\boxed{(f(x)-f(y))\cdot(x-y)\le L\abs{x-y}^{2}\ \forall x,y\iff Df(x)v\cdot v\le L\abs{v}^{2}\ \forall x,v.}
$$

:::

:::

:::

:::
