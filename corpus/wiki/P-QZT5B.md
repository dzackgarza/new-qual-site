---
schema: qual/card@1
id: P-QZT5B
kind: problem
title: The first Borel–Cantelli lemma
classification:
  areas:
  - real-analysis
  topics:
  - borel-cantelli
  - measure-theory
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Show that if $\sum \mu(E_k) < \infty$ then almost every $x\in X$ is in at most finitely many $E_k$.
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. It suffices to show $\mu(\limsup_k E_k) = 0$.
Proof: $\limsup_k E_k = \cap_{n\ge1}\cup_{k\ge n} E_k$ is the set of points lying in infinitely many $E_k$; if it has measure $0$, then almost every $x$ lies in only finitely many $E_k$.
<1>2. $\mu(\cup_{k\ge n} E_k) \le \sum_{k\ge n}\mu(E_k)$.
Proof: countable subadditivity of $\mu$.
<1>3. $\sum_{k\ge n}\mu(E_k) \to 0$ as $n \to \infty$.
Proof: $\sum_k \mu(E_k) < \infty$, so the tails of the series vanish.
<1>4. $\mu(\limsup_k E_k) = 0$.
Proof: $\limsup_k E_k \subseteq \cup_{k\ge n} E_k$ for every $n$, so by <1>2 and <1>3, $\mu(\limsup_k E_k) \le \sum_{k\ge n}\mu(E_k) \to 0$.
<1>5. Q.E.D.
:::
