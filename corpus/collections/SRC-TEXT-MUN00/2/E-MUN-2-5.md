---
schema: qual/card@1
id: E-MUN-2-5
kind: problem
title: Left inverses, right inverses, and bijectivity
classification:
  areas:
  - topology
  topics:
  - Functions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 2, Exercise 5; the stored statement matches.
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
    Read against Munkres, Topology (2000), §2 Exercise 5, printed p. 21; the statement
    of left and right inverse and the five parts are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 2.5,
    printed pp. 16-17 (tmp/sources/munkres-solutions-whitman.pdf). He notes there that
    (e) is Lemma 2.1 of the text, which Munkres leaves to the exercises; the card's
    chain g = g o i_B = g o (f o h) = (g o f) o h = i_A o h = h is that proof.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps from the retained Whitman solution (Exercise 2.5, printed pp. 16-17); statement unchanged. Each of the five parts is a numbered step; the injectivity and surjectivity facts of (a) are separate steps because (b), (c) and (e) use one of them apiece by reference; (d) exhibits its two inverses in each case. No page or citation change: the exercise and the definition of left and right inverse are both on printed p. 21.

---

::: {.exercise}

In general, let us denote the identity function for a set $C$ by $i_C$ . That is, define $i_C: C \to C$ to be the function given by the rule $i_C(x) = x$ for all $x \in C$ . Given $f: A \to B$, we say that a function $g: B \to A$ is a left inverse for $f$ if $g \circ f = i_A$ ; and we say that $h: B \to A$ is a right inverse for $f$ if $f \circ h = i_B$ .

(a) Show that if $f$ has a left inverse, $f$ is injective; and if $f$ has a right inverse, $f$ is surjective.

(b) Give an example of a function that has a left inverse but no right inverse.

(c) Give an example of a function that has a right inverse but no left inverse.

(d) Can a function have more than one left inverse?
More than one right inverse?

(e) Show that if $f$ has both a left inverse $g$ and a right inverse $h$, then $f$ is bijective and $g = h = f^{-1}$ .

:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 2.5** (`tmp/sources/munkres-solutions-whitman.pdf`), all five parts; part (e) is Lemma 2.1 of Munkres, which the book leaves to the exercises.

Throughout $f:A\to B$ is a function and $i_C:C\to C$ is the identity map of a set $C$; $g:B\to A$ is a left inverse of $f$ when $g\circ f=i_A$, and $h:B\to A$ a right inverse when $f\circ h=i_B$ (§2).

::: pf

::: {.pf-step #part-a}
(a) A left inverse of $f$ forces $f$ to be injective, and a right inverse forces it to be surjective.

::: pf-proof

::: {.pf-step #injective}
If $g\circ f=i_A$ then $f$ is injective.

::: pf-proof
Suppose $f(a_1)=f(a_2)$. Applying $g$ and using $g\circ f=i_A$ gives $a_1=g(f(a_1))=g(f(a_2))=a_2$.

:::

:::

::: {.pf-step #surjective}
If $f\circ h=i_B$ then $f$ is surjective.

::: pf-proof
For $b\in B$ we have $b=i_B(b)=f(h(b))$, so every $b$ is a value of $f$.

:::

:::

:::

:::

::: {.pf-step #part-b}
(b) A function with a left inverse and no right inverse: the inclusion $f:\{0\}\to\{0,1\}$.

::: pf-proof
Define $g:\{0,1\}\to\{0\}$ by $g(0)=g(1)=0$; then $g\circ f=i_{\{0\}}$, so $g$ is a left inverse. The element $1\notin f(\{0\})$, so $f$ is not surjective and by step [](#surjective){.pf-ref} it has no right inverse.

:::

:::

::: {.pf-step #part-c}
(c) A function with a right inverse and no left inverse: the constant map $f:\{0,1\}\to\{0\}$.

::: pf-proof
The map $h:\{0\}\to\{0,1\}$ with $h(0)=0$ satisfies $f\circ h=i_{\{0\}}$, so it is a right inverse. Since $f(0)=f(1)$ and $0\neq1$, $f$ is not injective and by step [](#injective){.pf-ref} it has no left inverse.

:::

:::

::: {.pf-step #part-d}
(d) A function can have more than one left inverse, and more than one right inverse.

::: pf-proof

::: {.pf-step #two-left}
The inclusion $f:\{0,1\}\to\{0,1,2\}$ has two left inverses.

::: pf-proof
A map $g:\{0,1,2\}\to\{0,1\}$ is a left inverse exactly when $g(0)=0$ and $g(1)=1$; the value $g(2)$ is unconstrained. So the two maps with $g(2)=0$ and with $g(2)=1$ are distinct left inverses.

:::

:::

::: {.pf-step #two-right}
The constant surjection $f:\{0,1\}\to\{0\}$ has two right inverses.

::: pf-proof
Both $h_0$ with $h_0(0)=0$ and $h_1$ with $h_1(0)=1$ satisfy $f\circ h=i_{\{0\}}$, and $h_0\neq h_1$.

:::

:::

:::

:::

::: {.pf-step #part-e}
(e) If $f$ has a left inverse $g$ and a right inverse $h$, then $f$ is bijective and $g=h=f^{-1}$.

::: pf-proof
By step [](#injective){.pf-ref} $f$ is injective and by step [](#surjective){.pf-ref} it is surjective, hence bijective, so it has a two-sided inverse $f^{-1}$. For the identification,
$$
g=g\circ i_B=g\circ(f\circ h)=(g\circ f)\circ h=i_A\circ h=h,
$$
where the outer equalities use the definitions of the identity maps, the middle one associativity of composition, and the substitutions $g\circ f=i_A$ and $f\circ h=i_B$. So $g$ and $h$ are the same map, and it inverts $f$ on both sides, whence it is $f^{-1}$.

:::

:::

:::

:::
