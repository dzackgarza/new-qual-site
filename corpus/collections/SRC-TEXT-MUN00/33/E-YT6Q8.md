---
schema: qual/card@1
id: E-YT6Q8
kind: problem
title: Connected normal and regular spaces with more than one point are uncountable
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Separation Axioms
relations: []
review: draft
---

::: {.exercise}

(a) Show that a connected normal space having more than one point is uncountable.

(b) Show that a connected regular space having more than one point is uncountable.
[Hint: Any countable space is Lindelöf.]
:::

::: {.solution}
(a) Let \(X\) be connected and normal, with distinct points \(a,b\). Since normal spaces are \(T_1\), the singleton sets \(\{a\},\{b\}\) are closed. By Urysohn's lemma there is a continuous function
\[
f:X\to[0,1]
\]
with \(f(a)=0\) and \(f(b)=1\). The image \(f(X)\) is connected and contains \(0\) and \(1\), so
\[
f(X)=[0,1].
\]
Thus \(X\) surjects onto an uncountable set and is therefore uncountable.

(b) Let \(X\) be connected, regular, and have more than one point. If \(X\) were countable, then it would be Lindelöf. A regular Lindelöf space is normal by §32. Part (a) would then imply \(X\) is uncountable, contradiction. Hence \(X\) is uncountable.
:::
