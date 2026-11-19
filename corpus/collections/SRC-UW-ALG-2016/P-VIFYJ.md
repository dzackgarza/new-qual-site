---
schema: qual/card@1
id: P-VIFYJ
kind: problem
title: $\CC[x,y]/(y^2-(x-1)^3-(x-1)^2)$ is a domain, its real points, and its integral
  closure
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Provenance recorded: Problem 6 of the Algebra Preliminary Examination, Autumn 2016
    (University of Washington), printed p. 1 of the two-page paper retained at
    assets/attachments/UW-Algebra-Qual-2016.pdf, is the statement the card answers, and the
    paragraph at the head of the solution records that the paper prints no solutions, so the
    argument is the card's own; the earlier audit note on this card had recorded the same fact
    inside the note only, and the paragraph now states it on the card. Checked: the statement,
    including the printed definition of the integral closure, against the paper's text layer at the
    page named; `qualc.authoring check` on the card, and `tmp/lam.sh` for the numbering and the
    QED. Not checked: no retained solution set exists for this paper to compare the argument with,
    the mathematics of the card is not re-proved in this pass, and no other card of the collection
    in this pass.
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Repaired and restructured. The card was a label-step skeleton with empty proofs over ten
    unjustified nested claims. The answers are right and unchanged — A is a domain, its real
    points are the nodal cubic with a loop over [0,1], and the integral closure is C[t] with t =
    y/(x-1). Added: the irreducibility argument in C[x][y] with the criterion 'monic y^2 - c
    reducible iff c is a square' and the parity check on the exponent of x, which the card had
    sketched as bullet points; the parametrisation y = ±(x-1)sqrt(x) with the node at x = 1 and
    the loop described; the computations t^2 = x and t^3 - t = y in K; and the closing argument
    that C[t], being a PID, is integrally closed, with Frac(C[t]) = K. Not claimed: a retained
    solution set; the collection's provenance is the examination paper only.
---

::: {.problem}
Let $A = \CC[x,y]/(y^2-(x-1)^3 - (x-1)^2)$.

(a) Show that $A$ is an integral domain and sketch the $\RR$-points of $\Spec A$.

(b) Find the integral closure of $A$.
Recall that for an integral domain $A$ with fraction field $K$, the integral closure of $A$ in $K$ is the set of all elements of $K$ integral over $A$.
:::

::: {.solution}
Throughout $A = \CC[x,y]/(y^{2} - (x-1)^{3} - (x-1)^{2})$, $f \coloneqq y^{2} - (x-1)^{3} - (x-1)^{2} = y^{2} - x(x-1)^{2}$ is the defining polynomial, and $K \coloneqq \operatorname{Frac}(A)$. The problem is Problem 6 of the Algebra Preliminary Examination, Autumn 2016 (University of Washington), printed p. 1 of the two-page paper retained at `assets/attachments/UW-Algebra-Qual-2016.pdf`; the paper prints no solutions and no solutions sheet accompanies it, so the argument below is the card's own.

::: pf

::: {.pf-step #domain}
(a) $A$ is an integral domain.

::: pf-proof
$\CC[x]$ is a UFD and $f = y^{2} - x(x-1)^{2}$ is monic of degree $2$ in $y$ over it. A monic polynomial $y^{2} - c$ is reducible in $R[y]$, for $R$ a UFD, exactly when $c$ is a square in $R$: a factorization into monic linears is $y^{2} - c = (y - r)(y + r)$ with $r \in R$ and $r^{2} = c$. Here $c = x(x-1)^{2}$ is not a square in $\CC[x]$, because the irreducible $x$ occurs in it to the odd power $1$ and exponents in a square are even. So $f$ is irreducible in $\CC[x][y] = \CC[x,y]$, and in a UFD an irreducible element is prime, so $(f)$ is a prime ideal and $A = \CC[x,y]/(f)$ is a domain.

:::

:::

::: {.pf-step #real}
(a) The $\RR$-points of $\Spec A$ form the nodal cubic with a loop over $[0,1]$.

::: pf-proof
A real point is a pair $(x,y) \in \RR^{2}$ with $y^{2} = x(x-1)^{2}$, which forces $x \ge 0$ (the right side is $\ge 0$ only for $x \ge 0$) and gives $y = \pm(x-1)\sqrt{x}$ for $x > 0$, the two signs meeting at $x = 0$ (where $y = 0$) and at $x = 1$ (where $y = 0$ again, and the factor $(x-1)^{2}$ makes the curve singular there, a node). Between $x = 0$ and $x = 1$ the two branches bound a closed loop, and for $x > 1$ they run off to infinity as two unbounded branches.

:::

:::

::: {.pf-step #t}
(b) The element $t \coloneqq y/(x-1) \in K$ is integral over $A$, and $A = \CC[t^{2}, t^{3}-t] \subseteq \CC[t]$.

::: pf-proof
In $K$ one has $t^{2} = y^{2}/(x-1)^{2} = x(x-1)^{2}/(x-1)^{2} = x$, so $t$ is a root of the monic polynomial $T^{2} - x \in A[T]$ and is therefore integral over $A$. Then $t^{3} - t = t\cdot t^{2} - t = tx - t = t(x-1) = y$, so $y \in \CC[t]$ and $x = t^{2} \in \CC[t]$; hence the composite $\CC[x,y] \to A \to K$ lands in $\CC[t]$, and since $t^{2}$ and $t^{3}-t$ generate the same subalgebra as $x$ and $y$, $A = \CC[t^{2}, t^{3}-t]$ inside $\CC[t]$.

:::

:::

::: {.pf-step #closure}
(b) $\CC[t]$ is integral over $A$ and integrally closed in $K$, hence it is the integral closure of $A$.

::: pf-proof
$\CC[t]$ is generated as an $A$-algebra by the single element $t$, which is integral over $A$ by step [](#t){.pf-ref}, so $\CC[t]$ is an integral extension of $A$. The ring $\CC[t]$ is a polynomial ring over a field, hence a PID, hence integrally closed in its fraction field; and $\operatorname{Frac}(\CC[t]) = \CC(t)$, which equals $K$ because $t = y/(x-1)$ lies in $K$ and $x = t^{2}$, $y = t^{3}-t$ lie in $\CC(t)$. An integral extension of $A$ inside $K$ that is integrally closed in $K$ is the integral closure of $A$ in $K$, so that closure is $\CC[t]$.

:::

:::

::: pf-step
The answers: $A$ is a domain whose real points form the nodal cubic with a loop over $[0,1]$, and the integral closure of $A$ in $K$ is $\boxed{\CC[t]}$ with $t = y/(x-1)$, so $A = \CC[t^{2}, t^{3}-t]$ and the normalization is $\CC[t]$.

::: pf-proof
Steps [](#domain){.pf-ref} and [](#real){.pf-ref} are part (a), and steps [](#t){.pf-ref} and [](#closure){.pf-ref} are part (b). The two coincidences $t^{2} = x$ and $t^{3}-t = y$ identify $A$ with the coordinate ring of the parametrized curve $(t^{2}, t^{3}-t)$, which is the standard normalization of a nodal cubic.

:::

:::

:::
:::
