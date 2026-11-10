---
schema: qual/card@1
id: E-BBGSH
kind: problem
title: Quotients of the plane by level-set relations
classification:
  areas:
  - topology
  topics:
  - Quotient Topology
  - Homeomorphisms
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §22 Exercise 4, printed p. 145, with Corollary
    22.3; the two equivalence relations are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 22.4, PDF pp. 27-28. In each part a continuous
    surjection whose fibres are the classes has a continuous right inverse, hence is a
    quotient map, and Corollary 22.3 makes the induced bijection a homeomorphism: the
    quotient is R in (a) and R_+ in (b). (tmp/sources/munkres-solutions-positron-ch2.pdf).
---

::: {.exercise}

(a) Define an equivalence relation on the plane $X = \RR^2$ as follows:

$$
x_0 \times y_0 \sim x_1 \times y_1 \quad \text{if } x_0 + y_0^2 = x_1 + y_1^2.
$$

Let $X^*$ be the corresponding quotient space.
It is homeomorphic to a familiar space; what is it?
[Hint: Set $g(x \times y) = x + y^2$.]

(b) Repeat (a) for the equivalence relation

$$
x_0 \times y_0 \sim x_1 \times y_1 \quad \text{if } x_0^2 + y_0^2 = x_1^2 + y_1^2.
$$
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 22.4, PDF pp. 27--28** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); both parts are theirs, with the second written out with the right inverse $t\mapsto(\sqrt t,0)$.

(a) Let $X=\RR^{2}$ with $x_{0}\times y_{0}\sim x_{1}\times y_{1}$ iff $x_{0}+y_{0}^{2}=x_{1}+y_{1}^{2}$, and let $g(x,y)=x+y^{2}$, a continuous surjection $\RR^{2}\to\RR$ whose fibres are exactly the classes, so that $X^{*}=\{g^{-1}(\{t\})\mid t\in\RR\}$. The map $h(t)=t\times0$ is continuous and $g(h(t))=t$, so $h$ is a right inverse of $g$ and $g$ is a quotient map by Exercise 22.2(a). By Corollary 22.3 (printed p. 142) the induced bijection $f:X^{*}\to\RR$ is continuous, and it is a homeomorphism because $g$ is a quotient map. So $X^{*}$ is homeomorphic with $\RR$.

(b) With $x_{0}\times y_{0}\sim x_{1}\times y_{1}$ iff $x_{0}^{2}+y_{0}^{2}=x_{1}^{2}+y_{1}^{2}$, take $g(x,y)=x^{2}+y^{2}$, a continuous surjection $\RR^{2}\to\RR_{+}$ whose fibres are the classes. The map $h(t)=\sqrt t\times0$ is continuous with $g(h(t))=t$, so $g$ is a quotient map by Exercise 22.2(a), and Corollary 22.3 gives that $X^{*}$ is homeomorphic with $\RR_{+}$.
:::
