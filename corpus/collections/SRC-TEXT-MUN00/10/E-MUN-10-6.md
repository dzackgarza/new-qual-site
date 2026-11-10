---
schema: qual/card@1
id: E-MUN-10-6
kind: problem
title: Properties of the minimal uncountable well-ordered set $S_{\Omega}$
classification:
  areas:
  - topology
  topics:
  - Well-Ordered Sets
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §10 Exercise 6, printed p. 67, with S_Omega as
    defined in Lemma 10.2, printed p. 66; all three parts are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 10.6, printed pp.
    110-111. The counting lemma (uncountable minus countable is uncountable), (a) S_Omega
    cannot have a largest element, (b) the elements above any alpha are uncountable, and (c)
    the set X_0 of elements without an immediate predecessor is uncountable are his. In (c)
    his argument is the one kept: X_0 is not bounded above, because otherwise the tail above
    a bound would be a countable well-ordered set in which every element has both an
    immediate predecessor and an immediate successor, and then Theorem 10.3 makes X_0
    uncountable.
---

::: {.exercise}

Let $S_{\Omega}$ be the minimal uncountable well-ordered set.

(a) Show that $S_{\Omega}$ has no largest element.

(b) Show that for every $\alpha \in S_{\Omega}$, the subset $\{x \mid \alpha < x\}$ is uncountable.

(c) Let $X_0$ be the subset of $S_{\Omega}$ consisting of all elements $x$ such that $x$ has no immediate predecessor.
Show that $X_0$ is uncountable.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 10.6, printed pp. 110--111** (`tmp/sources/munkres-solutions-whitman.pdf`); all three parts and the counting lemma are his.

Throughout, $<$ is the well-order of $S_{\Omega}$, and $S_{\alpha}=\{y\in S_{\Omega}\mid y<\alpha\}$. By Lemma 10.2 the set $S_{\Omega}$ is uncountable and every section $S_{\alpha}$ of it is countable, and by Theorem 7.5 a countable union of countable sets is countable.

**Lemma.** If $A$ is uncountable and $B\subset A$ is countable, then $A-B$ is uncountable. Indeed $A=(A-B)\cup B$, so were $A-B$ countable, $A$ would be a union of two countable sets and hence countable.

(a) Suppose $S_{\Omega}$ had a largest element $\alpha$. Then every $x\in S_{\Omega}$ satisfies $x\le\alpha$, so $x\in S_{\alpha}$ or $x=\alpha$, that is
$$
S_{\Omega}=S_{\alpha}\cup\{\alpha\}.
$$
The section $S_{\alpha}$ is countable and $\{\alpha\}$ is countable, so $S_{\Omega}$ is countable by Theorem 7.5, contradicting the uncountability of $S_{\Omega}$. Hence $S_{\Omega}$ has no largest element.

(b) Let $\alpha\in S_{\Omega}$ and put $T_{\alpha}=\{x\in S_{\Omega}\mid \alpha<x\}$. Then
$$
T_{\alpha}=S_{\Omega}-\big(S_{\alpha}\cup\{\alpha\}\big),
$$
because $x\notin T_{\alpha}$ means $x\le\alpha$, i.e. $x\in S_{\alpha}$ or $x=\alpha$. The set $S_{\alpha}\cup\{\alpha\}$ is countable, so $T_{\alpha}$ is uncountable by the lemma.

(c) Let $X_{0}=\{x\in S_{\Omega}\mid x$ has no immediate predecessor$\}$. We show first that $X_{0}$ is not bounded above in $S_{\Omega}$.

Suppose on the contrary that $\alpha\in S_{\Omega}$ is an upper bound of $X_{0}$, so that every $x\in S_{\Omega}$ with $\alpha<x$ has an immediate predecessor: were some such $x$ without one, $x$ would lie in $X_{0}$ and violate $\alpha<x\le$ (upper bound). By (a), $S_{\Omega}$ has no largest element, so by Exercise 10.2(a) every element of $S_{\Omega}$ has an immediate successor; and if $x\in T_{\alpha}$ and $y$ is the immediate successor of $x$, then $\alpha<x<y$, so $y\in T_{\alpha}$ as well. Thus every element of $T_{\alpha}$ has an immediate successor in $T_{\alpha}$. By (b), $T_{\alpha}$ is uncountable, hence nonempty, so it has a smallest element $\beta$.

Define $f:\ZZ_{+}\to T_{\alpha}$ by $f(1)=\beta$ and by letting $f(n+1)$ be the immediate successor of $f(n)$ in $T_{\alpha}$, which exists by the preceding paragraph. The formula is defined on every function from a nonempty section of $\ZZ_{+}$ into $T_{\alpha}$, so the principle of recursive definition gives such an $f$; and $f(n)<f(n+1)$ for all $n$, so $f$ is strictly increasing and hence injective.

It is also surjective. If $T_{\alpha}-f(\ZZ_{+})$ were nonempty, it would have a smallest element $y$, since $T_{\alpha}\subset S_{\Omega}$ is well ordered. Then $y\ne\beta=f(1)$, and $\beta<y$ because $\beta$ is the smallest element of $T_{\alpha}$. By the first paragraph $y$ has an immediate predecessor $x$ in $S_{\Omega}$, and $\beta\le x$ because $\beta<y$ and $x$ is the largest element below $y$; so $\alpha<\beta\le x<y$ gives $x\in T_{\alpha}$. Since $x<y$ and $y$ is the smallest element of $T_{\alpha}-f(\ZZ_{+})$, we get $x=f(n)$ for some $n$, and then $f(n+1)$, the immediate successor of $x$ in $T_{\alpha}$, equals $y$, contradicting $y\notin f(\ZZ_{+})$. Hence $f$ is a bijection $\ZZ_{+}\to T_{\alpha}$ and $T_{\alpha}$ is countable, contradicting (b).

So $X_{0}$ has no upper bound in $S_{\Omega}$. By Theorem 10.3 a countable subset of $S_{\Omega}$ has an upper bound in $S_{\Omega}$; contrapositively, a subset of $S_{\Omega}$ with no upper bound is uncountable. Hence $X_{0}$ is uncountable.

As Whitman notes, $S_{\Omega}$ has the order type of the first uncountable ordinal $\omega_{1}$ and $X_{0}$ corresponds to its set of limit ordinals.
:::
