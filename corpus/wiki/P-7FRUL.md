---
schema: qual/card@1
id: P-7FRUL
kind: problem
title: "Facts used: $H_(T^2) = [\\ZZ, \\ZZ^2, \\ZZ, 0\\rightarrow]$ $N^{(1)} \\homotopic S^1$, so $H_{\\geq 2}(N) = 0$."
classification:
  areas:
  - topology
  topics:
  - mayer-vietoris
  - homology
relations: []
review: draft
---

Facts used:

- $H_*(T^2) = [\ZZ, \ZZ^2, \ZZ, 0\rightarrow]$

- $N^{(1)} \homotopic S^1$, so $H_{\geq 2}(N) = 0$.

- A SES $0\to A\to B \to F \to 0$ with $F$ free splits.

- $0\to A \to B \mapsvia{\cong} C \to D \to 0$ implies $A = D = 0$.
  Let $N$ be the knotted solid torus, so that $\del N = T^2$, and let $X = S^3 - N$.
  Then

- $S^3 = N \union_{T^2} X$

- $N \cap X = T^2$

and we apply Mayer-Vietoris to $S^3$:

$$
4\qquad H_4(T^2) \to H_4(N) \times H_4(X) \to H_4(S^3) \\
3\qquad H_3(T^2) \to H_3(N) \times H_3(X) \to H_3(S^3) \\
2\qquad H_2(T^2) \to H_2(N) \times H_2(X) \to H_2(S^3) \\
1\qquad H_1(T^2) \to H_1(N) \times H_1(X) \to H_1(S^3) \\
0\qquad H_0(T^2) \to H_0(N) \times H_0(X) \to H_0(S^3) \\
$$

where we can plug in known information and deduce some maps:
$$
\begin{align}
4\qquad &0 \to &0 \qquad\to &0 \mapsvia{\del_4} \\
3\qquad &0 \to &H_3(X) \qquad\to &\ZZ \mapsvia{\del_3}\\
2\qquad &\ZZ \to &H_2(X) \qquad\to &0 \mapsvia{\del_2}\\
1\qquad &\ZZ^2 \cong &\ZZ \times H_1(X) \qquad\to &0 \mapsvia{\del_1}\\
0\qquad &\ZZ \to &\ZZ \times H_0(X) \qquad\to &\ZZ \to 0 \\
\end{align}
$$

We then deduce:

- $H_0(X) = \ZZ$ by the splitting of the line 0 SES $$0 \to \ZZ \to \ZZ \cross H_0(X) \to \ZZ \to 0$$ yielding $Z\cross H_0(X) \cong \ZZ \times \ZZ$.

- $H_1(X) = \ZZ$ by the line 1 SES $$0 \to \ZZ^2 \to \ZZ \cross H_1(X) \to 0$$ which yields an isomorphism.

- $H_2(X) = H_3(X) = 0$ by examining the SES spanning lines 3 and 2: $$0 \injects H_3(X) \injects \ZZ \mapsvia{\cong_{\del_3}} \ZZ \surjects H_2(X) \surjects 0$$ Since $\del_3$ must be an isomorphism, this forces the edge terms to be zero.
  $\qed$
