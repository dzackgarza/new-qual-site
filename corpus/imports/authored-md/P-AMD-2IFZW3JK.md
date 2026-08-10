---
schema: qual/card@1
id: P-AMD-2IFZW3JK
kind: problem
title: Show that the Mayer-Vietoris sequence is natural, i.e.
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
---

::: {.problem}
Show that the Mayer-Vietoris sequence is natural, i.e. If $X\mapsvia{f} Y$ where $f(A) \subset C$ and $f(B) \subset D$, then this commutes:
$$
\begin{CD}
H_n(X) @>>> H_n(A\intersect B) @>>> H_n(A) \oplus H_n(B) @>>> H_{n-1}(X)\\
@VVf_*V @VVf_*V  @VVf_*V @VVf_*V\\
H_n(Y) @>>> H_n(C\intersect D) @>>> H_n(C) \oplus H_n(D) @>>> H_{n-1}(Y)\\
\end{CD}
$$
:::
