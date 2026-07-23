---
schema: qual/card@1
id: P-ZGEFJ
kind: problem
title: "In order for $IS$ to be a submodule of $A$, we need to show the follow\u2026"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---
In order for $IS$ to be a submodule of $A$, we need to show the following implication:
$$
x\in IS,~a\in A \implies xa, ax \in IS.
$$

Suppose $x\in IS$.
Then by definition, $x = \sum_{i=1}^n r_i a_i$ for some $r_i \in R, a_i\in A$.

But then
\[
\begin{align*}
xa &= \left( \sum_{i=1}^n r_i a_i \right) a \\
&= \sum_{i=1}^n r_i a_i a \\
&\definedas \sum_{i=1}^n r_i a_i',
\end{align*}
\]

where $a_i' \definedas a_i a$ for each $i$, which is still an element of $A$ since $A$ itself is a module and thus closed under multiplication.

But this expresses $xa$ as an element of $IS$. Similarly, we have
\[
\begin{align*}
ax &= a \left( \sum_{i=1}^n r_i a_i \right)\\
&= \sum_{i=1}^n a r_i a_i a \\
&\definedas \sum_{i=1}^n r_i a a_i, \\
&\definedas \sum_{i=1}^n r_i a_i',
\end{align*}
\]

and so $ax \in IS$ as well.

## Part 2

Letting $R/I \actson A/IA$ be the action given by $r+I \actson + IA \definedas ra + IA$, we need to show the following:

- $r.(x + y) = r.x + r.y$,
- $(r + r').x = r.x + r'.x$,
- $(rs).x = r.(s.x)$, and
- $1.x = x$.

Letting $\oplus$ denote the addition defined on cosets, we have
\[
\begin{align*}
r \actson (x + IA \oplus y + IA) 
&\definedas r \actson x + y + IA \\
&\definedas r(x+y) + IA \\
&= rx + ry + IA \\
&\definedas rx + IA \oplus ry + IA \\
&\definedas (r \actson x + IA) \oplus (r\actson y + IA)
.\end{align*}
\]

\[
\begin{align*}
(r + s) \actson x + IA 
&\definedas (r+s)x + IA \\
&\definedas rx + sx + IA \\
&\definedas rx + IA \oplus sx + IA \\
&\definedas (rs \actson IA) \oplus (sx \actson IA)
.\end{align*}
\]

\[
\begin{align*}
(rs) \actson x + IA &\definedas rsx + IA \\
&= r(sx) + IA \\
&\definedas r \actson(sx + IA) \\
&= r \actson (s \actson x + IA)
.\end{align*}
\]


\[
\begin{align*}
1 \actson x + IA &\definedas 1x + IA = x + IA
.\end{align*}
\]

