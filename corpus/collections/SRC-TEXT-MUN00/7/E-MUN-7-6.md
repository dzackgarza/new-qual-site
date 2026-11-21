---
schema: qual/card@1
id: E-MUN-7-6
kind: problem
title: Schroeder–Bernstein theorem and equal cardinality
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
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 7, Exercise 6; the stored statement matches.
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
    Read against Munkres, Topology (2000), §7 Exercise 6, printed pp. 51-52; both parts
    are stored as printed, with the book's own hint for (a) reproduced.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 7.6,
    printed pp. 89-90 (tmp/sources/munkres-solutions-whitman.pdf). The chain A_1 sup
    B_1 sup A_2 sup ... and the rule h = f on the union of the differences A_n - B_n and
    h = identity elsewhere are the book's hint and his proof; the card proves the three
    things the hint leaves implicit - h maps into B, f carries A_n - B_n bijectively onto
    A_{n+1} - B_{n+1}, and the two pieces of the image are disjoint with union B. Part
    (b) is his reduction to (a) through B = g(C). No defect found.
---

::: {.exercise}

We say that two sets $A$ and $B$ have the same cardinality if there is a bijection of $A$ with $B$.

(a) Show that if $B \subset A$ and if there is an injection
$$
f \colon A \longrightarrow B,
$$
then $A$ and $B$ have the same cardinality.
[Hint: Define $A_{1} = A$, $B_{1} = B$, and for $n > 1$, $A_{n} = f(A_{n-1})$ and $B_{n} = f(B_{n-1})$. (Recursive definition again!)
Note that $A_{1} \supset B_{1} \supset A_{2} \supset B_{2} \supset A_{3} \supset \cdots$. Define a bijection $h \colon A \to B$ by the rule
$$
h(x) = \begin{cases} f(x) & \text{if } x \in A_{n} - B_{n} \text{ for some } n, \\ x & \text{otherwise.} \end{cases}
$$
]

(b) Theorem (Schroeder-Bernstein theorem).
If there are injections $f \colon A \to C$ and $g \colon C \to A$, then $A$ and $C$ have the same cardinality.
:::

::: {.solution}

The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 7.6, printed pp. 89--90** (`tmp/sources/munkres-solutions-whitman.pdf`); the sets $A_{n}$, $B_{n}$, the union of the differences and the piecewise map $h$ are the book's hint, and the verification that $h$ is a bijection is his; the card states the three points the hint leaves implicit.

::: pf

::: {.pf-step #chain}

With $A_{1}=A$, $B_{1}=B$ and $A_{n}=f(A_{n-1})$, $B_{n}=f(B_{n-1})$ for $n>1$, one has $A_{1}\supset B_{1}\supset A_{2}\supset B_{2}\supset A_{3}\supset\cdots$.

::: pf-proof

$B_{1}=B\subset A=A_{1}$ by hypothesis. Applying the increasing operator $S\mapsto f(S)$, which preserves inclusions, to $B_{n}\subset A_{n}$ gives $B_{n+1}=f(B_{n})\subset f(A_{n})=A_{n+1}$, and applying it to $A_{n+1}\subset B_{n}$ (established for the previous index) gives $A_{n+2}\subset B_{n+1}$. So the two families interleave as claimed, by induction on $n$.

:::

:::

::: {.pf-step #differences}

With $R=\bigcup_{n\ge1}(A_{n}-B_{n})$, the piecewise rule $h(x)=f(x)$ for $x\in R$ and $h(x)=x$ for $x\notin R$ defines a map $A\to B$.

::: pf-proof

If $x\notin R$ then in particular $x\notin A_{1}-B_{1}=A-B$, so $x\in B$, and $h(x)=x\in B$. If $x\in R$ then $x\in A_{n}-B_{n}\subset A_{n}$ for some $n$, so $f(x)\in f(A_{n})=A_{n+1}\subset B_{2}\subset B$, and $h(x)=f(x)\in B$. So every value of $h$ lies in $B$, and $h$ is defined on all of $A$ since $R$ and its complement cover $A$.

:::

:::

::: {.pf-step #images}

$f$ maps $A_{n}-B_{n}$ bijectively onto $A_{n+1}-B_{n+1}$.

::: pf-proof

For $S\subset A$, injectivity of $f$ gives $f(A_{n}-S)=f(A_{n})-f(S)$: the inclusion $\subset$ is clear, and if $f(x)\in f(A_{n})-f(S)$ with $x\in A_{n}$, then $x\notin S$, since $x\in S$ would put $f(x)\in f(S)$. Taking $S=B_{n}$ and using $f(A_{n})=A_{n+1}$, $f(B_{n})=B_{n+1}$ gives $f(A_{n}-B_{n})=A_{n+1}-B_{n+1}$, and the restriction is injective, hence a bijection onto that set.

:::

:::

::: {.pf-step #bij}

(a) $h$ is a bijection $A\to B$, so $A$ and $B$ have the same cardinality.

::: pf-proof

By step [](#images){.pf-ref}, $h$ carries $R=\bigcup_{n\ge1}(A_{n}-B_{n})$ bijectively onto $\bigcup_{n\ge1}(A_{n+1}-B_{n+1})=\bigcup_{n\ge2}(A_{n}-B_{n})=R\cap B$. On the complement, $h$ is the identity of $A-R$, whose image is $A-R$; and $A-R\subset B$ because $A-B=A_{1}-B_{1}\subset R$, so $A-R\subset B$, while $A-R$ meets $R\cap B$ trivially. Two disjoint pieces map bijectively onto two disjoint pieces whose union is $(R\cap B)\cup(A-R)=B$, so $h$ is injective and surjective:
$$
\boxed{h:A\to B\ \text{is a bijection, hence } \cardinality{A}=\cardinality{B}.}
$$

:::

:::

::: {.pf-step #sb}

(b) If there are injections $f:A\to C$ and $g:C\to A$, then $A$ and $C$ have the same cardinality.

::: pf-proof

Let $B=g(C)\subset A$. The map $g$ with codomain restricted to its image is a bijection $C\to B$, with inverse $g^{-1}:B\to C$. The composite $g\circ f:A\to B$ is injective, being a composite of injections, so by part (a) of step [](#bij){.pf-ref} there is a bijection $k:A\to B$; then $g^{-1}\circ k:A\to C$ is a bijection. This is the Schroeder--Bernstein theorem:
$$
\boxed{\text{injections } A\to C \text{ and } C\to A \implies \cardinality{A}=\cardinality{C}.}
$$

:::

:::

:::

:::
