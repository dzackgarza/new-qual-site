---
schema: qual/card@1
id: E-YTG4V
kind: problem
title: Continuity of the field operations on $\RR$
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
  - Metric Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §21 Exercise 12, printed p. 135, with Lemma 21.4;
    the four parts and the three hints are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 21.12, PDF pp. 26-27. Delta = epsilon over two for
    addition, the three-term expansion for multiplication, the five cases of the preimage of
    an interval under the reciprocal, and subtraction and quotient as composites with
    negation and the reciprocal. (tmp/sources/munkres-solutions-positron-ch2.pdf).
---

::: {.exercise}

Prove continuity of the algebraic operations on $\RR$, as follows.
Use the metric $d(a, b) = \abs{a - b}$ on $\RR$ and the metric on $\RR^2$ given by the equation

$$
\rho((x, y), (x_0, y_0)) = \max\theset{\abs{x - x_0}, \abs{y - y_0}}.
$$

(a) Show that addition is continuous.
Hint: Given $\epsilon$, let $\delta = \epsilon/2$ and note that

$$
d(x + y, x_0 + y_0) \leq \abs{x - x_0} + \abs{y - y_0}.
$$

(b) Show that multiplication is continuous.
Hint: Given $(x_0, y_0)$ and $0 < \epsilon < 1$, let

$$
3\delta = \epsilon/(\abs{x_0} + \abs{y_0} + 1)
$$

and note that

$$
d(xy, x_0y_0) \leq \abs{x_0}\abs{y - y_0} + \abs{y_0}\abs{x - x_0} + \abs{x - x_0}\abs{y - y_0}.
$$

(c) Show that the operation of taking reciprocals is a continuous map from $\RR - \theset{0}$ to $\RR$.
[Hint: Show the inverse image of the interval $(a, b)$ is open. Consider five cases, according as $a$ and $b$ are positive, negative, or zero.]

(d) Show that the subtraction and quotient operations are continuous.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 21.12, PDF pp. 26--27** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the four parts are theirs, following the book's hints. Whitman's printed pp. 249--250 gives the same four.

Throughout $d(a,b)=\abs{a-b}$ on $\RR$ and $\rho((x,y),(x_{0},y_{0}))=\max\{\abs{x-x_{0}},\abs{y-y_{0}}\}$ on $\RR^{2}$, which induces the product topology (Exercise 21.3(a)).

(a) *Addition.* Let $(x_{0},y_{0})\in\RR^{2}$ and $\varepsilon>0$; take $\delta=\varepsilon/2$. If $\rho((x,y),(x_{0},y_{0}))<\delta$ then
$$
d(x+y,x_{0}+y_{0})\le\abs{x-x_{0}}+\abs{y-y_{0}}\le2\rho((x,y),(x_{0},y_{0}))<2\delta=\varepsilon .
$$

(b) *Multiplication.* Let $(x_{0},y_{0})\in\RR^{2}$ and $\varepsilon>0$; choose $0<\delta<\min\{\varepsilon/(\abs{x_{0}}+\abs{y_{0}}+1),1\}$. If $\rho((x,y),(x_{0},y_{0}))<\delta$ then
$$
d(xy,x_{0}y_{0})\le\abs{x_{0}}\abs{y-y_{0}}+\abs{y_{0}}\abs{x-x_{0}}+\abs{x-x_{0}}\abs{y-y_{0}}
<\delta\big(\abs{x_{0}}+\abs{y_{0}}+\delta\big)<\frac{\varepsilon}{\abs{x_{0}}+\abs{y_{0}}+1}\big(\abs{x_{0}}+\abs{y_{0}}+1\big)=\varepsilon,
$$
using $\delta<1$.

(c) *Reciprocals.* Let $f(x)=1/x$ on $\RR-\{0\}$. For an interval $(a,b)$,
$$
f^{-1}\big((a,b)\big)=\begin{cases}(1/b,\,1/a),&0<a<b,\\ (1/b,\,1/a),&a<b<0,\\ (-\infty,\,1/a)\cup(1/b,\,+\infty),&a<0<b,\\ (1/b,\,+\infty)=f^{-1}((a,b)),&a=0<b,\\ (-\infty,\,1/a),&a<b=0,\end{cases}
$$
that is, in every case an open subset of $\RR-\{0\}$ (the five cases being exactly those the hint lists). Since the open intervals form a basis of $\RR$, $f$ is continuous.

(d) *Subtraction and quotient.* The map $g(x)=-x$ and the identity are continuous on $\RR$, so $(x,y)\mapsto x\times(-y)$ is continuous by Exercise 18.10, and the subtraction $x-y$ is the composite of it with addition, hence continuous. Similarly $x/y$ on $\RR\times(\RR-\{0\})$ is the composite of $(x,y)\mapsto x\times(1/y)$, which is continuous by (c) with Exercise 18.10, and multiplication, hence continuous.
:::
