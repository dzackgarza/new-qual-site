---
schema: qual/card@1
id: P-AGH25NOETHERIAN
kind: problem
title: $\PP^n$ is noetherian, and the irreducible components of a projective algebraic set
classification:
  areas:
  - algebraic-geometry
  topics:
  - Noetherian Spaces
  - Irreducible Components
  - Zariski Topology
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared both parts with the retained Hartshorne I.2.5 transcription. The proof uses the projective ideal correspondence for the descending chain condition, then proves existence and uniqueness of the irredundant decomposition, including the empty algebraic set.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $k$ be algebraically closed and let $n\ge0$.

(a) Show that $\PP_k^n$ is a noetherian topological space.

(b) Show that every algebraic set in $\PP_k^n$ can be written uniquely as a finite union of irreducible algebraic sets, no one containing another.
These are called its **irreducible components**.
:::

::: {.solution}
Uniqueness of a finite decomposition means uniqueness of its collection of components, without an ordering.
An irreducible space is nonempty, and the empty algebraic set is represented by the empty union.

<1>1. The space $\PP_k^n$ is noetherian.

::: {.proof}
For a descending chain of closed subsets
$$
Y_1\supseteq Y_2\supseteq\cdots,
$$
the [[P-AGH24CORRESPONDENCE|projective ideal correspondence]] gives an ascending chain
$$
I(Y_1)\subseteq I(Y_2)\subseteq\cdots
$$
in $S=k[x_0,\ldots,x_n]$.
The Hilbert basis theorem makes $S$ noetherian, so there is $N$ for which $I(Y_j)=I(Y_N)$ whenever $j\ge N$ [@Har10a, Chapter I, §1].
Applying $Z$ and using $Z(I(Y_j))=Y_j$ gives $Y_j=Y_N$ for all those $j$.
Thus every descending chain of closed subsets stabilizes, which is the [[D-9DIKB|noetherian condition]], proving (a).
:::

<1>2. Every projective algebraic set is a finite union of irreducible algebraic sets.

::: {.proof}
Suppose that the family of closed subsets without such a decomposition were nonempty.
The descending chain condition from step <1>1 supplies a minimal member $Y$ of this family.
It is not empty, since the empty union represents the empty set.
It is not irreducible, since then it alone would be a finite decomposition.
Consequently $Y=A\cup B$ for two proper closed subsets $A,B\subsetneq Y$.
They are also closed in $\PP^n$.
Minimality of $Y$ makes each of them a finite union of irreducible closed subsets.
Combining the two finite unions gives such a decomposition of $Y$, a contradiction.
Hence the assumed family is empty.

From any finite decomposition, discard repetitions and any member contained in a different member.
Removing such a member does not change the union, and after finitely many removals no distinct members contain one another.
This gives existence in the form required by (b).
:::

<1>3. The decomposition in step <1>2 with no member containing another is unique.

::: {.proof}
If an irreducible subset $T$ is contained in a finite union of closed sets $C_1,\ldots,C_s$, then $T$ is contained in one $C_j$.
Indeed, the subsets $T\cap C_j$ are closed in $T$ and cover it; induction on $s$ using the definition of irreducibility gives the assertion.

Suppose
$$
Y=Y_1\cup\cdots\cup Y_r=Z_1\cup\cdots\cup Z_s
$$
are two decompositions satisfying the stated conditions.
For fixed $i$, the assertion just proved gives $Y_i\subseteq Z_j$ for some $j$.
Applying it again gives $Z_j\subseteq Y_h$ for some $h$.
Thus $Y_i\subseteq Y_h$, and the noncontainment condition in the first decomposition forces $h=i$.
Both inclusions are then equalities, so $Y_i=Z_j$.
Every $Y_i$ therefore occurs in the second decomposition, and the same argument with the decompositions exchanged shows that every $Z_j$ occurs in the first.
They have exactly the same members.

These members are precisely the maximal irreducible closed subsets of $Y$.
Any irreducible closed subset is contained in a member by the first paragraph, and no member can be properly contained in a larger irreducible closed subset without being contained in another member.
For $Y=\varnothing$, no nonempty irreducible component occurs, so its empty decomposition is also unique.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>1 proves (a), while steps <1>2--<1>3 prove existence and uniqueness in (b).
:::
:::
