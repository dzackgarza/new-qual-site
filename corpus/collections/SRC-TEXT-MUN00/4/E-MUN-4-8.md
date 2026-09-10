---
schema: qual/card@1
id: E-MUN-4-8
kind: problem
title: Greatest lower bound property of $\mathbb{R}$
classification:
  areas:
  - topology
  topics:
  - Integers and Real Numbers
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 4, Exercise 8; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

(a) Show that $\mathbb{R}$ has the greatest lower bound property.

(b) Show that $\inf \{1 / n \mid n \in \mathbb{Z}_+\} = 0$ .

(c) Show that given $a$ with $0 < a < 1$, $\inf \{a^n \mid n \in \mathbb{Z}_+\} = 0$ . [Hint: Let $h = (1 - a) / a$, and show that $(1 + h)^n \geq 1 + nh$ .]
:::

::: {.solution}
(a) Let \(A\subset\mathbb R\) be nonempty and bounded below. Then
\[
-A=\{-a:a\in A\}
\]
is nonempty and bounded above. Let
\[
s=\sup(-A).
\]
For every \(a\in A\), \(-a\le s\), so \(-s\le a\); hence \(-s\) is a lower bound of \(A\). If \(\ell\) is any lower bound of \(A\), then \(\ell\le a\) for all \(a\in A\), so \(-a\le-\ell\) for all \(a\in A\). Thus \(-\ell\) is an upper bound of \(-A\), whence \(s\le-\ell\), i.e.
\[
\ell\le-s.
\]
Therefore \(-s=\inf A\), proving the greatest lower bound property.

(b) Every \(1/n\) is positive, so \(0\) is a lower bound. If \(c>0\), the Archimedean property gives \(n\in\mathbb Z_+\) with
\[
n>1/c,
\]
hence
\[
0<1/n<c.
\]
So no positive number is a lower bound. Therefore
\[
\boxed{\inf\{1/n:n\in\mathbb Z_+\}=0.}
\]

(c) Let \(0<a<1\) and put
\[
h=\frac{1-a}{a}>0,
\qquad
\frac1a=1+h.
\]
By induction,
\[
(1+h)^n\ge1+nh
\]
for every \(n\ge1\): the induction step follows from
\[
(1+h)^{n+1}\ge(1+nh)(1+h)=1+(n+1)h+nh^2\ge1+(n+1)h.
\]
Hence
\[
a^n=\frac1{(1+h)^n}\le\frac1{1+nh}.
\]
Given \(\varepsilon>0\), the Archimedean property lets us choose \(n\) with \(1+nh>1/\varepsilon\), so \(a^n<\varepsilon\). Since all \(a^n>0\), it follows that
\[
\boxed{\inf\{a^n:n\in\mathbb Z_+\}=0.}
\]
:::
