---
schema: qual/card@1
id: E-HAT-4.2-30
kind: problem
title: "Fiber bundle projections from subspaces of $\\RR^2$"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Cards read. Verdict record is m7__proofs-4-2-14-26.md (14-26: 11 correct, 16 and 26 each a single named step; both repaired) and m5__proofs-4-2-27-39.md (27-39: 10 correct, 28, 29 defective single cases, 34 a wrong intermediate assertion; all three repaired). No card in this slice has an unmet piece.

- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 30; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the classification, which is what Queue D asks for on this card. The fibers, the shape of a subspace of R homeomorphic to R, the family h_t and the local trivialization are separate steps; the necessity is argued from the connectedness of the base rather than asserted, and the sufficiency now produces one family of homeomorphisms covering all four admissible shapes instead of the two representative cases the published solution works out. The exercise is covered by Proudfoot's Homework #7, §4.2 Exercise 30, printed p. 1, which lists the same four shapes; the uniform construction is the card's own and the card says so. Locators checked against the book: the exercise on printed p. 392. No statement repair.
---

::: {.problem}
Let $E$ be a subspace of $\RR^2$ obtained by deleting a subspace of $\{0\} \times \RR$.
For which such spaces $E$ is the projection $E \to \RR$, $(x, y) \mapsto x$, a fiber bundle?
:::

::: {.solution}
The published solution covering this exercise is **Nicholas Proudfoot, *Math 634: Algebraic Topology I* (University of Oregon, Fall 2015), Solutions to Homework #7, §4.2 Exercise 30, printed p. 1** (`tmp/sources/uoregon-proudfoot-634-hw7.pdf`, text version `tmp/sources/uoregon-proudfoot-634-hw7.md`); its coverage line reads "Exercises from Hatcher: Chapter 4.2, Problems 1, 2, 30, 31, 32, 39". It lists the four admissible shapes of the deleted set and exhibits explicit fiber-preserving homeomorphisms for two representative cases, with the rest "easily derived". The uniform construction below — one family $h_t$ of homeomorphisms of the interval covering all four shapes at once — is the card's own. The statement is Hatcher, *Algebraic Topology* (2002), §4.2 Exercise 30.

Write $E=\RR^2-\bigl(\{0\}\times A\bigr)$ and $p(x,y)=x$.

::: pf

::: {.pf-step #fibers}
For $x\ne0$ the fiber of $p$ is $\RR$, and $p^{-1}(0)=\RR-A$; hence a necessary condition for $p$ to be a fiber bundle is $\RR-A\cong\RR$.

::: pf-proof
Over $x\ne0$ no point of $\{0\}\times A$ lies in the fiber, so $p^{-1}(x)=\{x\}\times\RR\cong\RR$. Over $0$ the fiber is $\{(0,y):y\notin A\}=\{0\}\times(\RR-A)$. A fiber bundle over a connected base has fibers homeomorphic to one another — over a trivializing neighbourhood each fiber is carried homeomorphically to the model fiber — and $\RR$ is connected, so $\RR-A\cong\RR$ is necessary.
:::

:::

::: {.pf-step #interval}
A subspace of $\RR$ homeomorphic to $\RR$ is an open interval $(a,b)$ with $-\infty\le a<b\le\infty$.

::: pf-proof
A subspace of $\RR$ homeomorphic to $\RR$ is connected, hence an interval; it is a one-manifold without boundary, so no point of it is an endpoint of the interval in the relative topology, and an interval with no endpoint in the space is of the form $(a,b)$ or all of $\RR$, with possibly infinite endpoints. Conversely every such interval is homeomorphic to $\RR$.
:::

:::

::: {.pf-step #transition}
For $I=(a,b)$ and small $t>0$ there is an increasing homeomorphism $h_t:\RR\to I$ equal to the identity off the $t$-neighbourhoods of the finite ends of $I$, continuous jointly in $(t,y)$, with $h_t(y)\to y$ as $t\to0$ for each $y\in I$.

::: pf-proof
At a finite left endpoint $a$ put $h_t(y)=a+t\exp\bigl((y-a-t)/t\bigr)$ for $y\le a+t$ and $h_t(y)=y$ for $y\ge a+t$: the two formulas agree at $y=a+t$, the first is strictly increasing with image $(a,a+t]$, and it sends the left tail onto the tail of $I$. At a finite right endpoint $b$ put $h_t(y)=b-t\exp\bigl(-(y-b+t)/t\bigr)$ for $y\ge b-t$ and $h_t(y)=y$ for $y\le b-t$, symmetrically. For $t$ so small that $a+t<b-t$ the two regions are disjoint and the identity holds in between; if an endpoint is infinite no compression is needed there. The result is a strictly increasing surjection $\RR\to I$, hence a homeomorphism, and the formulas are jointly continuous in $(t,y)$ with the stated limit.
:::

:::

::: {.pf-step #trivialization}
If $\RR-A=I$ is an open interval then $p$ is a fiber bundle.

::: pf-proof
Away from $x=0$ the projection is already a product: $p^{-1}\bigl((0,\infty)\bigr)=(0,\infty)\times\RR$ and $p^{-1}\bigl((-\infty,0)\bigr)=(-\infty,0)\times\RR$. It remains to trivialize over $(-\varepsilon,\varepsilon)$. Define
$$
H:p^{-1}\bigl((-\varepsilon,\varepsilon)\bigr)\longrightarrow(-\varepsilon,\varepsilon)\times I,
\qquad
H(x,y)=\begin{cases}(x,h_{\abs{x}}(y)),&x\ne0,\\ (0,y),&x=0,\end{cases}
$$
with $h_t$ from step [](#transition){.pf-ref}. It is fiber preserving, and it is a bijection because each $h_t$ is one. Continuity at the central fiber follows from $h_t(y)\to y$ as $t\to0$, uniformly on compact subsets of $I$ by the explicit formulas; the inverse is given by $h_t^{-1}$ in the first factor, and the same limiting behaviour of $h_t^{-1}$ gives its continuity. So $H$ is a fiber-preserving homeomorphism, and with the two product regions this trivializes $p$ over all of $\RR$. Together with steps [](#fibers){.pf-ref} and [](#interval){.pf-ref} this gives: $p$ is a fiber bundle exactly when $\RR-A$ is an open interval, possibly unbounded — that is, exactly when $A$ is $\varnothing$, a closed half-line, or the union of two closed half-lines, which are the four shapes the published solution lists.
:::

:::

:::
:::
