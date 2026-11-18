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

The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 10.6, printed pp. 110--111** (`tmp/sources/munkres-solutions-whitman.pdf`); all three parts and the counting lemma are his. Throughout, $<$ is the well-order of $S_{\Omega}$ and $S_{\alpha}=\{y\in S_{\Omega}\mid y<\alpha\}$; by Lemma 10.2 the set $S_{\Omega}$ is uncountable and every section $S_{\alpha}$ of it is countable, and by Theorem 7.5 a countable union of countable sets is countable.

::: pf

::: {.pf-step #lemma}

If $A$ is uncountable and $B\subset A$ is countable, then $A-B$ is uncountable.

::: pf-proof

$A=(A-B)\cup B$. If $A-B$ were countable, then $A$ would be the union of two countable sets, hence countable by Theorem 7.5, contradicting the uncountability of $A$. So $A-B$ is uncountable.

:::

:::

::: {.pf-step #nolargest}

(a) $S_{\Omega}$ has no largest element.

::: pf-proof

Suppose $\alpha$ were largest. Then every $x\in S_{\Omega}$ satisfies $x\le\alpha$, that is $x\in S_{\alpha}$ or $x=\alpha$, so $S_{\Omega}=S_{\alpha}\cup\{\alpha\}$. The section $S_{\alpha}$ is countable by Lemma 10.2 and $\{\alpha\}$ is countable, so by Theorem 7.5 $S_{\Omega}$ would be countable, contradicting its uncountability. Hence no largest element exists.

:::

:::

::: {.pf-step #tail}

(b) For every $\alpha\in S_{\Omega}$ the set $T_{\alpha}=\{x\in S_{\Omega}\mid\alpha<x\}$ is uncountable.

::: pf-proof

$x\notin T_{\alpha}$ means $x\le\alpha$, i.e. $x\in S_{\alpha}$ or $x=\alpha$, so $T_{\alpha}=S_{\Omega}-\bigl(S_{\alpha}\cup\{\alpha\}\bigr)$. The set $S_{\alpha}\cup\{\alpha\}$ is countable, being a union of two countable sets, and $S_{\Omega}$ is uncountable; step [](#lemma){.pf-ref} then makes $T_{\alpha}$ uncountable.

:::

:::

::: {.pf-step #unbounded}

(c) $X_{0}=\{x\in S_{\Omega}:x \text{ has no immediate predecessor}\}$ is not bounded above in $S_{\Omega}$.

::: pf-proof

Suppose $\alpha\in S_{\Omega}$ is an upper bound of $X_{0}$. Then every $x\in S_{\Omega}$ with $\alpha<x$ has an immediate predecessor: were such an $x$ without one, $x$ would lie in $X_{0}$ and violate $x\le\alpha$. By (a) of step [](#nolargest){.pf-ref}, $S_{\Omega}$ has no largest element, so every element of $S_{\Omega}$ has an immediate successor (Exercise 10.2(a)); and if $x\in T_{\alpha}$ with immediate successor $y$, then $\alpha<x<y$, so $y\in T_{\alpha}$. Hence every element of $T_{\alpha}$ has an immediate successor inside $T_{\alpha}$. By step [](#tail){.pf-ref} $T_{\alpha}$ is uncountable, hence nonempty, and being a subset of the well-ordered set $S_{\Omega}$ it has a smallest element $\beta$.

:::

:::

::: {.pf-step #sequence}

(c) There is an injective map $f:\ZZ_{+}\to T_{\alpha}$ with $f(n)<f(n+1)$.

::: pf-proof

Define $f(1)=\beta$ and let $f(n+1)$ be the immediate successor of $f(n)$ in $T_{\alpha}$, which exists by the argument of step [](#unbounded){.pf-ref}. This is a legitimate recursive definition, since the recipe is defined on every function from a nonempty section of $\ZZ_{+}$ into $T_{\alpha}$ and takes values in $T_{\alpha}$. As $f(n)<f(n+1)$ for every $n$, the map is strictly increasing, hence injective.

:::

:::

::: {.pf-step #surjective}

(c) That map $f$ is also surjective, so $T_{\alpha}$ would be countable.

::: pf-proof

Suppose $T_{\alpha}-f(\ZZ_{+})$ is nonempty; being a subset of the well-ordered set $S_{\Omega}$, it has a smallest element $y$. Then $y\ne\beta=f(1)$ and $\beta<y$, since $\beta$ is the smallest element of $T_{\alpha}$. By step [](#unbounded){.pf-ref} $y$ has an immediate predecessor $x$ in $S_{\Omega}$, and $\beta\le x$ because $\beta<y$ and $x$ is the largest element below $y$; so $\alpha<\beta\le x<y$ gives $x\in T_{\alpha}$. Since $x<y$ and $y$ is the smallest element of $T_{\alpha}-f(\ZZ_{+})$, we have $x=f(n)$ for some $n$; then $f(n+1)$, the immediate successor of $x$ in $T_{\alpha}$, equals $y$, contradicting $y\notin f(\ZZ_{+})$. So $f$ is a bijection $\ZZ_{+}\to T_{\alpha}$ and $T_{\alpha}$ is countable, contradicting step [](#tail){.pf-ref}.

:::

:::

::: {.pf-step #conclusion}

(c) $X_{0}$ is uncountable.

::: pf-proof

Steps [](#unbounded){.pf-ref} and [](#surjective){.pf-ref} show that no $\alpha$ bounds $X_{0}$ above. By Theorem 10.3 every countable subset of $S_{\Omega}$ has an upper bound in $S_{\Omega}$; contrapositively, a subset of $S_{\Omega}$ with no upper bound is uncountable. Hence
$$
\boxed{X_{0}\ \text{is uncountable}.}
$$
As the published solution notes, $S_{\Omega}$ has the order type of the first uncountable ordinal $\omega_{1}$ and $X_{0}$ corresponds to its set of limit ordinals.

:::

:::

:::

:::
