---
schema: qual/card@1
id: P-LOXDS
kind: problem
title: Uncountable $E\subset[0,1]$ is uncountable on both sides of some $t$
classification:
  areas:
  - complex-analysis
  topics:
  - Point-Set Topology
  - Counterexamples
relations: []
review: draft
---

:::{.problem}
Show that if $E\subset [0, 1]$ is uncountable, then there is some $t\in \RR$ such that $E\intersect (-\infty ,t)$ and $E\intersect (t, \infty)$ are also uncountable.
:::


:::{.solution}
See 3.2.12 of Understanding analysis 2ed. of Abbott.
Show something stronger, that the following set is nonempty and open:
\[
S \da \ts{t\in \RR \st E \intersect (-\infty, t), E \intersect (t, \infty) \text{ are uncountable}}
\subseteq \RR
.\]
Write
\[
S_- &\da \ts{ t\in \RR \st E \intersect (- \infty, t) \text{ is countable}} \\
S_+ &\da \ts{ s\in \RR \st E \intersect (s, \infty) \text{ is countable}}
.\]

Note that $S_- \neq \RR$ since then we could write $E = \Union_{n\in \ZZ} E \intersect (- \infty, n)$ as a countable union of countable sets.

Claim: $S = (\sup S_-, \inf S_+)$.

We prove the two inclusions.

First, $S \subseteq (\sup S_-, \inf S_+)$.
Let $t \in S$, so both $E \cap (-\infty, t)$ and $E \cap (t, \infty)$ are uncountable.
Then $t \notin S_-$ (since $E \cap (-\infty, t)$ is uncountable, not countable), and $t \notin S_+$.
Now $S_-$ is downward closed: if $s \in S_-$ and $s' < s$, then $E \cap (-\infty, s') \subseteq E \cap (-\infty, s)$ is countable, so $s' \in S_-$.
Hence every element of $S_-$ is $< t$ (if some $s \in S_-$ satisfied $s \ge t$, then $t \in S_-$ by downward closure, a contradiction), so $t \ge \sup S_-$.
Similarly $S_+$ is upward closed, so every element of $S_+$ is $> t$, giving $t \le \inf S_+$.
Thus $t \in [\sup S_-, \inf S_+]$.
It remains to rule out the endpoints: if $t = \sup S_-$, then for every $s < t$ we have $s \in S_-$, so $E \cap (-\infty, s)$ is countable for all $s < t$; writing $E \cap (-\infty, t) = \bigcup_{n} E \cap (-\infty, t - 1/n)$ expresses $E \cap (-\infty, t)$ as a countable union of countable sets, hence countable, contradicting $t \in S$.
So $t > \sup S_-$, and symmetrically $t < \inf S_+$.
Therefore $t \in (\sup S_-, \inf S_+)$.

Conversely, let $t \in (\sup S_-, \inf S_+)$.
Since $t > \sup S_-$, we have $t \notin S_-$ (if $t \in S_-$ then $t \le \sup S_-$), so $E \cap (-\infty, t)$ is uncountable.
Since $t < \inf S_+$, we have $t \notin S_+$, so $E \cap (t, \infty)$ is uncountable.
Hence $t \in S$.

Finally, $S$ is nonempty and open.
First note $S_- \cap S_+ = \emptyset$: if $t$ lay in both, then $E \cap (-\infty, t)$ and $E \cap (t, \infty)$ would both be countable, so $E = (E \cap (-\infty, t)) \cup (E \cap (t, \infty)) \cup (E \cap \{t\})$ would be countable, contradicting that $E$ is uncountable.
Since $S_-$ is downward closed and $S_+$ is upward closed, their disjointness forces $\sup S_- \le \inf S_+$ (if $\sup S_- > \inf S_+$, some $t$ with $\inf S_+ < t < \sup S_-$ would lie in both).
Moreover $\sup S_- < \inf S_+$: if $\sup S_- = \inf S_+ = c$, then $E \cap (-\infty, c) = \bigcup_n E \cap (-\infty, c - 1/n)$ is a countable union of countable sets (each $c - 1/n < c = \sup S_-$ lies in $S_-$), hence countable, so $c \in S_-$; symmetrically $E \cap (c, \infty) = \bigcup_n E \cap (c + 1/n, \infty)$ is countable, so $c \in S_+$, contradicting $S_- \cap S_+ = \emptyset$.
Therefore $(\sup S_-, \inf S_+)$ is a nonempty open interval, and by the two inclusions above it equals $S$, so $S$ is nonempty and open.




