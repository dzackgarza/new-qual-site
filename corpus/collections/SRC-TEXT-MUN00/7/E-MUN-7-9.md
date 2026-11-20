---
schema: qual/card@1
id: E-MUN-7-9
kind: problem
title: Recursion formulas that fall outside the standard principle
classification:
  areas:
  - topology
  topics:
  - Countable and Uncountable Sets
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 7, Exercise 9; the stored statement and printed hint match the source. The printed hint in part (b) is incorrect as stated; the solution supplies a corrected recursive second solution.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §7 Exercise 9, printed pp. 52-53; the three
    parts and both hints are stored as printed.
- event: source-corrected
  by: claude
  date: 2026-11-10
  note: >-
    Part (b)'s printed hint does not produce a solution. If f agrees with h off 3 and
    f(3) = -h(3), then the equation (*) at n = 3 reads f(3) = [f(4)]^2 - [f(2)]^2 =
    [h(4)]^2 - [h(2)]^2 = h(3), so f(3) = h(3); and h(3)^2 = 3 by (*) at n = 2, so
    h(3) = +-sqrt3 is nonzero and the negated value fails the equation. Dan Whitman's
    manual reaches the same conclusion on its printed p. 92 ("the hint as given does not
    exactly work") and then repairs it by defining f(3) = -sqrt3 and propagating the
    recursion. The card states the obstruction and carries that repaired construction;
    what is corrected is the hint, not the statement of the exercise.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 7.9,
    printed pp. 92-93 (tmp/sources/munkres-solutions-whitman.pdf). Part (a) is his
    reformulation h(n+1) = sqrt(h(n) + h(n-1)^2) with positivity, (b) his f with
    f(3) = -sqrt3 and the recursion for n > 3, and (c) the two contradictory values of
    h(3).
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the three-part prose solution into Lamport steps and checked the statement against Munkres, *Topology* (2000), §7 Exercise 9, printed p. 52. Part (a) now runs the principle of recursive definition on the pair sequence $g(n)=(h(n),h(n+1))$ rather than asserting that the two-term recurrence is directly of the theorem's form; the reformulation, the induction giving $g(n)=(h(n),h(n+1))$, the positivity induction and the verification of each clause were checked. Part (b) records that the printed hint fails at $n=3$ and gives the repaired construction, whose radicands $4-\sqrt3$ and later are positive. Part (c) is the two-clause contradiction at $n=2$ and $n=3$. The reformulation and the pair argument are the card's own; Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 7.9, printed pp. 92--93, gives the same reformulation, the repaired construction and the contradiction.
---

::: {.exercise}

(a) The formula

(\*)
$$
\begin{aligned}
h(1) &= 1, \\
h(2) &= 2, \\
h(n) &= [h(n+1)]^{2} - [h(n-1)]^{2} \quad \text{for } n \geq 2
\end{aligned}
$$
is not one to which the principle of recursive definition applies.
Show that nevertheless there does exist a function $h \colon \ZZ_{+} \to \RR$ satisfying this formula.
[Hint: Reformulate (\*) so that the principle will apply and require $h$ to be positive.]

(b) Show that the formula (\*) of part (a) does not determine $h$ uniquely.
[Hint: If $h$ is a positive function satisfying (\*), let $f(i) = h(i)$ for $i \neq 3$, and let $f(3) = -h(3)$.]

(c) Show that there is no function $h \colon \ZZ_{+} \to \RR$ satisfying the formula
$$
\begin{aligned}
h(1) &= 1, \\
h(2) &= 2, \\
h(n) &= [h(n+1)]^{2} + [h(n-1)]^{2} \quad \text{for } n \geq 2.
\end{aligned}
$$
:::

::: {.solution}
No retained solution set is used for the recursion itself: the reformulation below is the card's own, built so that Munkres's principle of recursive definition (Theorem 8.4) applies to a one-term recursion on pairs. Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 7.9, supplies the same reformulation for (a), the repaired construction for (b) and the contradiction for (c); the statement is Munkres, *Topology* (2000), §7 Exercise 9.

::: pf

::: {.pf-step #not-applicable}
(a) The formula (\*) is not one to which the principle of recursive definition applies as it stands.

::: pf-proof
Theorem 8.4 defines $h(n)$ from the values of $h$ on the section $\{1,\dots,n-1\}$. The third clause of (\*) relates $h(n)$ to $[h(n+1)]^2$, a value at the later index $n+1$, so it does not have the form $h(n)=\rho(h\restrictionof{\{1,\dots,n-1\}})$ for any $\rho$.
:::
:::

::: {.pf-step #reformulate}
(\*) is equivalent, for positive $h$, to $h(1)=1$, $h(2)=2$ and $h(n+1)=\sqrt{h(n)+[h(n-1)]^2}$ for $n\geq2$.

::: pf-proof
For $n\geq2$ the clause $h(n)=[h(n+1)]^2-[h(n-1)]^2$ rearranges to $[h(n+1)]^2=h(n)+[h(n-1)]^2$. If all values are positive, $h(n+1)$ is the positive square root of the right side, and conversely the square root formula implies the clause because squaring recovers it.
:::
:::

::: {.pf-step #pairs}
The principle of recursive definition applies to the recursion $g(1)=(1,2)$, $g(n+1)=\bigl(\text{second}(g(n)),\ \sqrt{\text{second}(g(n))+\text{first}(g(n))^2}\bigr)$ on $A=\RR^2$.

::: pf-proof
Take $a_0=(1,2)$ and, for a function $\varphi$ on the section $\{1,\dots,n\}$ with values in $A$, let $\rho(\varphi)$ be the pair whose first entry is $\varphi_2(n)$ and whose second entry is $\sqrt{\varphi_2(n)+\varphi_1(n)^2}$, where $\varphi_1,\varphi_2$ are the coordinate functions. This assigns an element of $A$ to every such $\varphi$, so Theorem 8.4 gives a unique $g:\ZZ_+\to A$ with $g(n+1)=\rho(g\restrictionof{\{1,\dots,n\}})$.
:::
:::

::: {.pf-step #first-coordinate}
With $h(n)\coloneqq$ the first coordinate of $g(n)$, one has $g(n)=(h(n),h(n+1))$ for every $n$, and $h(1)=1$, $h(2)=2$.

::: pf-proof
The first coordinate of $g(n+1)$ is the second coordinate of $g(n)$, by the definition of $\rho$; that is $h(n+1)=\text{second}(g(n))$, so $g(n)=(h(n),h(n+1))$. Then $h(1)$ and $h(2)$ are the two coordinates of $g(1)=(1,2)$.
:::
:::

::: {.pf-step #satisfies}
For every $n\geq2$, $h(n)=[h(n+1)]^2-[h(n-1)]^2$.

::: pf-proof
The second coordinate of $g(n+1)$ is $\sqrt{\text{second}(g(n))+\text{first}(g(n))^2}$ by the definition of $\rho$, that is $h(n+2)=\sqrt{h(n+1)+h(n)^2}$. Squaring and renaming $m=n+1$ gives $[h(m+1)]^2=h(m)+[h(m-1)]^2$, that is $h(m)=[h(m+1)]^2-[h(m-1)]^2$, for $m\geq2$. Together with step [](#first-coordinate){.pf-ref} the initial values are those of (\*).
:::
:::

::: {.pf-step #positive}
$h(n)>0$ for every $n$, so the square roots taken above are the positive ones.

::: pf-proof
$h(1)=1>0$ and $h(2)=2>0$; and $h(n+2)=\sqrt{h(n+1)+h(n)^2}>0$ whenever $h(n+1)>0$. By induction on $n$ every value is positive and every square root taken is the positive one.
:::
:::

::: {.pf-step #exists}
(a) There exists $h:\ZZ_+\to\RR$ satisfying (\*).

::: pf-proof
Steps [](#reformulate){.pf-ref}, [](#pairs){.pf-ref}, [](#first-coordinate){.pf-ref}, [](#satisfies){.pf-ref} and [](#positive){.pf-ref} produce $h$ satisfying the three clauses of (\*).
:::
:::

::: {.pf-step #third-value}
For the positive solution, $h(3)=\sqrt3$.

::: pf-proof
The clause at $n=2$ reads $2=[h(3)]^2-[h(1)]^2=[h(3)]^2-1$, so $[h(3)]^2=3$ and, $h(3)$ being positive, $h(3)=\sqrt3$.
:::
:::

::: {.pf-step #hint-fails}
(b) The printed hint does not work: changing only the value at $3$ leaves the clause at $n=3$ false.

::: pf-proof
If $f(i)=h(i)$ for $i\neq3$ and $f(3)=-h(3)$, then the clause at $n=2$ still holds, because it involves $[f(3)]^2=[h(3)]^2$; but the clause at $n=3$ reads $f(3)=[f(4)]^2-[f(2)]^2=h(3)$, since $f(4)=h(4)$ and $f(2)=h(2)$. As $h(3)=\sqrt3\neq0$ by step [](#third-value){.pf-ref}, $f(3)=-\sqrt3\neq h(3)$, so that clause fails.
:::
:::

::: {.pf-step #nonunique}
(b) Some function satisfying (\*) differs from the positive solution, so (\*) does not determine $h$ uniquely.

::: pf-proof
Set $f(1)=1$, $f(2)=2$, $f(3)=-\sqrt3$, and for $n\geq3$ set $f(n+1)=\sqrt{f(n)+[f(n-1)]^2}$, the radicand being positive: at $n=3$ it is $4-\sqrt3>0$, and for $n\geq4$ the term $f(n)$ has just been defined as a positive square root, so the radicand is positive. The clause at $n=2$ holds because $[f(3)]^2-[f(1)]^2=3-1=2=f(2)$, and at $n\geq3$ it holds by construction. Since $f(3)\neq h(3)$, the function $f$ is a second solution.
:::
:::

::: {.pf-step #none}
(c) There is no $h:\ZZ_+\to\RR$ with $h(n)=[h(n+1)]^2+[h(n-1)]^2$ for $n\geq2$, $h(1)=1$, $h(2)=2$.

::: pf-proof
At $n=2$ the formula gives $2=[h(3)]^2+1$, so $[h(3)]^2=1$ and $h(3)=\pm1$. At $n=3$ it gives $h(3)=[h(4)]^2+[h(2)]^2=[h(4)]^2+4\geq4$, contradicting $h(3)=\pm1$. So no such function exists.
:::
:::

:::
:::
