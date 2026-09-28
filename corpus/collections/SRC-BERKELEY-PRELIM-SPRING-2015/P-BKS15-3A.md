---
schema: qual/card@1
id: P-BKS15-3A
kind: problem
title: Images of polynomial maps $\RR\to\RR$ and $\RR^2\to\RR$
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
  note: Checked against the vendored UC Berkeley Spring 2015 Graduate Preliminary Examination.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the one-variable degree classification, the explicit parametrization of the positive half-line, the connected-image and line-restriction argument in two variables, and realization of every listed image type.
---

::: {.problem}
(a) Describe all sets of reals that can be the image of the real line under a polynomial with real coefficients.

(b) Find the image of the real plane under the polynomial
$$
x^2+(xy-1)^2.
$$

(c) Describe all sets of reals that can be the image of the real plane under a polynomial in two variables with real coefficients.
:::

::: {.solution}
<1>1. A constant polynomial $p\in\RR[t]$ has image a singleton.

::: {.proof}
If $p(t)=c$ for every $t\in\RR$, then
$$
p(\RR)=\{c\}.
$$
Conversely, every singleton occurs in this way.
:::

<1>2. Every nonconstant odd-degree polynomial $p\in\RR[t]$ has image $\RR$.

::: {.proof}
Let the leading term of $p$ be $at^d$, where $a\neq0$ and $d$ is odd. Then the limits of $p(t)$ as $t\to+\infty$ and $t\to-\infty$ have opposite signs and infinite magnitude. Hence, for every $r\in\RR$, there are $u<v$ with
$$
p(u)<r<p(v)
$$
or with the two inequalities reversed. Since $p$ is continuous, the intermediate value theorem gives some $t\in[u,v]$ such that $p(t)=r$.
:::

<1>3. Every nonconstant even-degree polynomial $p\in\RR[t]$ has image a closed half-line.

::: {.proof}
Write the leading term as $at^d$, where $d$ is even. If $a>0$, then
$$
p(t)\longrightarrow+\infty
$$
as $t\to\pm\infty$. Choose $R>0$ so large that
$$
\abs{t}\geq R
\quad\Longrightarrow\quad
p(t)>p(0).
$$
By the extreme value theorem, $p$ attains a minimum $m$ on $[-R,R]$, and the displayed inequality shows that this is a global minimum. Continuity and the limit $p(t)\to+\infty$ then imply
$$
p(\RR)=[m,\infty).
$$

If $a<0$, apply the same argument to $-p$. Thus $p$ has a global maximum $M$ and
$$
p(\RR)=(-\infty,M].
$$
:::

<1>4. The sets occurring in part (a) are exactly
$$
\boxed{
\{c\},\qquad
\RR,\qquad
[c,\infty),\qquad
(-\infty,c]
}
$$
with $c\in\RR$.

::: {.proof}
Steps <1>1--<1>3 show that no other image is possible. Conversely, the four displayed types are realized respectively by
$$
c,\qquad
t,\qquad
t^2+c,\qquad
c-t^2.
$$
This proves part (a).
:::

<1>5. For
$$
F(x,y)\coloneqq x^2+(xy-1)^2,
$$
one has
$$
F(x,y)>0
$$
for every $(x,y)\in\RR^2$.

::: {.proof}
Both summands are nonnegative. If their sum were $0$, then $x=0$ and $xy-1=0$ simultaneously. But $x=0$ gives $xy-1=-1$, a contradiction.
:::

<1>6. The image in part (b) is
$$
\boxed{(0,\infty)}.
$$

::: {.proof}
Step <1>5 shows that the image is contained in $(0,\infty)$. Conversely, let $r>0$ and choose
$$
x=\sqrt r,
\qquad
y=\frac1{\sqrt r}.
$$
Then $xy=1$, so
$$
F(x,y)=x^2+(xy-1)^2=r.
$$
Thus every positive real number occurs. This proves part (b).
:::

<1>7. If $P\in\RR[x,y]$ is nonconstant, then $P(\RR^2)$ is an interval.

::: {.proof}
The plane $\RR^2$ is connected and $P$ is continuous. Therefore its image under $P$ is connected. The connected subsets of $\RR$ are precisely the intervals.
:::

<1>8. If $P\in\RR[x,y]$ is nonconstant, then $P(\RR^2)$ is unbounded.

::: {.proof}
Choose $u,v\in\RR^2$ with $P(u)\neq P(v)$. Define
$$
q(t)\coloneqq P\bigl(u+t(v-u)\bigr).
$$
Then $q\in\RR[t]$ and
$$
q(0)=P(u)\neq P(v)=q(1),
$$
so $q$ is nonconstant. Every nonconstant one-variable polynomial is unbounded in absolute value as $\abs{t}\to\infty$. Hence $q(\RR)$ is unbounded, and since
$$
q(\RR)\subseteq P(\RR^2),
$$
the latter set is unbounded as well.
:::

<1>9. Therefore the image of a nonconstant polynomial $P\in\RR[x,y]$ is one of
$$
\RR,
\qquad
[c,\infty),
\qquad
(c,\infty),
\qquad
(-\infty,c],
\qquad
(-\infty,c)
$$
for some $c\in\RR$.

::: {.proof}
By step <1>7 the image is an interval, and by step <1>8 it is unbounded. An interval unbounded in both directions is $\RR$. If it is unbounded only above, its finite infimum $c$ is either attained or not attained, giving respectively $[c,\infty)$ or $(c,\infty)$. The case of an interval unbounded only below is analogous.
:::

<1>10. Every set listed in step <1>9 occurs, and constant polynomials add exactly the singleton images.

::: {.proof}
The polynomial $x$ has image $\RR$. The polynomials
$$
x^2+c
\qquad\text{and}\qquad
c-x^2
$$
have images $[c,\infty)$ and $(-\infty,c]$. By step <1>6,
$$
c+F(x,y)
\qquad\text{and}\qquad
c-F(x,y)
$$
have images $(c,\infty)$ and $(-\infty,c)$. Finally, the constant polynomial $c$ has image $\{c\}$.

Thus the sets occurring in part (c) are exactly
$$
\boxed{
\{c\},\quad
\RR,\quad
[c,\infty),\quad
(c,\infty),\quad
(-\infty,c],\quad
(-\infty,c)
}
$$
with $c\in\RR$.
:::

<1>11. Q.E.D.

::: {.proof}
Step <1>4 proves part (a), step <1>6 proves part (b), and step <1>10 proves part (c).
:::
:::
