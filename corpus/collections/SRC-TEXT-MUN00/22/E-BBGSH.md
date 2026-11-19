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
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2 and re-checked against the retained set, whose
    Exercise 22.4 is at line 912 of `tmp/sources/munkres-solutions-positron-ch2.md`: in each part
    a continuous surjection whose fibres are the classes is shown to have a continuous right
    inverse, hence to be a quotient map by Exercise 22.2(a), and Corollary 22.3 makes the induced
    bijection a homeomorphism. Added: the two implications inside Exercise 22.2(a) that the set
    cites by number (openness of $U$ from openness of $g^{-1}(U)$ via $U=h^{-1}(g^{-1}(U))$, and
    continuity of $g$ by hypothesis), the surjectivity of each $g$ exhibited by an explicit point,
    and the description of the level sets in the final step. No defect found in the statement of
    §22 Exercise 4, printed p. 145. Not claimed: a printed publication, the source being a posted
    solution set.
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
The retained published solution is **positron0802, *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 22.4, PDF pp. 27--28** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); both parts are its, with the second written out with the right inverse $t\mapsto(\sqrt t,0)$. Write $\RR_+=[0,\infty)$.

::: pf

::: {.pf-step #criterion}
Let $X$ be a space, $\sim$ an equivalence relation on it with quotient map $\pi\colon X\to X^*$, and $g\colon X\to Z$ a continuous surjection whose fibres are exactly the equivalence classes. If $g$ has a continuous right inverse $h\colon Z\to X$, then $X^*$ is homeomorphic to $Z$.

::: pf-proof
Since the fibres of $g$ are the classes, $g(x)=g(x')$ exactly when $x\sim x'$, so $g$ induces a bijection $f\colon X^*\to Z$ with $g=f\circ\pi$; that is the situation of Corollary 22.3 of §22, and by that corollary $f$ is continuous. A continuous surjection $g$ with a continuous right inverse $h$ (so $g\circ h=\operatorname{id}_Z$) is a quotient map, which is Exercise 22.2(a): if $g^{-1}(U)$ is open then $U=h^{-1}(g^{-1}(U))$ is open, and $g$ is continuous by hypothesis. Hence $g=f\circ\pi$ is a quotient map, and a continuous bijection out of the quotient $X^*$ induced by a quotient map is a homeomorphism, again by Corollary 22.3.
:::

:::

::: {.pf-step #part-a}
For the relation $x_0\times y_0\sim x_1\times y_1$ iff $x_0+y_0^2=x_1+y_1^2$, the quotient $X^*$ is homeomorphic to $\RR$.

::: pf-proof
Take $g\colon\RR^2\to\RR$, $g(x,y)=x+y^2$. It is continuous, being a polynomial, and surjective since $g(t,0)=t$. Its fibres are exactly the classes, because $g(x_0,y_0)=g(x_1,y_1)$ says $x_0+y_0^2=x_1+y_1^2$. The map $h(t)=(t,0)$ is continuous and $g(h(t))=t$, so $h$ is a continuous right inverse; step [](#criterion){.pf-ref} applies with $Z=\RR$ and gives $X^*\cong\RR$. This is the hint's map.
:::

:::

::: {.pf-step #part-b}
For the relation $x_0^2+y_0^2=x_1^2+y_1^2$, the quotient $X^*$ is homeomorphic to $\RR_+$.

::: pf-proof
Take $g\colon\RR^2\to\RR_+$, $g(x,y)=x^2+y^2$. It is continuous and surjective, since every $t\ge0$ is $g(\sqrt t,0)$, and its fibres are the classes, the relation being equality of $x^2+y^2$. The map $h\colon\RR_+\to\RR^2$, $h(t)=(\sqrt t,0)$, is continuous on $\RR_+$ and satisfies $g(h(t))=t$, so it is a continuous right inverse and step [](#criterion){.pf-ref} applies with $Z=\RR_+$.
:::

:::

::: {.pf-step}
$\boxed{X^*\cong\RR\text{ in (a)},\qquad X^*\cong\RR_+\text{ in (b)}}$.

::: pf-proof
The two parts are steps [](#part-a){.pf-ref} and [](#part-b){.pf-ref}; in each, the quotient is the space of level sets of the indicated continuous function, and the level sets of $g(x,y)=x+y^2$ are the parabolas $x=t-y^2$ and those of $g(x,y)=x^2+y^2$ the circles of radius $\sqrt t$ about the origin together with the origin itself when $t=0$.
:::

:::

:::
:::
