---
schema: qual/card@1
id: T-2W5WN
kind: theorem
title: "UCT for Change of Group"
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
---
:::{.theorem title="UCT for Change of Group"}
For changing coefficients from $\ZZ$ to $G$ an arbitrary group, there are short exact sequences

\[
0\to \tor_\ZZ^0 (H_{i}(X;\ZZ), A) &\to H_{i}(X;A)\to \Tor_\ZZ^1 (H_{i-1}(X;\ZZ ),A)\to 0 \\
& \quad \Downarrow \\ \\
0 \to H_{i} X \tensor G &\to H_{i}(X; G) \to \tor_\ZZ^1(H_{i-1}X, G) \to 0 
\]
and 
\[
0\to \ext_{\ZZ}^{1}(H_{i-1}(X; \ZZ),A) &\to H^{i}(X; A)\to \ext_{\ZZ}^{0}(H_{i}(X; \ZZ),A) \to 0 \\
&\quad \Downarrow \\ \\ 
0 \to \ext (H_{i-1} X, G) &\to H^i(X;G) \to \hom(H_{i} X, G) \to 0
.\]
These split unnaturally:
\[
H_{i}(X;G) &= (H_{iX}\tensor G) \oplus \tor(H_{i-1}X; G) \\
H^i(X; G) &= \hom(H_{i}X, G) \oplus \ext(H_{i-1}X; G)
\]

When all of the $H_{i}X$ are all finitely generated (e.g. if $G$ is a field), writing $H_{i}(X; \ZZ) = \ZZ^{\beta_{i}} \oplus T_{i}$ as the sum of a free and a torsionfree module, we have
\[
H^i(X; \ZZ) &\cong \ZZ^{\beta_{i}} \times T_{i-1} \\
H^i(X; A) &\cong \qty{H_i(X; G)}\dual \da \hom_\ZZ(H_{i}(X; G), G)
.\]

In other words, letting $F(\wait)$ be the free part and $T(\wait)$ be the torsion part, we have
\[
H^i(X; \ZZ) &= F(H_{i}(X; \ZZ)) \times T(H_{i-1}(X; \ZZ))\\
H_{i}(X; \ZZ) &= F(H^i(X; \ZZ)) \times T(H^{i+1}(X; \ZZ))
\]
:::
